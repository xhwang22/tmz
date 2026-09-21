#!/usr/bin/env python3
"""Render the approved overview with editable labels and existing pictograms.

Run: uv run --python 3.11 --with pillow --with cairosvg python \
     scripts/render_overview_layout_review.py
Add --publish to export figures/overview.{svg,pdf,png} and its provenance.
The stable build preview is overwritten; no numbered versions are created.
"""
from pathlib import Path
from collections import deque
from io import BytesIO
import base64
import hashlib
import html
import json
import argparse

import cairosvg
from PIL import Image, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "output/imagegen/overview-panel-c-action-cycle-20260921-v12.png"
OUT = ROOT / "build/overview-layout-current"
PAPER = ROOT / "figures"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--publish", action="store_true", help="also replace the canonical manuscript exports")
args = parser.parse_args()
W, H = 1840, 800
PRINT_WIDTH_IN = 5.4
GREEN, DARK = "#62AAA5", "#477D79"
NAVY, INK, GRAY = "#29577F", "#25272B", "#707982"
BG_GREEN, BG_PEACH, BG_BLUE = "#F1F7F5", "#FCF4EE", "#F1F5FA"
src = Image.open(SOURCE).convert("RGB")
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == "f3169240b9af4d0fb3f4ea9d892082e701793c36014a16afa03da45a5190bf40", "Illustration source changed"
sprite_metadata = {}
image_placements = []

# Boxes are measured on a 1300 x 770 rendering of the existing generated art.
CROPS = {
    # One focal object per task family, rather than a reduced multi-object scene.
    "visual": (52, 78, 180, 182),
    "image": (357, 87, 445, 174),
    "text": (702, 83, 789, 182),
    "research": (1081, 87, 1183, 183),
    "database": (46, 302, 90, 355),
    "outputs": (200, 301, 246, 357),
    "human": (34, 574, 136, 678),
    "direction": (385, 445, 468, 528),
    "program": (536, 447, 620, 528),
    "diagnostics": (833, 448, 910, 534),
    "checking": (648, 352, 684, 387),
    "best": (820, 250, 892, 315),
    "lock": (951, 279, 978, 309),
    "selection": (1073, 339, 1266, 415),
    "refinement": (1073, 493, 1266, 569),
    "training": (1073, 651, 1266, 727),
}


def cutout(box, name):
    """Remove only background connected to crop edges; keep enclosed paper.

    This is mechanical compositing for a layout proof, not new illustration.
    """
    box = tuple(round(v * (src.width / 1300 if i % 2 == 0 else src.height / 770))
                for i, v in enumerate(box))
    im = src.crop(box).convert("RGBA")
    px = im.load()
    w, h = im.size
    refs = [px[1, 1][:3], px[w - 2, 1][:3], px[1, h - 2][:3], px[w - 2, h - 2][:3]]
    seen = set()
    queue = deque([(x, 0) for x in range(w)] + [(x, h - 1) for x in range(w)]
                  + [(0, y) for y in range(h)] + [(w - 1, y) for y in range(h)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen or x < 0 or y < 0 or x >= w or y >= h:
            continue
        seen.add((x, y))
        c = px[x, y][:3]
        threshold = 10 if name == "text" else 36
        if min(max(abs(c[k] - ref[k]) for k in range(3)) for ref in refs) > threshold:
            continue
        px[x, y] = (*c, 0)
        queue.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))
    if name == "human":
        # The original art has an incoming arrow above the sheet; it is not
        # part of this illustration and must not become a dangling connector.
        for x in range(round(w * .75), w):
            for y in range(round(h * .24)):
                px[x, y] = (*px[x, y][:3], 0)
    if name in {"visual", "image", "text", "research"}:
        # Fit visible artwork, not inconsistent source margins, to the same box.
        bounds = im.getchannel("A").getbbox()
        if bounds:
            im = im.crop(bounds)
    buf = BytesIO()
    im.save(buf, format="PNG")
    sprite_metadata[name] = {"pixels": list(im.size), "sha256": hashlib.sha256(buf.getvalue()).hexdigest()}
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


sprites = {k: cutout(v, k) for k, v in CROPS.items()}
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}">
<title>IterEval — preference mining, evaluator evolution and downstream applications</title>
<desc>One unaccepted candidate supplies both a checking result and retained diagnostic observations. A question drawn from those observations motivates another revision within the same direction, without requiring the rejected program to be inherited. Candidate acceptance remains independent. Pictograms reuse AI-generated illustrations. This is a constructed example, not an observed trajectory.</desc>
<defs>
  <marker id="green" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{DARK}" stroke-width="1.5"/></marker>
  <marker id="navy" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{NAVY}" stroke-width="1.5"/></marker>
  <marker id="gray" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{GRAY}" stroke-width="1.5"/></marker>
</defs><rect width="{W}" height="{H}" fill="white"/>
<g font-family="DejaVu Sans, sans-serif" fill="{INK}">''']
labels = []


def rect(x, y, w, h, fill, stroke="none", radius=18, sw=1.5):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def text(x, y, value, size=28, weight=400, fill=INK, anchor="start", max_width=None):
    font_name = "DejaVuSans-Bold.ttf" if weight >= 600 else "DejaVuSans.ttf"
    font = ImageFont.truetype(font_name, size)
    tw = font.getlength(value)
    left = x - (tw if anchor == "end" else tw / 2 if anchor == "middle" else 0)
    assert left >= 0 and left + tw <= W, (value, left, tw)
    if max_width is not None:
        assert font.getlength(value) <= max_width, (value, font.getlength(value), max_width)
    if y < 770:
        panel = next(((lo, hi) for lo, hi in ((20, 370), (390, 1480), (1500, 1820)) if lo <= x <= hi), None)
        if panel:
            assert left >= panel[0] + 8 and left + tw <= panel[1] - 8, ("panel overflow", value, left, tw)
    ink = font.getbbox(value, anchor="ls")
    labels.append({"text": value, "size": size, "weight": weight, "x": x,
                   "baseline": y, "left": left, "width": tw,
                   "ink_box": [left + ink[0], y + ink[1], left + ink[2], y + ink[3]]})
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{html.escape(value)}</text>')


def lines(x, y, values, size=28, gap=36, **kwargs):
    for i, value in enumerate(values):
        text(x, y + i * gap, value, size=size, **kwargs)


def icon(name, x, y, w, h):
    pixels = sprite_metadata[name]["pixels"]
    ppi = max(pixels[0] / w, pixels[1] / h) * W / PRINT_WIDTH_IN
    image_placements.append({"name": name, "box": [x, y, w, h], **sprite_metadata[name], "effective_ppi": ppi})
    parts.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" xlink:href="{sprites[name]}" preserveAspectRatio="xMidYMid meet"/>')


def path(d, color=DARK, width=3, marker="green", dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    end = f' marker-end="url(#{marker})"' if marker else ""
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{end}{extra}/>')


def panel_letter(x, y, letter):
    parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{NAVY}"/>')
    text(x, y + 9, letter, size=27, fill="white", weight=600, anchor="middle")


# Flatter three-panel composition. The revision story spans the center; its
# independent selection rule occupies a shallow band below, not a tall sidebar.
rect(20, 20, 350, 742, BG_PEACH, "#E8CEBD", 25)
rect(390, 20, 1090, 742, BG_GREEN, "#BAD6D1", 25)
rect(1500, 20, 320, 742, BG_BLUE, "#CDDAE7", 25)
panel_letter(50, 53, "a")
lines(80, 50, ["Disagreement-based", "preference mining"], size=23, gap=33, weight=600, max_width=280)
panel_letter(423, 53, "b")
text(459, 64, "Depth-first evaluator evolution", size=34, weight=600, max_width=990)
text(418, 107, "Reject the candidate, retain the direction and diagnostics", size=27, fill=DARK, max_width=1034)
panel_letter(1533, 53, "c")
lines(1566, 51, ["Downstream", "applications"], size=28, gap=34, weight=600, max_width=240)

# A: compact pictorial input row, two label routes, and signal priority table.
text(195, 126, "Open-ended tasks", size=26, anchor="middle")
for name, cx, label in [("visual", 75, "Visuals"), ("image", 155, "Image/3D"),
                        ("text", 235, "Text"), ("research", 315, "Research")]:
    rect(cx - 36, 138, 72, 56, "#FFF9F4", "#EADACF", radius=10, sw=1)
    icon(name, cx - 25, 143, 50, 46)
    text(cx, 212, label, size=16, anchor="middle", max_width=79)
icon("database", 80, 220, 40, 44)
icon("outputs", 245, 220, 40, 44)
lines(100, 286, ["Existing", "datasets"], size=24, gap=26, anchor="middle")
lines(265, 286, ["New", "outputs"], size=24, gap=26, anchor="middle")
path("M100 317 V319 Q100 325 112 325 H183", color=GRAY, marker=None, width=2)
path("M265 317 V319 Q265 325 253 325 H195 V332", color=GRAY, marker="gray", width=2)
rect(43, 337, 304, 140, "#FFFFFF", "#E2CEBF", 12)
text(195, 367, "Metrics and judges", size=24, weight=600, anchor="middle", max_width=285)
for x, name in [(79, "S1"), (137, "S2"), (195, "S3")]:
    text(x, 397, name, size=23, anchor="middle")
text(289, 397, "Sample", size=22, anchor="middle")
rect(50, 403, 290, 31, "#F0F0F0", radius=5)
rect(50, 439, 290, 31, "#DCEAF3", radius=5)
for y, values, priority in [(426, ["A>B", "A>B", "A>B"], "Less"), (462, ["A>B", "B>A", "A>B"], "More")]:
    for x, value in zip([79, 137, 195], values):
        text(x, y, value, size=20, anchor="middle")
    text(289, y, priority, size=23, anchor="middle", weight=600)
for x in (108, 166, 225):
    path(f"M{x} 405 V469", "#D8D9D9", 1, None)
text(195, 508, "+ random sample", size=24, anchor="middle", fill=GRAY)
path("M195 517 V537", color=GRAY, marker="gray", width=2)
icon("human", 57, 550, 79, 86)
lines(151, 568, ["Reuse labels", "or ask humans", "for new ones"], size=24, gap=31, max_width=190)
rect(53, 652, 285, 53, "#F7E4D6", "#DCAF8D", radius=13)
text(195, 687, "Human feedback", size=27, weight=600, anchor="middle", max_width=266)
text(195, 741, "Signals can share errors", size=22, anchor="middle", fill=GRAY)

# B: zoom in on one failed trial, rather than giving three example edits equal
# visual weight. The retained record, not the program chain, is the focal object.
rect(416, 140, 1038, 420, "#E7F2EF", "#B7D7D0", radius=23)
icon("direction", 434, 155, 67, 67)
text(518, 174, "One direction, successive revisions", size=27, weight=600, fill=DARK, max_width=690)
text(518, 214, "Example: make layout errors count in the final score", size=27, max_width=885)
text(1430, 173, "Base model fixed", size=22, anchor="end", fill=GRAY)
path("M442 239 H1428", "#C1DAD4", 1.5, None)

def program(x, title, edit):
    """One complete candidate plus an example edit, not an architecture diagram.

    The note describes this revision only. It implies neither a fixed component
    taxonomy nor unconditional inheritance from the previous candidate.
    """
    text(x + 119, 286, title, size=25, weight=600, anchor="middle", max_width=254)
    # Retain the complete-program shell and pictorial code-and-pencil asset.
    rect(x + 5, 317, 238, 127, "#C9DBD6", radius=10)
    rect(x, 310, 238, 127, "#FFFFFF", "#90ACA6", radius=10)
    rect(x + 1, 311, 236, 27, "#E5EBED", radius=9)
    text(x + 14, 331, "Complete program", size=18, fill=NAVY)
    icon("program", x + 11, 351, 56, 68)
    rect(x + 76, 346, 151, 78, "#E5F1EC", "#B7D5CD", radius=8, sw=1)
    text(x + 86, 365, "Example edit", size=16, fill=GRAY, max_width=132)
    lines(x + 86, 390, edit, size=18, gap=24, fill=DARK, max_width=132)


program(446, "Candidate", ["Add a layout", "error detector"])
program(1190, "Next revision", ["Pass findings", "into scoring"])

# A stacked, open diagnostic record gives observations and interpretation
# different visual roles. Earlier pages persist; the front page is this trial.
rect(759, 274, 370, 275, "#C7DDD5", "#ACCCC1", radius=13, sw=1)
rect(753, 268, 370, 275, "#E3EEE8", "#B9D2C7", radius=13, sw=1)
rect(747, 262, 370, 275, "#FFFEFA", "#87B6A4", radius=13, sw=1.8)
icon("diagnostics", 762, 276, 44, 47)
text(821, 300, "Retain diagnostics", size=25, weight=600, fill=DARK, max_width=282)
path("M766 329 H1097", "#D4E0D7", 1.3, None)
text(769, 353, "Observed in execution", size=18, weight=600, fill=NAVY, max_width=323)
lines(769, 384, ["Layout errors detected.", "Final scores unchanged."], size=23, gap=29, max_width=327)
path("M766 429 H1097", "#D4E0D7", 1.3, None)
text(769, 454, "Agent’s next question", size=18, weight=600, fill=DARK, max_width=323)
lines(769, 485, ["Do these findings reach", "the scoring step?"], size=23, gap=29, max_width=327)

# Horizontal flow carries diagnostic information, not unconditional code
# inheritance. A failed candidate's actual parent is chosen by the Method rule.
path("M688 373 H737", width=3.3)
path("M1132 373 H1180", width=3.3)
rect(450, 460, 230, 39, "#E5EBE9", "#CBD7D2", radius=9, sw=1)
text(565, 486, "No agreement gain", size=21, anchor="middle", fill=GRAY, max_width=218)
text(565, 529, "Not accepted", size=21, weight=600, anchor="middle", fill=NAVY, max_width=235)
path("M1309 442 V455", width=2.5)
text(1309, 481, "Run and inspect again", size=20, anchor="middle", fill=DARK, max_width=238)
# Later execution observations return to the same diagnostic record. Keep this
# local return path away from candidate checking and the direction-ending exit.
path("M1309 493 V511 Q1309 524 1296 524 H1157 Q1144 524 1144 511 V498 Q1144 485 1131 485", width=2.5)

# Candidate measurement links join one common checking procedure. They are
# dashed and never connect rejection to a direction-ending decision.
path("M446 407 H433 V588 H790", NAVY, 2.2, None, "7 6")
path("M1428 407 H1441 V588 H790", NAVY, 2.2, None, "7 6")
path("M790 588 V650", NAVY, 2.2, "navy", "7 6")
text(811, 620, "Test each candidate", size=21, fill=NAVY)
text(445, 620, "Keep diagnostics after rollback", size=19, fill=DARK, max_width=330)

# A group exit allows ending at any revision. It is not tied to C2 or failure.
path("M1410 560 V583", GRAY, 2.2, "gray")
icon("direction", 1385, 589, 48, 48)
text(1368, 620, "End direction → start another", size=20, anchor="end", fill=GRAY)

# Independent candidate selection uses the lower band rather than another
# vertical panel. The caption carries detailed guards and parent-choice rules.
path("M418 640 H1450", "#D5E2DF", 1.3, None)
lines(445, 684, ["Candidate", "acceptance"], size=27, gap=32, weight=600)
icon("checking", 752, 659, 75, 65)
text(790, 746, "Same checking set", size=22, anchor="middle")
path("M845 686 H892", NAVY, 2.5, "navy")
lines(914, 667, ["Better agreement + passed checks", "→ update best program"], size=19, gap=27, max_width=360)
rect(903, 707, 365, 30, "#DDEBE8", radius=7)
text(915, 729, "No gain → keep best program", size=20, weight=600, fill=NAVY, max_width=342)
path("M1269 686 H1294", NAVY, 2.5, "navy")
icon("best", 1305, 653, 91, 77)
text(1350, 749, "Best program", size=24, weight=600, anchor="middle", max_width=222)

# Only B leaves after search. No direction/candidate directly feeds an app.
path("M1407 686 H1514", NAVY, 2.8, "navy")
rect(1473, 668, 29, 36, "white", radius=6)
icon("lock", 1474, 670, 27, 31)

# Feedback enters the direction header, via an unobstructed outer gutter.
path("M338 679 H380 V192 H431", DARK, 3, "green")

# C: same pictorial applications, with tighter vertical spacing and less text.
for y, height, name, title in [
    (123, 184, "selection", ["Output selection"]),
    (325, 194, "refinement", ["Critic-guided", "refinement"]),
    (537, 204, "training", ["Reward-guided", "training"]),
]:
    fill = {"selection": "#E7EFF8", "refinement": "#EFF2F1", "training": "#F7E7E2"}[name]
    rect(1521, y, 278, height, fill, radius=17)
    lines(1660, y + 35, title, size=26, gap=30, weight=600, anchor="middle", max_width=258)
    art_y = y + (64 if name == "selection" else 86)
    icon(name, 1544, art_y, 232, 87)
    if name == "selection":
        text(1660, y + 170, "Rank and select", size=22, anchor="middle", fill=GRAY)
    if name == "training":
        text(1660, y + 189, "Planned", size=22, anchor="middle", fill=GRAY)

# Short disclosure stays visible while all detailed caveats live in the spec.
text(20, 789, "Constructed example, not an observed trajectory", size=21, fill=GRAY)
text(1477, 789, "Best program fixed after search", size=21, fill=NAVY, anchor="end")
for i, label in enumerate(labels):
    a = label["ink_box"]
    for previous in labels[:i]:
        b = previous["ink_box"]
        overlap = min(a[2], b[2]) > max(a[0], b[0]) and min(a[3], b[3]) > max(a[1], b[1])
        assert not overlap, ("text overlap", previous["text"], label["text"])
parts.append("</g></svg>")
OUT.mkdir(parents=True, exist_ok=True)
svg = "\n".join(parts)
(OUT / "overview.svg").write_text(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / "overview.png"), output_width=W, output_height=H)
manifest = {
    "status": "canonical manuscript figure" if args.publish else "stable layout preview", "canvas": [W, H],
    "layout": "wide persistent direction; one unaccepted trial feeds a prominent retained diagnostic record and a targeted next revision; independent lower acceptance band",
    "supersedes": "tall 1680 x 1060 review proof, overwritten at the author's request",
    "aspect_ratio": W / H,
    "source_image": str(SOURCE.relative_to(ROOT)),
    "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "generator": "scripts/render_overview_layout_review.py",
    "generation_provenance": ".paper/overview-panel-c-action-cycle-20260921.md",
    "constructed_illustration": True, "empirical_evidence": False,
    "new_generation": False, "print_width_in": PRINT_WIDTH_IN,
    "font_size_pt": [min(t["size"] for t in labels) * PRINT_WIDTH_IN * 72 / W,
                     max(t["size"] for t in labels) * PRINT_WIDTH_IN * 72 / W],
    "embedded_images": image_placements,
    "method_palette": [GREEN, DARK], "crop_reference_canvas": [1300, 770],
    "crop_boxes": CROPS, "text": labels,
    "task_icons": {"single_object": True, "centers": [75, 155, 235, 315],
                   "image_box": [50, 46], "top": 143, "label_baseline": 212},
    "revision_example": {
        "evidence_status": "constructed illustration, not observed results",
        "direction": "Make layout errors count in the final score",
        "example_edits": ["Add a layout error detector", "Pass findings into scoring"],
        "terminology_mapping": {"Best program": "B", "diagnostic history": "z"},
        "highlight_semantics": "the same unaccepted candidate contributes observed outcomes and a separate checking result; retained diagnostics survive program fallback and motivate the next revision",
        "diagnostic_links": "observed outcomes and agent-proposed next tests inform a revision of W; subsequent observations return to the same record; the parent policy still applies",
        "acceptance": "the first candidate illustrates non-acceptance with retained diagnostics; no acceptance or gain is asserted for the next revision",
        "branching": "group-level exit after the agent ends the direction, not after rejection or a prescribed number of revisions",
    },
    "verification": {"label_count": len(labels), "text_ink_overlap": False, "panel_and_local_width_checks": True},
    "limitations": ["Labels are 3.4–7.2 pt at the approved 5.4-inch width; small-label readability remains limited", "Some pictograms fall below the repository's 600-PPI raster-line-art target; labels and connectors remain vector", "The next revision illustrates allowed continuation, not mandatory depth or measured gain", "Working-parent policy and access guards remain in Method/caption", "The agent's question is not a verified causal diagnosis; example edits are not an evaluator taxonomy"],
}
if args.publish:
    (PAPER / "overview.svg").write_text(svg)
    (PAPER / "overview.png").write_bytes((OUT / "overview.png").read_bytes())
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=str(PAPER / "overview.pdf"),
                    output_width=PRINT_WIDTH_IN * 96,
                    output_height=PRINT_WIDTH_IN * 96 * H / W)
    manifest.update({
        "paper_layout": "figures/overview.tex", "paper_graphic": "figures/overview.pdf",
        "files": {f"figures/overview.{ext}": hashlib.sha256((PAPER / f"overview.{ext}").read_bytes()).hexdigest()
                  for ext in ("svg", "pdf", "png")},
    })
    (PAPER / "overview.manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(OUT / "overview.png")
