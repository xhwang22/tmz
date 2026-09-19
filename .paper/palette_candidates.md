# Reference-based palette candidates

2026-09-17. Author-requested layout review; no final palette approval is implied.
Every plotted number is explicitly simulated, not a measurement or forecast.

## Complete five-color ensembles

The author requested using the five colors together. Each candidate draws
only from one supplied reference's labeled HEX values, not JPEG pixel estimates.

| Candidate | Static judge | Static tools / seed | Prompt optimization | Program search | ERA |
| --- | --- | --- | --- | --- | --- |
| A / reference_pastel | #74A9C5 | #C2E5CF | #EDDDAB | #F2B8AE | #DD7389 |
| B / reference_blue_orange | #72BCD5 | #AADCE0 | #FFE6B7 | #F7AA58 | #EF8A47 |
| C / reference_ocean | #4198AC | #BFDFD2 | #DBCB92 | #ECB66C | #ED8D5A |

A is the provisional manuscript palette. The five non-metric methods are a
fixed type-based subset, not the five highest-scoring methods. Two metric-only
references remain in the seven-method table and are neutral gray in cost plots.

The complete labeled source sequences are:

- Reference 1: #74A9C5 #C2E5CF #EDDDAB #F2B8AE #DD7389.
- Reference 2: #376795 #528FAD #72BCD5 #AADCE0 #FFE6B7 #FFD06F #F7AA58 #EF8A47 #E76254.
- Reference 3: #BFDFD2 #51999F #4198AC #7BC0CD #DBCB92 #ECB66C #EA9E58 #ED8D5A.

White paper and neutral ink (#25272B; numerical labels #202226) remain common.
Keep source base colors intact. Darker companions are restricted to fine strokes
and small diagram labels; do not darken pastel fills to support white labels.
Density fills use 88% source color over white. No new purple/copper base is added.

Mappings are local to the quantity and explicit in captions. The four domain
families use the first four colors in the expanded interval and C2 displays.
Four H levels likewise use four colors, not an invented fifth level. Reused/new
split-violin halves use left/right position and sparse hatching. The signed
component heatmap uses all five colors with cream at zero and fixed -6/+6 limits.
All five acquisition policies have equal-width source-colored lines, distinct
markers/dashes, and their own 10–90% bands. Rank plots use four ranks plus unscored;
outcome plots retain seed/tie/ERA shares and a separate abstention column.

## All-domain overview, bounded diagnostic detail

Main Figure 2 is a 22-row C1 atlas, grouped 6/6/5/5 in source-plan taxonomy order.
Panel (a) gives five method-wise OOD agreement columns with printed percentages
and tiny bars on an identical 0–100% scale. Color identifies method, not score.
Panel (b) aligns paired ERA-minus-seed OOD effects and 95% group-bootstrap
intervals. R/N tags preserve illustrative feedback provenance; they do not
claim actual label availability or make the settings permanent domain classes.
Do not reorder tasks by performance or omit null/negative contrasts.

C1 now has 22 synthetic cohorts (11 per setting), preserving the original eight
C1 cohorts' group records and summaries while adding fourteen. These are not
22 executed evaluations. C1 macro tables, selection and cost summaries use all
22. Appendix Figure 4 reports both ID and OOD paired intervals for all domains.

The unchanged eight diagnostic cohorts remain in the annotation, component,
and C2 detail figures. Their scope is stated, not confused with full coverage.
The former main mechanism figure is now appendix Figure 8; C2 is Figure 9.
No C3 outcomes or evaluator-tuning outcomes are simulated.

## Reproduce and inspect

Run make simulated, make palettes, make check, and make figures.

build/reference-palettes/ contains the three-way reference-comparison.png,
local original thumbnails in reference-sources.png, and overview-comparison.png.
Each candidate has main-figures.png and a two-page native-vector
main-figures.pdf (main atlas plus appendix diagnostic proof), isolated chart
PNGs/PDFs, the overview proof, and grayscale atlas/ablation previews.

review.json records source hashes, exact five-distinct-color mappings,
14 CSV/table byte-comparisons to the canonical fixtures, 110 atlas-value checks,
22 paired-effect checks, and 29 small-text/background contrast checks.
The three candidates have identical data, scales, typography, and geometry;
palette selection cannot change a numerical outcome. Contrast checks do not
establish universal color-vision accessibility; labels, positions and patterns
remain necessary.

Native chart width is 5.4 inches, with embedded TeX Gyre Heros and unchanged
official ICLR body fonts. Full-page review must check label padding and
caption placement, not just successful compilation. The author reference JPEGs
remain untracked inputs and are not manuscript assets or automatically pushed
files. No new image/model calls, training, empirical claims, or push occur in
this pass. Previous build directories are local archives.

## Later main-figure choice (2026-09-19)

The approved v20 landscape composite replaces the atlas in main Figure 2.
It uses pale family-color ramps for the baselines and a common lake-green ERA
accent, with Source Sans 3 / Source Serif 4. Its fixed-hash balanced synthetic
subset is separately documented in data/simulated/landscape/README.md.
The earlier palette candidates above remain historical comparisons; they do
not override this main-figure choice or alter the remaining appendix figures.
