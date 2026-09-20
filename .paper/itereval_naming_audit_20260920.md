# IterEval naming revision — 2026-09-20

## Naming and scope

- Title: Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks.
- Framework: IterEval — iterative evaluator self-improvement from human feedback.
- First introduction: “We present IterEval, a framework for self-evolving evaluators across open-ended tasks.”
- Components: disagreement-based preference mining; depth-first evaluator evolution. No component acronyms.

Applied to the title/PDF metadata, Abstract, Introduction, Method, Related Work, studies, analysis, discussion, conclusion, appendix, diagram labels, plot labels, and table labels. Framework-level system comparisons use IterEval; search-level explanations use depth-first evaluator evolution. The glossary and active-TeX checker record this distinction. The title uses natural wrapping to avoid an isolated final word, without changing template typography.

The revision preserves the mining score, random anchor, existing-preference reuse, missing-label annotation, search equations, candidate acceptance, program inheritance, and direction continuation. It changes no experiment or implementation behavior. Historical identifiers, citation keys, source paths, and raw fixture keys remain unchanged. Previous Related Work/bibliography edits and other agents' untracked figure work are not overwritten. No commit or push was performed.

## Numerical and figure preservation

All 30 tracked CSVs under `data/simulated/`, including both landscape directories, are byte-identical to HEAD `030c3eafc20b07cad57ec276721c56cc10b56e95`. The isolated chart regeneration also matched all 14 root CSVs before its PDFs/table were copied into the manuscript. Legacy `ERA` data keys map only at display time to `IterEval`; manifests now state this mapping.

The overview and budget diagram received label edits, not a redesign. Five generated chart PDFs, the numerical C1 table, and the C1 landscape use the updated labels. Unchanged charts were retained. File hashes were refreshed only after confirming numerical invariance; arithmetic and cohort checks were not relaxed.

The frozen appendix landscape had two text labels changed. Its SVG's font metadata differs from the original PDF, so reconverting the SVG would alter typography. `scripts/relabel_legacy_landscape.py` instead replaces those two PDF text spans using the existing Source Sans fonts and verifies unchanged vector drawing paths and all other text tokens. It also regenerates the PNG preview. The SVG has the corresponding text-only edits; existing group identifiers are preserved.

The pre-revision PDF is available from the commit above at `figures/simulated/landscape_outcomes.pdf`, SHA256 `9fc904f4454765bcd6a778c1488e80fd1ee8768898130119c18b95e83d08a84f`. A local copy is in `build/itereval-previous/`. The relabel script accepts that separate original via `--source`, requires PyMuPDF and the Source fonts in `build/figure-fonts/`, and never reads or writes numerical fixtures. Ordinary paper builds use the saved PDF and need neither this original copy nor PyMuPDF.

## Verification

- `make paper.pdf`: passes; 36 total pages, 10 main-text pages.
- `scripts/check_terminology.py`: passes for all 28 active TeX inputs.
- `scripts/check_memory.py`: passes; 49 claims, 12 figures, 15 tables; C27/C28 remain gaps.
- `scripts/check_simulated_results.py`: passes, including independent table arithmetic and new displayed-name checks.
- `scripts/check_landscape_results.py` and `scripts/check_c1_landscape.py`: pass; values, cohorts, intervals, fonts, and disclosures retained.
- Extracted full-PDF text contains no standalone ERA/IPM or retired full method name.
- No undefined citations or overfull boxes; `git diff --check` passes.
- Title page, overview, main landscape/table page, and relabeled legacy landscape inspected visually. Figure 2 and Table 1 remain in the main text, on page 9.

`scripts/check_paper.py` still reports 10 main pages against the initial-submission limit of 9, plus 17 unused entries among 52 bibliography records. There are 35 cited references. These pre-existing issues are not hidden by deleting bibliography records or reducing official typography; `make check` therefore does not fully pass.

## Evidence boundary

This is a naming revision, not an empirical validation. The latest author-edited Abstract/Introduction assert gains in preference mining, sustained improvement, alignment, and downstream use. These claims remain unverified; C27/C28 stay `gap`. Their wording was preserved except for names, and stale memory entries were synchronized without upgrading evidence status. Title-page, figure, data, and conclusion simulation disclosures remain. No models, annotation, experiments, or training were run.
