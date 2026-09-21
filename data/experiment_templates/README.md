# Empty empirical-record templates

These files contain headers only: no simulated data, results, executable configurations, or experiment authorization.

Complete and freeze the run manifest first. Export authorized raw records into a separate versioned result directory; keep these templates empty. Join outputs by hashes, inputs by original/source groups, and runs by method/configuration hashes. Derive summaries only from versioned raw records and analysis.

Use PENDING for unmeasured and NOT_APPLICABLE for inapplicable endpoints. Empty numeric values are missing, not zero.

- Human judgments: a / b / tie / abstain / insufficient. Overall and dimensional judgments are different records. Major regressions are relative to the declared starting output.
- Human rankings: ties follow the frozen policy; pair-only labels cannot supply a complete ranking.
- Artifact scores: retain failed calls and missing repeats. Repeats are not independent searches.
- Search events: observed diagnostics and agent interpretation have separate references. A direction ID does not verify semantic continuity.
- Costs: distinguish mining, search, terminal/final assessment, deployment, refinement, and training; include retries.
- Summaries: record metric, unit, comparator, cohort rule, intervals, requested/complete counts, domain set, search count, and source hashes.

Publish only permitted, appropriately anonymized artifacts. See [the fill plan](../../.paper/experiment_fill_plan.md).
