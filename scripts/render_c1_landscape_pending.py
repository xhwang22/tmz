#!/usr/bin/env python3
"""Keep the approved Fig3 geometry/palette; draw no invented result marks."""
import hashlib
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import Wedge
import numpy as np
from render_c1_landscape import ROOT, WIDTH, HEIGHT, FAMILIES, INK, MUTED, GRID, ERA, configure

def render():
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

    text(.13, 3.46, "RESULTS PENDING", size=6.8, role="strong",
         bbox=dict(boxstyle="square,pad=.22", facecolor="#FBECEF", edgecolor="none"))
    text(5.27, 3.46, "Original layout · no empirical measurements", ha="right", size=6.8, color=MUTED)
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
    text(cx, cy-.11, "candidate tasks", size=5.6, ha="center", color=MUTED)
    for y, value, label in ((2.87, "4", "families"), (2.37, "Held-out", "within domain"),
                            (1.87, "N: TBD", "selection pool")):
        text(2.28, y, value, size=12, role="serif", ha="center")
        text(2.28, y-.16, label, ha="center", color=MUTED)


    panel("b", "Deployment cost & quality", 2.88, 3.25)
    text(3.0, 3.08, "Matched inputs; actual model and tool cost", size=7.1, color=MUTED)
    x0, y0, w, h = 3.18, 1.88, 2.07, 1.03
    for frac in (.25, .5, .75, 1):
        line([x0, x0+w], [y0+h*frac]*2)
    line([x0, x0+w], [y0]*2, color="#A8B0B8")
    line([x0]*2, [y0, y0+h], color="#A8B0B8")
    text(x0+w/2, y0+h*.55, "Measurements pending", ha="center", color=MUTED, role="italic", size=8.2)
    text(x0+w/2, y0-.26, "Deployment cost / output", ha="center", size=8)
    text(x0-.26, y0+h/2, "Preference agreement", ha="center", rotation=90, size=8)
    text(3.00, 1.46, "Family colors preserved", color=MUTED, size=7)
    for i, (_, _, _, color) in enumerate(FAMILIES):
        ax.plot(4.58+i*.19, 1.46, marker="s", ms=5, mfc=color, mec="none", linestyle="none")

    panel("c", "Agreement gains across tasks", .13, 1.31)
    text(5.27, 1.31, "Paired differences; no result marks yet", ha="right", color=MUTED, size=6.7)
    left, right, bottom, bh, gap = .40, 5.27, .41, .55, .12
    step = (right-left-gap*3)/22
    pos = left
    for family, name, count, color in FAMILIES:
        width = count*step
        text(pos+width/2, bottom+bh+.18, name, size=8.1, role="italic", ha="center")
        line([pos, pos+width], [bottom+bh+.07]*2, color=color, lw=1.4, solid_capstyle="round")
        ax.axvspan(pos, pos+width, ymin=bottom/HEIGHT, ymax=(bottom+bh)/HEIGHT,
                   facecolor=tint(color,.13), edgecolor="none")
        for j in range(count):
            center=pos+(j+.5)*step
            text(center, bottom-.10, f"{family}{j+1}", size=6.1, ha="center")
        text(pos+width/2, bottom+bh*.68, "vs Seed: pending", size=7, ha="center", color=MUTED)
        text(pos+width/2, bottom+bh*.30, "vs GEPA: pending", size=7, ha="center", color=ERA)
        pos += width+gap
    text(.13,.10,"Task sectors show candidate scope, not sample shares; final plots use admitted domains only.",size=6.7,color=MUTED)
    target=ROOT/"figures/c1_landscape_pending"
    for ext in ("pdf","svg","png"):
        fig.savefig(target.with_suffix("."+ext), dpi=300,
                    metadata={"Creator":"IterEval reporting template"} if ext=="pdf" else None)
    plt.close(fig)
    files={str(target.with_suffix("."+ext).relative_to(ROOT)):hashlib.sha256(target.with_suffix("."+ext).read_bytes()).hexdigest()
           for ext in ("pdf","svg","png")}
    source=ROOT/"scripts/render_c1_landscape_pending.py"
    files[str(source.relative_to(ROOT))]=hashlib.sha256(source.read_bytes()).hexdigest()
    manifest={"kind":"unmeasured_reporting_template","empirical_evidence":False,"quantitative_marks":False,
              "original_geometry":"figures/simulated/c1_landscape.pdf",
              "preserved":"5.4 x 3.57 inch canvas; exact annular sectors, family colors, typography and panel locations",
              "paper_graphic":"figures/c1_landscape_pending.pdf","files":files}
    target.with_suffix(".manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")

if __name__=="__main__":
    render()
