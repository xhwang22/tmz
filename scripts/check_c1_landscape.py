#!/usr/bin/env python3
"""Independent full-cohort C1 fixture audit, not evidence of method efficacy."""
import csv
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
import re
import subprocess

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/simulated/c1_landscape"
METHODS = ("Static judge", "Static tools", "Prompt optimization", "Program search", "ERA")


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert rows and all(r["provenance"] == "SIMULATED" for r in rows), path
    return rows


def close(a, b):
    assert math.isclose(float(a), float(b), rel_tol=1e-10, abs_tol=1e-9), (a, b)


def index(rows, fields):
    out = {tuple(r[f] for f in fields): r for r in rows}
    assert len(out) == len(rows), fields
    return out


def main():
    manifest = json.loads((DATA / "manifest.json").read_text())
    assert manifest["simulation_only"] and not manifest["empirical_evidence"]
    assert manifest["generates_observations"] is False
    assert manifest["canvas_inches"] == [5.4, 3.57]
    assert manifest["requested_ood_inputs"] == 3520 and manifest["bootstrap_replicates"] == 2000
    assert manifest["methods"] == list(METHODS)
    expected_outputs = {str(p.relative_to(ROOT)) for p in DATA.glob("*.csv")}
    expected_outputs.update("figures/simulated/c1_landscape"+ext for ext in (".pdf", ".svg", ".png"))
    expected_outputs.update(("scripts/render_c1_landscape.py", "figures/c1_landscape.tex"))
    assert set(manifest["output_files"]) == expected_outputs
    assert set(manifest["source_files"]) == {"data/simulated/c1_groups.csv", "data/simulated/c1_cohorts.csv",
                                            "figures/simulated/landscape_outcomes.pdf"}
    for relative, digest in {**manifest["source_files"], **manifest["output_files"]}.items():
        path = (ROOT / relative).resolve()
        path.relative_to(ROOT)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, relative
    cohorts = read(ROOT / "data/simulated/c1_cohorts.csv")
    raw = defaultdict(dict)
    for row in read(ROOT / "data/simulated/c1_groups.csv"):
        if row["split"] == "OOD" and row["method"] in METHODS:
            key = (row["domain"], row["input_group"])
            assert row["method"] not in raw[key]
            raw[key][row["method"]] = row
    retained = index(read(DATA / "input-cohorts.csv"), ("domain", "input_group"))
    assert set(raw) == set(retained) and len(raw) == 3520
    for key, values in raw.items():
        assert set(values) == set(METHODS)
        assert int(retained[key]["complete_all_methods"]) == int(all(v["complete"] == "1" for v in values.values()))
    bars = index(read(DATA / "bars.csv"), ("domain", "method"))
    selection = index(read(DATA / "selection.csv"), ("domain", "method"))
    geometry = index(read(DATA / "bar-geometry.csv"), ("domain", "method"))
    expected = {(r["domain"], m) for r in cohorts for m in METHODS}
    assert set(bars) == set(selection) == set(geometry) == expected and len(expected) == 110
    for cohort in cohorts:
        domain = cohort["domain"]
        requested = sorted((gid, group) for (did, gid), group in raw.items() if did == domain)
        assert len(requested) == int(cohort["groups"]) == 160
        complete = [group for gid, group in requested if retained[(domain, gid)]["complete_all_methods"] == "1"]
        seed = int(hashlib.sha256(("c1-landscape-20260920|"+domain).encode()).hexdigest()[:16], 16)
        draws = np.random.default_rng(seed).integers(0, len(complete), (2000, len(complete)))
        for m in METHODS:
            r, s, g = bars[(domain, m)], selection[(domain, m)], geometry[(domain, m)]
            assert r["family"] == s["family"] == domain[3:5] and r["split"] == s["split"] == "OOD"
            assert int(r["complete_groups"]) == len(complete)
            assert int(r["requested_groups"]) == int(s["requested_groups"]) == 160
            values = np.asarray([float(group[m]["pairwise"]) for group in complete])
            lo, hi = np.quantile(values[draws].mean(axis=1), [.025, .975])
            for field, v in (("agreement_pct", values.mean()), ("lower_pct", lo), ("upper_pct", hi)):
                close(r[field], 100*v)
            successes = sum(float(group[m]["best_of_4"] or 0) for _, group in requested)
            close(s["successes"], successes)
            close(s["best_of_4_pct"], 100*successes/160)
            close(g["full_scale_height_inches"], .55)
            close(g["zero_inches"], .41)
            for geometric, field in (("mean_inches", "agreement_pct"), ("lower_inches", "lower_pct"), ("upper_inches", "upper_pct")):
                close(g[geometric], .41+.55*float(r[field])/100)
    points = index(read(DATA / "family-points.csv"), ("family", "method"))
    assert set(points) == {(f, m) for f in ("SV", "IG", "TG", "AR") for m in ("Static tools", "ERA")}
    for (family, method), r in points.items():
        b = [row for row in bars.values() if row["family"] == family and row["method"] == method]
        s = [row for row in selection.values() if row["family"] == family and row["method"] == method]
        assert int(r["domain_count"]) == len(b) == len(s) == (6 if family in ("SV", "IG") else 5)
        close(r["agreement_pct"], np.mean([float(x["agreement_pct"]) for x in b]))
        close(r["best_of_4_pct"], np.mean([float(x["best_of_4_pct"]) for x in s]))
        close(r["x_inches"], 3.18+(float(r["agreement_pct"])-68)/8*2.07)
        close(r["y_inches"], 1.88+(float(r["best_of_4_pct"])-47)/12*1.03)
    # A fixture must not be silently retuned into a uniformly favorable story.
    effects = [float(bars[(c["domain"], "ERA")]["agreement_pct"])-float(bars[(c["domain"], "Static tools")]["agreement_pct"]) for c in cohorts]
    assert min(effects) < 0 < max(effects)
    pdf = ROOT / "figures/simulated/c1_landscape.pdf"
    txt = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
    assert "SIMULATED" in txt and "not experimental results" in txt
    assert "IterEval" in txt and not re.search(r"\b(?:ERA|IPM)\b", txt)
    assert set(re.findall(r"\b(?:SV|IG|TG|AR)\d+\b", txt)) == {r["domain"][3:] for r in cohorts}
    fonts = subprocess.check_output(["pdffonts", str(pdf)], text=True)
    assert "Type 3" not in fonts and "SourceSans3" in fonts and "SourceSerif4" in fonts
    assert all(line.split()[-5] == "yes" for line in fonts.splitlines()[2:] if line.strip())
    print("C1 landscape: all 3,520 inputs, 110 common-cohort means/intervals, eight family points verified.")
    print("Old source/figure hashes, negative contrasts, embedded fonts, and SIMULATED disclosure preserved.")


if __name__ == "__main__":
    main()
