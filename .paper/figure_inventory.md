# Figure and table inventory

Authoritative captions and claim links are in `figures.yml`: 11 figures (two main, nine appendix) and 15 tables.
Two figures are conceptual, one is a blank budget-comparison placeholder, and eight are explicitly simulated quantitative displays.
No display reports measured performance.
The abstract remains author-edited; the current organization follows plan §5.

| ID / location | Source | Purpose / status |
| --- | --- | --- |
| Fig1 / main | figures/overview.tex | (a) four domain families; (b) existing-dataset mining and new preference collection; (c) ERA acceptance and continuation; (d) C1 alignment/selection, C2 refinement, planned C3; Conceptual specification with constructed examples; no measured results |
| Fig2 / main | figures/budget_tests.tex | (a) search under equal total model-and-tool cost at frozen prices; (b) acquisition under equal original-input annotation units; Unmeasured reporting placeholders; equal units alone do not establish equal human time |
| Fig3 / appendix | figures/evaluator.tex | (a) one artifact; (b) routed observations; (c) dimensional criteria; (d) synthesis; Conceptual specification with constructed examples; no measured results |
| Fig4 / appendix | figures/simulated_landscape.tex | (a) balanced input composition across 22 tasks; (b) assigned cost versus OOD agreement, 110 domain points and ten setting means; (c) four family bar panels in one row, five methods per task; Balanced synthetic OOD subset for layout, distinct from full-cohort appendix data; no empirical efficacy or label availability established |
| Fig5 / appendix | figures/simulated_alignment.tex | (a) ID paired effects; (b) OOD paired effects; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig6 / appendix | figures/simulated_acquisition.tex | (a) reused preferences; (b) new preferences; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig7 / appendix | figures/simulated_annotation.tex | (a) valid-pair agreement; (b) requested-rating abstention; (c) group consensus outcomes; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig8 / appendix | figures/simulated_selection.tex | (a) reused preferences; (b) new preferences; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig9 / appendix | figures/simulated_ablation.tex | (a) conditional component effects; (b) cumulative feedback detail; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig10 / appendix | figures/simulated_refinement.tex | (a) paired quality differences; (b) diverging preference shares and a separate abstention column; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig11 / appendix | figures/simulated_cost.tex | (a) paired-setting deployment costs; (b) paired-setting agreement; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |

| ID | Label | Source / status |
| --- | --- | --- |
| Tab1 | tab:main-alignment | sections/results.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab2 | tab:downstream-results | sections/results.tex; Unmeasured empirical C2/C3 status; dashes are not zeros |
| Tab3 | tab:domains | sections/appendix.tex; Research scope; not data readiness or completed evaluation |
| Tab4 | tab:human-provenance | sections/appendix.tex; Two-setting provenance and protocol specification |
| Tab5 | tab:readiness | sections/appendix.tex; Readiness audit requirements, not measured coverage |
| Tab6 | tab:access | sections/appendix.tex; Data access and independence contract |
| Tab7 | tab:adaptation | sections/appendix.tex; Planned calibration, evaluator fine-tuning, and program-evolution alternatives; no executed or simulated tuning outcomes |
| Tab8 | tab:reporting | sections/appendix.tex; Required empirical outputs and interpretation boundaries |
| Tab9 | tab:external-endpoints | sections/appendix.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab10 | tab:training | sections/appendix.tex; Design-only C3 training controls |
| Tab11 | tab:full-ablations | sections/appendix.tex; Planned matched comparisons, not empirical component effects |
| Tab12 | tab:search-results | sections/appendix.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab13 | tab:simulation-cohorts | sections/appendix.tex; Explicit illustrative assignments, not actual data availability |
| Tab14 | tab:results | sections/appendix.tex; Explicit simulated C1 numerical example; not experimental results |
| Tab15 | tab:manifest | sections/appendix.tex; Experiment fields requiring author decisions |

The main table joins C1 alignment and selection; the downstream table separates C2 refinement from design-only C3.
Table 1 specifies equal-domain means and fixed-search-replicate input-group intervals, with eligible-domain counts and endpoint-specific common cohorts required when results are inserted.
Table 2 separates ID/OOD ERA-minus-seed major-regression rate contrasts; per-arm rates and completion remain required in the appendix.
The budget figure contains no curves: it reserves matched-search-budget and matched-human-budget comparisons.
The approved landscape composite is now in the appendix, unchanged; its 2,880 synthetic inputs differ from the full-cohort alignment plots.
All numeric fixtures, chart assets, and hashes are preserved.
Figure 1 retains the original palette, scoped font, native canvas, and disclosed photograph; its labels now explicitly cover mining existing datasets.

Review whole PDF pages as well as individual charts.
Table/figure floats are kept near their discussions without changing template fonts or margins.
The isolated previews under `build/reorganization-review/` are local checks, not new manuscript assets.
Historical revision records retain their contemporary display IDs.
