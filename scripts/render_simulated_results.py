#!/usr/bin/env python3
"""Reproducible, explicitly SIMULATED paper-layout fixtures; no model/API calls.

These toy data are not a simulation of ERA's actual implementation, a power
analysis, or a prediction of experimental effects. Domain assignments, noise,
effects, and costs are chosen solely to exercise the reporting/plotting code.
Never mix these files with collected human feedback or experimental outputs.
"""

import csv
import hashlib
import itertools
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
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
INK, MUTED, GRID = "#303C43", "#68767C", "#E5EAEC"
# The author's three references share a blue/sea-glass/sand/coral vocabulary.
# Roles, not chart order, determine colors; method colors never change by panel.
BLUE, SKY, TEAL, MINT = "#376795", "#7BC0CD", "#51999F", "#BFDFD2"
GOLD, CREAM, PEACH, CORAL = "#DBCB92", "#FFE6B7", "#ECB66C", "#ED8D5A"
GREEN, BROWN, RED = "#3E7F81", "#A77535", "#AD5D39"
METHOD_COLORS = ["#A8B4BA", GOLD, SKY, BLUE, MINT, PEACH, CORAL]
RANK_COLORS = [TEAL, MINT, CREAM, CORAL, "#E8ECEE"]
SETTING_COLORS = {"Reuse": TEAL, "Collect": PEACH}
SETTINGS = ("Reuse", "Collect")
SETTING_TITLES = {"Reuse": "Reused preferences", "Collect": "New preferences"}
METHODS = ("Single metric", "Metric ensemble", "Static judge", "Static tools",
           "Prompt optimization", "Program search", "P2E (ERA)")
SHORT_METHODS = ("Metric", "Ensemble", "Static judge", "Static tools",
                 "Prompt opt.", "Program search", "P2E (ERA)")
POLICIES = ("Random", "Uncertainty", "Model conflict", "Run instability", "Multi-source")
POLICY_COLORS = [BLUE, TEAL, BROWN, "#9BA9AD", CORAL]
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
CHARTS = ("alignment", "acquisition", "annotation", "selection", "ablation", "refinement", "cost")
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
        "axes.edgecolor": "#BEC8CD", "axes.linewidth": .55,
        "grid.color": GRID, "grid.linewidth": .55,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.spines.left": False, "axes.spines.bottom": False,
        "xtick.major.size": 0, "ytick.major.size": 0,
        "xtick.major.pad": 5, "ytick.major.pad": 5,
        "axes.labelpad": 6, "lines.solid_capstyle": "round",
        "savefig.facecolor": "white", "figure.facecolor": "white",
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "axes.unicode_minus": True,
    })


def panel(ax, letter, title):
    ax.set_title(f"{letter}  {title}", loc="left", pad=10, fontweight="bold")
    ax.set_axisbelow(True)


def save(fig, name, note):
    fig.text(.98, .975, "SIMULATED DATA  /  NOT EXPERIMENTAL RESULTS",
             ha="right", va="top", color=RED, fontsize=6.8, weight="bold")
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
        "Author": "", "Creator": "P2E synthetic reporting fixtures",
        "CreationDate": None, "ModDate": None,
    })
    fig.savefig(PREVIEW / f"{name}.png", dpi=220)
    plt.close(fig)


def cohort_rows(ax, labels=True):
    """A quiet, fixed row order makes domain panels directly comparable."""
    ax.set(yticks=range(8), ylim=(7.6, -.65))
    ax.set_yticklabels([c[2] for c in COHORTS] if labels else [])
    ax.axhline(3.5, color=GRID, lw=.8, zorder=0)


def setting_brackets(fig, left, bottom, height):
    fig.text(left, bottom + height * .77, "REUSED", color=MUTED,
             rotation=90, va="center", ha="center", fontsize=6.5, weight="bold")
    fig.text(left, bottom + height * .24, "NEW", color=MUTED,
             rotation=90, va="center", ha="center", fontsize=6.5, weight="bold")


def compact_legend(fig, handles, ncol, y=.12):
    return fig.legend(handles=handles, loc="center", bbox_to_anchor=(.52, y),
                      ncol=ncol, frameon=False, handlelength=1.5,
                      handletextpad=.55, columnspacing=1.4, labelspacing=.5)


def c1_data():
    rng = np.random.default_rng(SEED + 1)
    brng = np.random.default_rng(SEED + 101)
    rows, records, summary = [], {}, {}
    # Deliberately heterogeneous, with null/negative ERA-vs-seed contrasts.
    era_factors = [.69, .77, .88, 1.05, .78, .72, 1.11, .86]
    domain_noise = [.97, 1.14, .84, 1.24, 1.08, .95, 1.18, 1.04]
    noise = np.array([1.70, 1.39, 1.14, 1.01, .98, .93, 1.0])
    costs = np.array([.22, .63, .78, 1.00, 1.12, 1.38, 1.51])
    for ci, (setting, domain, _, _, _) in enumerate(COHORTS):
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
        setting = next(c[0] for c in COHORTS if c[1] == domain)
        for metric in METRICS:
            mean, lo, hi = stats[metric]
            aggregate.append(dict(setting=setting, domain=domain, split=split, method=method,
                                  metric=metric, mean=mean, lower=lo, upper=hi,
                                  coverage=stats["coverage"], cost_units=stats["cost"]))
    write_csv("c1_summary.csv", aggregate)
    return records, summary


def alignment(records):
    """Paired effects, not four overlapping encodings of absolute scores."""
    rng = np.random.default_rng(SEED + 111)
    fig, axes = plt.subplots(1, 2, figsize=(5.4, 2.95))
    fig.subplots_adjust(left=.255, right=.965, top=.84, bottom=.235, wspace=.23)
    rows = []
    for ax, split, letter in zip(axes, ("ID", "OOD"), "ab"):
        ax.axvspan(-12, 0, color="#F6F8F9", zorder=0)
        for i, (setting, domain, *_) in enumerate(COHORTS):
            seed = records[(domain, split, "Static tools")][:, 0]
            era = records[(domain, split, "P2E (ERA)")][:, 0]
            paired = np.isfinite(seed) & np.isfinite(era)
            mean, lo, hi = bootstrap(100 * (era[paired] - seed[paired]), rng)
            ax.errorbar(mean, i, xerr=[[mean-lo], [hi-mean]], fmt="D", ms=4.2,
                        color=RED, mfc=CORAL, mew=.7, elinewidth=1.05, capsize=2, zorder=3)
            rows.append(dict(setting=setting, domain=domain, split=split,
                             complete_pairs=int(paired.sum()), delta_pp=mean, lower=lo, upper=hi))
        cohort_rows(ax, labels=letter == "a")
        ax.axvline(0, color="#97A5AC", lw=.75, zorder=1)
        ax.set(xlim=(-12, 16), xticks=[-10, 0, 10])
        ax.grid(axis="x")
        panel(ax, letter, "ID test" if split == "ID" else "OOD test")
    setting_brackets(fig, .025, .235, .605)
    fig.text(.60, .105, r"$\Delta$ agreement vs. static tools (percentage points)",
             ha="center", fontsize=8)
    write_csv("alignment_effects.csv", rows)
    save(fig, "alignment", "Diamonds: paired means. Whiskers: 95% bootstrap intervals over synthetic input groups.")


def acquisition():
    rng = np.random.default_rng(SEED + 2)
    budgets = np.array([20, 50, 100, 200])
    base = {"Reuse": [[65,69,73,77], [66,71,75,78], [65,71,76,79], [64,69,73,77], [65,73,78,81]],
            "Collect": [[64,68,73,77], [65,70,75,77], [66,69,74,78], [64,70,72,76], [63,69,76,78]]}
    rows = []
    fig, axes = plt.subplots(1,2,figsize=(5.4,2.85))
    fig.subplots_adjust(left=.10,right=.975,top=.83,bottom=.34,wspace=.24)
    for ax, setting, letter in zip(axes, SETTINGS, "ab"):
        common = rng.normal(0, 1.0, (12, 4))
        for i, policy in enumerate(POLICIES):
            values = np.array(base[setting][i]) + common + rng.normal(0, .65, (12, 4))
            low, high = np.quantile(values, [.1,.9], axis=0)
            if i in (0, 4):
                ax.fill_between(budgets,low,high,color=POLICY_COLORS[i],alpha=.13,lw=0)
            ax.plot(budgets,values.mean(axis=0),color=POLICY_COLORS[i],ls=POLICY_STYLES[i],
                    marker=POLICY_MARKERS[i],ms=3.6 if i in (0,4) else 2.1,
                    lw=1.6 if i in (0,4) else .75, alpha=1 if i in (0,4) else .7,
                    zorder=3 if i in (0,4) else 2,label=policy)
            for run in range(12):
                for j,b in enumerate(budgets):
                    rows.append(dict(setting=setting,policy=policy,synthetic_run=run,
                                     human_units=int(b),anchor_units=10,agreement_pct=values[run,j]))
        panel(ax,letter,SETTING_TITLES[setting])
        ax.set(xlim=(12,210),ylim=(60,84),xticks=budgets,yticks=[60,70,80],
               xlabel="Annotation budget")
        ax.grid(axis="y")
        ax.spines["bottom"].set_visible(True)
    axes[0].set_ylabel("Held-out agreement (%)")
    handles, labels = axes[0].get_legend_handles_labels()
    compact_legend(fig, handles, 3, y=.115)
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
    a=fig.add_axes([.115,.30,.235,.53])
    b=fig.add_axes([.445,.30,.17,.53])
    c=fig.add_axes([.70,.30,.275,.53])
    y=np.arange(8)
    for ax in (a,b,c):
        cohort_rows(ax,labels=False)
        ax.grid(axis="x")
    for i,s in enumerate(summaries):
        a.errorbar(s["agreement"],i,xerr=[[s["agreement"]-s["lower"]],
                   [s["upper"]-s["agreement"]]],fmt="o",color=GREEN,mfc=TEAL,
                   ms=3.7,mew=.6,elinewidth=.8,capsize=1.8,zorder=3)
        b.plot([0,s["abstention"]],[i,i],color=GOLD,lw=2,zorder=2)
        b.scatter(s["abstention"],i,color=BROWN,s=15,zorder=3)
    a.set(yticklabels=[c[1].replace("TD-","") for c in COHORTS],xlim=(0,100),
          xticks=[50,75,100],xlabel="Valid pairs (%)")
    a.set_xlim(48,100)
    b.set(xlim=(0,20),xticks=[0,10,20],xlabel="All ratings (%)")
    panel(a,"a","Agreement")
    panel(b,"b","Abstention")
    left=np.zeros(8)
    shares=np.array([s["shares"] for s in summaries])
    for j,(label,color,hatch) in enumerate(zip(["Decisive","Tie","No consensus","Insufficient votes"],
                                             [MINT,CREAM,CORAL,"#E8ECEE"],[None,None,None,"///"])):
        c.barh(y,shares[:,j],left=left,height=.60,color=color,edgecolor="white",lw=.45,hatch=hatch,label=label,zorder=3)
        left+=shares[:,j]
    c.set(xlim=(0,100),xticks=[0,50,100],xlabel="Input groups (%)")
    panel(c,"c","Group outcome")
    setting_brackets(fig,.022,.30,.53)
    handles,_=c.get_legend_handles_labels()
    compact_legend(fig,handles,4,y=.12)
    save(fig,"annotation","Three simulated raters per group. Agreement, abstention, and consensus use distinct denominators.")


def selection(records,summary):
    fig,axes=plt.subplots(1,2,figsize=(5.4,3.05))
    fig.subplots_adjust(left=.10,right=.975,top=.83,bottom=.35,wspace=.25)
    chosen=["Static judge","Static tools","Program search","P2E (ERA)"]
    rows=[]
    for ax,setting,letter in zip(axes,SETTINGS,"ab"):
        cohort=[c for c in COHORTS if c[0]==setting]
        for j,method in enumerate(chosen):
            regrets=np.concatenate([records[(c[1],"ID",method)][:,3] for c in cohort])
            ranks=np.where(np.isfinite(regrets),np.rint(np.nan_to_num(regrets)*3),4).astype(int)
            counts=np.bincount(ranks,minlength=5)
            bottom=0
            for rank,n in enumerate(counts):
                value=100*n/len(ranks)
                ax.bar(j,value,bottom=bottom,width=.61,color=RANK_COLORS[rank],
                       edgecolor="white",lw=.6,hatch="///" if rank==4 else None,zorder=3)
                if rank==0:
                    ax.text(j,value/2,f"{value:.0f}%",color="white",ha="center",va="center",fontsize=8)
                bottom+=value
                rows.append(dict(setting=setting,method=method,selected_rank=str(rank+1) if rank<4 else "unscored",
                                 count=int(n),denominator=len(ranks),share_pct=value))
        ax.set(ylim=(0,100),yticks=[0,25,50,75,100],xticks=range(4),
               xticklabels=["Static\njudge","Static\ntools","Program\nsearch","P2E\n(ERA)"])
        ax.grid(axis="y")
        panel(ax,letter,SETTING_TITLES[setting])
    axes[0].set_ylabel("Selected rank: share of inputs (%)")
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
    a=fig.add_axes([.105,.30,.40,.53])
    b=fig.add_axes([.65,.30,.325,.53])
    cmap=LinearSegmentedColormap.from_list("effects",[TEAL,"#FAFAF7",CORAL])
    im=a.imshow(effects,cmap=cmap,norm=TwoSlopeNorm(vcenter=0,vmin=-6,vmax=6),aspect="auto")
    for (i,j),v in np.ndenumerate(effects):
        a.text(j,i,f"{v:+.1f}",ha="center",va="center",fontsize=7.1)
        for g in range(N_GROUPS):
            rows.append(dict(setting=COHORTS[i][0],domain=COHORTS[i][1],component=components[j],
                             input_group=f"SIM-ABL-{i}-{g:04d}",delta_pp=v+rng.normal(0,7)))
    a.set(yticks=range(8),yticklabels=[c[1].replace("TD-","") for c in COHORTS],
          xticks=range(6),xticklabels=components)
    a.axhline(3.5,color="white",lw=3)
    a.set_xticks(np.arange(-.5,6,1),minor=True)
    a.set_yticks(np.arange(-.5,8,1),minor=True)
    a.grid(which="minor",color="white",lw=.65)
    a.tick_params(which="minor",size=0)
    panel(a,"a","Component effects")
    # Display the means actually exported, rather than the input effect parameters.
    actual=np.array([[np.mean([r["delta_pp"] for r in rows if r["domain"]==c[1] and r["component"]==comp])
                      for comp in components] for c in COHORTS])
    im.set_data(actual)
    for txt,v in zip(a.texts,actual.flat):txt.set_text("0.0" if abs(v)<.05 else f"{v:+.1f}")
    cax=fig.add_axes([.16,.18,.29,.022])
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
        positions=x+(-.17 if si==0 else .17)
        color=SETTING_COLORS[setting]
        for j,pos in enumerate(positions):
            b.scatter(pos+vrng.uniform(-.09,.09,N_GROUPS),values[:,j],s=2.0,
                      color=color,alpha=.23,lw=0,zorder=1)
        b.boxplot(values,positions=positions,widths=.23,patch_artist=True,
                  showfliers=False,whis=(10,90),manage_ticks=False,
                  boxprops=dict(facecolor="white",edgecolor=color,lw=.9),
                  medianprops=dict(color=INK,lw=1),
                  whiskerprops=dict(color=color,lw=.75),capprops=dict(color=color,lw=.75))
        for g in range(N_GROUPS):
            for j,h in enumerate(["H0","H0+H1","H0+H1+H2","H0+H1+H2+H3"]):
                granularity_rows.append(dict(setting=setting,input_group=f"SIM-H-{g:04d}",
                                             feedback=h,agreement_pct=values[g,j]))
    b.set(xticks=x,xticklabels=[r"$H_0$",r"+$H_1$",r"+$H_2$",r"+$H_3$"],
          ylim=(62,88),yticks=[65,75,85],xlim=(-.55,3.55),
          ylabel="Agreement (%)",xlabel="Cumulative feedback")
    b.grid(axis="y");panel(b,"b","Feedback detail")
    fig.legend(handles=[Patch(facecolor="white",edgecolor=SETTING_COLORS[s],label=SETTING_TITLES[s]) for s in SETTINGS],
               loc="center",bbox_to_anchor=(.79,.12),ncol=1,frameon=False,handlelength=1)
    write_csv("component_effects.csv",rows);write_csv("granularity.csv",granularity_rows)
    save(fig,"ablation","Synthetic paired effects are not additive. Boxes: quartiles; whiskers: 10–90%; dots: input groups.")


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
        outcome=np.where(abstain,"Abstain",np.where(abs(diff)<.15,"Tie",np.where(diff>0,"P2E wins","Seed wins")))
        shares.append([100*np.mean(outcome==k) for k in ["P2E wins","Tie","Seed wins","Abstain"]])
        changes.append([(100*np.mean((v-base)>.15),100*np.mean((v-base)<-.15)) for v in [seed,era]])
        for i in range(N_GROUPS):
            rows.append(dict(setting=setting,domain=domain,input_group=f"SIM-C2-{ci}-{i:04d}",
                             y0_quality=base[i],seed_quality=seed[i],p2e_quality=era[i],
                             blinded_outcome=outcome[i],seed_major_regression=int(seed[i]-base[i]<-.8),
                             p2e_major_regression=int(era[i]-base[i]<-.8)))
    write_csv("refinement_groups.csv",rows)
    fig,axes=plt.subplots(1,2,figsize=(5.4,3.45))
    fig.subplots_adjust(left=.12,right=.975,top=.84,bottom=.28,wspace=.28)
    a,b=axes;y=np.arange(8);left=np.zeros(8);shares=np.array(shares)
    vrng=np.random.default_rng(SEED+205)
    differences=[np.array([r["p2e_quality"]-r["seed_quality"] for r in rows if r["domain"]==c[1]]) for c in COHORTS]
    violins=a.violinplot(differences,positions=y,vert=False,widths=.68,
                        showextrema=False,showmedians=False,bw_method=.35)
    for i,body in enumerate(violins["bodies"]):
        vertices=body.get_paths()[0].vertices
        vertices[:,1]=np.minimum(vertices[:,1],i)
        body.set_facecolor(TEAL);body.set_edgecolor(TEAL);body.set_alpha(.27);body.set_linewidth(.65)
        a.scatter(differences[i],i+vrng.uniform(.04,.24,N_GROUPS),s=2.2,
                  color=TEAL,alpha=.32,lw=0,zorder=2)
        q1,median,q3=np.quantile(differences[i],[.25,.5,.75])
        a.plot([q1,q3],[i-.075,i-.075],color=GREEN,lw=2.1,zorder=3)
        a.scatter(median,i-.075,s=12,color="white",edgecolor=GREEN,lw=.75,zorder=4)
    extent=max(3,np.ceil(max(abs(v).max() for v in differences)))
    a.set(xlim=(-extent,extent),xticks=[-2,0,2],xlabel="Quality difference (toy units)")
    a.axvline(0,color="#97A5AC",lw=.8,zorder=0)
    a.grid(axis="x")
    panel(a,"a","Paired quality change")
    for j,(label,color,hatch) in enumerate(zip(["P2E wins","Tie","Seed wins","Abstain"],
                                             [CORAL,CREAM,BLUE,"#E8ECEE"],[None,None,None,"///"])):
        b.barh(y,shares[:,j],left=left,height=.63,color=color,edgecolor="white",lw=.6,hatch=hatch,label=label)
        if j in (0,2):
            for i,v in enumerate(shares[:,j]):
                if v>15:b.text(left[i]+v/2,i,f"{v:.0f}",ha="center",va="center",fontsize=7.3,
                              color="white" if j==2 else INK)
        left+=shares[:,j]
    b.set(xlim=(0,100),xticks=[0,25,50,75,100],xlabel="Input groups (%)")
    panel(b,"b","Preference outcomes")
    for ax in axes:cohort_rows(ax,labels=False)
    a.set_yticklabels([c[1].replace("TD-","") for c in COHORTS])
    setting_brackets(fig,.022,.28,.56)
    handles,_=b.get_legend_handles_labels()
    compact_legend(fig,handles,4,y=.12)
    save(fig,"refinement","Difference = P2E-refined minus Seed-refined. All artifacts and judgments here are synthetic.")


def cost(summary):
    fig,axes=plt.subplots(1,2,figsize=(5.4,3.2))
    fig.subplots_adjust(left=.10,right=.975,top=.83,bottom=.385,wspace=.25)
    rows=[]
    markers=["s","^","o","o","v","P","D"]
    for ax,setting,letter in zip(axes,SETTINGS,"ab"):
        cohort=[c for c in COHORTS if c[0]==setting]
        points=[]
        for mi,method in enumerate(METHODS):
            x=np.mean([summary[(c[1],"ID",method)]["cost"] for c in cohort])
            y=100*np.mean([summary[(c[1],"ID",method)]["pairwise"][0] for c in cohort])
            points.append((x,y))
            ax.scatter(x,y,s=31 if mi==6 else 25,marker=markers[mi],color=METHOD_COLORS[mi],
                       edgecolor=INK,linewidth=.35,zorder=3)
            offset={0:(5,-4),1:(5,-5),2:(-7,6),3:(-6,-11),4:(5,5),5:(-5,6),6:(6,-4)}[mi]
            ax.annotate(str(mi+1),(x,y),xytext=offset,textcoords="offset points",fontsize=7,color=INK)
            rows.append(dict(setting=setting,method=method,cost_units=x,agreement_pct=y))
        frontier=[p for p in points if not any(q[0]<=p[0] and q[1]>=p[1] and q!=p for q in points)]
        frontier=sorted(frontier)
        ax.plot(*np.array(frontier).T,color="#A9B6BC",lw=.8,ls=(0,(3,3)),zorder=1)
        ax.set(xlim=(0,1.90),ylim=(60,85),xticks=[0,.5,1,1.5],yticks=[60,70,80],
               xlabel="Cost (relative units)")
        ax.grid(axis="y")
        panel(ax,letter,SETTING_TITLES[setting])
    axes[0].set_ylabel("Pairwise agreement (%)")
    handles=[Line2D([],[],marker=markers[i],ms=4,ls="none",color=METHOD_COLORS[i],
                    markeredgecolor=INK,markeredgewidth=.35,
                    label=f"{i+1} {SHORT_METHODS[i]}") for i in range(7)]
    compact_legend(fig,handles,3,y=.13)
    write_csv("cost_summary.csv",rows)
    save(fig,"cost","Dashed paths join nondominated toy points. Costs are assigned, not measured deployment costs.")


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
        cohort=[c for c in COHORTS if c[0]==setting]
        for method in METHODS:
            values=[]
            for split in ("ID","OOD"):
                for metric in METRICS:
                    val=np.mean([summary[(c[1],split,method)][metric][0] for c in cohort])
                    values.append(f"{val:.2f}" if metric=="rank_regret" else f"{100*val:.1f}")
            if method=="P2E (ERA)":lines.append(r"\rowcolor{pEvoWash}")
            lines.append(method+" & "+" & ".join(values)+r" \\")
    lines.extend([r"\bottomrule",r"\end{tabularx}"])
    (OUT/"c1_table.tex").write_text("\n".join(lines)+"\n",encoding="utf-8")
    coverage=[]
    for setting in SETTINGS:
        for split in ("ID","OOD"):
            cohort=[c for c in COHORTS if c[0]==setting]
            for method in METHODS:
                coverage.append(dict(setting=setting,split=split,method=method,
                                     macro_coverage=np.mean([summary[(c[1],split,method)]["coverage"] for c in cohort])))
    write_csv("macro_coverage.csv",coverage)


def main():
    for path in (DATA,OUT,PREVIEW):path.mkdir(parents=True,exist_ok=True)
    configure()
    records,summary=c1_data()
    alignment(records);acquisition();annotation();selection(records,summary)
    ablation();refinement();cost(summary);tables(summary)
    write_csv("cohorts.csv",[dict(setting=s,domain=d,short_name=n,family=f,groups=N_GROUPS)
                            for s,d,n,f,_ in COHORTS])
    files=(sorted(DATA.glob("*.csv"))+sorted(OUT.glob("*.pdf"))+[OUT/"c1_table.tex",
           Path(__file__).resolve()]+[ROOT/f"figures/simulated_{name}.tex" for name in CHARTS])
    manifest={
        "simulation_only":True,"empirical_evidence":False,"seed":SEED,
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


if __name__=="__main__":main()
