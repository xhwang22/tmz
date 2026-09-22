# ICLR 2027 format

- Official template: `ICLR/Master-Template`, `iclr2027/`, commit
  `46ed6f4c6cef5b175dde23639e77d44c3463b230`.
- Initial main-text limit: 9 pages. Rebuttal/camera-ready: 10 pages.
- References and appendices are outside the main-text limit.
- Anonymous review mode; do not enable `\iclrfinalcopy` for this draft.
- US Letter; official font sizes, margins and text area unchanged.
- Natbib author–year citations; supplied `.bst`; single-paragraph abstract.
- Figure captions below; table captions above; vector artwork for diagrams,
  quantitative marks, and text. Chart PDFs have native 5.4-inch canvases;
  figure typography is scoped and does not replace the official Times body.
  Since round 48, active figure text uses TeX Gyre Pagella (Palatino-compatible),
  with Pazo/Palladio math in native TeX figures. Captions and tables retain
  their official fonts. The rebuilt PDF remains nine main pages and 33 total.
  Fonts must be embedded, with no Type 3 fallbacks. Audit photos at 300 DPI
  and raster line art at 600 DPI; text and diagram linework remain vector.
  These are repository quality thresholds, not an additional official ICLR rule.
  Figure 1 previews the author-requested shared case strip above equal-width
  method panels at 5.4 inches, retaining the original branch visualizations
  and nine photographic insets (335–741 PPI). Vector labels are approximately
  4.6–6.8 points after typography refinement, an acknowledged readability
  limitation. The compact 1840 × 880 figure
  remains unchanged in round 47; the shortened Related Work restores nine
  main-text pages (33 total), meeting the initial page limit. This does not
  resolve the figure-label limitations or empirical evidence gaps.
  Figure 2 prints the approved
  horizontal three-panel overview at 5.4 inches, with vector labels/connectors
  and reused AI-generated pictograms. Labels are approximately 3.4–7.2 points;
  some pictograms fall below the raster-line-art target. These are documented
  limitations, not a claim of print readiness. Unused images remain archived.
- Simulated quantitative fixtures are expressly marked, not empirical results.
  The author-requested layout draft is not a results-bearing submission;
  `scripts/check_simulated_results.py --submission` must reject it while these
  fixtures remain. Simulation disclosures cannot be removed without replacing
  the data and auditing the resulting claims.
- Required AI use statement, at most one page, outside the page limit.
- Recommended ethics and reproducibility statements, each at most one page,
  outside the page limit and before references.
- Author sign-off and policy-specific disclosures remain pending.

The PDF status notice clarifies that the template's review header is not a claim
of actual submission. Repository documentation is not anonymized; submission
artifacts require a separate anonymity review.
