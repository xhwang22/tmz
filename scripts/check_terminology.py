#!/usr/bin/env python3
"""Check known terminology drift in the active manuscript (offline).

This intentionally does not rename bibliography entries, historical files, or
LaTeX identifiers. Context-sensitive distinctions still require human review.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INPUT = re.compile(r"\\(?:input|include)\{([^}]+)\}")
IDENTIFIER = re.compile(
    r"\\(?:label|(?:eq|auto|page|c|C)?ref|input|include|bibliography|"
    r"bibliographystyle|cite\w*|includegraphics)\*?"
    r"(?:\[[^\]]*\])*\{[^}]*\}"
)
RULES = (
    (r"\bacquisition\b", "Use IPM, data mining, or sampling for the defined operation."),
    (r"\bdisagreement-based (?:data|preference) mining\b", "The method is Informative Preference Mining (IPM)."),
    (r"\b(?:falsification|evidence|diagnostic)-guided\b", "ERA is depth-first evaluator evolution."),
    (r"\b(?:refutation|refuted|falsification)\b", "Describe diagnostic results without restoring the retired framing."),
    (r"\bworking[- ](?:state|version)\b", "Use working program or program inheritance."),
    (r"\b(?:candidate (?:promotion|adoption)|development promotion)\b", "Use candidate acceptance."),
    (r"\bdirection persistence\b", "Use direction continuation."),
    (r"\b(?:human evidence|(?:adaptation )?evidence table)\b", "Use human feedback or feedback table as appropriate."),
    (r"\bsupervision\b", "Use human feedback when referring to the paper's H0–H3 data."),
    (r"\bevaluator program\b", "Use evaluation program."),
    (r"\b(?:scorer calibration|evaluator weight fine-tuning)\b", "Use score calibration or evaluator fine-tuning."),
    (r"\bcandidate (?:group|pool|comparison)s?\b", "Use output group/pool/comparison for generated artifacts."),
)


def visible_source(source):
    """Ignore comments/identifiers, retaining line numbers and visible labels."""
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    return IDENTIFIER.sub(lambda m: "\n" * m.group().count("\n"), source)


def active_sources(path, seen):
    path = path.resolve()
    path.relative_to(ROOT)
    if path in seen:
        return
    seen.add(path)
    source = path.read_text(encoding="utf-8")
    yield path, source
    uncommented = re.sub(r"(?<!\\)%[^\n]*", "", source)
    for name in INPUT.findall(uncommented):
        child = ROOT / name
        if not child.suffix:
            child = child.with_suffix(".tex")
        yield from active_sources(child, seen)


def main():
    errors = []
    seen = set()
    for path, source in active_sources(ROOT / "main.tex", seen):
        text = visible_source(source)
        for pattern, advice in RULES:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: {match.group()!r}: {advice}")
    if errors:
        print("Terminology check failed:\n" + "\n".join(errors))
        return 1
    print(f"Terminology check passed: {len(seen)} active TeX files; legacy identifiers preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
