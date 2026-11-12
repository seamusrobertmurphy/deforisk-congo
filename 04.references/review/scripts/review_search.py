#!/usr/bin/env python3
"""Run the review searches built from 04.references/review/search-terms.csv.

Usage, from the repository root
  python3 04.references/review/scripts/review_search.py store
  python3 04.references/review/scripts/review_search.py openalex
  python3 04.references/review/scripts/review_search.py s2

Each run writes the records one source returned to 02.inputs/derived/review-hits-<source>.csv,
their abstracts to 02.inputs/review/raw/review-abstracts-<source>.csv, and appends one row per
query to 02.inputs/derived/review-search-log.csv. Every log row carries the SHA-256 digest of
the protocol, the search terms and the screening rule as they stood when the query ran.
No request carries an email address.
"""
import csv
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

REVIEW = "04.references/review"
DERIVED = "02.inputs/derived"
RAW = "02.inputs/review/raw"
STORE = "../library-science"
UA = {"User-Agent": "literature-review-script/1.0"}
FROZEN = ["protocol.md", "search-terms.csv", "screening-rule.md"]
HIT_FIELDS = ["source", "route", "source_id", "doi", "title", "year", "type", "venue",
              "language", "first_author", "cited_by"]
LOG_FIELDS = ["run_at", "source", "route", "query", "reported", "retrieved", "cap",
              "status", "digest"]


def digest():
    h = hashlib.sha256()
    for name in FROZEN:
        with open(os.path.join(REVIEW, name), "rb") as f:
            h.update(f.read())
    return h.hexdigest()


def routes():
    """Return {route: [(concept, [terms])]} in file order, refusing a term with no source."""
    out = {}
    with open(os.path.join(REVIEW, "search-terms.csv"), newline="") as f:
        for row in csv.DictReader(f):
            if row["source"] not in ("statement", "synonym", "seed"):
                sys.exit(f"term {row['term']!r} has no recognised source")
            concepts = out.setdefault(row["route"], [])
            for name, terms in concepts:
                if name == row["concept"]:
                    terms.append(row["term"])
                    break
            else:
                concepts.append((row["concept"], [row["term"]]))
    return out


def quoted(term):
    return f'"{term}"' if " " in term else term


def openalex_query(concepts):
    return " AND ".join("(" + " OR ".join(quoted(t) for t in terms) + ")" for _, terms in concepts)


def s2_query(concepts):
    return " + ".join("(" + " | ".join(quoted(t) for t in terms) + ")" for _, terms in concepts)


def get(url, tries=6, wait=10):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return json.load(r), "ok"
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code not in (429, 500, 502, 503, 504):
                break
        except Exception as e:
            last = type(e).__name__
        time.sleep(wait * (i + 1))
    return None, last


def clean_doi(doi):
    if not doi:
        return ""
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip(), flags=re.I).lower()


def abstract_from_index(index):
    if not index:
        return ""
    words = {}
    for word, places in index.items():
        for p in places:
            words[p] = word
    return " ".join(words[k] for k in sorted(words))


def short_name(name):
    """Surname with initials, "Mark A. Friedl" to "Friedl MA", as a reference list prints it."""
    parts = re.split(r"\s+", (name or "").strip())
    if not parts or not parts[0]:
        return ""
    if "," in name:
        surname, given = [s.strip() for s in name.split(",", 1)]
        rest = re.split(r"[\s\-\u2010\u2011.]+", given)
    else:
        surname, rest = parts[-1], re.split(r"[\s\-\u2010\u2011.]+", " ".join(parts[:-1]))
    return (surname + " " + "".join(w[0] for w in rest if w)).strip()


def write(source, hits, abstracts, log):
    for h in hits:
        h["first_author"] = short_name(h["first_author"])
    os.makedirs(DERIVED, exist_ok=True)
    os.makedirs(RAW, exist_ok=True)
    with open(os.path.join(DERIVED, f"review-hits-{source}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, HIT_FIELDS)
        w.writeheader()
        w.writerows(hits)
    with open(os.path.join(RAW, f"review-abstracts-{source}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "doi", "abstract"])
        w.writerows(abstracts)
    path = os.path.join(DERIVED, "review-search-log.csv")
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, LOG_FIELDS)
        if new:
            w.writeheader()
        w.writerows(log)
    for row in log:
        print(f"{row['source']:9} {row['route']:5} reported {row['reported']:>5} "
              f"retrieved {row['retrieved']:>5} {row['status']}")


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_openalex(plan, dig):
    hits, abstracts, log = [], [], []
    for route, concepts in plan.items():
        if concepts[0][0] == "cites":
            seed, _ = get(f"https://api.openalex.org/works/doi:{concepts[0][1][0]}?select=id")
            if not seed:
                log.append(dict(run_at=now(), source="openalex", route=route, query=f"cites {concepts[0][1][0]}",
                                reported="", retrieved=0, cap="", status="seed not found", digest=dig))
                continue
            filt = f"cites:{seed['id'].rsplit('/', 1)[-1]}"
            query = f"cites {concepts[0][1][0]}"
        else:
            query = openalex_query(concepts)
            filt = f"title_and_abstract.search:{query}"
        page, got, reported, status = 1, 0, "", "ok"
        while True:
            url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
                "filter": filt, "per_page": 200, "page": page,
                "select": "id,doi,display_name,publication_year,type,language,primary_location,"
                          "authorships,abstract_inverted_index,cited_by_count"})
            data, status = get(url)
            if not data:
                break
            reported = data["meta"]["count"]
            for w in data["results"]:
                src = (w.get("primary_location") or {}).get("source") or {}
                authors = w.get("authorships") or []
                sid = w["id"].rsplit("/", 1)[-1]
                hits.append(dict(source="openalex", route=route, source_id=sid, doi=clean_doi(w.get("doi")),
                                 title=w.get("display_name") or "", year=w.get("publication_year") or "",
                                 type=w.get("type") or "", venue=src.get("display_name") or "",
                                 language=w.get("language") or "",
                                 first_author=(authors[0]["author"]["display_name"] if authors else ""),
                                 cited_by=w.get("cited_by_count") or 0))
                abstracts.append([sid, clean_doi(w.get("doi")), abstract_from_index(w.get("abstract_inverted_index"))])
                got += 1
            if got >= reported or not data["results"]:
                break
            page += 1
            time.sleep(1.5)
        log.append(dict(run_at=now(), source="openalex", route=route, query=query, reported=reported,
                        retrieved=got, cap="", status=status, digest=dig))
    write("openalex", hits, abstracts, log)


def run_s2(plan, dig):
    hits, abstracts, log = [], [], []
    fields = "title,abstract,year,externalIds,venue,publicationTypes,authors,citationCount"
    for route, concepts in plan.items():
        got, reported, status = 0, "", "ok"
        if concepts[0][0] == "cites":
            query = f"cites {concepts[0][1][0]}"
            offset = 0
            while True:
                url = (f"https://api.semanticscholar.org/graph/v1/paper/DOI:{concepts[0][1][0]}/citations?"
                       + urllib.parse.urlencode({"fields": fields, "limit": 1000, "offset": offset}))
                data, status = get(url)
                if not data:
                    break
                batch = [c["citingPaper"] for c in data.get("data", []) if c.get("citingPaper", {}).get("paperId")]
                papers = batch
                reported = (reported or 0) + len(batch)
                for p in papers:
                    got += add_s2(p, route, hits, abstracts)
                if "next" not in data:
                    break
                offset = data["next"]
                time.sleep(3)
        else:
            query = s2_query(concepts)
            token = None
            while True:
                params = {"query": query, "fields": fields}
                if token:
                    params["token"] = token
                data, status = get("https://api.semanticscholar.org/graph/v1/paper/search/bulk?"
                                   + urllib.parse.urlencode(params))
                if not data:
                    break
                reported = data.get("total", "")
                for p in data.get("data", []):
                    got += add_s2(p, route, hits, abstracts)
                token = data.get("token")
                if not token:
                    break
                time.sleep(3)
        log.append(dict(run_at=now(), source="s2", route=route, query=query, reported=reported,
                        retrieved=got, cap="", status=status, digest=dig))
        time.sleep(3)
    write("s2", hits, abstracts, log)


def add_s2(p, route, hits, abstracts):
    ids = p.get("externalIds") or {}
    authors = p.get("authors") or []
    hits.append(dict(source="s2", route=route, source_id=p["paperId"], doi=clean_doi(ids.get("DOI")),
                     title=p.get("title") or "", year=p.get("year") or "",
                     type=";".join(p.get("publicationTypes") or []), venue=p.get("venue") or "",
                     language="", first_author=(authors[0].get("name", "") if authors else ""),
                     cited_by=p.get("citationCount") or 0))
    abstracts.append([p["paperId"], clean_doi(ids.get("DOI")), p.get("abstract") or ""])
    return 1


def run_store(plan, dig):
    hits, abstracts, log = [], [], []
    with open(os.path.join(STORE, "library/manifest.csv"), newline="") as f:
        manifest = list(csv.DictReader(f))
    notes = {}
    for name in os.listdir(os.path.join(STORE, "sources")):
        if name.endswith(".md") and not name.startswith("._"):
            with open(os.path.join(STORE, "sources", name), encoding="utf-8", errors="replace") as f:
                notes[name[:-3]] = f.read()
    for route, concepts in plan.items():
        if concepts[0][0] == "cites":
            continue
        patterns = [[re.compile(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", re.I) for t in terms]
                    for _, terms in concepts]
        got = 0
        for row in manifest:
            text = (row.get("title") or "") + " " + (row.get("original_filename") or "") + " " + notes.get(row.get("key") or "", "")
            if all(any(p.search(text) for p in group) for group in patterns):
                sid = row.get("key") or row.get("sha256", "")[:12]
                hits.append(dict(source="store", route=route, source_id=sid, doi=clean_doi(row.get("doi")),
                                 title=row.get("title") or row.get("original_filename") or "",
                                 year=row.get("year") or "", type="", venue=row.get("container") or "",
                                 language="", first_author="", cited_by=""))
                abstracts.append([sid, clean_doi(row.get("doi")), ""])
                got += 1
        log.append(dict(run_at=now(), source="store", route=route, query=openalex_query(concepts),
                        reported=got, retrieved=got, cap="", status="ok", digest=dig))
    write("store", hits, abstracts, log)


if __name__ == "__main__":
    if not os.path.isdir(REVIEW):
        sys.exit("run from the repository root")
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    run = {"store": run_store, "openalex": run_openalex, "s2": run_s2}.get(which)
    if not run:
        sys.exit("usage: review_search.py store|openalex|s2")
    run(routes(), digest())
