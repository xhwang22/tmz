#!/usr/bin/env python3
"""Reproducible, explicitly SIMULATED paper-layout fixtures; no model/API calls.

These toy data are not a simulation of ERA's actual implementation, a power
analysis, or a prediction of experimental effects. Domain assignments, noise,
effects, and costs are chosen solely to exercise the reporting/plotting code.
Never mix these files with collected human feedback or experimental outputs.
"""

import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm, to_rgb
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter
from matplotlib.text import Text
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/simulated"
OUT = ROOT / "figures/simulated"
PREVIEW = ROOT / "build/simulation-review"
SEED = 20260916
N_GROUPS = 160
N_REPEATS = 3
N_BOOT = 1000
DEFAULT_PALETTE = "reference_pastel"
ON_FILL = "#202226"


def contrast(a, b):
    def luminance(color):
        channels = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4
                    for v in to_rgb(color)]
        return sum(v * weight for v, weight in zip(channels, (.2126, .7152, .0722)))
    low, high = sorted((luminance(a), luminance(b)))
    return (high + .05) / (low + .05)


def companion(color, minimum=5.2):
    """Darken toward black for fine strokes/text, preserving the source hue.

    Scaling sRGB keeps HSV hue/saturation fixed; lowering HLS lightness on a
    pastel would instead make its companion unexpectedly vivid. Fills are exact.
    """
    source = to_rgb(color)
    scale = 1.0
    while True:
        result = "#" + "".join(f"{round(v * scale * 255):02X}" for v in source)
        if contrast(result, "#FFFFFF") >= minimum or scale <= .01:
            return result
        scale = max(0, scale - .005)


def on_fill(color):
    """Light source colors keep their original hue and receive dark labels."""
    return ON_FILL if contrast(ON_FILL, color) >= 4.5 else "#FFFFFF"


def reference_palette(title, description, source, swatches, indices):
    # HEX values are transcribed from the author's labeled swatches, not
    # sampled from JPEG pixels or mixed with an unrelated palette.
    roles = {role: swatches[index] for role, index in indices.items()}
    palette = dict(title=title, description=description, source=source,
                   source_swatches=swatches, source_indices=indices, **roles)
    palette.update(INK="#25272B", MUTED="#60656C", GRID="#E8EAED", NEUTRAL="#E6E8EB")
    palette.update(BLUE_INK=companion(roles["BLUE"]), GOLD_INK=companion(roles["GOLD"], 5.4),
                   GREEN=companion(roles["TEAL"]),
                   BROWN=companion(roles["PEACH"]), RED=companion(roles["ROSE"]),
                   RESEARCH=companion(roles["LILAC"]), ERA_EDGE=companion(roles["ROSE"], 3.0))
    return palette


PALETTES = {
    "reference_pastel": reference_palette(
        "Reference 1 / Five-color ensemble", "The complete blue, mint, cream, peach and rose set",
        "color_reference.jpg",
        ("#74A9C5", "#C2E5CF", "#EDDDAB", "#F2B8AE", "#DD7389"),
        dict(BLUE=0, SKY=0, TEAL=1, MINT=1, GOLD=2, CREAM=2, PEACH=3, ROSE=4, LILAC=3)),
    "reference_blue_orange": reference_palette(
        "Reference 2 / Cool-to-warm ensemble", "Five ordered colors from the supplied cool-to-warm sequence",
        "color_reference_1.jpg",
        ("#376795", "#528FAD", "#72BCD5", "#AADCE0", "#FFE6B7", "#FFD06F",
         "#F7AA58", "#EF8A47", "#E76254"),
        dict(BLUE=2, SKY=3, TEAL=3, MINT=3, GOLD=5, CREAM=4, PEACH=6, ROSE=7, LILAC=6)),
    "reference_ocean": reference_palette(
        "Reference 3 / Ocean ensemble", "Five coordinated colors from the supplied ocean palette",
        "color_reference_2.jpg",
        ("#BFDFD2", "#51999F", "#4198AC", "#7BC0CD", "#DBCB92", "#ECB66C",
         "#EA9E58", "#ED8D5A"),
        dict(BLUE=2, SKY=3, TEAL=0, MINT=0, GOLD=4, CREAM=4, PEACH=5, ROSE=7, LILAC=6)),
}

# The old pLilac token remains a compatibility alias, not an extra purple hue.
TEX_ROLES = {"pSky": "SKY", "pMint": "MINT", "pCream": "CREAM", "pPeach": "PEACH",
             "pRose": "ROSE", "pLilac": "LILAC", "pBlue": "BLUE_INK", "pTeal": "GREEN",
             "pGold": "GOLD_INK", "pNew": "BROWN", "pEvo": "RED", "pResearch": "RESEARCH", "pInk": "INK",
             "pMuted": "MUTED", "pLine": "GRID", "pRed": "RED"}


def use_palette(name):
    global FIVE_COLORS, RANK_COLORS, SETTING_COLORS, POLICY_COLORS, METHOD_COLORS, FAMILY_COLORS
    globals().update({key: value for key, value in PALETTES[name].items() if key.isupper()})
    FIVE_COLORS = [BLUE, MINT, CREAM, PEACH, ROSE]
    RANK_COLORS = list(FIVE_COLORS)
    SETTING_COLORS = {"Reuse": TEAL, "Collect": PEACH}
    POLICY_COLORS = list(FIVE_COLORS)
    # Color is a complete categorical system, not an ERA/seed dichotomy.
    # The two metric-only anchors remain neutral; all seven stay in the table.
    METHOD_COLORS = dict(zip(("Static judge", "Static tools", "Prompt optimization",
                             "Program search", "ERA"), FIVE_COLORS))
    FAMILY_COLORS = dict(zip(("Structured visuals", "Images / 3D", "Text generation",
                             "Automated research"), FIVE_COLORS[:4]))


use_palette(DEFAULT_PALETTE)
SETTINGS = ("Reuse", "Collect")
SETTING_TITLES = {"Reuse": "Reused preferences", "Collect": "New preferences"}
METHODS = ("Single metric", "Metric ensemble", "Static judge", "Static tools",
           "Prompt optimization", "Program search", "ERA")
SHORT_METHODS = ("Metric", "Ensemble", "Static judge", "Static tools",
                 "Prompt opt.", "Program search", "ERA")
DISPLAY_METHODS = METHODS[2:]
POLICIES = ("Random", "Uncertainty", "Model conflict", "Run instability", "Multi-source")
POLICY_STYLES = ["--", "-.", ":", (0, (4, 1, 1, 1)), "-"]
POLICY_MARKERS = ["o", "s", "^", "v", "D"]
COHORTS = [
    ("Reuse", "TD-SV4", "Spec. web", "Structured visuals", 0),
    ("Reuse", "TD-IG1", "Captioning", "Images / 3D", 1),
    ("Reuse", "TD-TG1", "Summarization", "Text generation", 2),
    ("Reuse", "TD-AR1", "Research ideas", "Automated research", 3),
    ("Collect", "TD-SV2", "Web reconstruction", "Structured visuals", 0),
    ("Collect", "TD-IG3", "Image editing", "Images / 3D", 1),
    ("Collect", "TD-TG2", "RAG answers", "Text generation", 2),
    ("Collect", "TD-AR2", "Ablation plans", "Automated research", 3),
]
# Keep the original eight diagnostic fixtures (and their random streams) intact.
# C1 now covers the complete source-plan taxonomy. These extra assignments are
# layout fixtures, NOT assertions that reusable/new labels exist in a domain.
C1_COHORTS = COHORTS + [
    ("Reuse", "TD-SV1", "Brief → single slide", "Structured visuals", 0),
    ("Reuse", "TD-SV3", "Data → visualization", "Structured visuals", 0),
    ("Collect", "TD-SV5", "Sources → slide deck", "Structured visuals", 0),
    ("Collect", "TD-SV6", "Topic → slide deck", "Structured visuals", 0),
    ("Reuse", "TD-IG2", "Text → image", "Images / 3D", 1),
    ("Collect", "TD-IG4", "Super-resolution", "Images / 3D", 1),
    ("Reuse", "TD-IG5", "Text → 3D", "Images / 3D", 1),
    ("Collect", "TD-IG6", "Image → 3D", "Images / 3D", 1),
    ("Reuse", "TD-TG3", "Translation", "Text generation", 2),
    ("Collect", "TD-TG4", "Instruction constraints", "Text generation", 2),
    ("Reuse", "TD-TG5", "Open dialogue", "Text generation", 2),
    ("Reuse", "TD-AR3", "Table → insight", "Automated research", 3),
    ("Collect", "TD-AR4", "Related work", "Automated research", 3),
    ("Collect", "TD-AR5", "Peer-review critique", "Automated research", 3),
]
DOMAIN_NAMES = {
    **{domain: name for _, domain, name, *_ in C1_COHORTS},
    "TD-SV2": "Screenshot → webpage", "TD-SV4": "Specification → webpage",
    "TD-IG1": "Detailed captioning", "TD-IG3": "Instruction-based editing",
    "TD-TG1": "Document summarization", "TD-TG2": "RAG long-form answers",
}
DOMAIN_ORDER = sorted(C1_COHORTS, key=lambda row: (row[4], int(row[1][5:])))
CHARTS = ("outcomes", "alignment", "acquisition", "annotation", "selection", "ablation", "refinement", "cost")
METRICS = ("pairwise", "top_region", "best_of_4", "rank_regret")


def write_csv(name, rows):
    """Every row carries a provenance sentinel, even when copied in isolation."""
    rows = [{"provenance": "SIMULATED", **row} for row in rows]
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def bootstrap(values, rng):
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if not len(values):
        return np.nan, np.nan, np.nan
    sampled = values[rng.integers(0, len(values), (N_BOOT, len(values)))].mean(axis=1)
    low, high = np.quantile(sampled, [.025, .975])
    return float(values.mean()), float(low), float(high)


def configure():
    plt.rcParams.update({
        "font.family": ["TeX Gyre Heros", "DejaVu Sans"], "font.size": 8,
        "mathtext.fontset": "dejavusans",
        "axes.titlesize": 8.5, "axes.labelsize": 8,
        "xtick.labelsize": 7.3, "ytick.labelsize": 7.5,
        "legend.fontsize": 7.3, "text.color": INK, "axes.labelcolor": INK,
        "xtick.color": MUTED, "ytick.color": MUTED,
        "axes.edgecolor": "#BBC5CB", "axes.linewidth": .5,
        "grid.color": GRID, "grid.linewidth": .45,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.spines.left": False, "axes.spines.bottom": False,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "xtick.major.pad": 5, "ytick.major.pad": 5,
        "axes.labelpad": 6, "lines.solid_capstyle": "round",
        "savefig.facecolor": "white", "figure.facecolor": "white",
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "axes.unicode_minus": True,
        "hatch.linewidth": .45,
    })


def tint(color, amount=.12):
    """Mix with paper white; opacity is explicit and consistent in PDF output."""
    return tuple(1 - amount * (1 - v) for v in to_rgb(color))


def panel(ax, letter, title):
    # Offset-point placement keeps the hierarchy identical across panel sizes.
    ax.annotate(letter, (0, 1), xycoords="axes fraction", xytext=(0, 11), textcoords="offset points",
                ha="left", va="baseline", fontsize=9, weight="bold",
                annotation_clip=False)
    ax.annotate(title, (0, 1), xycoords="axes fraction", xytext=(13, 11), textcoords="offset points",
                ha="left", va="baseline", fontsize=8.5,
                annotation_clip=False)
    ax.plot([0, 1], [1.025, 1.025], transform=ax.transAxes,
            color=GRID, lw=.5, clip_on=False)
    ax.set_axisbelow(True)


def save(fig, name, note):
    fig.text(.025, .975, "SIMULATED DATA", ha="left", va="top", color=RED,
             fontsize=6.8, weight="bold",
             bbox=dict(facecolor=tint(ROSE), edgecolor="none", pad=2.5))
    fig.text(.975, .975, "NOT EXPERIMENTAL RESULTS", ha="right", va="top",
             color=MUTED, fontsize=6.8)
    fig.text(.02, .027, note, va="bottom", color=MUTED, fontsize=6.8)
    # Preserve a true 5.4-inch canvas. Detect clipping instead of silently
    # shrinking/cropping labels with bbox_inches='tight'. Review overlaps too.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    frame = fig.bbox
    for artist in fig.findobj(match=Text):
        if not artist.get_visible() or not artist.get_text():
            continue
        box = artist.get_window_extent(renderer)
        if box.width and box.height and (box.x0 < -1 or box.y0 < -1
                or box.x1 > frame.width + 1 or box.y1 > frame.height + 1):
            raise ValueError(f"{name}: text outside canvas: {artist.get_text()!r}")
    fig.savefig(OUT / f"{name}.pdf", metadata={
        "Title": f"SIMULATED DATA — {name}",
        "Subject": "Layout fixtures, not empirical evidence or expected performance",
        "Author": "", "Creator": "Evaluator-evolution synthetic reporting fixtures",
        "CreationDate": None, "ModDate": None,
    })
    fig.savefig(PREVIEW / f"{name}.png", dpi=220)
    plt.close(fig)


def cohort_rows(ax, labels=True):
    """A quiet, fixed row order makes domain panels directly comparable."""
    ax.set(yticks=range(8), ylim=(7.6, -.65))
    ax.set_yticklabels([c[2] for c in COHORTS] if labels else [])
    for i in (0, 2, 4, 6):
        ax.axhspan(i-.48, i+.48, color="#F8F9FA", lw=0, zorder=0)
    ax.axhline(3.5, color="#BAC6CB", lw=.55, zorder=1)


def setting_brackets(fig, left, bottom, height):
    fig.text(left, bottom + height * .77, "REUSED", color=MUTED,
             rotation=90, va="center", ha="center", fontsize=7, weight="bold")
    fig.text(left, bottom + height * .24, "NEW", color=MUTED,
             rotation=90, va="center", ha="center", fontsize=7, weight="bold")


def compact_legend(fig, handles, ncol, y=.12):
    return fig.legend(handles=handles, loc="center", bbox_to_anchor=(.52, y),
                      ncol=ncol, frameon=False, handlelength=1.5,
                      handletextpad=.55, columnspacing=1.4, labelspacing=.5)


def family_legend(fig, y=.12, x=.52):
    labels = ("SV · Visual", "IG · Image / 3D", "TG · Text", "AR · Research")
    return fig.legend(handles=[Patch(facecolor=color, label=label)
                               for color, label in zip(FAMILY_COLORS.values(), labels)],
                      loc="center", bbox_to_anchor=(x, y), ncol=4, frameon=False,
                      handlelength=1.15, handletextpad=.45, columnspacing=1.15,
                      fontsize=7)


def c1_data():
    rng = np.random.default_rng(SEED + 1)
    brng = np.random.default_rng(SEED + 101)
    rows, records, summary = [], {}, {}
    # Deliberately heterogeneous, with null/negative ERA-vs-seed contrasts.
    era_factors = [.69, .77, .88, 1.05, .78, .72, 1.11, .86,
                   .91, 1.08, .75, 1.0, 1.06, .83, .98, .73, 1.12, .90, .68, .98, 1.09, .81]
    domain_noise = [.97, 1.14, .84, 1.24, 1.08, .95, 1.18, 1.04,
                    1.03, .92, 1.15, 1.21, 1.11, .88, 1.27, 1.19, .87, 1.04, 1.16, .99, 1.22, 1.08]
    noise = np.array([1.70, 1.39, 1.14, 1.01, .98, .93, 1.0])
    costs = np.array([.22, .63, .78, 1.00, 1.12, 1.38, 1.51])
    for ci, (setting, domain, _, _, _) in enumerate(C1_COHORTS):
        for split in ("ID", "OOD"):
            latent = rng.normal(size=(N_GROUPS, 4))
            human_order = np.argsort(-latent, axis=1)
            human_ranks = np.argsort(human_order, axis=1)
            shared_error = rng.normal(0, .18, (N_GROUPS, 4))
            split_noise = 1.0 if split == "ID" else 1.22
            for mi, method in enumerate(METHODS):
                sd = noise[mi] * domain_noise[ci] * split_noise
                if mi == 6:
                    sd *= era_factors[ci]
                stable_error = rng.normal(0, sd, (N_GROUPS, 4))
                repeat_noise = rng.normal(0, .22, (N_GROUPS, 4, N_REPEATS))
                scores = np.median((latent + shared_error + stable_error)[..., None]
                                   + repeat_noise, axis=2)
                complete = rng.random(N_GROUPS) > (.004 + .002 * (mi >= 3))
                pairwise, top = [], []
                for i in range(N_GROUPS):
                    outcomes, top_outcomes = [], []
                    for a, b in itertools.combinations(range(4), 2):
                        good = float((scores[i, a] - scores[i, b]) *
                                     (latent[i, a] - latent[i, b]) > 0)
                        outcomes.append(good)
                        if min(human_ranks[i, a], human_ranks[i, b]) < 2:
                            top_outcomes.append(good)
                    pairwise.append(np.mean(outcomes))
                    top.append(np.mean(top_outcomes))
                chosen_rank = human_ranks[np.arange(N_GROUPS), scores.argmax(axis=1)]
                values = np.column_stack([pairwise, top, chosen_rank == 0, chosen_rank / 3])
                values[~complete] = np.nan
                group_cost = costs[mi] * rng.lognormal(0, .20, N_GROUPS)
                records[(domain, split, method)] = values
                s = {key: bootstrap(values[:, k], brng) for k, key in enumerate(METRICS)}
                s.update(coverage=float(complete.mean()), cost=float(group_cost.mean()))
                summary[(domain, split, method)] = s
                for i in range(N_GROUPS):
                    rows.append(dict(setting=setting, domain=domain, split=split,
                        input_group=f"SIM-{ci:02d}-{split}-{i:04d}", method=method,
                        human_order="|".join(map(str, human_order[i])),
                        median_scores="|".join(f"{v:.8f}" for v in scores[i]),
                        complete=int(complete[i]), **{m: (f"{values[i,k]:.8f}" if complete[i] else "")
                        for k, m in enumerate(METRICS)}, cost_units=f"{group_cost[i]:.6f}"))
    write_csv("c1_groups.csv", rows)
    aggregate = []
    for (domain, split, method), stats in summary.items():
        setting = next(c[0] for c in C1_COHORTS if c[1] == domain)
        for metric in METRICS:
            mean, lo, hi = stats[metric]
            aggregate.append(dict(setting=setting, domain=domain, split=split, method=method,
                                  metric=metric, mean=mean, lower=lo, upper=hi,
                                  coverage=stats["coverage"], cost_units=stats["cost"]))
    write_csv("c1_summary.csv", aggregate)
    return records, summary


def domain_layout():
    """Taxonomy order, with a separate heading row for each of 6/6/5/5 tasks."""
    positions, headings, cursor = {}, [], 0.0
    for family in FAMILY_COLORS:
        members = [c for c in DOMAIN_ORDER if c[3] == family]
        headings.append((family, cursor, len(members)))
        cursor += 1.12
        for cohort in members:
            positions[cohort[1]] = cursor
            cursor += 1.0
        cursor += .60
    return positions, headings, (cursor-.5, -.60)


def domain_labels(ax, positions, headings, limits):
    ax.set(xlim=(0, 1), ylim=limits)
    ax.axis("off")
    for family, y, count in headings:
        ax.text(0, y, f"{family} · {count}", fontsize=8, weight="bold", va="center")
    for setting, domain, *_ in DOMAIN_ORDER:
        y = positions[domain]
        ax.text(0, y, domain[3:], fontsize=7, color=MUTED, va="center")
        ax.text(.205, y, DOMAIN_NAMES[domain], fontsize=7.5, va="center")
        ax.text(.975, y, "R" if setting == "Reuse" else "N", fontsize=7, color=MUTED,
                ha="right", va="center")


def alignment(records):
    """Both splits for all 22 domains; a shared paired-effect scale."""
    rng = np.random.default_rng(SEED + 111)
    rows = []
    for subset in (COHORTS, C1_COHORTS[len(COHORTS):]):
        for split, (setting, domain, *_) in itertools.product(("ID", "OOD"), subset):
            seed = records[(domain, split, "Static tools")][:, 0]
            era = records[(domain, split, "ERA")][:, 0]
            paired = np.isfinite(seed) & np.isfinite(era)
            mean, lo, hi = bootstrap(100 * (era[paired] - seed[paired]), rng)
            rows.append(dict(setting=setting, domain=domain, split=split,
                             complete_pairs=int(paired.sum()), delta_pp=mean, lower=lo, upper=hi))
    write_csv("alignment_effects.csv", rows)
    lookup = {(r["domain"], r["split"]): r for r in rows}
    positions, headings, limits = domain_layout()
    fig = plt.figure(figsize=(5.4, 5.5))
    labels = fig.add_axes([.025, .13, .405, .735])
    domain_labels(labels, positions, headings, limits)
    axes = [fig.add_axes([.49, .13, .18, .735]), fig.add_axes([.78, .13, .18, .735])]
    for ax, split, letter in zip(axes, ("ID", "OOD"), "ab"):
        ax.set(ylim=limits, yticks=[], xlim=(-12, 16), xticks=[-10, 0, 10])
        for _, domain, _, family, _ in DOMAIN_ORDER:
            r, y = lookup[(domain, split)], positions[domain]
            mean, lo, hi = (r[k] for k in ("delta_pp", "lower", "upper"))
            color = FAMILY_COLORS[family]
            ax.errorbar(mean, y, xerr=[[mean-lo], [hi-mean]], fmt="D", ms=3.6,
                        color=companion(color, 3.0), mfc=color, mew=.55, elinewidth=.8,
                        capsize=1.6, zorder=3)
        for _, y, _ in headings:
            ax.axhline(y, color=GRID, lw=.5)
        ax.axvline(0, color=MUTED, lw=.7, ls=(0, (2, 2)), zorder=1)
        ax.grid(axis="x")
        panel(ax, letter, f"{split} test")
        ax.set_xlabel("ERA − seed (pp)", fontsize=7.5)
    fig.text(.025, .914, "22 DOMAINS / 4 FAMILIES", fontsize=8, weight="bold")
    save(fig, "alignment", "R: reused / N: new preferences (illustrative assignments only).\n"
         "Diamonds: paired means. Whiskers: 95% bootstrap intervals over synthetic input groups.")


def acquisition():
    rng = np.random.default_rng(SEED + 2)
    budgets = np.array([20, 50, 100, 200])
    base = {"Reuse": [[65,69,73,77], [66,71,75,78], [65,71,76,79], [64,69,73,77], [65,73,78,81]],
            "Collect": [[64,68,73,77], [65,70,75,77], [66,69,74,78], [64,70,72,76], [63,69,76,78]]}
    rows = []
    fig, axes = plt.subplots(1,2,figsize=(5.4,2.95))
    fig.subplots_adjust(left=.10,right=.975,top=.80,bottom=.34,wspace=.26)
    for ax, setting, letter in zip(axes, SETTINGS, "ab"):
        common = rng.normal(0, 1.0, (12, 4))
        for i, policy in enumerate(POLICIES):
            values = np.array(base[setting][i]) + common + rng.normal(0, .65, (12, 4))
            low, high = np.quantile(values, [.1,.9], axis=0)
            ax.fill_between(budgets,low,high,color=POLICY_COLORS[i],alpha=.14,lw=0)
            line, = ax.plot(budgets,values.mean(axis=0),color=POLICY_COLORS[i],ls=POLICY_STYLES[i],
                    marker=POLICY_MARKERS[i],ms=4.1,
                    markerfacecolor=POLICY_COLORS[i],
                    markeredgecolor=companion(POLICY_COLORS[i],3.0), markeredgewidth=.45,
                    lw=1.7, alpha=1, zorder=3,label=policy)
            # Fine companion outlines keep the light mint/cream lines readable
            # without replacing the actual source colors with dark strokes.
            line.set_path_effects([pe.Stroke(linewidth=2.15, foreground=companion(POLICY_COLORS[i],3.0)),
                                   pe.Normal()])
            if i in (0,4):
                end=values.mean(axis=0)[-1]
                # Keep near-equal endpoints legible without changing their data.
                offset=5 if i==4 else -7
                ax.annotate(f"{end:.1f}", (200,end), xytext=(6,offset),
                            textcoords="offset points", fontsize=7,
                            va="center", color=INK,
                            bbox=dict(facecolor="white",edgecolor="none",pad=.5))
            for run in range(12):
                for j,b in enumerate(budgets):
                    rows.append(dict(setting=setting,policy=policy,synthetic_run=run,
                                     human_units=int(b),anchor_units=10,agreement_pct=values[run,j]))
        panel(ax,letter,SETTING_TITLES[setting])
        ax.set(xlim=(12,238),ylim=(60,84),xticks=budgets,yticks=[60,70,80],
               xlabel="Annotation budget")
        ax.grid(axis="y")
        ax.spines["bottom"].set_visible(True)
    axes[0].set_ylabel("Held-out agreement (%)")
    handles, labels = axes[0].get_legend_handles_labels()
    compact_legend(fig, handles, 3, y=.135)
    write_csv("acquisition.csv",rows)
    save(fig,"acquisition","Bands: 10–90% of 12 toy runs. Each budget includes the same 10-unit random anchor.")


def annotation():
    rng = np.random.default_rng(SEED + 3)
    brng = np.random.default_rng(SEED + 103)
    rows, summaries = [], []
    error_probs = [.13,.17,.12,.23,.18,.13,.20,.18]
    abstain_probs = [.06,.09,.03,.14,.08,.07,.12,.10]
    for ci,(setting,domain,*_) in enumerate(COHORTS):
        target = rng.choice(3,N_GROUPS,p=[.46,.46,.08])
        votes = np.repeat(target[:,None],3,axis=1)
        mistakes = rng.random(votes.shape) < error_probs[ci]
        votes[mistakes] = rng.integers(0,3,mistakes.sum())
        votes[rng.random(votes.shape)<abstain_probs[ci]] = -1
        group_agreement, decisive, tie, no_consensus, abstentions = [],0,0,0,0
        for i,v in enumerate(votes):
            valid = v[v>=0]
            comparisons = [a==b for a,b in itertools.combinations(valid,2)]
            group_agreement.append(np.mean(comparisons) if comparisons else np.nan)
            counts = np.bincount(valid,minlength=3)
            if len(valid)<2:
                outcome="insufficient votes"; abstentions+=1
            elif counts.max()<2:
                outcome="no consensus"; no_consensus+=1
            elif counts.argmax()==2:
                outcome="tie"; tie+=1
            else:
                outcome="decisive"; decisive+=1
            rows.append(dict(setting=setting,domain=domain,input_group=f"SIM-ANN-{ci}-{i:04d}",
                             rater_1=int(v[0]),rater_2=int(v[1]),rater_3=int(v[2]),
                             group_agreement=group_agreement[-1],group_outcome=outcome))
        _, lo, hi = bootstrap(100*np.asarray(group_agreement), brng)
        summaries.append(dict(setting=setting,domain=domain,agreement=100*np.nanmean(group_agreement),
                              lower=lo,upper=hi,
                              abstention=100*np.mean(votes==-1),
                              shares=100*np.array([decisive,tie,no_consensus,abstentions])/N_GROUPS))
    write_csv("annotation_groups.csv",rows)
    write_csv("annotation_summary.csv",[dict(setting=s["setting"],domain=s["domain"],
        agreement_pct=s["agreement"],lower=s["lower"],upper=s["upper"],abstention_pct=s["abstention"],
        decisive_pct=s["shares"][0],tie_pct=s["shares"][1],no_consensus_pct=s["shares"][2],
        insufficient_pct=s["shares"][3]) for s in summaries])
    fig=plt.figure(figsize=(5.4,3.05))
    a=fig.add_axes([.115,.29,.24,.51])
    b=fig.add_axes([.445,.29,.16,.51])
    c=fig.add_axes([.70,.29,.275,.51])
    y=np.arange(8)
    for ax in (a,b,c):
        cohort_rows(ax,labels=False)
        ax.grid(axis="x")
    for i,s in enumerate(summaries):
        a.errorbar(s["agreement"],i,xerr=[[s["agreement"]-s["lower"]],
                   [s["upper"]-s["agreement"]]],fmt="o",color=MUTED,mfc=TEAL,
                   ms=3.7,mew=.6,elinewidth=.8,capsize=1.8,zorder=3)
        b.barh(i,s["abstention"],height=.31,color=tint(ROSE,.55),
               edgecolor="none",zorder=2)
        b.text(s["abstention"]+.65,i,f'{s["abstention"]:.1f}',va="center",
               fontsize=7,color=INK)
    a.set(yticklabels=[c[1].replace("TD-","") for c in COHORTS],xlim=(0,100),
          xticks=[50,75,100],xlabel="Valid pairs (%)")
    a.set_xlim(48,100)
    b.set(xlim=(0,20),xticks=[0,10,20],xlabel="All ratings (%)")
    panel(a,"a","Agreement")
    panel(b,"b","Abstention")
    left=np.zeros(8)
    shares=np.array([s["shares"] for s in summaries])
    for j,(label,color,hatch) in enumerate(zip(["Decisive","Tie","No consensus","Insufficient votes"],
                                             [BLUE,CREAM,PEACH,NEUTRAL],[None,None,None,"///"])):
        c.barh(y,shares[:,j],left=left,height=.54,color=color,edgecolor="white",lw=.5,hatch=hatch,label=label,zorder=3)
        if j==0:
            for i,v in enumerate(shares[:,j]):
                c.text(v/2,i,f"{v:.0f}",va="center",ha="center",fontsize=7,
                       color=on_fill(BLUE),zorder=4)
        left+=shares[:,j]
    c.set(xlim=(0,100),xticks=[0,50,100],xlabel="Input groups (%)")
    panel(c,"c","Consensus")
    setting_brackets(fig,.022,.29,.51)
    handles,_=c.get_legend_handles_labels()
    compact_legend(fig,handles,4,y=.12)
    save(fig,"annotation","Three simulated raters per group. Agreement, abstention, and consensus use distinct denominators.")


def selection(records,summary):
    # Horizontal ribbons keep method names readable and make rank-1 shares
    # comparable against a common left edge, without tall blocks of flat color.
    fig,axes=plt.subplots(1,2,figsize=(5.4,2.65))
    fig.subplots_adjust(left=.205,right=.975,top=.78,bottom=.32,wspace=.24)
    chosen=["Static judge","Static tools","Program search","ERA"]
    rows=[]
    for ax,setting,letter in zip(axes,SETTINGS,"ab"):
        cohort=[c for c in C1_COHORTS if c[0]==setting]
        ax.axhspan(2.56,3.44,color=tint(ROSE,.08),lw=0,zorder=0)
        for j,method in enumerate(chosen):
            regrets=np.concatenate([records[(c[1],"ID",method)][:,3] for c in cohort])
            ranks=np.where(np.isfinite(regrets),np.rint(np.nan_to_num(regrets)*3),4).astype(int)
            counts=np.bincount(ranks,minlength=5)
            left=0
            for rank,n in enumerate(counts):
                value=100*n/len(ranks)
                ax.barh(j,value,left=left,height=.50,color=RANK_COLORS[rank],
                       edgecolor="white",lw=.6,hatch="///" if rank==4 else None,zorder=3)
                if rank==0:
                    ax.text(value/2,j,f"{value:.1f}%",color=on_fill(BLUE),ha="center",va="center",fontsize=7.4)
                left+=value
                rows.append(dict(setting=setting,method=method,selected_rank=str(rank+1) if rank<4 else "unscored",
                                 count=int(n),denominator=len(ranks),share_pct=value))
        ax.set(xlim=(0,100),xticks=[0,25,50,75,100],ylim=(3.6,-.6),yticks=range(4),
               yticklabels=chosen if letter=="a" else [],xlabel="Share of all inputs (%)")
        ax.grid(axis="x")
        panel(ax,letter,SETTING_TITLES[setting])
    handles=[Patch(facecolor=color,label=label,hatch="///" if i==4 else None)
             for i,(color,label) in enumerate(zip(RANK_COLORS,["Rank 1","Rank 2","Rank 3","Rank 4","Unscored"]))]
    compact_legend(fig,handles,5,y=.12)
    write_csv("selection_ranks.csv",rows)
    save(fig,"selection","ID test; equal-sized toy cohorts. Rank 1 is best. Failed scoring remains in the denominator.")


def ablation():
    rng=np.random.default_rng(SEED+4)
    vrng=np.random.default_rng(SEED+204)
    effects=np.array([[.8,1.1,1.0,4.0,2.8,.9],[1.4,.3,1.9,3.0,2.0,-.5],
                      [.2,3.7,2.6,.7,1.3,1.8],[-.6,1.5,3.2,.3,1.0,2.0],
                      [2.0,.7,1.2,4.4,3.2,.5],[1.4,.5,1.1,3.9,2.6,1.0],
                      [.5,2.0,1.2,1.1,-1.1,.8],[.3,2.9,3.5,-.5,1.8,2.7]])
    components=["A","K","V","T","Π","G"]
    rows=[]
    fig=plt.figure(figsize=(5.4,3.3))
    a=fig.add_axes([.10,.30,.435,.50])
    b=fig.add_axes([.65,.30,.325,.50])
    # Full diverging source sequence. Cream is the explicitly marked zero;
    # the signed limits stay -6/+6, and exact numbers remain in every cell.
    cmap=LinearSegmentedColormap.from_list("effects",FIVE_COLORS)
    im=a.imshow(effects,cmap=cmap,norm=TwoSlopeNorm(vcenter=0,vmin=-6,vmax=6),aspect="auto")
    for (i,j),v in np.ndenumerate(effects):
        a.text(j,i,f"{v:+.1f}",ha="center",va="center",fontsize=7.1,color=ON_FILL)
        for g in range(N_GROUPS):
            rows.append(dict(setting=COHORTS[i][0],domain=COHORTS[i][1],component=components[j],
                             input_group=f"SIM-ABL-{i}-{g:04d}",delta_pp=v+rng.normal(0,7)))
    a.set(yticks=range(8),yticklabels=[c[1].replace("TD-","") for c in COHORTS],
          xticks=range(6),xticklabels=[f"{key}\n{label}" for key,label in
                                     zip(components,["Views","Rubric","Module","Tools","Route","Fusion"])])
    a.tick_params(axis="x",labelsize=7)
    a.axhline(3.5,color="white",lw=4)
    a.set_xticks(np.arange(-.5,6,1),minor=True)
    a.set_yticks(np.arange(-.5,8,1),minor=True)
    a.grid(which="minor",color="white",lw=1.1)
    a.tick_params(which="minor",size=0)
    panel(a,"a","Component effects")
    setting_brackets(fig,.016,.30,.50)
    # Display the means actually exported, rather than the input effect parameters.
    actual=np.array([[np.mean([r["delta_pp"] for r in rows if r["domain"]==c[1] and r["component"]==comp])
                      for comp in components] for c in COHORTS])
    im.set_data(actual)
    for txt,v in zip(a.texts,actual.flat):txt.set_text("0.0" if abs(v)<.05 else f"{v:+.1f}")
    cax=fig.add_axes([.17,.18,.295,.022])
    cb=fig.colorbar(im,cax=cax,orientation="horizontal",ticks=[-6,0,6])
    cb.outline.set_visible(False)
    cb.set_label("Full minus fixed (pp)",fontsize=7.3,labelpad=4)
    cb.ax.tick_params(labelsize=7,pad=3)
    granularity_rows=[]
    x=np.arange(4)
    for si,(setting,means) in enumerate([("Reuse",[72,77,79,78.5]),("Collect",[71,74.5,78,78.2])]):
        values=np.array(means)+rng.normal(0,2.4,(N_GROUPS,4))
        # Preserve the data RNG stream; this bootstrap is also used in the
        # original reporting fixture, independently of the display choice.
        for i in x: bootstrap(values[:,i],rng)
        direction=-1 if si==0 else 1
        violins=b.violinplot(values,positions=x,widths=.76,showextrema=False,
                            showmedians=False,bw_method=.35)
        for j,body in enumerate(violins["bodies"]):
            color=FIVE_COLORS[j]
            vertices=body.get_paths()[0].vertices
            vertices[:,0]=(np.minimum(vertices[:,0],j) if si==0
                           else np.maximum(vertices[:,0],j))
            body.set_facecolor(tint(color,.88));body.set_edgecolor(color)
            body.set_alpha(1);body.set_linewidth(.55)
            if si:
                body.set_edgecolor(companion(color, 3.0))
                body.set_hatch("/")
            b.scatter(j+direction*vrng.uniform(.045,.31,N_GROUPS),values[:,j],
                      s=1.5,color=companion(color,3.0),alpha=.32,lw=0,zorder=2)
            low,q1,med,q3,high=np.quantile(values[:,j],[.1,.25,.5,.75,.9])
            pos=j+direction*.08
            dark=MUTED
            b.plot([pos,pos],[low,high],color=dark,lw=.65,zorder=3)
            b.plot([pos,pos],[q1,q3],color=dark,lw=2.2,zorder=4)
            b.scatter(pos,med,s=8,color="white",edgecolor=dark,lw=.55,zorder=5)
        for g in range(N_GROUPS):
            for j,h in enumerate(["H0","H0+H1","H0+H1+H2","H0+H1+H2+H3"]):
                granularity_rows.append(dict(setting=setting,input_group=f"SIM-H-{g:04d}",
                                             feedback=h,agreement_pct=values[g,j]))
    b.set(xticks=x,xticklabels=[r"$H_0$",r"+$H_1$",r"+$H_2$",r"+$H_3$"],
          ylim=(62,88),yticks=[65,75,85],xlim=(-.55,3.55),
          ylabel="Agreement (%)",xlabel="Cumulative feedback")
    b.grid(axis="y");panel(b,"b","Feedback detail")
    fig.legend(handles=[Patch(facecolor="#F2F3F4",edgecolor=MUTED,hatch=None if s=="Reuse" else "/",
                              label=SETTING_TITLES[s]+(" · left" if s=="Reuse" else " · right")) for s in SETTINGS],
               loc="center",bbox_to_anchor=(.79,.12),ncol=1,frameon=False,handlelength=1)
    write_csv("component_effects.csv",rows);write_csv("granularity.csv",granularity_rows)
    save(fig,"ablation","Paired effects are not additive. Split violins: groups; thick bars: IQR; thin bars: 10–90%.")


def refinement():
    rng=np.random.default_rng(SEED+5)
    rows,shares,changes=[],[],[]
    era_deltas=[.3,.18,.16,-.06,.20,.33,-.13,.11]
    for ci,(setting,domain,*_) in enumerate(COHORTS):
        base=rng.normal(0,1,N_GROUPS)
        common=rng.normal(0,.25,N_GROUPS)
        seed=base+.22+common+rng.normal(0,.56,N_GROUPS)
        era=base+.22+era_deltas[ci]+common+rng.normal(0,.60,N_GROUPS)
        abstain=rng.random(N_GROUPS)<.05
        diff=era-seed
        outcome=np.where(abstain,"Abstain",np.where(abs(diff)<.15,"Tie",np.where(diff>0,"ERA wins","Seed wins")))
        shares.append([100*np.mean(outcome==k) for k in ["ERA wins","Tie","Seed wins","Abstain"]])
        changes.append([(100*np.mean((v-base)>.15),100*np.mean((v-base)<-.15)) for v in [seed,era]])
        for i in range(N_GROUPS):
            rows.append(dict(setting=setting,domain=domain,input_group=f"SIM-C2-{ci}-{i:04d}",
                             y0_quality=base[i],seed_quality=seed[i],era_quality=era[i],
                             blinded_outcome=outcome[i],seed_major_regression=int(seed[i]-base[i]<-.8),
                             era_major_regression=int(era[i]-base[i]<-.8)))
    write_csv("refinement_groups.csv",rows)
    fig=plt.figure(figsize=(5.4,3.45))
    a=fig.add_axes([.12,.28,.355,.52])
    b=fig.add_axes([.585,.28,.33,.52])
    axes=(a,b);y=np.arange(8);shares=np.array(shares)
    for ax in axes:cohort_rows(ax,labels=False)
    vrng=np.random.default_rng(SEED+205)
    differences=[np.array([r["era_quality"]-r["seed_quality"] for r in rows if r["domain"]==c[1]]) for c in COHORTS]
    violins=a.violinplot(differences,positions=y,vert=False,widths=.68,
                        showextrema=False,showmedians=False,bw_method=.35)
    for i,body in enumerate(violins["bodies"]):
        vertices=body.get_paths()[0].vertices
        vertices[:,1]=np.minimum(vertices[:,1],i)
        color=FAMILY_COLORS[COHORTS[i][3]]
        dark=MUTED
        body.set_facecolor(tint(color,.88));body.set_edgecolor(color)
        body.set_alpha(1);body.set_linewidth(.6)
        a.scatter(differences[i],i+vrng.uniform(.04,.24,N_GROUPS),s=2.2,
                  color=companion(color,3.0),alpha=.48,lw=0,zorder=2)
        q1,median,q3=np.quantile(differences[i],[.25,.5,.75])
        a.plot([q1,q3],[i-.075,i-.075],color=dark,lw=2.1,zorder=3)
        a.scatter(median,i-.075,s=12,color="white",edgecolor=dark,lw=.75,zorder=4)
    extent=max(3,np.ceil(max(abs(v).max() for v in differences)))
    a.set(xlim=(-extent,extent),xticks=[-2,0,2],xlabel="Quality difference (toy units)")
    a.axvline(0,color="#A9B7C0",lw=.75,ls=(0,(2,2)),zorder=1)
    a.grid(axis="x")
    panel(a,"a","Paired quality change")
    # A diverging preference balance preserves the all-input denominator.
    # Ties straddle zero; abstentions have a separate, aligned percentage column
    # so they cannot look like evidence favoring either refinement method.
    for i,(era_share,tie_share,seed_share,abstain_share) in enumerate(shares):
        for value,left,color in [(seed_share,-tie_share/2-seed_share,METHOD_COLORS["Static tools"]),
                                 (tie_share,-tie_share/2,CREAM),
                                 (era_share,tie_share/2,ROSE)]:
            b.barh(i,value,left=left,height=.52,color=color,edgecolor="white",lw=.5,zorder=3)
        b.text(-tie_share/2-seed_share/2,i,f"{seed_share:.0f}",color=on_fill(METHOD_COLORS["Static tools"]),
               ha="center",va="center",fontsize=7,zorder=4)
        b.text(tie_share/2+era_share/2,i,f"{era_share:.0f}",color=on_fill(ROSE),
               ha="center",va="center",fontsize=7,zorder=4)
        b.text(1.14,i,f"{abstain_share:.1f}",transform=b.get_yaxis_transform(),
               va="center",ha="right",fontsize=7,color=MUTED)
    b.axvline(0,color="#A9B7C0",lw=.65,zorder=1)
    b.set(xlim=(-66,66),xticks=[-60,-30,0,30,60],xticklabels=[60,30,0,30,60],
          xlabel="Share of all input groups (%)")
    b.grid(axis="x")
    panel(b,"b","Preference balance")
    b.annotate("Abst.\n(%)",(1.14,1),xycoords="axes fraction",xytext=(0,6),textcoords="offset points",
               ha="right",va="bottom",fontsize=6.8,color=MUTED,annotation_clip=False)
    a.set_yticklabels([c[1].replace("TD-","") for c in COHORTS])
    setting_brackets(fig,.022,.28,.52)
    handles=[Patch(facecolor=METHOD_COLORS["Static tools"],label="Seed wins"),Patch(facecolor=CREAM,label="Tie"),
             Patch(facecolor=ROSE,label="ERA wins")]
    compact_legend(fig,handles,3,y=.12)
    save(fig,"refinement","Difference = ERA-refined minus Seed-refined. All artifacts and judgments here are synthetic.")


def read_fixture(name):
    with (DATA / name).open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    if not rows or any(row.get("provenance") != "SIMULATED" for row in rows):
        raise ValueError(f"The layout renderer accepts only disclosed simulated fixtures: {name}")
    return rows


def outcomes():
    """A complete 22-domain score matrix with aligned paired OOD effects.

    Five method colors are used together, never as a score heatmap. All small
    bars share a true 0–100% scale; printed percentages are the primary readout.
    C1 values come from per-method complete groups, paired intervals from joint
    completeness. The fixed method subset is type-based, not selected by rank.
    """
    summaries = read_fixture("c1_summary.csv")
    effects = read_fixture("alignment_effects.csv")
    lookup = {(r["domain"], r["method"]): r for r in summaries
              if r["split"] == "OOD" and r["metric"] == "pairwise"}
    paired = {r["domain"]: r for r in effects if r["split"] == "OOD"}
    positions, headings, limits = domain_layout()
    fig = plt.figure(figsize=(5.4, 6.0))
    labels = fig.add_axes([.025, .135, .357, .705])
    a = fig.add_axes([.403, .135, .355, .705])
    b = fig.add_axes([.812, .135, .163, .705])
    domain_labels(labels, positions, headings, limits)
    a.set(xlim=(0, 5), ylim=limits, xticks=[], yticks=[])
    b.set(ylim=limits, yticks=[], xlim=(-12, 16), xticks=[-10, 0, 10])
    fig.text(.025, .925, "22 DOMAINS / 4 FAMILIES", fontsize=8, weight="bold")
    fig.text(.403, .925, "a  OOD agreement (%)", fontsize=8.4)
    fig.text(.812, .925, "b  Paired gain", fontsize=8.4)
    fig.text(.375, .87, "H", fontsize=7, color=MUTED, ha="right")
    for j, method in enumerate(DISPLAY_METHODS):
        color = METHOD_COLORS[method]
        a.axvspan(j+.035, j+.965, color=tint(color, .13), lw=0, zorder=0)
        name = ("Static\njudge", "Static\ntools", "Prompt\nopt.", "Prog.\nsearch", "ERA")[j]
        a.text(j+.5, 1.02, name, transform=a.get_xaxis_transform(), ha="center",
               va="bottom", fontsize=7.3, weight="bold" if method == "ERA" else "normal",
               linespacing=1.2)
        a.plot([j+.13, j+.87], [1.006, 1.006], transform=a.get_xaxis_transform(),
               color=color, lw=3.0, clip_on=False)
    b.text(.5, 1.023, "ERA − seed\n95% interval", transform=b.transAxes,
           ha="center", va="bottom", fontsize=7.1, color=MUTED, linespacing=1.2)
    display_values, display_effects = [], []
    for i, (setting, domain, *_) in enumerate(DOMAIN_ORDER):
        y = positions[domain]
        for j, method in enumerate(DISPLAY_METHODS):
            row, color = lookup[(domain, method)], METHOD_COLORS[method]
            value = 100 * float(row["mean"])
            # Identical length and origin in every cell; no per-domain rescaling.
            a.plot([j+.14, j+.86], [y+.27, y+.27], color="#E2E5E8", lw=1.3, zorder=1)
            a.plot([j+.14, j+.14+.72*value/100], [y+.27, y+.27],
                   color=color, lw=2.9, zorder=2, solid_capstyle="butt")
            a.text(j+.5, y-.09, f"{value:.1f}", ha="center", va="center", fontsize=7.5,
                   color=ON_FILL, weight="bold" if method == "ERA" else "normal")
            display_values.append(dict(setting=setting, domain=domain, method=method,
                                       split="OOD", agreement_pct=value))
        row = paired[domain]
        mean, lo, hi = (float(row[k]) for k in ("delta_pp", "lower", "upper"))
        b.errorbar(mean, y, xerr=[[mean-lo], [hi-mean]], fmt="D", ms=3.6,
                   mfc=ROSE, color=ERA_EDGE, mew=.65, elinewidth=.8, capsize=1.4, zorder=3)
        display_effects.append(dict(domain=domain, split="OOD", delta_pp=mean, lower=lo, upper=hi,
                                   complete_pairs=int(row["complete_pairs"])))
    for _, y, _ in headings:
        # White header bands preserve grouping without assigning 22 hue labels.
        a.axhspan(y-.50, y+.53, color="white", lw=0, zorder=4)
        b.axhline(y, color=GRID, lw=.5)
    b.axvline(0, color=MUTED, lw=.7, ls=(0, (2, 2)), zorder=1)
    b.grid(axis="x")
    b.set_xlabel("Gain (pp)", fontsize=7.5)
    fig.text(.403, .091, "Bars share a 0–100% scale.", fontsize=7.1, color=MUTED)
    (PREVIEW / "outcomes-summary.json").write_text(json.dumps({
        "simulation_only": True, "sources": ["c1_summary.csv", "alignment_effects.csv"],
        "methods": list(DISPLAY_METHODS), "domains": [c[1] for c in DOMAIN_ORDER],
        "family_sizes": {family: count for family, _, count in headings},
        "agreement_denominator": "Per-method complete input groups, not domain averages",
        "effect_denominator": "Jointly completed ERA/static-tools input groups",
        "method_values": display_values, "paired_effects": display_effects}, indent=2) + "\n",
        encoding="utf-8")
    save(fig, "outcomes", "H: reused (R) / new (N) preferences; assignments do not assert actual label availability.\n"
         "All 22 domains are synthetic layout fixtures, not completed experiments. C2 is reported separately.")


def cost(summary):
    """Linked profiles share method rows instead of a seven-item number key."""
    fig,axes=plt.subplots(1,2,figsize=(5.4,3.0))
    fig.subplots_adjust(left=.225,right=.97,top=.80,bottom=.29,wspace=.32)
    rows=[]
    points={}
    for setting in SETTINGS:
        cohort=[c for c in C1_COHORTS if c[0]==setting]
        for mi,method in enumerate(METHODS):
            x=np.mean([summary[(c[1],"ID",method)]["cost"] for c in cohort])
            y=100*np.mean([summary[(c[1],"ID",method)]["pairwise"][0] for c in cohort])
            points[(setting,method)]=(x,y)
            rows.append(dict(setting=setting,method=method,cost_units=x,agreement_pct=y))
    for k,ax in enumerate(axes):
        for i,method in enumerate(METHODS):
            if i%2==0:ax.axhspan(i-.44,i+.44,color="#F8F9FA",lw=0,zorder=0)
            values=[points[(s,method)][k] for s in SETTINGS]
            color=METHOD_COLORS.get(method, "#A3A8B0")
            ax.plot(values,[i-.10,i+.10],color=color,lw=3.0,zorder=2)
            for j,setting in enumerate(SETTINGS):
                ax.scatter(values[j],i+(-.10 if j==0 else .10),s=23,
                           marker="o" if j==0 else "s",facecolor=color if j==0 else "white",
                           edgecolor=companion(color,3.0),lw=.65,zorder=3)
        ax.set(ylim=(6.65,-.65),yticks=range(7),
               yticklabels=SHORT_METHODS if k==0 else [])
        ax.grid(axis="x")
    axes[0].set(xlim=(0,1.75),xticks=[0,.5,1,1.5],xlabel="Assigned cost (relative units)")
    axes[1].set(xlim=(60,82),xticks=[60,70,80],xlabel="Pairwise agreement (%)")
    panel(axes[0],"a","Deployment cost")
    panel(axes[1],"b","Alignment")
    handles=[Line2D([],[],marker="o" if j==0 else "s",ms=4.5,ls="none",
                    color=MUTED,mfc=MUTED if j==0 else "white",label=SETTING_TITLES[s])
             for j,s in enumerate(SETTINGS)]
    compact_legend(fig,handles,2,y=.12)
    write_csv("cost_summary.csv",rows)
    save(fig,"cost","Lines pair the two settings for one evaluator. Costs are assigned, not measured compute.")


def tables(summary):
    lines=["% GENERATED SIMULATED DATA. Do not cite as experimental results.",
           r"\begin{tabularx}{\linewidth}{@{}P{3.8cm}*{8}{>{\raggedleft\arraybackslash}X}@{}}",r"\toprule",
           r"& \multicolumn{4}{c}{ID test} & \multicolumn{4}{c}{OOD test} \\",
           r"\cmidrule(lr){2-5}\cmidrule(l){6-9}",
           r"Evaluator & Pair & Top & Bo4 & Reg & Pair & Top & Bo4 & Reg \\",r"\midrule"]
    for si,setting in enumerate(SETTINGS):
        if si:lines.append(r"\addlinespace")
        lines.append(r"\multicolumn{9}{@{}l}{\textcolor{pEvo}{\textbf{SIMULATED}}\quad "
                     + SETTING_TITLES[setting] + r"} \\")
        cohort=[c for c in C1_COHORTS if c[0]==setting]
        for method in METHODS:
            values=[]
            for split in ("ID","OOD"):
                for metric in METRICS:
                    val=np.mean([summary[(c[1],split,method)][metric][0] for c in cohort])
                    values.append(f"{val:.2f}" if metric=="rank_regret" else f"{100*val:.1f}")
            if method=="ERA":lines.append(r"\rowcolor{pEvoWash}")
            lines.append(method+" & "+" & ".join(values)+r" \\")
    lines.extend([r"\bottomrule",r"\end{tabularx}"])
    (OUT/"c1_table.tex").write_text("\n".join(lines)+"\n",encoding="utf-8")
    coverage=[]
    for setting in SETTINGS:
        for split in ("ID","OOD"):
            cohort=[c for c in C1_COHORTS if c[0]==setting]
            for method in METHODS:
                coverage.append(dict(setting=setting,split=split,method=method,
                                     macro_coverage=np.mean([summary[(c[1],split,method)]["coverage"] for c in cohort])))
    write_csv("macro_coverage.csv",coverage)


def main(palette=DEFAULT_PALETTE, preview_root=None):
    global DATA, OUT, PREVIEW
    if preview_root is not None:
        destination = Path(preview_root).resolve()
        destination.relative_to(ROOT / "build")
        DATA, OUT, PREVIEW = (destination / name for name in ("data", "pdf", "png"))
    use_palette(palette)
    for path in (DATA,OUT,PREVIEW):path.mkdir(parents=True,exist_ok=True)
    configure()
    records,summary=c1_data()
    alignment(records);acquisition();annotation();selection(records,summary)
    ablation();refinement();outcomes();cost(summary);tables(summary)
    write_csv("cohorts.csv",[dict(setting=s,domain=d,short_name=n,family=f,groups=N_GROUPS)
                            for s,d,n,f,_ in COHORTS])
    write_csv("c1_cohorts.csv",[dict(setting=s,domain=d,short_name=DOMAIN_NAMES[d],family=f,groups=N_GROUPS)
                               for s,d,n,f,_ in DOMAIN_ORDER])
    if preview_root is not None:
        print(f"Rendered isolated {palette} previews in {destination}; canonical fixtures untouched.")
        return
    files=(sorted(DATA.glob("*.csv"))+sorted(OUT.glob("*.pdf"))+[OUT/"c1_table.tex",
           Path(__file__).resolve()]+[ROOT/f"figures/simulated_{name}.tex" for name in CHARTS])
    manifest={
        "simulation_only":True,"empirical_evidence":False,"seed":SEED,
        "palette":palette,"palette_status":"Provisional author-review candidate, not a final author choice.",
        "main_composite":"outcomes.pdf covers all 22 domains with five method-wise OOD agreement columns and paired ERA-minus-seed intervals; C2 and component details remain separate eight-domain fixtures.",
        "coverage":{"c1_domains":22,"diagnostic_domains":8,"families":[6,6,5,5],"c1_domains_per_setting":11},
        "purpose":"Author-requested quantitative layout examples; never evidence of method effectiveness.",
        "not_valid_for":["empirical claims","power analysis","method ranking","actual data availability",
                         "annotation quality claims","acquisition effectiveness","training outcomes"],
        "domain_assignment":"Illustrative only. Reuse/Collect are construction settings, not fixed domain classes.",
        "algorithm":"Independent toy data generators, not ERA execution. No models, APIs, real artifacts, or annotators.",
        "cohort_groups":N_GROUPS,"candidates_per_c1_group":4,"complete_scores_per_candidate":N_REPEATS,
        "bootstrap_replicates":N_BOOT,"intervals":"95% resampling intervals over synthetic input groups only",
        "acquisition":"12 toy runs; bands are 10–90% quantiles, not confidence intervals; N_H includes a 10-unit anchor.",
        "annotation":"0/1 are candidate preferences, 2 is a tie, -1 is abstention; 3 toy raters per group.",
        "versions":{"matplotlib":matplotlib.__version__,"numpy":np.__version__},
        "files":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
    }
    (DATA/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(f"Rendered {len(CHARTS)} SIMULATED charts and a numerical table; no experiments executed.")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--palette", choices=PALETTES, default=DEFAULT_PALETTE)
    parser.add_argument("--preview-root", type=Path,
                        help="Isolate all outputs below this build/ directory; never change canonical assets")
    args = parser.parse_args()
    if args.palette != DEFAULT_PALETTE and args.preview_root is None:
        parser.error("Candidate palettes require --preview-root; canonical figures also share preamble.tex colors")
    main(args.palette, args.preview_root)
