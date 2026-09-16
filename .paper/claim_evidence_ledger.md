# Claim–evidence ledger

Evidence paths below are relative to the source project, not this paper repository.
The ledger supports writing consistency; it is not an experimental result log.

| ID | Manuscript statement | Evidence | Status / permitted inference |
| --- | --- | --- | --- |
| M0 | The revision method is instantiated for distinct evaluation standards; slides are one candidate application | `docs/plans/p2e_v2_plan.md` §2; user scope clarification | Research scope; no universal scorer or demonstrated cross-domain transfer |
| M1 | ERA revises representation, rubric, specialists, tools, routing and synthesis | `docs/era_algorithm.md` §§1–2; `docs/plans/p2e_v2_plan.md` | Method representation; no effectiveness claim |
| M2 | Runtime scores one artifact without its opponent or H0 | `docs/era_algorithm.md` §1; runtime contract in `README.md` | Deployment interface; no claim of immunity to every leakage risk |
| M3 | Each artifact is scored at least three times; medians precede strict comparison | `docs/era_algorithm.md` §1 | Measurement definition, not observed reliability |
| M4 | Proposal Train and sealed development Train are separate; Val is terminal | `docs/era_algorithm.md` §§3–5; `docs/era_main_search.md`; `harness_evolution/multidomain/era_search.py` | Access and selection protocol; adaptive development is not unbiased test evidence |
| M5 | Proposals use original evidence, mechanism hypotheses and bounded edits | `docs/era_algorithm.md` §4 | Implemented method interface; no claim of causal diagnosis or semantic trust region |
| M6 | Working and best programs differ; continuation may retain a non-promoted program | `docs/era_algorithm.md` §§4–5 | Allocation capability; benefit needs controlled comparison |
| M7 | Semantic synthesis uses anchored scores and finding references | `docs/semantic_synthesis.md`; `harness_evolution/multidomain/score_scale.py`; `harness_evolution/multidomain/semantic_fusion.py` | Optional mechanism; reference coverage is not proof of semantic correctness |
| H1 | Full program revision may outperform prompt-only adaptation | Motivation plus proposed experiments | Hypothesis only; all quantitative cells pending |
| H2 | An evolved scorer may improve fixed-pool selection | `docs/plans/p2e_v2_plan.md`, C1 | Planned endpoint; pair-only accuracy is insufficient |
| H3 | Evolved feedback may improve freshly generated artifacts | `docs/plans/p2e_v2_plan.md`, C2 | Planned study; requires shared fresh starts and new blinded human labels |
| P1 | Coverage and missing-outcome bounds supplement complete-pair accuracy | Mathematical accounting in Appendix A | Reporting definition, not measurements or a confidence interval |
| P2 | Grouped 95% intervals and matched-budget ablations assess differences | `sections/experiments.tex`; Appendix A/C | Analysis proposal; not a frozen completed analysis |

Not permitted without new evidence: measured accuracy gains; statistical
significance; superiority to GEPA or program-search methods; demonstrated
cross-domain transfer; annotation efficiency; correct causal explanations;
reward-training benefits; completed human studies; or universal leakage freedom.

Do not cite internal positive targets, successful synthetic tests, study entry
points, or engineering availability as empirical support for these claims.
