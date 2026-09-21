#!/usr/bin/env python3
"""Check assigned aggregates and their exports, not experimental validity."""
import argparse
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path
import re
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/ideal_scenario"
OUT = ROOT / "figures/ideal_scenario"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def close(actual, expected, message, tolerance=0.051):
    require(abs(float(actual) - float(expected)) <= tolerance, message)


def preference(counts):
    w, t, l = map(int, counts.split("/"))
    return 100 * (w + t / 2) / (w + t + l)


def audit():
    d = json.loads((DATA / "scenario.json").read_text())
    manifest = json.loads((DATA / "manifest.json").read_text())
    require(d["provenance"] == "SIMULATED_IDEAL_SCENARIO" and d["empirical_evidence"] is False,
            "Assigned aggregates must not be relabeled as observations")
    for flag in ("simulation_only", "aggregate_scenario_only", "no_statistical_inference"):
        require(manifest[flag] is True, f"Missing disclosure: {flag}")
    require(manifest["empirical_evidence"] is False, "Manifest misstates empirical status")
    expected = {str(p.relative_to(ROOT)) for p in OUT.iterdir() if p.suffix in {".tex", ".pdf", ".svg", ".png"}}
    expected |= {"data/ideal_scenario/scenario.json", "scripts/render_ideal_scenario.py", "scripts/render_c1_landscape.py"}
    require(set(manifest["files"]) == expected, "Manifest does not cover the exact source/export set")
    for name, digest in manifest["files"].items():
        p = (ROOT / name).resolve()
        p.relative_to(ROOT)
        require(hashlib.sha256(p.read_bytes()).hexdigest() == digest, f"Stale export/source: {name}; run make ideal")

    n = len(d["methods"])
    require(n == 7 and len(set(d["methods"])) == n, "Seven distinct main methods required")
    require(len(d["pair"]) == n and all(len(row) == len(d["design"]["domains"]) for row in d["pair"]), "Domain/method shape mismatch")
    for key in ("bon", "reg", "coverage", "top", "cost", "resourceRows"):
        require(len(d[key]) == n, f"Method count mismatch: {key}")
    means = list(map(statistics.mean, d["pair"]))
    main_rows = [line.split(" & ") for line in (OUT / "main.tex").read_text().splitlines() if " & " in line][:n]
    for i, row in enumerate(main_rows):
        close(row[1], means[i], "Main agreement differs from equal-domain mean")
        close(row[2], d["bon"][i], "Main selection mismatch")
        close(row[3], d["reg"][i], "Main regret mismatch", .00051)
        close(row[4].rstrip("\\"), d["coverage"][i], "Main coverage mismatch")
        require(d["resourceRows"][i][0] == d["methods"][i], "Cost-table method order mismatch")
        close(d["resourceRows"][i][3], d["cost"][i], "Deployment cost differs between table and plot", .0001)

    for study, domain, row in d["downstream"]:
        close(row[1], preference(row[0]), f"Tie-adjusted preference mismatch: {study}/{domain}")
        require(sum(map(int, row[0].split("/"))) == int(row[3]), "Downstream count mismatch")
    for row in d["downstreamDetail"]:
        close(row[2], preference(row[1]), f"Detail preference mismatch: {row[0]}")
        judged, requested = map(int, row[-1].split("/"))
        require(sum(map(int, row[1].split("/"))) == judged <= requested, "Detail denominator mismatch")
    c2 = [list(map(int, row[0].split("/"))) for study, domain, row in d["downstream"] if study == "C2"]
    pooled = [sum(row[i] for row in c2) for i in range(3)]
    detail = next(row for row in d["downstreamDetail"] if row[0] == "C2: IterEval / Seed")
    require(detail[1] == "/".join(map(str, pooled)), "C2 main/detail counts disagree")

    controls = [float(row[1]) for row in d["searchRows"]]
    for row in d["searchRows"]:
        close(row[2], float(row[1]) - controls[3], "Search contrast mismatch")
    for i, curve in enumerate(d["heldoutCurves"].values()):
        require(len(curve) == len(d["checkpoints"]), "Checkpoint shape mismatch")
        close(curve[-1], controls[i], "Search endpoint differs from control table")
    close(controls[3], means[-1], "Full IterEval differs across tables")
    for curve in d["devCurves"].values():
        require(len(curve) == len(d["checkpoints"]) and all(a <= b for a,b in zip(curve, curve[1:])), "Best-development curve must not decrease")
    require(sum(d["directionOutcomes"]["counts"]) == 100, "Direction shares must partition 100%")
    mining = [float(row[4]) for row in d["miningRows"][:4]]
    for name, row_index in (("Random", 2), ("Mined", 3), ("Uncertainty", 4)):
        close(d["miningCurves"][name][d["labelBudgets"].index(100)], d["miningRows"][row_index][4], "Mining curve/table endpoint mismatch")
    close(mining[3], controls[3], "Full mined condition differs across studies")
    close(mining[1], controls[1], "History-only mined condition differs across studies")

    values = dict(re.findall(r"\\newcommand\{\\(Result\w+)\}\{([^}]+)\}", (OUT / "numbers.tex").read_text()))
    derived = {
        "ResultPair": means[-1], "ResultSeedGain": means[-1]-means[1],
        "ResultGepaGain": means[-1]-means[4], "ResultDeployCost": d["cost"][-1]/d["cost"][1],
        "ResultParentGain": controls[3]-controls[2], "ResultDirectionGain": controls[2]-controls[1],
        "ResultHistoryGain": controls[1]-controls[0],
        "ResultInteraction": (mining[3]-mining[2])-(mining[1]-mining[0]),
        "ResultCtwoPreference": preference(detail[1]),
        "ResultCthreePreference": preference(next(row[0] for study, domain, row in d["downstream"] if study == "C3")),
    }
    require(set(values) == set(derived), "Prose-number macro coverage mismatch")
    for name, expected in derived.items():
        close(values[name], expected, f"Prose macro mismatch: {name}")
    rounded = str(Decimal(str(derived["ResultCtwoPreference"])).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
    require(values["ResultCtwoPreference"] == rounded, "C2 prose uses a different rounding rule from its table")

    sources = "\n".join((ROOT / f"sections/{name}.tex").read_text() for name in ("experiments", "results", "appendix"))
    for block in re.findall(r"\\begin\{(?:figure|table|longtable)\}[\s\S]*?\\end\{(?:figure|table|longtable)\}", sources):
        if "ideal_scenario/" in block or re.search(r"figures/(?:results_landscape|search_dynamics|mining_results)_pending", block) or "\\IdealDomainRows" in block:
            require("Simulated ideal scenario" in block, "Active numerical caption lost its disclosure")
    require("quantitative displays use simulated data" in (ROOT / "main.tex").read_text(), "Title-page notice missing")
    claims = json.loads((ROOT / ".paper/claims.yml").read_text())["claims"]
    require(all(c["status"] == "gap" and not c["evidence_artifacts"] for c in claims if c["id"] in {"C27", "C28"}), "Scenario must not close empirical gaps")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submission", action="store_true")
    args = parser.parse_args()
    try:
        audit()
    except (ValueError, KeyError, OSError, StopIteration) as exc:
        sys.exit(f"ERROR: {exc}")
    print("Ideal-scenario exports, aggregate arithmetic, prose numbers and disclosures agree. No empirical validation.")
    if args.submission:
        sys.exit("SUBMISSION BLOCKED: replace assigned aggregates with audited observations and revise claims.")
