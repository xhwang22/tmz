#!/usr/bin/env python3
"""Offline structural checks for the manuscript; not an empirical-claim audit."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
visited = set()


def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def read_tex(relative, ancestors=()):
    path = (ROOT / relative).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        raise ValueError(f"Input escapes repository: {relative}") from None
    if path in ancestors:
        raise ValueError(f"Cyclic TeX input: {relative}")
    visited.add(path)
    text = uncomment(path.read_text(encoding="utf-8"))

    def expand(match):
        name = match.group(1)
        if not Path(name).suffix:
            name += ".tex"
        return read_tex(name, (*ancestors, path))

    return re.sub(r"\\input\{([^}]+)\}", expand, text)


try:
    manuscript = read_tex("main.tex")
except (ValueError, OSError) as exc:
    sys.exit(str(exc))

bib = (ROOT / "references.bib").read_text(encoding="utf-8")
entries = re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,", bib)
counts = Counter(entries)
keys = set(entries)
duplicates = sorted(key for key, n in counts.items() if n > 1)
if duplicates:
    errors.append(f"Duplicate bibliography keys: {duplicates}")

cited = set()
for group in re.findall(
    r"\\cite(?:t|p|alp|alt|author|year|yearpar)?\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}",
    manuscript,
):
    cited.update(key.strip() for key in group.split(","))
if cited - keys:
    errors.append(f"Undefined citations: {sorted(cited - keys)}")
if keys - cited:
    errors.append(f"Unused references: {sorted(keys - cited)}")

sources = json.loads((ROOT / ".paper/reference_sources.json").read_text())
source_keys = {item["key"] for item in sources["references"]}
if source_keys != keys:
    errors.append("Reference provenance keys do not match the bibliography.")

labels = re.findall(r"\\label\{([^}]+)\}", manuscript)
duplicate_labels = [key for key, n in Counter(labels).items() if n > 1]
if duplicate_labels:
    errors.append(f"Duplicate labels: {duplicate_labels}")
refs = set(re.findall(r"\\(?:ref|eqref|pageref)\{([^}]+)\}", manuscript))
if refs - set(labels):
    errors.append(f"Undefined cross-references: {sorted(refs - set(labels))}")
if r"\iclrfinalcopy" in manuscript:
    errors.append("Anonymous draft unexpectedly enables final-copy mode.")
if re.search(r"\bP2E\b|\\PtwoE\b", manuscript):
    errors.append("The retired project name remains in an active manuscript input.")
if re.search(r"/(?:home|mnt)/|gh[pousr]_[A-Za-z0-9_]{20,}", manuscript):
    errors.append("Potential private path or credential in manuscript.")

graphic_uses = re.findall(
    r"\\includegraphics(?:\[([^\]]*)\])?\{([^}]+)\}", manuscript
)
graphics = {relative for _, relative in graphic_uses}
print_widths = {}
units_per_inch = {"in": 1, "cm": 2.54, "mm": 25.4, "pt": 72.27, "bp": 72}
for options, relative in graphic_uses:
    # Figures use explicit native widths, without outer resizebox/scalebox.
    match = re.search(r"(?:^|,)\s*width\s*=\s*([0-9.]+)\s*(in|cm|mm|pt|bp)(?:,|$)", options)
    if not match:
        errors.append(f"Graphic needs an explicit physical print width: {relative}")
        continue
    print_widths.setdefault(relative, []).append(
        float(match.group(1)) / units_per_inch[match.group(2)]
    )
assets = json.loads((ROOT / ".paper/figure_assets.json").read_text())
recorded_graphics = set()
for asset in assets["generated_images"]:
    relative = asset["path"]
    path = (ROOT / relative).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        errors.append(f"Figure asset escapes repository: {relative}")
        continue
    recorded_graphics.add(relative)
    if not path.is_file():
        errors.append(f"Missing generated figure: {relative}")
        continue
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != asset["sha256"]:
        errors.append(f"Figure does not match recorded SHA-256: {relative}")
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        errors.append(f"Expected PNG figure: {relative}")
        continue
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (asset["width"], asset["height"]):
        errors.append(f"Figure dimensions do not match provenance: {relative}")
    declared_cm = asset.get("max_print_width_cm")
    if not isinstance(declared_cm, (int, float)) or declared_cm <= 0:
        errors.append(f"Missing positive max_print_width_cm: {relative}")
    else:
        declared_in = declared_cm / 2.54
        if width / declared_in < 600:
            errors.append(f"Figure below 600 DPI at declared maximum print width: {relative}")
        for printed_in in print_widths.get(relative, []):
            if printed_in > declared_in + 1e-6:
                errors.append(f"TeX width exceeds the recorded print-width budget: {relative}")
            if printed_in <= 0 or width / printed_in < 600:
                errors.append(f"Figure below 600 DPI at its actual TeX width: {relative}")
    for prompt in asset["prompts"]:
        if not (ROOT / prompt).is_file():
            errors.append(f"Missing figure prompt: {prompt}")

# Vector charts have data/generator provenance, not image-model provenance.
# Keep the two validation paths separate; PDFs have no meaningful raster DPI.
manifest = json.loads((ROOT / "data/simulated/manifest.json").read_text())
if manifest.get("simulation_only") is not True or manifest.get("empirical_evidence") is not False:
    errors.append("Quantitative fixture provenance does not disclose simulation.")
for relative in sorted(graphics):
    if not relative.endswith(".pdf"):
        continue
    path = (ROOT / relative).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        errors.append(f"Vector graphic escapes repository: {relative}")
        continue
    recorded_graphics.add(relative)
    if not path.is_file():
        errors.append(f"Missing vector figure: {relative}")
        continue
    data = path.read_bytes()
    if not data.startswith(b"%PDF-"):
        errors.append(f"Expected vector PDF: {relative}")
    if hashlib.sha256(data).hexdigest() != manifest["files"].get(relative):
        errors.append(f"Vector figure does not match data manifest: {relative}")
    if any(abs(width - 5.4) > 1e-6 for width in print_widths.get(relative, [])):
        errors.append(f"Vector chart does not retain its 5.4-inch native width: {relative}")
if graphics != recorded_graphics:
    errors.append("Referenced graphics and figure provenance do not match.")
for asset in assets.get("archived_images", []):
    if asset["path"] in graphics:
        errors.append(f"Archived illustration is still referenced: {asset['path']}")
    path = (ROOT / asset["path"]).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        errors.append(f"Archived asset escapes repository: {asset['path']}")
        continue
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != asset["sha256"]:
        errors.append(f"Archived image missing or hash changed: {asset['path']}")
    for prompt in asset["prompts"]:
        if not (ROOT / prompt).is_file():
            errors.append(f"Missing archived prompt: {prompt}")

aux_path = ROOT / "build/main.aux"
if aux_path.exists():
    aux = aux_path.read_text()
    marker = re.search(
        r"\\newlabel\{first-post-main-page\}\{\{[^}]*\}\{(\d+)\}", aux
    )
    if not marker:
        errors.append("Cannot determine main-text page count.")
    else:
        main_pages = int(marker.group(1)) - 1
        print(f"Main text: {main_pages} pages (ICLR initial limit: 9)")
        if main_pages > 9:
            errors.append("Main text exceeds the initial-submission page limit.")
    log = (ROOT / "build/main.log").read_text(errors="replace")
    for pattern in [
        r"Overfull \\[hv]box",
        r"There were undefined references",
        r"There were undefined citations",
        r"Rerun to get cross-references right",
        r"multiply defined",
    ]:
        if re.search(pattern, log):
            errors.append(f"Unresolved build issue matching: {pattern}")
else:
    errors.append("Build missing; run make before checking the paper.")

print(f"TeX inputs: {len(visited)}; cited references: {len(cited)}; labels: {len(labels)}")
print(f"Graphics: {len(recorded_graphics)}; raster resolution and vector provenance checked")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print("Structural checks passed. Empirical results and author review remain pending.")
