# ICLR 2027 format

- Official template: `ICLR/Master-Template`, `iclr2027/`, commit
  `46ed6f4c6cef5b175dde23639e77d44c3463b230`.
- Initial main-text limit: 9 pages. Rebuttal/camera-ready: 10 pages.
- References and appendices are outside the main-text limit.
- Anonymous review mode; do not enable `\iclrfinalcopy` for this draft.
- US Letter; official font sizes, margins and text area unchanged.
- Natbib author–year citations; supplied `.bst`; single-paragraph abstract.
- Figure captions below; table captions above; vector artwork for diagrams,
  quantitative marks, and text. Eight chart PDFs have native 5.4-inch canvases;
  figure typography is scoped and does not replace the official Times body.
  Fonts must be embedded, with no Type 3 fallbacks. Audit photos at 300 DPI
  and raster line art at 600 DPI; text and diagram linework remain vector.
  These are repository quality thresholds, not an additional official ICLR rule.
  Figure 1 directly prints the approved three-column SVG export at 5.4 inches,
  preserving all nine photographic insets (at least 300 DPI). Its vector labels
  are approximately 2.5–4.7 points, an acknowledged readability limitation;
  the author rejected the separate print reflow. Figure 2 retains the original
  overview photograph and pictograms. Unused generated images remain archived.
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
