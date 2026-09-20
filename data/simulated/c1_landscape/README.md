# Main-text C1 landscape: simulated layout fixture

This is not an experiment, an expected effect size, or evidence for ERA.
The script reads existing `../c1_groups.csv` records without changing them.
No new observations, C2/C3 results, or training outcomes are generated.
The historical `figures/simulated/landscape_outcomes.pdf` is preserved.

The design retains its 5.4 × 3.57-inch canvas, Source Sans 3 / Source Serif 4,
four-quarter task ring, upper-right scatter, and four family bar panels.
The new content follows plan §5.1.2 (C1 alignment and candidate selection):

- The ring is the 22-task taxonomy, not a measured dataset composition.
  Equal family quadrants are schematic; tasks divide their family equally.
- Bars use all OOD inputs with complete scores from all five displayed methods
  within each domain, rather than the historical 2,880-input balanced subset.
  All five means share that domain's same cohort. Whiskers are 95% percentile
  intervals from 2,000 paired original-input bootstrap draws within domain.
  They do not describe independent-search variation.
- The scatter connects static-tool seed and ERA family summaries.
  The x-axis is an equal-domain mean of the bar values.
  The y-axis is equal-domain Best-of-4 accuracy across all 160 requested inputs
  per domain, counting incomplete scoring as failed selection.
  Connections identify the same family; they are not trajectories or causal
  arrows. Family averages do not establish a per-task correlation.
- All 3,520 requested OOD inputs remain in `input-cohorts.csv`, including
  incomplete ones. Negative task and family contrasts remain unchanged.
- Table 1, not this five-method illustration, specifies the complete empirical
  comparison, including calibration and evaluator fine-tuning.

Reproduce with `python3 scripts/render_c1_landscape.py`.
It uses NumPy and Matplotlib, loading hash-pinned Adobe OFL fonts from the local
`build/figure-fonts/` cache or their official repository if absent.
Normal paper compilation uses committed PDFs and needs no font downloads.
Run `python3 scripts/check_c1_landscape.py` for an independent numerical,
geometry, provenance, font-embedding, and disclosure audit.
Every export row carries `SIMULATED`; the manifest hashes inputs and outputs.
The existing submission guard remains active.
