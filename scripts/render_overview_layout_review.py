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
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont
from figure_fonts import FAMILY, SVG_FAMILY, font_path
from figure_connectors import STYLE as CONNECTOR_STYLE, arrow_marker, underbrace

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
    "visual": (50, 76, 182, 184),
    "image": (357, 87, 445, 174),
    "text": (700, 81, 794, 185),
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
    """Extract pictograms without erasing pale faces or document interiors.

    Close one-pixel outline gaps before filling enclosed foreground. Detached
    arrow/text fragments are excluded explicitly; this is not new illustration.
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
        threshold = 10 if name == "text" else 22
        if min(max(abs(c[k] - ref[k]) for k in range(3)) for ref in refs) > threshold:
            continue
        px[x, y] = (*c, 0)
        queue.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))
    original_mask = im.getchannel("A")
    # At source resolution, broken anti-aliased outlines allow the background
    # flood to enter white paper/skin. Close those gaps, then restore interiors.
    mask = original_mask.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.MinFilter(3))
    flood = Image.new("L", (w + 2, h + 2), 0)
    flood.paste(mask, (1, 1))
    ImageDraw.floodfill(flood, (0, 0), 128)
    holes = flood.crop((1, 1, w + 1, h + 1)).point(lambda v: 255 if v == 0 else 0)
    # Use closing only to identify interiors, not to grow the visible silhouette.
    mask = ImageChops.lighter(original_mask, holes)
    draw = ImageDraw.Draw(mask)
    if name == "human":
        draw.rectangle((w * .75, 0, w, h * .24), fill=0)
    if name == "lock":
        draw.rectangle((0, 0, w * .22, h), fill=0)
    if name == "training":
        # Keep only the robot and output card. Both the old arrow and raster
        # Reward label are rebuilt as vector elements at their original slots.
        draw.rectangle((w * 62 / 193, 0, w * 131 / 193, h), fill=0)
        draw.rounded_rectangle((w * 12 / 193, h * 24 / 76, w * 48 / 193, h * 58 / 76),
                               radius=round(w * 8 / 193), fill=255)
        draw.rectangle((w * 20 / 193, h * 63 / 76, w * 40 / 193, h * 72 / 76), fill=255)
        # The white neck and open-bottom torso are not enclosed by an outline;
        # flood filling therefore mistook them for the pale panel background.
        # Restore only points inside the original body, including the shoulders.
        for polygon in (
            [(21, 57), (42, 57), (40, 63), (42, 71), (20, 71), (22, 63)],
            [(12, 68), (15, 65), (19, 64), (18, 71), (12, 71)],
            [(44, 64), (49, 66), (51, 71), (45, 71)],
        ):
            draw.polygon([(round(x * w / 193), round(y * h / 76)) for x, y in polygon], fill=255)
    if name in {"selection", "training"}:
        # The pale sheet outlines are only 1–2 source pixels wide; color-keying
        # breaks them into fragments. Preserve the pictorial foreground, but
        # reconstruct these simple paper silhouettes and their marks in SVG.
        # Coordinates/overlap order remain the same, not a new icon language.
        if name == "selection":
            draw.rectangle((0, 0, w * 59 / 193, h), fill=0)
            draw.rectangle((w * 134 / 193, 0, w, h), fill=0)
        else:
            draw.rectangle((w * 131 / 193, 0, w, h), fill=0)
    if name == "visual":
        # Isolate the front window along its rounded outline. The old straight
        # trim removed the right border together with the rear-window fragment.
        outline = Image.new("L", (w, h), 0)
        ImageDraw.Draw(outline).rounded_rectangle(
            (w * 3 / 132, h * 3 / 108, w * 129 / 132, h * 104 / 108),
            radius=round(w * 6 / 132), fill=255)
        mask = ImageChops.darker(mask, outline)
    if name == "image":
        # Keep the mug silhouette, excluding the original floor/background.
        outline = Image.new("L", (w, h), 0)
        ImageDraw.Draw(outline).polygon([(round(x * w / 88), round(y * h / 87)) for x, y in
            [(24, 9), (30, 5), (43, 3), (65, 3), (77, 5), (84, 10),
             (84, 23), (81, 67), (80, 73), (75, 77), (64, 81), (48, 83),
             (37, 81), (28, 78), (25, 73), (23, 60), (17, 59), (9, 54),
             (4, 47), (1, 39), (2, 31), (5, 24), (12, 20), (23, 18)]], fill=255)
        mask = ImageChops.darker(mask, outline)
        # The handle opening is background, unlike enclosed document/skin areas.
        seed = (round(w * .18), round(h * .46))
        hole_color = px[seed[0], seed[1]][:3]
        queue, visited = deque([seed]), set()
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited or not (0 <= x < w * .30 and h * .20 < y < h * .83):
                continue
            visited.add((x, y))
            if max(abs(px[x, y][i] - hole_color[i]) for i in range(3)) <= 30:
                mask.putpixel((x, y), 0)
                queue.extend(((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))
    # Discard tiny detached remnants, without touching multi-object scenes.
    if name not in {"selection", "training"}:
        pixels = mask.load()
        remaining = {(x, y) for y in range(h) for x in range(w) if pixels[x, y]}
        components = []
        while remaining:
            seed = remaining.pop()
            component, queue = [seed], deque([seed])
            while queue:
                x, y = queue.popleft()
                for neighbor in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if neighbor in remaining:
                        remaining.remove(neighbor)
                        component.append(neighbor)
                        queue.append(neighbor)
            components.append(component)
        largest = max(map(len, components), default=0)
        for component in components:
            if len(component) < largest * .025:
                for x, y in component:
                    pixels[x, y] = 0
    # Unmatte only the silhouette edge. Interior paper/skin stays fully opaque;
    # edge colors no longer carry a pale halo from the old panel background.
    inner = mask.filter(ImageFilter.MinFilter(3))
    for y in range(h):
        for x in range(w):
            if mask.getpixel((x, y)) and not inner.getpixel((x, y)):
                color = px[x, y][:3]
                background = min(refs, key=lambda ref: max(abs(color[i] - ref[i]) for i in range(3)))
                alpha = min(1.0, max(abs(color[i] - background[i]) for i in range(3)) / 85)
                if alpha > 0:
                    rgb = tuple(round(max(0, min(255, (color[i] - (1 - alpha) * background[i]) / alpha))) for i in range(3))
                    px[x, y] = (*rgb, 255)
                mask.putpixel((x, y), round(alpha * 255))
    im.putalpha(mask)
    assert mask.getbbox(), ("Empty pictogram", name)
    if name in {"human", "training"}:
        probes = {"human": [(.40, .37), (.72, .55)], "training": [(30 / 193, 66 / 76)]}
        for x, y in probes[name]:
            assert mask.getpixel((round(w * x), round(h * y))) == 255, ("Erased pale interior", name)
    if name == "lock":
        assert mask.crop((0, 0, round(w * .20), h)).getbbox() is None, "Stray lock connector"
    if name == "training":
        assert mask.crop((round(w * 64 / 193), 0, round(w * 130 / 193), h)).getbbox() is None, "Raster connector/text remains"
    if name in {"visual", "image", "text", "research"}:
        # Fit visible artwork, not inconsistent source margins, to the same box.
        bounds = im.getchannel("A").getbbox()
        if bounds:
            # Transparent breathing room prevents SVG viewport edges from
            # touching anti-aliased contours, even when displayed very small.
            artwork = im.crop(bounds)
            im = Image.new("RGBA", (artwork.width + 6, artwork.height + 6))
            im.paste(artwork, (3, 3))
    buf = BytesIO()
    im.save(buf, format="PNG")
    sprite_metadata[name] = {"pixels": list(im.size), "sha256": hashlib.sha256(buf.getvalue()).hexdigest()}
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


# The refinement scene consists only of paper, a speech bubble and sparkles;
# trace it in place below to preserve its complete contours at any scale.
sprites = {k: cutout(v, k) for k, v in CROPS.items() if k != "refinement"}
parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}">
<title>IterEval — preference mining, evaluator evolution and downstream applications</title>
<desc>One unaccepted candidate supplies both a checking result and retained diagnostic observations. A question drawn from those observations motivates another revision within the same direction, without requiring the rejected program to be inherited. Candidate acceptance remains independent. Pictograms reuse AI-generated illustrations. This is a constructed example, not an observed trajectory.</desc>
<defs>
  {arrow_marker("green", DARK, 13, 10)}
  {arrow_marker("navy", NAVY, 12, 9)}
  {arrow_marker("gray", GRAY, 10, 8)}
  {arrow_marker("gray-small", GRAY, 7, 6)}
</defs><rect width="{W}" height="{H}" fill="white"/>
<g font-family="{SVG_FAMILY}" fill="{INK}">''']
labels = []


def rect(x, y, w, h, fill, stroke="none", radius=18, sw=1.5):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def text(x, y, value, size=28, weight=400, fill=INK, anchor="start", max_width=None):
    font = ImageFont.truetype(str(font_path("bold" if weight >= 600 else "regular")), size)
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
path(underbrace(100, 265, 317, 195, depth=10), color=GRAY, marker=None, width=2.3)
path("M195 327 V334", color=GRAY, marker="gray-small", width=2.1)
rect(43, 337, 304, 148, "#FFFFFF", "#E2CEBF", 12)
text(195, 367, "Metrics and judges", size=24, weight=600, anchor="middle", max_width=285)
for x, name in [(92, "Signal 1"), (206, "Signal 2")]:
    text(x, 397, name, size=22, anchor="middle", max_width=88)
text(289, 397, "Sample", size=22, anchor="middle")
rect(50, 403, 290, 31, "#F0F0F0", radius=5)
for x in (92, 206):
    text(x, 427, "A > B", size=26, anchor="middle", fill=GRAY)
text(149, 427, "=", size=27, anchor="middle", fill=GRAY)
text(289, 427, "Less", size=23, anchor="middle", fill=GRAY)
# Opposite rankings are visible without scanning a dense signal matrix.
# Blue/copper encode conflicting preferences, not correct/incorrect judgments.
rect(50, 442, 290, 37, BG_PEACH, radius=6)
rect(52, 442, 80, 37, "#E2EDF5", "#7C9EB8", radius=6, sw=1.6)
rect(166, 442, 80, 37, "#F6E2D7", "#BD846B", radius=6, sw=1.6)
text(92, 471, "A > B", size=28, weight=600, anchor="middle", fill=NAVY, max_width=78)
text(149, 472, "≠", size=32, weight=600, anchor="middle", fill="#8D553E")
text(206, 471, "B > A", size=28, weight=600, anchor="middle", fill="#8D553E", max_width=78)
text(289, 471, "More", size=24, weight=600, anchor="middle", fill="#8D553E")
text(195, 510, "Conflict → sample more", size=23, weight=600, anchor="middle", fill="#8D553E", max_width=320)
text(195, 538, "+ random sample", size=24, anchor="middle", fill=GRAY)
path("M195 546 V555", color=GRAY, marker="gray-small", width=2.1)
icon("human", 57, 550, 79, 86)
lines(151, 581, ["Reuse labels", "or ask humans", "for new ones"], size=24, gap=26, max_width=190)
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
path("M688 373 H737", width=2.8)
path("M1132 373 H1180", width=2.8)
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
path("M446 407 H441 Q433 407 433 415 V578 Q433 588 443 588 H790", NAVY, 2.1, None, "7 6")
path("M1428 407 H1433 Q1441 407 1441 415 V578 Q1441 588 1431 588 H790", NAVY, 2.1, None, "7 6")
path("M790 588 V650", NAVY, 2.1, "navy", "7 6")
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
path("M338 679 H370 Q380 679 380 669 V202 Q380 192 390 192 H431", DARK, 2.8, "green")

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
    # Match SVG preserveAspectRatio=xMidYMid meet for the 242×95 crop.
    scene_pixels = [242, 95] if name == "refinement" else sprite_metadata[name]["pixels"]
    scale = min(232 / scene_pixels[0], 87 / scene_pixels[1])
    art_width = scene_pixels[0] * scale
    art_left = 1544 + (232 - art_width) / 2
    def scene_line(x0, y0, x1, y1, color="#B5BAC5", width=1.5, arrow=False):
        path(f"M{art_left + x0 * art_width / 193:.2f} {art_y + y0 * 87 / 76:.2f} "
             f"L{art_left + x1 * art_width / 193:.2f} {art_y + y1 * 87 / 76:.2f}",
             color, width, "gray" if arrow else None)
    # Reconstruct the thin paper contours at their original positions, then
    # place the retained illustration in front. The folds and small stars are
    # complete paths, so no source crop can truncate them.
    unit_x, unit_y = art_width / 193, 87 / 76
    def paper(x, yy, ww, hh, fold=False, stroke="#ACACB6", fill="#EEEFF0"):
        xx, top = art_left + x * unit_x, art_y + yy * unit_y
        ww, hh = ww * unit_x, hh * unit_y
        if not fold:
            rect(xx, top, ww, hh, fill, stroke, radius=3.8, sw=1.6)
        else:
            f = 13 * unit_x
            parts.append(f'<path d="M{xx+4} {top} H{xx+ww-f} L{xx+ww} {top+f} V{top+hh-4} '
                         f'Q{xx+ww} {top+hh} {xx+ww-4} {top+hh} H{xx+4} '
                         f'Q{xx} {top+hh} {xx} {top+hh-4} V{top+4} Q{xx} {top} {xx+4} {top} Z" '
                         f'fill="{fill}" stroke="{stroke}" stroke-width="1.6" stroke-linejoin="round"/>')
            parts.append(f'<path d="M{xx+ww-f} {top} V{top+f-3} Q{xx+ww-f} {top+f} {xx+ww-f+3} {top+f} '
                         f'H{xx+ww} Z" fill="#D8DDE1" stroke="{stroke}" stroke-width="1.2" stroke-linejoin="round"/>')
    if name == "selection":
        for box in ((3, 23, 30, 44), (159, 23, 30, 44), (22, 17, 45, 55), (126, 17, 45, 55)):
            paper(*box)
        for x0, x1 in ((4, 16), (31, 55), (137, 162), (177, 186)):
            for sy in (30, 40, 50):
                scene_line(x0, sy, x1, sy)
    if name == "refinement":
        paper(4, 10, 57, 63)
        paper(126, 11, 56, 62, fold=True)
        for x0, x1 in ((16, 47), (138, 171)):
            for sy in (24, 35, 46, 57):
                scene_line(x0, sy, x1 - (7 if sy == 57 else 0) - (8 if sy == 24 and x0 == 138 else 0), sy)
        scene_line(70, 42, 116, 42, color=GRAY, width=2.2, arrow=True)
        parts.append(f'<g id="refinement-speech-bubble" transform="translate({art_left} {art_y}) scale({unit_x} {unit_y})">'
                     '<path d="M53 1 H97 Q102 1 102 6 V25 Q102 30 97 30 H73 L60 41 V30 H53 '
                     'Q49 30 49 25 V6 Q49 1 53 1 Z" fill="#BFE4E6" stroke="#334C55" '
                     'stroke-width="1.9" stroke-linejoin="round"/>'
                     '<path d="M59 11 H93 M59 19 H82" fill="none" stroke="#21A6B5" '
                     'stroke-width="2.7" stroke-linecap="round"/></g>')
        for cx, cy, r in ((183, 8, 7), (190, 23, 4)):
            xx, yy, rr = art_left + cx * unit_x, art_y + cy * unit_y, r * unit_x
            parts.append(f'<path d="M{xx} {yy-rr} Q{xx+rr*.22} {yy-rr*.22} {xx+rr} {yy} '
                         f'Q{xx+rr*.22} {yy+rr*.22} {xx} {yy+rr} '
                         f'Q{xx-rr*.22} {yy+rr*.22} {xx-rr} {yy} '
                         f'Q{xx-rr*.22} {yy-rr*.22} {xx} {yy-rr} Z" fill="#F2B44F"/>')
    if name == "training":
        paper(136, 12, 52, 59, stroke=NAVY, fill="#EFF1F6")
        for sy, x1 in ((29, 162), (40, 175), (51, 159)):
            scene_line(145, sy, x1, sy, color="#9EB8ED", width=1.8)
        scene_line(72, 40, 125, 40, color=GRAY, width=2.2, arrow=True)
    if name != "refinement":
        icon(name, 1544, art_y, 232, 87)
    if name == "selection":
        text(1660, y + 170, "Rank and select", size=22, anchor="middle", fill=GRAY)
    if name == "training":
        text(1660, art_y + 75, "Reward", size=20, anchor="middle", fill=INK)
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
    "icon_cleanup": {
        "method": "expanded source crops and transparent margins, conservative foreground masks, restored open robot torso; vector reconstruction of fragile panel-c paper/bubble contours",
        "preserved": "original pictorial objects and in-figure placement boxes; source resolution is not increased",
        "removed": ["detached arrow fragments", "mug floor remnants", "baked-in Reward label", "panel-c raster arrows and broken paper/bubble contours"],
        "restored": ["human face and paper", "full task-document fold and right border", "front-window outline", "robot neck and torso", "panel-c paper contours, folds, bubble tail and complete stars"],
        "vector_text": ["Reward"],
        "panel_c": "same scene positions and pictorial foregrounds; native vector paper contours, folds, speech bubble, stars, arrows and document strokes",
        "vector_scene": "refinement-speech-bubble",
        "review": "scripts/review_overview_icons.py produces a stable light/dark background contact sheet",
    },
    "font_family": FAMILY,
    "connector_style": CONNECTOR_STYLE,
    "connector_revision": "fixed-size filled arrowheads, rounded route corners and one continuous data-input brace; unchanged endpoint relationships and solid/dashed meanings",
    "font_size_pt": [min(t["size"] for t in labels) * PRINT_WIDTH_IN * 72 / W,
                     max(t["size"] for t in labels) * PRINT_WIDTH_IN * 72 / W],
    "embedded_images": image_placements,
    "method_palette": [GREEN, DARK], "crop_reference_canvas": [1300, 770],
    "crop_boxes": CROPS, "text": labels,
    "task_icons": {"single_object": True, "centers": [75, 155, 235, 315],
                   "image_box": [50, 46], "top": 143, "label_baseline": 212},
    "mining_example": {
        "signals_shown": 2,
        "agreement": ["A > B", "A > B"],
        "conflict": ["A > B", "B > A"],
        "encoding": "explicit equality/inequality and blue/copper ranking badges; copper denotes conflict, not incorrectness",
        "selection": "relative sampling priority; retain random sampling for shared errors",
        "scope": "constructed examples of agreement and disagreement, not a limit on the number of mining signals or a guarantee of information value",
    },
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
