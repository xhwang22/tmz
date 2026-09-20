#!/usr/bin/env python3
"""Audit synthetic reporting fixtures offline; passing never establishes evidence.

Uses only the standard library and Poppler's pdftotext. --submission is a
deliberately failing gate while the manuscript contains simulated results.
The audit recomputes exported quantities independently of the plotting code.
"""

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
import re
import statistics
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/simulated"
CHARTS = ("outcomes", "alignment", "acquisition", "annotation", "selection", "ablation", "refinement", "cost")
METHODS = ("Single metric", "Metric ensemble", "Static judge", "Static tools",
           "Prompt optimization", "Program search", "ERA")
METRICS = ("pairwise", "top_region", "best_of_4", "rank_regret")
SETTINGS = ("Reuse", "Collect")
SPLITS = ("ID", "OOD")
GROUPS = 160
ERRORS = []


def require(condition, message):
    if not condition and len(ERRORS) < 60:
        ERRORS.append(message)


def close(actual, expected, context, tolerance=2e-7):
    require(math.isclose(float(actual), float(expected), abs_tol=tolerance, rel_tol=1e-7),
            f"{context}: got {actual}, expected {expected}")


def bounded(value, lower, upper, context):
    value = float(value)
    require(math.isfinite(value) and lower - 1e-8 <= value <= upper + 1e-8,
            f"{context}: outside [{lower}, {upper}]")


def rows(name):
    require(b"\r" not in (DATA / name).read_bytes(),
            f"Fixture must use canonical LF line endings: {name}")
    with (DATA / name).open(newline="", encoding="utf-8") as source:
        result = list(csv.DictReader(source))
    require(bool(result), f"Empty fixture: {name}")
    require(all(r.get("provenance") == "SIMULATED" for r in result),
            f"Missing per-row SIMULATED provenance: {name}")
    return result


def index_unique(records, fields, context):
    index = {tuple(r[f] for f in fields): r for r in records}
    require(len(index) == len(records), f"Duplicate keys: {context}")
    return index


def check_manifest():
    manifest = json.loads((DATA / "manifest.json").read_text())
    require(manifest.get("simulation_only") is True, "Simulation-only flag changed")
    require(manifest.get("empirical_evidence") is False, "Fixtures must never be empirical evidence")
    for key, value in {"seed": 20260916, "cohort_groups": GROUPS,
                       "candidates_per_c1_group": 4, "complete_scores_per_candidate": 3,
                       "bootstrap_replicates": 1000}.items():
        require(manifest.get(key) == value, f"Unexpected design constant: {key}")
    expected = ({str(p.relative_to(ROOT)) for p in DATA.glob("*.csv")}
                | {f"figures/simulated/{name}.pdf" for name in CHARTS}
                | {f"figures/simulated_{name}.tex" for name in CHARTS}
                | {"figures/simulated/c1_table.tex", "scripts/render_simulated_results.py"})
    require(set(manifest["files"]) == expected, "Manifest does not cover the exact fixture set")
    for relative, digest in manifest["files"].items():
        path = (ROOT / relative).resolve()
        path.relative_to(ROOT)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"Stale fixture or generator hash: {relative}")
    for name in CHARTS:
        pdf = ROOT / f"figures/simulated/{name}.pdf"
        require(pdf.read_bytes().startswith(b"%PDF-"), f"Invalid vector PDF: {name}")
        text = subprocess.run(["pdftotext", str(pdf), "-"], check=True,
                              capture_output=True, text=True).stdout
        text = " ".join(text.split())
        require("SIMULATED DATA" in text and "NOT EXPERIMENTAL RESULTS" in text,
                f"Missing visible disclosure inside chart: {name}")
        if name in ("outcomes", "alignment"):
            expected_codes = {f"{family}{i}" for family, count in (("SV", 6), ("IG", 6), ("TG", 5), ("AR", 5))
                              for i in range(1, count + 1)}
            plotted_codes = set(re.findall(r"\b(?:SV|IG|TG|AR)\d+\b", text))
            require(plotted_codes == expected_codes, f"{name}: not all 22 domain labels are visible")
        wrapper = (ROOT / f"figures/simulated_{name}.tex").read_text()
        require(r"\includegraphics[width=5.4in]" in wrapper,
                f"Native figure width changed: {name}")
    for path in DATA.glob("*.csv"):
        rows(path.name)
    return manifest


def check_c1(cohorts):
    records = rows("c1_groups.csv")
    index = index_unique(records, ("domain", "split", "input_group", "method"), "C1 groups")
    require(len(index) == len(cohorts) * 2 * GROUPS * len(METHODS), "Wrong C1 group count")
    grouped = defaultdict(list)
    identities = {}
    for r in records:
        domain, split, group, method = (r[k] for k in ("domain", "split", "input_group", "method"))
        require(domain in cohorts and r["setting"] == cohorts[domain]["setting"], "C1 cohort mismatch")
        require(split in SPLITS and method in METHODS and group.startswith("SIM-"), "Unexpected C1 identity")
        key = (domain, split, group)
        order = tuple(map(int, r["human_order"].split("|")))
        require(sorted(order) == list(range(4)), "C1 requires a complete four-candidate ranking")
        require(identities.setdefault(key, order) == order, "Methods do not share the C1 ranking")
        scores = tuple(map(float, r["median_scores"].split("|")))
        require(len(scores) == 4 and all(map(math.isfinite, scores)), "Invalid C1 score vector")
        require(r["complete"] in ("0", "1"), "Invalid completeness indicator")
        require(math.isfinite(float(r["cost_units"])) and float(r["cost_units"]) > 0, "Invalid toy cost")
        grouped[(domain, split, method)].append(r)
        if r["complete"] == "0":
            require(all(r[m] == "" for m in METRICS), "Incomplete scores must remain missing")
            continue
        ranks = {candidate: rank for rank, candidate in enumerate(order)}
        good, top = [], []
        for a, b in itertools.combinations(range(4), 2):
            correct = float((scores[a] - scores[b]) * (ranks[b] - ranks[a]) > 0)
            good.append(correct)
            if min(ranks[a], ranks[b]) < 2:
                top.append(correct)
        chosen_rank = ranks[max(range(4), key=lambda i: scores[i])]
        expected = (statistics.mean(good), statistics.mean(top), int(chosen_rank == 0), chosen_rank / 3)
        for metric, value in zip(METRICS, expected):
            bounded(r[metric], 0, 1, metric)
            close(r[metric], value, f"Group metric {metric}")
    require(set(grouped) == set(itertools.product(cohorts, SPLITS, METHODS)), "C1 cell coverage changed")
    for cell in grouped.values():
        require(len(cell) == GROUPS, "C1 cell is not a complete input cohort")
    for domain, split in itertools.product(cohorts, SPLITS):
        groups = [{r["input_group"] for r in grouped[(domain, split, method)]} for method in METHODS]
        require(all(g == groups[0] for g in groups), "Unmatched C1 input pools")

    summaries = rows("c1_summary.csv")
    summary_index = index_unique(summaries, ("domain", "split", "method", "metric"), "C1 summary")
    require(set(summary_index) == set(itertools.product(cohorts, SPLITS, METHODS, METRICS)),
            "C1 summary coverage changed")
    for r in summaries:
        cell = grouped[(r["domain"], r["split"], r["method"])]
        require(r["setting"] == cohorts[r["domain"]]["setting"], "C1 summary setting mismatch")
        complete = [g for g in cell if g["complete"] == "1"]
        close(r["mean"], statistics.mean(float(g[r["metric"]]) for g in complete), "C1 mean")
        close(r["coverage"], len(complete) / GROUPS, "C1 coverage")
        close(r["cost_units"], statistics.mean(float(g["cost_units"]) for g in cell), "C1 cost", 1e-6)
        for key in ("mean", "lower", "upper"):
            bounded(r[key], 0, 1, f"C1 {key}")
        require(float(r["lower"]) <= float(r["mean"]) <= float(r["upper"]), "Invalid C1 interval")

    effects = rows("alignment_effects.csv")
    effect_index = index_unique(effects, ("domain", "split"), "Paired alignment effects")
    require(set(effect_index) == set(itertools.product(cohorts, SPLITS)), "Missing paired effect")
    for r in effects:
        pairs = [(index[(r["domain"], r["split"], g["input_group"], "ERA")], g)
                 for g in grouped[(r["domain"], r["split"], "Static tools")]]
        paired = [100 * (float(a["pairwise"]) - float(b["pairwise"]))
                  for a, b in pairs if a["complete"] == b["complete"] == "1"]
        close(r["delta_pp"], statistics.mean(paired), "Paired alignment difference", 2e-6)
        require(int(r["complete_pairs"]) == len(paired), "Paired effect denominator mismatch")
        for key in ("delta_pp", "lower", "upper"):
            bounded(r[key], -100, 100, f"Effect {key}")
        require(float(r["lower"]) <= float(r["delta_pp"]) <= float(r["upper"]), "Invalid paired interval")

    coverage = rows("macro_coverage.csv")
    coverage_index = index_unique(coverage, ("setting", "split", "method"), "Macro coverage")
    require(set(coverage_index) == set(itertools.product(SETTINGS, SPLITS, METHODS)), "Coverage cells changed")
    for r in coverage:
        values = [float(summary_index[(d, r["split"], r["method"], "pairwise")]["coverage"])
                  for d, c in cohorts.items() if c["setting"] == r["setting"]]
        close(r["macro_coverage"], statistics.mean(values), "Macro coverage")

    ranks = rows("selection_ranks.csv")
    rank_index = index_unique(ranks, ("setting", "method", "selected_rank"), "Selected ranks")
    selected = ("Static judge", "Static tools", "Program search", "ERA")
    require(set(rank_index) == set(itertools.product(SETTINGS, selected, ("1", "2", "3", "4", "unscored"))),
            "Selection rank cells changed")
    for setting, method in itertools.product(SETTINGS, selected):
        pool = [g for d, c in cohorts.items() if c["setting"] == setting for g in grouped[(d, "ID", method)]]
        counts = Counter("unscored" if g["complete"] == "0" else
                         str(round(float(g["rank_regret"]) * 3) + 1) for g in pool)
        for rank in ("1", "2", "3", "4", "unscored"):
            r = rank_index[(setting, method, rank)]
            require(int(r["denominator"]) == len(pool) and int(r["count"]) == counts[rank],
                    "Selected ranks must retain all input groups")
            close(r["share_pct"], 100 * counts[rank] / len(pool), "Selected rank share")

    # Build an independent textual expectation for the generated numerical table.
    table = (ROOT / "figures/simulated/c1_table.tex").read_text()
    actual = [line.strip() for line in table.splitlines() if any(line.startswith(m + " & ") for m in METHODS)]
    expected = []
    for setting, method in itertools.product(SETTINGS, METHODS):
        cells = []
        for split, metric in itertools.product(SPLITS, METRICS):
            values = [float(summary_index[(d, split, method, metric)]["mean"])
                      for d, c in cohorts.items() if c["setting"] == setting]
            mean = statistics.mean(values)
            cells.append(f"{mean:.2f}" if metric == "rank_regret" else f"{100 * mean:.1f}")
        expected.append(method + " & " + " & ".join(cells) + r" \\")
    require(actual == expected, "Numerical TeX table and C1 data disagree")
    require(table.count(r"\textbf{SIMULATED}") == 2, "Table setting disclosures missing")

    costs = rows("cost_summary.csv")
    cost_index = index_unique(costs, ("setting", "method"), "Cost summary")
    require(set(cost_index) == set(itertools.product(SETTINGS, METHODS)), "Cost comparison cells changed")
    for r in costs:
        means = [summary_index[(d, "ID", r["method"], "pairwise")]
                 for d, c in cohorts.items() if c["setting"] == r["setting"]]
        close(r["agreement_pct"], 100 * statistics.mean(float(m["mean"]) for m in means), "Cost plot agreement")
        close(r["cost_units"], statistics.mean(float(m["cost_units"]) for m in means), "Cost plot cost")


def check_annotation(cohorts):
    records = rows("annotation_groups.csv")
    index_unique(records, ("domain", "input_group"), "Annotation groups")
    require(len(records) == GROUPS * len(cohorts), "Annotation cohort size changed")
    grouped = defaultdict(list)
    for r in records:
        votes = [int(r[f"rater_{i}"]) for i in range(1, 4)]
        require(set(votes) <= {-1, 0, 1, 2}, "Unknown rater code")
        valid = [v for v in votes if v >= 0]
        counts = Counter(valid)
        comparisons = [int(a == b) for a, b in itertools.combinations(valid, 2)]
        if comparisons:
            close(r["group_agreement"], statistics.mean(comparisons), "Within-group agreement")
        else:
            require(math.isnan(float(r["group_agreement"])), "Agreement without two valid raters")
        outcome = ("insufficient votes" if len(valid) < 2 else "no consensus" if max(counts.values()) < 2
                   else "tie" if counts[2] >= 2 else "decisive")
        require(r["group_outcome"] == outcome, "Consensus rule mismatch")
        require(r["domain"] in cohorts and r["setting"] == cohorts[r["domain"]]["setting"], "Annotation cohort mismatch")
        grouped[r["domain"]].append(r)
    summaries = rows("annotation_summary.csv")
    index = index_unique(summaries, ("domain",), "Annotation summary")
    require(set(index) == {(d,) for d in cohorts}, "Annotation domain coverage changed")
    for r in summaries:
        groups = grouped[r["domain"]]
        require(len(groups) == GROUPS, "Unbalanced annotation cohort")
        valid = [float(g["group_agreement"]) for g in groups if math.isfinite(float(g["group_agreement"]))]
        close(r["agreement_pct"], 100 * statistics.mean(valid), "Mean eligible-group agreement")
        abstentions = sum(int(g[f"rater_{i}"]) == -1 for g in groups for i in range(1, 4))
        close(r["abstention_pct"], 100 * abstentions / (3 * GROUPS), "Requested-rating abstention")
        for name, value in (("decisive_pct", "decisive"), ("tie_pct", "tie"),
                            ("no_consensus_pct", "no consensus"), ("insufficient_pct", "insufficient votes")):
            close(r[name], 100 * sum(g["group_outcome"] == value for g in groups) / GROUPS, "Group outcome share")
        require(float(r["lower"]) <= float(r["agreement_pct"]) <= float(r["upper"]), "Annotation interval reversed")


def check_other_fixtures(cohorts):
    policies = ("Random", "Uncertainty", "Model conflict", "Run instability", "Multi-source")
    acquisition = rows("acquisition.csv")
    index = index_unique(acquisition, ("setting", "policy", "synthetic_run", "human_units"), "Acquisition")
    require(set(index) == set(itertools.product(SETTINGS, policies, map(str, range(12)), ("20", "50", "100", "200"))),
            "Acquisition budgets, controls, or toy-run count changed")
    for r in acquisition:
        require(int(r["anchor_units"]) == 10 < int(r["human_units"]), "Matched random anchor is missing")
        bounded(r["agreement_pct"], 0, 100, "Acquisition agreement")

    effects = rows("component_effects.csv")
    index_unique(effects, ("domain", "component", "input_group"), "Component effects")
    require(len(effects) == len(cohorts) * 6 * GROUPS, "Component cohort size changed")
    for domain in cohorts:
        groups = [{r["input_group"] for r in effects if r["domain"] == domain and r["component"] == comp}
                  for comp in ("A", "K", "V", "T", "Π", "G")]
        require(all(len(g) == GROUPS and g == groups[0] for g in groups), "Unpaired component contrasts")
    for r in effects:
        bounded(r["delta_pp"], -100, 100, "Toy component effect")
        require(r["setting"] == cohorts[r["domain"]]["setting"], "Component setting mismatch")

    levels = ("H0", "H0+H1", "H0+H1+H2", "H0+H1+H2+H3")
    granularity = rows("granularity.csv")
    index_unique(granularity, ("setting", "input_group", "feedback"), "Granularity")
    require(len(granularity) == 2 * len(levels) * GROUPS, "Granularity cohort size changed")
    for setting in SETTINGS:
        groups = [{r["input_group"] for r in granularity if r["setting"] == setting and r["feedback"] == h}
                  for h in levels]
        require(all(len(g) == GROUPS and g == groups[0] for g in groups), "Granularity comparison is not paired")
    for r in granularity:
        bounded(r["agreement_pct"], 0, 100, "Granularity value")

    refinements = rows("refinement_groups.csv")
    index_unique(refinements, ("domain", "input_group"), "Refinements")
    require(Counter(r["domain"] for r in refinements) == Counter({d: GROUPS for d in cohorts}),
            "Refinement domain coverage changed")
    for r in refinements:
        y0, seed, era = (float(r[k]) for k in ("y0_quality", "seed_quality", "era_quality"))
        require(all(map(math.isfinite, (y0, seed, era))), "Nonfinite C2 latent utility")
        expected = "Tie" if abs(era - seed) < .15 else "ERA wins" if era > seed else "Seed wins"
        require(r["blinded_outcome"] in (expected, "Abstain"), "C2 preference threshold mismatch")
        require(int(r["seed_major_regression"]) == int(seed - y0 < -.8), "C2 seed regression mismatch")
        require(int(r["era_major_regression"]) == int(era - y0 < -.8), "C2 ERA regression mismatch")
        require(r["setting"] == cohorts[r["domain"]]["setting"], "Refinement setting mismatch")


def check_evidence_boundary():
    claims = json.loads((ROOT / ".paper/claims.yml").read_text())["claims"]
    for cid in ("C27", "C28"):
        claim = next(c for c in claims if c["id"] == cid)
        require(claim["status"] == "gap" and not claim.get("evidence_artifacts"),
                f"{cid}: a simulation must not close an empirical evidence gap")
    sources = "\n".join((ROOT / f"sections/{s}.tex").read_text() for s in ("results", "appendix"))
    for block in re.findall(r"\\begin\{figure\}[\s\S]*?\\end\{figure\}", sources):
        if r"\input{figures/simulated_" in block:
            require(r"\caption{\textbf{Simulated" in block, "Simulated chart caption lost its disclosure")
        if r"\input{figures/c1_landscape}" in block:
            require("simulated reporting layout, not experimental results" in block,
                    "Main-text C1 chart caption lost its disclosure")
    main = (ROOT / "main.tex").read_text()
    disclosures = (
        "quantitative displays use simulated data",
        "results are placeholders or simulated illustrations",
    )
    require(any(disclosure in main for disclosure in disclosures)
            and "empirical evaluation pending" in main,
            "Title-page draft disclosure missing")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submission", action="store_true", help="Reject simulated reporting fixtures")
    args = parser.parse_args()
    try:
        check_manifest()
        cohorts = {r["domain"]: r for r in rows("cohorts.csv")}
        require(len(cohorts) == 8, "Eight illustrative diagnostic cohorts are required")
        require(Counter(c["setting"] for c in cohorts.values()) == {"Reuse": 4, "Collect": 4},
                "Both settings must have four toy diagnostic cohorts")
        require(all(int(c["groups"]) == GROUPS for c in cohorts.values()), "Cohort groups changed")
        c1_cohorts = {r["domain"]: r for r in rows("c1_cohorts.csv")}
        expected_domains = {f"TD-{family}{i}" for family, count in (("SV", 6), ("IG", 6), ("TG", 5), ("AR", 5))
                            for i in range(1, count + 1)}
        require(set(c1_cohorts) == expected_domains, "C1 must cover all 22 source-plan domains")
        require(Counter(c["setting"] for c in c1_cohorts.values()) == {"Reuse": 11, "Collect": 11},
                "C1 must have eleven illustrative cohorts per setting")
        require(Counter(c["family"] for c in c1_cohorts.values()) == {
            "Structured visuals": 6, "Images / 3D": 6, "Text generation": 5, "Automated research": 5},
            "The C1 taxonomy must retain the 6/6/5/5 family structure")
        require(all(int(c["groups"]) == GROUPS for c in c1_cohorts.values()), "C1 cohort groups changed")
        require(all(c1_cohorts[d]["setting"] == c["setting"] for d, c in cohorts.items()),
                "Diagnostic and C1 cohort assignments disagree")
        check_c1(c1_cohorts)
        check_annotation(cohorts)
        check_other_fixtures(cohorts)
        check_evidence_boundary()
    except (OSError, ValueError, KeyError, TypeError, StopIteration, subprocess.SubprocessError) as exc:
        ERRORS.append(f"Cannot audit fixtures: {exc}")
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Simulation audit passed: provenance, hashes, paired metrics, denominators, tables, and disclosures.")
    print(f"Simulated C1 coverage: {len(c1_cohorts)} domains; diagnostic subset: {len(cohorts)} domains.")
    print(f"{len(CHARTS)} vector charts; no empirical claims, model execution, or human study established.")
    if args.submission:
        print("SUBMISSION BLOCKED: replace simulated fixtures with authorized measurements and re-audit claims.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
