#!/usr/bin/env python3
"""Offline paper-memory consistency checks (JSON-compatible YAML, standard library).

The upstream paper-memory skill's referenced validator was absent in this
environment. This checks its mandatory evidence contract plus repository links.
The unmodified upstream JSON Schema is vendored for optional full validation.
No structural check can establish empirical support or semantic correctness.
"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(message):
    errors.append(message)


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def local_file(relative):
    if not isinstance(relative, str) or Path(relative).is_absolute():
        raise ValueError(f"Expected a repository-relative path: {relative!r}")
    path = (ROOT / relative).resolve()
    path.relative_to(ROOT)
    if not path.is_file():
        raise ValueError(f"Missing memory artifact: {relative}")
    return path


def read(relative):
    return local_file(relative).read_text(encoding="utf-8")


def caption_for(text, label, kind="figure"):
    environments = "figure" if kind == "figure" else "table|longtable"
    pattern = r"\\begin\{(" + environments + r")\}[\s\S]*?\\end\{\1\}"
    for match in re.finditer(pattern, text):
        block = match.group(0)
        if "\\label{" + label + "}" not in block:
            continue
        start = block.find(r"\caption{")
        if start < 0:
            raise ValueError(f"Missing caption for {label}")
        start += len(r"\caption{")
        depth = 1
        for end in range(start, len(block)):
            escaped = end > 0 and block[end - 1] == "\\"
            if not escaped:
                if block[end] == "{":
                    depth += 1
                elif block[end] == "}":
                    depth -= 1
            if depth == 0:
                return normalize(block[start:end])
    raise ValueError(f"Missing {kind} environment for {label}")


try:
    claim_memory = json.loads(read(".paper/claims.yml"))
    figure_memory = json.loads(read(".paper/figures.yml"))
    history = json.loads(read(".paper/revision_history.yml"))
    claims = claim_memory["claims"]
    figures = figure_memory["figures"]
    tables = figure_memory["tables"]
    claim_ids = [c["id"] for c in claims]
    if claim_ids != [f"C{i}" for i in range(1, len(claims) + 1)]:
        fail("Claim IDs must be contiguous and unique.")
    figure_ids = [f["id"] for f in figures]
    if figure_ids != [f"Fig{i}" for i in range(1, len(figures) + 1)]:
        fail("Figure IDs must follow manuscript order.")
    table_ids = [t["id"] for t in tables]
    if table_ids != [f"Tab{i}" for i in range(1, len(tables) + 1)]:
        fail("Table IDs must follow manuscript order.")
    display_ids = set(figure_ids + table_ids)

    for claim in claims:
        cid = claim["id"]
        status = claim.get("status")
        if status not in {"draft", "supported", "rejected", "gap"}:
            fail(f"{cid}: unknown claim status {status!r}")
        if not isinstance(claim.get("text"), str) or not claim["text"].strip():
            fail(f"{cid}: empty claim text")
        evidence = claim.get("evidence_artifacts", [])
        if not evidence and status not in {"gap", "rejected"}:
            fail(f"{cid}: no evidence requires gap status")
        if status == "gap" and not claim.get("gap_reason", "").strip():
            fail(f"{cid}: gap status requires a reason")
        for artifact in evidence:
            local_file(artifact)
        if status != "rejected" and normalize(claim["text"]) not in normalize(read(claim["source"])):
            fail(f"{cid}: claim no longer matches its manuscript source")
        unknown = set(claim.get("figure_or_table", [])) - display_ids
        if unknown:
            fail(f"{cid}: unknown figures or tables {sorted(unknown)}")

    all_section_text = "\n".join(p.read_text(encoding="utf-8") for p in sorted((ROOT / "sections").glob("*.tex")))
    actual_figure_labels = set()
    for match in re.finditer(r"\\begin\{figure\}[\s\S]*?\\end\{figure\}", all_section_text):
        actual_figure_labels.update(re.findall(r"\\label\{([^}]+)\}", match.group(0)))
    if actual_figure_labels != {f["label"] for f in figures}:
        fail("Figure inventory does not exactly cover the manuscript figures.")
    actual_table_labels = set(re.findall(r"\\label\{(tab:[^}]+)\}", all_section_text))
    if actual_table_labels != {t["label"] for t in tables}:
        fail("Table inventory does not exactly cover the manuscript tables.")
    referenced_labels = set(re.findall(r"\\ref\{([^}]+)\}", all_section_text))

    for figure in figures:
        fid = figure["id"]
        local_file(figure["file"])
        text = read(figure["caption_source"])
        if caption_for(text, figure["label"]) != normalize(figure["caption_in_manuscript"]):
            fail(f"{fid}: caption memory is stale")
        expected_input = "\\input{" + str(Path(figure["file"]).with_suffix("")) + "}"
        if expected_input not in text:
            fail(f"{fid}: recorded source is not referenced by its caption file")
        for asset in figure.get("raster_assets", []):
            local_file(asset)

    for table in tables:
        if caption_for(read(table["file"]), table["label"], "table") != normalize(table["caption_in_manuscript"]):
            fail(f"{table['id']}: caption memory is stale")

    for display in figures + tables:
        did = display["id"]
        local_file(display["file"])
        if display["label"] not in referenced_labels:
            fail(f"{did}: missing manuscript callout")
        mapped = set(display["supports_claims"])
        expected = {c["id"] for c in claims if did in c.get("figure_or_table", [])}
        if mapped != expected:
            fail(f"{did}: claim links are not reciprocal")
        if mapped - set(claim_ids):
            fail(f"{did}: unknown claim link")

    revisions = history["revisions"]
    if [r["round"] for r in revisions] != list(range(1, len(revisions) + 1)):
        fail("Revision rounds must be consecutive.")
    for revision in revisions:
        for field in ["date", "trigger", "summary"]:
            if not revision.get(field):
                fail(f"Revision {revision['round']}: missing {field}")
        if set(revision.get("changed_claims", [])) - set(claim_ids):
            fail("Revision history references an unknown claim.")
        # Figure numbers are revision-local: do not rewrite old history when
        # the author changes the active display inventory.
        historical_scope = next((scope for scope in history.get("figure_id_scopes", [])
                                 if revision["round"] <= scope["through_round"]), None)
        snapshot = revision.get("figure_inventory_at_revision")
        if snapshot:
            valid_figure_ids = {entry["id"] for entry in snapshot}
        elif historical_scope:
            local_file(historical_scope["snapshot"])
            valid_figure_ids = set(historical_scope["ids"])
        else:
            valid_figure_ids = set(figure_ids)
        if set(revision.get("changed_figures", [])) - valid_figure_ids:
            fail("Revision history references an unknown figure.")

    domains = set(re.findall(r"\bTD-(?:SV|IG|TG|AR)\d+\b", read("sections/appendix.tex")))
    expected_domains = {f"TD-{family}{i}" for family, n in [("SV", 6), ("IG", 6), ("TG", 5), ("AR", 5)] for i in range(1, n + 1)}
    if domains != expected_domains:
        fail(f"Domain panorama mismatch: missing={sorted(expected_domains - domains)}, extra={sorted(domains - expected_domains)}")
    experimental_parts = re.findall(r"\\subsection\{([^}]+)\}", read("sections/experiments.tex"))
    if experimental_parts != ["Core results", "Ablation studies", "Analysis and studies"]:
        fail("Experimental design must retain the plan's three principal parts.")

except (OSError, ValueError, KeyError, TypeError) as exc:
    fail(str(exc))

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)

gaps = [c["id"] for c in claims if c["status"] == "gap"]
print(f"Memory: {len(claims)} claims; empirical gaps: {', '.join(gaps)}")
print(f"Coverage structure: {len(figures)} figures, {len(tables)} tables, {len(domains)} candidate domains")
print("Captions, evidence paths, claim links, and revision history are consistent.")
print("Specification support is not empirical evidence; author review remains pending.")
