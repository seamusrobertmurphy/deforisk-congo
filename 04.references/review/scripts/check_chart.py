import csv, re, sys

reader, name = sys.argv[1], sys.argv[2]
batch = list(csv.DictReader(open(f"02.inputs/review/raw/batch-chart-{name}.csv", newline="")))
ab = {r["record_id"]: " ".join(r["abstract"].split()) for r in batch}
rows = list(csv.DictReader(open(f"02.inputs/derived/chart/reader-{reader}-{name}.csv", newline="")))
FIELDS = ["record_id", "questions", "place", "area", "period", "data", "own_map", "method",
          "predictors", "validation", "measures", "purpose", "finding", "gap_quote"]
PURPOSE = {"research", "conservation planning", "REDD+ reference level", "carbon crediting",
           "national monitoring", "policy assessment", "other"}
OWN = {"yes", "no", "both", "not stated"}
problems = []
if list(rows[0].keys()) != FIELDS:
    problems.append(("header", list(rows[0].keys())))
if [r["record_id"] for r in rows] != [r["record_id"] for r in batch]:
    problems.append(("order", "wrong"))
for r in rows:
    i = r["record_id"]
    if not re.fullmatch(r"(q[1-8])( q[1-8])*", r["questions"]):
        problems.append((i, "questions", r["questions"]))
    if r["own_map"] not in OWN:
        problems.append((i, "own_map", r["own_map"]))
    if r["purpose"] not in PURPOSE:
        problems.append((i, "purpose", r["purpose"]))
    if len(r["finding"].split()) > 30:
        problems.append((i, "finding words", len(r["finding"].split())))
    for k in FIELDS[1:-1]:
        if re.search(r"[–—:;]|--", r[k]) or not r[k].strip():
            problems.append((i, k, "dash, colon, semicolon or empty", r[k][:60]))
    q = " ".join(r["gap_quote"].split())
    if q and q not in ab.get(i, ""):
        problems.append((i, "gap_quote not verbatim", q[:60]))
    if len(q.split()) > 60:
        problems.append((i, "gap_quote words", len(q.split())))
print(reader, name, len(rows), "rows", "problems", len(problems))
for p in problems:
    print(" ", p)
