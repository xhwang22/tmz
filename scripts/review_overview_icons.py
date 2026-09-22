"""Inspect the overview's embedded icons on pale and dark backgrounds."""
import base64
import json
from io import BytesIO
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont
from figure_fonts import font_path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "build/overview-layout-current"
svg = ET.parse(OUT / "overview.svg").getroot()
elements = svg.findall(".//{http://www.w3.org/2000/svg}image")
font = ImageFont.truetype(str(font_path()), 22)
sheet = Image.new("RGB", (1200, 5 * 270), "white")
draw = ImageDraw.Draw(sheet)
seen = set()
index = 0
for element in elements:
    href = element.get("{http://www.w3.org/1999/xlink}href")
    if href in seen:
        continue
    seen.add(href)
    icon = Image.open(BytesIO(base64.b64decode(href.split(",", 1)[1]))).convert("RGBA")
    x, y = (index % 4) * 300, (index // 4) * 270
    draw.rectangle((x, y + 35, x + 149, y + 265), fill="#F1F7F5")
    draw.rectangle((x + 150, y + 35, x + 298, y + 265), fill="#354553")
    draw.text((x + 8, y + 4), f"{index + 1}: {icon.width} × {icon.height}", fill="#25272B", font=font)
    icon.thumbnail((140, 215), Image.Resampling.LANCZOS)
    for dx in (0, 150):
        sheet.paste(icon, (x + dx + (150 - icon.width) // 2, y + 45 + (210 - icon.height) // 2), icon)
    index += 1
sheet.crop((0, 0, 1200, ((index + 3) // 4) * 270)).save(OUT / "icons-review.png")
print(OUT / "icons-review.png")

manifest = json.loads((OUT / "manifest.json").read_text())
source = Image.open(ROOT / manifest["source_image"]).convert("RGB")
raw = Image.new("RGB", (1400, 1200), "white")
draw = ImageDraw.Draw(raw)
for i, (name, box) in enumerate(manifest["crop_boxes"].items()):
    crop = source.crop(tuple(round(v * (source.width / 1300 if j % 2 == 0 else source.height / 770)) for j, v in enumerate(box)))
    crop.thumbnail((340, 250), Image.Resampling.LANCZOS)
    # Enlarge only the diagnostic proof, never the underlying icon asset.
    ratio = min(340 / crop.width, 240 / crop.height)
    crop = crop.resize((round(crop.width * ratio), round(crop.height * ratio)))
    x, y = (i % 4) * 350, (i // 4) * 300
    draw.text((x + 6, y + 2), f"{name}: {box[:2]}", fill="#25272B", font=font)
    raw.paste(crop, (x + (350 - crop.width) // 2, y + 45))
raw.save(OUT / "icons-source-review.png")

# A single stable proof includes the pixels just outside the extraction boxes.
# It exposes source-crop truncation separately from alpha-mask erosion.
context = Image.new("RGB", (1600, 1000), "white")
draw = ImageDraw.Draw(context)
for i, name in enumerate(("visual", "text", "human", "research", "selection", "refinement", "training", "diagnostics")):
    box = manifest["crop_boxes"][name]
    x0, y0, x1, y1 = box
    region = (x0 - 6, y0 - 6, x1 + 10, y1 + 7)
    crop = source.crop(tuple(round(v * (source.width / 1300 if j % 2 == 0 else source.height / 770)) for j, v in enumerate(region)))
    ratio = min(390 / crop.width, 200 / crop.height)
    crop = crop.resize((round(crop.width * ratio), round(crop.height * ratio)))
    x, y = (i % 2) * 800, (i // 2) * 250
    draw.text((x + 6, y + 2), f"{name}: {box}", fill="#25272B", font=font)
    context.paste(crop, (x + 5, y + 40))
    # Grid on a duplicate, leaving the unmarked source visible beside it.
    context.paste(crop, (x + 405, y + 40))
    sx, sy = crop.width / (region[2] - region[0]), crop.height / (region[3] - region[1])
    for dx in range(0, x1 - x0 + 10, 20):
        xx = x + 405 + (dx + 6) * sx
        draw.line((xx, y + 40, xx, y + 40 + crop.height), fill="#CF7591", width=1)
        draw.text((xx + 1, y + 42), str(dx), font=font, fill="#A12543")
    for dy in range(0, y1 - y0 + 7, 20):
        yy = y + 40 + (dy + 6) * sy
        draw.line((x + 405, yy, x + 405 + crop.width, yy), fill="#CF7591", width=1)
        draw.text((x + 406, yy), str(dy), font=font, fill="#A12543")
context.save(OUT / "icons-source-context.png")
