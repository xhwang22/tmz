# Figure integration and print-layout audit — round 35

## Scope

Integrate the author-updated v6 teaser, repair the method overview, give
depth-first search enough space, and use lake green for method identity.
Preserve the author-edited Abstract/Introduction argument, source implementation,
numerical observations, and empirical status. The user also authorized pushing
the repaired paper repository to GitHub.

## Figure responsibilities

| Display | Responsibility | Boundary |
| --- | --- | --- |
| Main Fig1 | Concrete image-editing trade-off and breadth/depth distinction | Constructed example, not measured preferences, search behavior, or acceptance |
| Main Fig2 | Preference mining followed by depth-first evolution; independent decisions | Program specification, not an efficacy plot |
| Main Fig3 and Tab1 | Cross-domain C1 landscape and full comparator matrix | Existing simulation / unmeasured table; no new results |
| Appendix Figs4–13 | Runtime, budget placeholder, and detailed quantitative layouts | Existing evidence statuses retained |

All previous figures shift by one; table numbers are unchanged. Current claim
links and captions are synchronized, while historical revision IDs stay intact.
The task taxonomy belongs in Fig3a and Tab2, not a duplicate overview gallery.

## Visual and semantic checks

- Lake green `#62AAA5` with dark `#477D79` matches the main C1 figure. Error
  labels retain red and explicit text; meaning does not depend on color alone.
- Fig2 reserves its lower panel for successive complete candidates within a
  direction, unvisited alternatives, and an exit to the next direction.
- Candidate acceptance updates the best program only with gain and guards.
  Inheritance is checked separately and may use an unaccepted candidate.
  Failed inheritance falls back to the pre-update best program; diagnostics
  remain available for continuation. Direction switching is budget-conditional.
- Mining includes existing datasets and newly generated outputs, compatible
  preference reuse or missing-label collection, and a random anchor. Agreement
  lowers priority, rather than proving correctness or excluding a pair.
- Terminal validation follows freezing and does not trigger edits or reranking.
- The three-column author SVG is preserved, apart from method colors and node
  numeral contrast. All text, geometry, and nine embedded images are checked
  for preservation by the exporter.
- Its 2.5–4.7 pt labels at paper width motivated a separate native-size print
  layout. The print version retains the case and search distinction, shortens
  diagnostic wording, and places the task above the comparison. Labels are at
  least 7 pt. Three original photos are extracted unchanged at 399–403 DPI;
  vector export is not presented as increased image resolution.

## Provenance and verification

`figures/teaser.manifest.json` connects the author SVG, nine embedded images,
three extracted print photos, and the supplied historical raster design.
The historical image is retained as a source artifact, not regenerated here.
No model version or new API call is asserted for this integration.
`scripts/render_teaser.py` exports the reference; `scripts/render_figures.py`
builds the actual native-size paper layout for visual review. Ordinary paper
compilation only needs the committed TeX and photo assets.

Reviewed the standalone teaser, overview, runtime and budget diagrams and the
paper's title/figure pages. Compilation has no overfull boxes, missing labels,
or undefined citations. Memory, terminology, teaser provenance and resolution,
simulation, balanced landscape, and main C1 arithmetic checks pass.
All 30 tracked CSVs and quantitative artwork are unchanged. Only the legacy
landscape manifest's display number changes from Fig5 to Fig6.

## Outstanding manuscript issues

The resulting PDF has 37 pages, including 11 main pages. It exceeds the
9-page initial-submission limit; this integration does not change official
typography or margins to hide that. Structural checks also report 17 existing
unused bibliography entries. C27/C28 and the favorable author-edited result
sentences still lack confirmatory evidence. Simulation disclosures and the
submission guard remain in place. These issues are not resolved by figure
layout, and the repository is not ready for a results-bearing submission.
