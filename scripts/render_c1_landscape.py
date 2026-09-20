#!/usr/bin/env python3
"""Reuse the approved landscape geometry with full-cohort C1 layout fixtures.

No observations are generated or changed. Read only the existing SIMULATED
input records; write derived summaries and a new figure, never the old one.
"""
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
import urllib.request

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import Rectangle, Wedge
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/simulated/c1_landscape"
ASSET = ROOT / "figures/simulated/c1_landscape"
METHODS = ("Static judge", "Static tools", "Prompt optimization", "Program search", "ERA")
FAMILIES = (("SV", "Structured visuals", 6, "#F2B8AE"),
            ("IG", "Images & 3D", 6, "#C2E5CF"),
            ("TG", "Text generation", 5, "#74A9C5"),
            ("AR", "Automated research", 5, "#EDDDAB"))
INK, MUTED, GRID, ERA = "#25272B", "#62666B", "#E9EAEB", "#62AAA5"
WIDTH, HEIGHT, N_BOOT = 5.4, 3.57, 2000
FONTS = {
    "SourceSans3-Regular.ttf": ("source-sans", "4644c81b86ec9caaa76b634889968ed3c4f4f52f054855933acc7c2b21e53b0f"),
    "SourceSans3-Semibold.ttf": ("source-sans", "a3f4f8dcf343a8f24dc61951de93f3ba1558b15cd250ba24af8a40e957081b7d"),
    "SourceSerif4-Regular.ttf": ("source-serif", "e5a4ee6a3d87bb9024796be390c6771e2a0eb1883dae25effaf57ca01668e24b"),
    "SourceSerif4-It.ttf": ("source-serif", "9d2950a8f1da66e21502c35d646a1d2148e79f9ea43fd2158cf02f5232e7f430"),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert rows and all(r["provenance"] == "SIMULATED" for r in rows)
    return rows


def write(name, rows):
    rows = [{"provenance": "SIMULATED", **r} for r in rows]
    with (DATA / name).open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def summaries():
    """Paired complete-cohort agreement; unconditional best-of-4 success."""
    raw = read(ROOT / "data/simulated/c1_groups.csv")
    groups = defaultdict(dict)
    for row in raw:
        if row["split"] == "OOD" and row["method"] in METHODS:
            groups[(row["domain"], row["input_group"])][row["method"]] = row
    cohorts = read(ROOT / "data/simulated/c1_cohorts.csv")
    bars, selections, retained = [], [], []
    for cohort in cohorts:
        domain = cohort["domain"]
        requested = sorted((gid, values) for (did, gid), values in groups.items() if did == domain)
        assert len(requested) == int(cohort["groups"]) == 160
        assert all(set(values) == set(METHODS) for _, values in requested)
        complete = [(gid, values) for gid, values in requested
                    if all(values[m]["complete"] == "1" for m in METHODS)]
        retained.extend(dict(domain=domain, input_group=gid,
                             complete_all_methods=int(all(values[m]["complete"] == "1" for m in METHODS)))
                        for gid, values in requested)
        seed = int(hashlib.sha256(("c1-landscape-20260920|" + domain).encode()).hexdigest()[:16], 16)
        indices = np.random.default_rng(seed).integers(0, len(complete), (N_BOOT, len(complete)))
        for method in METHODS:
            values = np.asarray([float(group[method]["pairwise"]) for _, group in complete])
            lower, upper = np.quantile(values[indices].mean(axis=1), [.025, .975])
            bars.append(dict(domain=domain, family=domain[3:5], method=method, split="OOD",
                             requested_groups=len(requested), complete_groups=len(complete),
                             agreement_pct=100*values.mean(), lower_pct=100*lower, upper_pct=100*upper))
            # Failed scoring is a failed selection, never removed from this denominator.
            successes = sum(int(float(group[method]["best_of_4"] or 0)) for _, group in requested)
            selections.append(dict(domain=domain, family=domain[3:5], method=method,
                                   split="OOD", requested_groups=len(requested), successes=successes,
                                   best_of_4_pct=100*successes/len(requested)))
    points = []
    for family, _, count, _ in FAMILIES:
        for method in ("Static tools", "ERA"):
            b = [r for r in bars if r["family"] == family and r["method"] == method]
            s = [r for r in selections if r["family"] == family and r["method"] == method]
            assert len(b) == len(s) == count
            points.append(dict(family=family, method=method, split="OOD", domain_count=count,
                               agreement_pct=float(np.mean([r["agreement_pct"] for r in b])),
                               best_of_4_pct=float(np.mean([r["best_of_4_pct"] for r in s]))))
    return bars, selections, points, retained


def configure():
    folder = ROOT / "build/figure-fonts"
    folder.mkdir(parents=True, exist_ok=True)
    for name, (repo, expected) in FONTS.items():
        path = folder / name
        if not path.exists():
            url = f"https://raw.githubusercontent.com/adobe-fonts/{repo}/release/TTF/{name}"
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = response.read()
            assert hashlib.sha256(payload).hexdigest() == expected
            path.write_bytes(payload)
        assert digest(path) == expected
        fontManager.addfont(str(path))
    plt.rcParams.update({"font.family": "Source Sans 3", "pdf.fonttype": 42,
                         "ps.fonttype": 42, "svg.fonttype": "none",
                         "svg.hashsalt": "c1-landscape-20260920", "axes.unicode_minus": True})
    return {role: FontProperties(fname=str(folder / name)) for role, name in
            zip(("body", "strong", "serif", "italic"), FONTS)}


def render(bars, points):
    props = configure()
    fig = plt.figure(figsize=(WIDTH, HEIGHT), dpi=220, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1], xlim=(0, WIDTH), ylim=(0, HEIGHT), aspect="equal")
    ax.set_axis_off()
    def text(x, y, value, size=7.3, role="body", **kwargs):
        prop = props[role].copy()
        prop.set_size(size)
        return ax.text(x, y, value, fontproperties=prop, va="center",
                       color=kwargs.pop("color", INK), **kwargs)
    def line(xs, ys, **kwargs):
        return ax.plot(xs, ys, color=kwargs.pop("color", GRID), lw=kwargs.pop("lw", .45), **kwargs)[0]
    def panel(letter, title, x, y):
        text(x, y, letter, size=9.2, role="strong")
        text(x+.18, y, title, size=10, role="serif")
    def tint(color, alpha):
        return tuple(1-alpha*(1-c) for c in to_rgb(color))

    text(.13, 3.46, "SIMULATED", size=6.8, role="strong",
         bbox=dict(boxstyle="square,pad=.22", facecolor="#FBECEF", edgecolor="none"))
    text(5.27, 3.46, "Layout fixture · not experimental results", ha="right", size=6.8, color=MUTED)
    panel("a", "Evaluation scope", .13, 3.25)
    cx, cy, angle = 1.04, 2.29, 90.
    for fi in (1, 3, 2, 0):
        family, _, count, color = FAMILIES[fi]
        ax.add_patch(Wedge((cx, cy), .48, angle-90+.65, angle-.65, width=.17,
                           facecolor=color, edgecolor="white", lw=.3))
        mid = np.deg2rad(angle-45)
        text(cx+.40*np.cos(mid), cy+.40*np.sin(mid), family, role="strong", ha="center")
        for j in range(count):
            start, end = angle-90*(j+1)/count, angle-90*j/count
            ax.add_patch(Wedge((cx, cy), .83, start+.55, end-.55, width=.335,
                               facecolor=tint(color, .56+.44*j/(count-1)), edgecolor="white", lw=.3))
            theta = (start+end)/2
            rotation = (theta-90+180) % 360 - 180
            if rotation < -90:
                rotation += 180
            if rotation > 90:
                rotation -= 180
            text(cx+.73*np.cos(np.deg2rad(theta)), cy+.73*np.sin(np.deg2rad(theta)),
                 f"{family}{j+1}", ha="center", rotation=rotation, rotation_mode="anchor")
        angle -= 90
    text(cx, cy+.045, "22", size=14, role="serif", ha="center")
    text(cx, cy-.11, "tasks", ha="center", color=MUTED)
    for y, value, label in ((2.87, "4", "families"), (2.37, "OOD", "test split"),
                            (1.87, "N = 4", "selection pool")):
        text(2.28, y, value, size=12, role="serif", ha="center")
        text(2.28, y-.16, label, ha="center", color=MUTED)

    panel("b", "Agreement & selection", 2.88, 3.25)
    text(3.0, 3.08, "Equal-domain means within each family", size=7.1, color=MUTED)
    x0, y0, w, h = 3.18, 1.88, 2.07, 1.03
    px = lambda x: x0+(x-68)/8*w
    py = lambda y: y0+(y-47)/12*h
    for y in (48, 52, 56):
        line([x0, x0+w], [py(y)]*2)
        text(x0-.07, py(y), str(y), ha="right", color=MUTED)
    for x in (68, 72, 76):
        text(px(x), y0-.08, str(x), ha="center", color=MUTED)
    line([x0, x0+w], [y0]*2, color="#A8B0B8")
    text(x0+w/2, y0-.26, "Pairwise agreement (%)", ha="center", size=8)
    text(x0-.26, y0+h/2, "Best-of-4 accuracy (%)", ha="center", rotation=90, size=8)
    plotted = []
    for family, _, _, color in FAMILIES:
        pair = [next(r for r in points if r["family"] == family and r["method"] == m)
                for m in ("Static tools", "ERA")]
        coords = [(px(r["agreement_pct"]), py(r["best_of_4_pct"])) for r in pair]
        line([p[0] for p in coords], [p[1] for p in coords], color=color, lw=1.5, zorder=2)
        for r, (x, y) in zip(pair, coords):
            assert x0 <= x <= x0+w and y0 <= y <= y0+h
            evolved = r["method"] == "ERA"
            ax.plot(x, y, marker="D" if evolved else "o", ms=5.2 if evolved else 4.4,
                    mfc=ERA if evolved else tint(color, .6), mec="#477D79" if evolved else MUTED,
                    mew=.65, linestyle="none", zorder=4)
            plotted.append(dict(**r, x_inches=x, y_inches=y))
        offsets = {"SV": (.08, .06), "IG": (.08, -.02), "TG": (-.22, .12), "AR": (.08, -.03)}
        dx, dy = offsets[family]
        text(coords[1][0]+dx, coords[1][1]+dy, family, size=7.3)
    for x, marker, label, color in ((3.30, "o", "Static tools (seed)", "#C6CFD0"),
                                   (4.69, "D", "IterEval", ERA)):
        ax.plot(x, 1.46, marker=marker, ms=4.2, mfc=color, mec=MUTED, mew=.55, linestyle="none")
        text(x+.09, 1.46, label)

    panel("c", "Agreement across tasks", .13, 1.31)
    text(5.27, 1.31, "OOD agreement (%)", ha="right", color=MUTED)
    left, right, bottom, bh, gap = .40, 5.27, .41, .55, .12
    step = (right-left-gap*3)/22
    lookup = {(r["domain"], r["method"]): r for r in bars}
    geometry = []
    for value in (0, 50, 100):
        line([left, right], [bottom+bh*value/100]*2,
             color="#A8B0B8" if value == 0 else GRID)
        text(left-.06, bottom+bh*value/100, str(value), ha="right", color=MUTED)
    pos = left
    for family, name, count, color in FAMILIES:
        width = count*step
        text(pos+width/2, bottom+bh+.18, name, size=8.1, role="italic", ha="center")
        line([pos, pos+width], [bottom+bh+.07]*2, color=color, lw=1.4, solid_capstyle="round")
        for j in range(count):
            domain = f"TD-{family}{j+1}"
            center = pos+(j+.5)*step
            for mi, method in enumerate(METHODS):
                r = lookup[(domain, method)]
                x, bw = center+(mi-2)*.030, .026
                fill = ERA if mi == 4 else tint(color, (.24, .40, .56, .72)[mi])
                height = bh*r["agreement_pct"]/100
                ax.add_patch(Rectangle((x-bw/2, bottom), bw, height, facecolor=fill, edgecolor="none", zorder=2))
                lo, hi = [bottom+bh*r[key]/100 for key in ("lower_pct", "upper_pct")]
                line([x, x], [lo, hi], color="#535C66", lw=.35, zorder=3)
                for y in (lo, hi):
                    line([x-.006, x+.006], [y, y], color="#535C66", lw=.35, zorder=3)
                geometry.append(dict(domain=domain, method=method, x_inches=x, zero_inches=bottom,
                                     full_scale_height_inches=bh, mean_inches=bottom+height,
                                     lower_inches=lo, upper_inches=hi))
            text(center, bottom-.13, domain[3:], ha="center", size=7.3)
        pos += width+gap
    text(.40, .105, "Static judge · Static tools · Prompt opt. · Program search · IterEval", color=MUTED)
    fig.savefig(ASSET.with_suffix(".pdf"), metadata={"Title": "SIMULATED C1 layout fixture",
                "Subject": "Not experimental results; full synthetic cohorts, not the historical subset.",
                "CreationDate": None, "ModDate": None})
    fig.savefig(ASSET.with_suffix(".svg"), metadata={"Date": None})
    svg = ASSET.with_suffix(".svg")
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
    fig.savefig(ASSET.with_suffix(".png"), dpi=300)
    plt.close(fig)
    return geometry, plotted


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    sources = [ROOT / "data/simulated" / name for name in ("c1_groups.csv", "c1_cohorts.csv")]
    protected = [ROOT / "figures/simulated/landscape_outcomes.pdf"]
    original = {str(p.relative_to(ROOT)): digest(p) for p in sources+protected}
    bars, selections, points, retained = summaries()
    geometry, plotted = render(bars, points)
    for name, rows in (("bars.csv", bars), ("selection.csv", selections), ("family-points.csv", plotted),
                       ("input-cohorts.csv", retained), ("bar-geometry.csv", geometry)):
        write(name, rows)
    assert all(digest(ROOT / p) == h for p, h in original.items())
    artifacts = list(DATA.glob("*.csv")) + [ASSET.with_suffix(ext) for ext in (".pdf", ".svg", ".png")]
    artifacts += [Path(__file__).resolve(), ROOT / "figures/c1_landscape.tex"]
    manifest = dict(simulation_only=True, empirical_evidence=False, generates_observations=False,
                    source_files=original, output_files={str(p.relative_to(ROOT)): digest(p) for p in artifacts},
                    canvas_inches=[WIDTH, HEIGHT], methods=list(METHODS), display_names={"ERA": "IterEval"}, domains=22,
                    requested_ood_inputs=len(retained), bootstrap_replicates=N_BOOT,
                    agreement_cohort="Jointly complete inputs across five displayed methods, within domain.",
                    selection_cohort="All 160 inputs per domain; failed scoring is failed selection.",
                    aggregation="Equal domain weights within family; no fitted relation or causal inference.",
                    ring="Taxonomy: equal family quadrants, equal task sectors within each family; not sample shares.",
                    scope="C1 only; no C2/C3, calibration, fine-tuning, search or acquisition efficacy is simulated.",
                    fonts=FONTS)
    (DATA / "manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    print("C1 landscape: 22 tasks, 110 bars, eight family points; existing SIMULATED records only.")


if __name__ == "__main__":
    main()
