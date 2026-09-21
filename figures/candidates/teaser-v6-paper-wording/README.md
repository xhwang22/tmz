# Teaser: manuscript-aligned wording, 2026-09-20

Text revision of `../teaser-v5-svg-flat-v3/teaser.svg`. The approved flat
surfaces, moderate outlines, sparse branches, node positions, card geometry,
and all nine raster insets are retained. The method panel now uses lake green
(`#62AAA5`, dark strokes `#477D79`); red remains an error status. No image generation.

## Files and reproduction

- `teaser.svg`: self-contained editable vector diagram with embedded insets.
- `teaser.png` / `teaser-2x.png`: previews.
- `teaser.pdf`: vector export with embedded TeX Gyre Heros fonts.
- `manifest.json`: source hashes, wording profile, and validation results.
- `wording-audit.md`: manuscript mapping and evidence boundaries.

From the repository root:

```bash
uv run --with cairosvg python scripts/render_teaser.py
python3 scripts/render_figures.py teaser overview
```

The current self-contained SVG is the source of truth; the older wording
profile records its history, not a reason to overwrite later SVG edits.
For live SVG editing, install TeX Gyre Heros to retain label metrics.
The manuscript directly prints this three-column layout through
`figures/teaser.tex` and `figures/teaser.pdf`, with all nine images intact.
The author rejected the separate `teaser-print.tex` reflow; do not reinstate it.
At 5.4 inches, small vector labels remain a readability limitation. Preserve
the approved geometry instead of treating that limitation as permission to redesign.
Paper previews are in `build/figure-review/teaser.{pdf,png}`; canonical exports
are `figures/teaser.{svg,pdf,png}`.

## Continuing figure-side work

Before subsequent wording revisions, read the latest paper terminology,
compressed context, relevant claim/figure memory, and the corresponding
manuscript paragraphs. Where available, check recent author decisions in the
Codex session named `iclr`. Its naming instruction at 2026-09-20 20:31 UTC is
the direct authority for this revision; the latest completed writing turn at
21:06 UTC corresponds to manuscript commit `bafe259`.

IterEval names the whole framework. The components are disagreement-based
preference mining and depth-first evaluator evolution, without IPM/ERA labels.
This teaser depicts the evolution component only. Do not add preference
mining machinery just to display the complete framework name.

Preserve the flat style unless the author requests a visual change. Wording
revisions should not overwrite canonical figures, manuscript sources, claims,
or shared figure memory without explicit integration approval. Keep candidate
acceptance, program inheritance, and direction continuation separate, and do
not upgrade illustrative outcomes into empirical support.
