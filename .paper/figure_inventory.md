# Figure and table inventory

Round 41, 2026-09-21. Exact captions and reciprocal claim links: `figures.yml`.
Four main figures, three appendix figures; two main tables, nineteen appendix tables.
No current display establishes empirical efficacy.

| Printed / internal ID | Stable label | TeX source | Evidence status |
| --- | --- | --- | --- |
| Fig. 1 / Fig1 | fig:teaser | figures/teaser.tex | Constructed illustration of the search distinction; no observed human preferences, optimizer trajectories, acceptance or gains |
| Fig. 2 / Fig2 | fig:overview | figures/overview.tex | Conceptual specification with constructed examples; no measured results |
| Fig. 3 / Fig3 | fig:c1-landscape | figures/results_landscape_pending.tex | Simulated ideal aggregates; not empirical evidence |
| Fig. 4 / Fig4 | fig:budget-tests | figures/search_dynamics_pending.tex | Simulated ideal aggregates; not empirical evidence |
| Fig. A1 / Fig5 | fig:runtime | figures/evaluator.tex | Conceptual specification with constructed examples; no measured results |
| Fig. A2 / Fig6 | fig:acquisition | figures/mining_results_pending.tex | Simulated ideal aggregates; not empirical evidence |
| Fig. A3 / Fig7 | fig:trajectory | figures/trajectory_results_pending.tex | Unfilled; no invented traces or recorded successful direction |

| Printed / internal ID | Stable label | Evidence status |
| --- | --- | --- |
| Table 1 / Tab1 | tab:main-alignment | Assigned ideal aggregates; no observations or statistical inference |
| Table 2 / Tab2 | tab:downstream-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A1 / Tab3 | tab:domains | Design, provenance or unmeasured reporting template; not completed execution |
| Table A2 / Tab4 | tab:data-sources | Design, provenance or unmeasured reporting template; not completed execution |
| Table A3 / Tab5 | tab:readiness | Design, provenance or unmeasured reporting template; not completed execution |
| Table A4 / Tab6 | tab:human-provenance | Design, provenance or unmeasured reporting template; not completed execution |
| Table A5 / Tab7 | tab:annotation-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A6 / Tab8 | tab:access | Design, provenance or unmeasured reporting template; not completed execution |
| Table A7 / Tab9 | tab:adaptation | Design, provenance or unmeasured reporting template; not completed execution |
| Table A8 / Tab10 | tab:cost-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A9 / Tab11 | tab:domain-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A10 / Tab12 | tab:full-ablations | Design, provenance or unmeasured reporting template; not completed execution |
| Table A11 / Tab13 | tab:search-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A12 / Tab14 | tab:mining-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A13 / Tab15 | tab:component-results | Assigned ideal aggregates; no observations or statistical inference |
| Table A14 / Tab16 | tab:downstream-detail | Assigned ideal aggregates; no observations or statistical inference |
| Table A15 / Tab17 | tab:external-endpoints | Design, provenance or unmeasured reporting template; not completed execution |
| Table A16 / Tab18 | tab:training | Design, provenance or unmeasured reporting template; not completed execution |
| Table A17 / Tab19 | tab:optional-results | Design, provenance or unmeasured reporting template; not completed execution |
| Table A18 / Tab20 | tab:reporting | Design, provenance or unmeasured reporting template; not completed execution |
| Table A19 / Tab21 | tab:manifest | Design, provenance or unmeasured reporting template; not completed execution |

## Numerical and visual sources

`data/ideal_scenario/scenario.json` feeds `scripts/render_ideal_scenario.py`.
Exports in `figures/ideal_scenario/` include vector PDFs, previews, table rows
and prose-number macros. The manifest checks both inputs and outputs.
Fig3 retains the original 5.4 × 3.57-inch annular layout and four-family/lake palette.
Its task gains and deployment scatter reuse Table1's underlying values.
Fig4 separates development progress, post-search held-out controls and direction
outcomes. FigA2 separates label-access and human-time budgets and the joint design.

Plots have no simulation banners; captions and the manuscript notice disclose
their assigned provenance. Real trajectories, permissions, uncertainty and
independent attribute results remain unfilled. Full filling requirements:
`experiment_fill_plan.md`.

## Historical resources

`archive/figures-round40.yml` preserves the previous inventory and caption texts.
Old `figures/simulated/` and `data/simulated/` are unchanged historical fixtures,
including `landscape_outcomes.pdf`. They are not included as current results.
Prior figure IDs are revision-local; do not use them as current callouts.
