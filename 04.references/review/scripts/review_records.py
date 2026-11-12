#!/usr/bin/env python3
"""Merge the search hits into the screening table, and draw screening batches.

Usage, from the repository root
  python3 04.references/review/scripts/review_records.py merge
  python3 04.references/review/scripts/review_records.py pilot
  python3 04.references/review/scripts/review_records.py batch <name> <ids file>

merge joins hits that share a DOI, then hits with no DOI that share a title, and writes one
row per unique record to 02.inputs/derived/review-records.csv. A record's identifier is drawn
from its DOI or title, so it stays the same when the searches run again, and screening
columns already entered are carried over by identifier.

pilot draws 12 records at random for each of the five questions, seed 20261111, without
drawing any record twice, and writes their identifiers to 02.inputs/derived/review-pilot-ids.csv.

batch writes the records named in an identifier file, with their abstracts, to
02.inputs/review/raw/batch-<name>.csv for a reader. That file stays out of git.
"""
import csv
import glob
import hashlib
import os
import random
import re
import sys

DERIVED = "02.inputs/derived"
RAW = "02.inputs/review/raw"
RECORDS = os.path.join(DERIVED, "review-records.csv")
SCREEN = ["reader_a", "reader_a_reason", "reader_a_questions", "reader_b", "reader_b_reason",
          "reader_b_questions", "decision", "reason", "questions", "settled_by", "full_text"]
FIELDS = ["record_id", "doi", "title", "year", "type", "venue", "language", "first_author",
          "routes", "questions_searched", "sources", "has_abstract"] + SCREEN


def norm_title(t):
    return re.sub(r"[^a-z0-9]", "", (t or "").lower())


def load_hits():
    hits = []
    for path in sorted(glob.glob(os.path.join(DERIVED, "review-hits-*.csv"))):
        with open(path, newline="") as f:
            hits.extend(csv.DictReader(f))
    abstracts = {}
    for path in sorted(glob.glob(os.path.join(RAW, "review-abstracts-*.csv"))):
        source = os.path.basename(path)[len("review-abstracts-"):-4]
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                abstracts[(source, row["source_id"])] = row["abstract"]
    return hits, abstracts


def merge():
    hits, abstracts = load_hits()
    groups, by_doi, by_title = [], {}, {}
    for h in hits:
        t = norm_title(h["title"])
        g = None
        if h["doi"] and h["doi"] in by_doi:
            g = by_doi[h["doi"]]
        elif t and t in by_title:
            g = by_title[t]
        if g is None:
            g = len(groups)
            groups.append([])
        groups[g].append(h)
        if h["doi"]:
            by_doi.setdefault(h["doi"], g)
        if t:
            by_title.setdefault(t, g)
    old = {}
    if os.path.exists(RECORDS):
        with open(RECORDS, newline="") as f:
            old = {r["record_id"]: r for r in csv.DictReader(f)}
    rows, texts = [], {}
    for members in groups:
        doi = next((m["doi"] for m in members if m["doi"]), "")
        title = max((m["title"] for m in members), key=len)
        key = doi or norm_title(title)
        rid = "r" + hashlib.sha1(key.encode()).hexdigest()[:8]
        best = max((abstracts.get((m["source"], m["source_id"]), "") for m in members), key=len)
        texts[rid] = best
        first = lambda field: next((m[field] for m in members if m[field]), "")
        routes = sorted({m["route"] for m in members})
        row = dict(record_id=rid, doi=doi, title=title, year=first("year"), type=first("type"),
                   venue=first("venue"), language=first("language"), first_author=first("first_author"),
                   routes=" ".join(routes),
                   questions_searched=" ".join(sorted({r[:2] for r in routes})),
                   sources=" ".join(sorted({m["source"] for m in members})),
                   has_abstract="yes" if len(best.split()) >= 30 else "no")
        for c in SCREEN:
            row[c] = old.get(rid, {}).get(c, "")
        rows.append(row)
    rows.sort(key=lambda r: r["record_id"])
    with open(RECORDS, "w", newline="") as f:
        w = csv.DictWriter(f, FIELDS)
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(RAW, "review-abstracts.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["record_id", "abstract"])
        w.writerows(sorted(texts.items()))
    print(f"{len(hits)} hits, {len(rows)} unique records, "
          f"{sum(r['has_abstract'] == 'yes' for r in rows)} with an abstract of 30 words or more")
    for q in ["q1", "q2", "q3", "q4", "q5"]:
        print(q, sum(q in r["questions_searched"].split() for r in rows))


def read_records():
    with open(RECORDS, newline="") as f:
        return list(csv.DictReader(f))


def pilot():
    rows = read_records()
    rng = random.Random(20261111)
    taken = []
    for q in ["q1", "q2", "q3", "q4", "q5"]:
        pool = [r["record_id"] for r in rows if q in r["questions_searched"].split() and r["record_id"] not in taken]
        taken += rng.sample(sorted(pool), 12)
    with open(os.path.join(DERIVED, "review-pilot-ids.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["record_id"])
        w.writerows([[i] for i in taken])
    print(len(taken), "pilot records")


def batch(name, ids_file):
    with open(ids_file, newline="") as f:
        ids = [r["record_id"] for r in csv.DictReader(f)]
    rows = {r["record_id"]: r for r in read_records()}
    with open(os.path.join(RAW, "review-abstracts.csv"), newline="") as f:
        abstracts = {r["record_id"]: r["abstract"] for r in csv.DictReader(f)}
    out = os.path.join(RAW, f"batch-{name}.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["record_id", "title", "year", "venue", "language", "type", "abstract"])
        for i in ids:
            r = rows[i]
            w.writerow([i, r["title"], r["year"], r["venue"], r["language"], r["type"], abstracts.get(i, "")])
    print(len(ids), "records written to", out)


def agree(path_a, path_b):
    """Agreement of two readers. Undecided counts with include, since both go on to full text."""
    def load(p):
        with open(p, newline="") as f:
            return {r["record_id"]: r for r in csv.DictReader(f)}
    a, b = load(path_a), load(path_b)
    ids = sorted(set(a) & set(b))
    if set(a) != set(b):
        print("records in one reader only", sorted(set(a) ^ set(b)))
    keep = lambda d: "exclude" if d == "exclude" else "keep"
    pairs = [(keep(a[i]["decision"]), keep(b[i]["decision"])) for i in ids]
    n = len(pairs)
    po = sum(x == y for x, y in pairs) / n
    pa = sum(x == "keep" for x, _ in pairs) / n
    pb = sum(y == "keep" for _, y in pairs) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")
    three = sum(a[i]["decision"] == b[i]["decision"] for i in ids)
    print(f"{n} records, keep or exclude agreed on {sum(x == y for x, y in pairs)}, kappa {kappa:.2f}, "
          f"all three decisions agreed on {three}")
    print(f"reader A kept {sum(x == 'keep' for x, _ in pairs)}, reader B kept {sum(y == 'keep' for _, y in pairs)}")
    return [i for i in ids if keep(a[i]["decision"]) != keep(b[i]["decision"])]


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "merge":
        merge()
    elif cmd == "pilot":
        pilot()
    elif cmd == "batch" and len(sys.argv) == 4:
        batch(sys.argv[2], sys.argv[3])
    elif cmd == "agree" and len(sys.argv) == 4:
        for i in agree(sys.argv[2], sys.argv[3]):
            print("disagree", i)
    else:
        sys.exit(__doc__)
