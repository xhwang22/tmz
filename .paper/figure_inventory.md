# Figure and table inventory

Authoritative captions and claim links are in `figures.yml`: 13 figures (three main, ten appendix) and 15 tables.
Three figures are conceptual, one is an unmeasured budget placeholder, and nine are explicitly simulated quantitative displays.
No display reports measured performance.

| ID / location | Source | Purpose / status |
| --- | --- | --- |
| Fig1 / main | figures/teaser.tex | (a) layout fidelity versus visual richness, with opposite human/evaluator rankings; (b) successive plausible directions in the default setup; (c) continued layout-fidelity revisions: detection, penalty and severity; Constructed illustration of the search distinction; no observed human preferences, optimizer trajectories, acceptance or gains |
| Fig2 / main | figures/overview.tex | (a) preference mining from existing datasets or new outputs; (b) retained diagnostics within a direction, independent candidate acceptance; (c) fixed best program for selection, refinement and planned reward-guided training; constructed example, not measured results |
| Fig3 / main | figures/c1_landscape.tex | (a) 22-task taxonomy, not measured sample composition; (b) seed and IterEval agreement versus Best-of-4 family means; (c) common-cohort OOD agreement across all 22 tasks; Explicit full-cohort simulated reporting fixture; no empirical alignment, selection, sampling, search, C2, or C3 efficacy |
| Fig4 / appendix | figures/evaluator.tex | (a) one artifact; (b) routed observations; (c) dimensional criteria; (d) synthesis; Conceptual specification with constructed examples; no measured results |
| Fig5 / appendix | figures/budget_tests.tex | (a) search under equal total budgets; (b) disagreement-based preference mining versus alternative sampling under equal human budgets; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Fig6 / appendix | figures/simulated_landscape.tex | (a) balanced input composition across 22 tasks; (b) assigned cost versus OOD agreement, 110 domain points and ten setting means; (c) four family bar panels in one row, five methods per task; Balanced synthetic OOD subset for layout, distinct from full-cohort appendix data; no empirical efficacy or label availability established |
| Fig7 / appendix | figures/simulated_alignment.tex | (a) ID paired effects; (b) OOD paired effects; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig8 / appendix | figures/simulated_acquisition.tex | (a) reused preferences; (b) new preferences; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig9 / appendix | figures/simulated_annotation.tex | (a) valid-pair agreement; (b) requested-rating abstention; (c) group consensus outcomes; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig10 / appendix | figures/simulated_selection.tex | (a) reused preferences; (b) new preferences; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig11 / appendix | figures/simulated_ablation.tex | (a) conditional component effects; (b) cumulative feedback detail; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig12 / appendix | figures/simulated_refinement.tex | (a) paired quality differences; (b) diverging preference shares and a separate abstention column; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |
| Fig13 / appendix | figures/simulated_cost.tex | (a) paired-setting deployment costs; (b) paired-setting agreement; Explicit simulated reporting fixture; not evidence of effectiveness, reliability, or efficiency |

| ID | Label | Source / status |
| --- | --- | --- |
| Tab1 | tab:main-alignment | sections/results.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab2 | tab:domains | sections/appendix.tex; Research scope; not data readiness or completed evaluation |
| Tab3 | tab:human-provenance | sections/appendix.tex; Two-setting provenance and protocol specification |
| Tab4 | tab:readiness | sections/appendix.tex; Readiness audit requirements, not measured coverage |
| Tab5 | tab:access | sections/appendix.tex; Data access and independence contract |
| Tab6 | tab:adaptation | sections/appendix.tex; Planned calibration, evaluator fine-tuning, and program-evolution alternatives; no executed or simulated tuning outcomes |
| Tab7 | tab:reporting | sections/appendix.tex; Required empirical outputs and interpretation boundaries |
| Tab8 | tab:downstream-results | sections/appendix.tex; Unmeasured empirical C2/C3 status; dashes are not zeros |
| Tab9 | tab:external-endpoints | sections/appendix.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab10 | tab:training | sections/appendix.tex; Design-only C3 training controls |
| Tab11 | tab:full-ablations | sections/appendix.tex; Planned matched comparisons, not empirical component effects |
| Tab12 | tab:search-results | sections/appendix.tex; Unmeasured reporting placeholders; no empirical result or expected effect size |
| Tab13 | tab:simulation-cohorts | sections/appendix.tex; Explicit illustrative assignments, not actual data availability |
| Tab14 | tab:results | sections/appendix.tex; Explicit simulated C1 numerical example; not experimental results |
| Tab15 | tab:manifest | sections/appendix.tex; Experiment fields requiring author decisions |

Figure 1 directly prints the approved three-column author-v6 image-editing teaser, including all nine images. Small vector labels remain a documented readability limit.
Its 2026-09-21 surface refinement adds pale headers, paper edges, shallow shadows and styled nodes. A subsequent panel-a update makes the criterion trade-off and opposite rankings explicit; images/crops, outer layout and panels b/c are unchanged.
Figure 2 now prints the approved horizontal three-panel composition from figures/overview.pdf, replacing the old circular four-panel figure. Palette, layout and pictograms match the stable preview; labels and connectors remain vector. Small labels and some low-resolution pictogram crops remain documented limitations.
Figure 3 and main Table 1 retain the C1 landscape and complete comparator matrix. The landscape artwork and numerical records are unchanged.
The former runtime, budget placeholder, and balanced-subset landscape are now appendix Figures 4, 5, and 6. Remaining appendix figures shift accordingly; all table numbers stay unchanged.
Lake-green method identity matches the main landscape. Red denotes error status, not the method.
Teaser preferences, scores, and paths are constructed examples, not evidence for empirical gaps C27/C28. Historical revision records retain their contemporary figure numbers.
