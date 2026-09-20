# Reviewer revision record — 2026-09-19

The author requested an independent reviewer subagent and repeated revision of Method, Experiments, Results, and Discussion.
`/root/reviewer_method_experiments` completed three rounds: substantive review, review of the revised draft, and targeted verification of the remaining corrections.
The reviewer did not edit the manuscript or run an empirical study.
Original comments and their snapshot anchors remain verbatim in [round 1](reviewer_round1_20260919.md), [round 2](reviewer_round2_20260919.md), and [round 3](reviewer_round3_20260919.md).
Locations below refer to the revised source, not to line numbers in the earlier snapshots.

## Round-1 responses

| ID | Reviewer comment (verbatim from the priority table) | Response | Current manuscript change | Evidence / disposition |
| --- | --- | --- | --- | --- |
| R1 | The central direction-allocation rule is not operationally stated; inherited candidate state, continued direction, and semantic refutation are still easy to confuse. | Clarify the distinct decisions and who makes them. | `sections/method.tex:54`, `:74`, `:85`; `sections/appendix.tex:344`, `:393`: acceptance updates best, measured eligibility governs inheritance, and the agent requests diagnostics, implementation, or pause within controller limits. | Native actions and inheritance rules; reviewed in rounds 2/3. No semantic-refutation oracle is claimed. |
| R2 | Promotion is described as sufficient for inheritance, although the inspected controller first requires known, complete, comparable inheritance evidence. | Correct the common prerequisite. | `sections/method.tex:74`: missing, incomplete, or incomparable required comparisons force inheritance to zero before the three eligible branches. The appendix states the same order. | `revision_control.inheritance_decision` and native wrapper; resolved, including the round-2 fallback correction below. |
| R3 | The objective omits execution randomness, and pair-weighted estimation differs from the input-weighted reporting definition. | Correct the target, estimator, and missing-outcome accounting. | `sections/method.tex:11`: sample inputs then strict within-input preferences and include finite-repeat randomness. `:25`: define the complete-execution estimator with equal input weights. `sections/appendix.tex:448`: covered weight, conditional agreement, and identification bounds. | C46; one canonical native development pair is explicitly a proxy. Bounds are not confidence intervals. |
| R4 | Comparator names and matched-budget statements do not define executable comparisons or isolate direction continuation. | Specify controlled contrasts and limit attribution. | `sections/appendix.tex:732`, `:744`: C1 and allocation contracts define editable scope, parent choice, own-run history, and eligibility. Frozen-price model-and-tool cost is the primary search budget. | Combined allocation/inheritance is tested, not isolated inheritance. Exact versions, prices, and baseline settings still require freezing. |
| R5 | Equal annotation units are not necessarily equal human effort, and replaying a historical corpus does not measure current annotation time. | Separate label efficiency from human-time efficiency. | `sections/experiments.tex:45`; `sections/results.tex:102`; `sections/appendix.tex:837`: distinguish original-input units, historical replay, and measured time including raters/adjudication/abstention. | Definitions resolved; no human-time benefit measured. Random anchors count within each arm's budget. |
| R6 | Discussion supplies neither the benefit/boundary of depth-first allocation nor interpretation across C1/C2/C3. | Replace the risk checklist with conditional interpretation. | `sections/discussion.tex:4`: continuation opportunity cost, history-only alternatives, development-only gains, and different requirements for selection, critique, and rewards. | Round-3 reviewer accepts the interpretation boundaries. C1/C2 cannot substitute for C3 evidence. |
| R7 | Main displays do not visibly encode all the estimands their captions promise, especially per-arm/per-split regressions. | Make cells and aggregation explicit. | `sections/results.tex:12`: equal-domain/fixed-replicate summaries with eligible-domain counts. `:52`: separate ID/OOD ERA-minus-seed regression contrasts. Companion reporting requirements are in Appendix H. | Updated Tab1/Tab2 captions and memory. Values remain pending, not zeros; no per-domain measurements exist yet. |
| R8 | The two central scientific hypotheses read as late auxiliary ablations, while the main opening emphasizes only evaluator and downstream quality. | Make the explanatory comparisons visible without renumbering C1–C3. | `sections/experiments.tex:4`, `:43`, `:47`: connect evaluator/downstream outcomes with the decisive search and acquisition contrasts. | Figure 2 reserves both matched-budget comparisons; neither is a finding. |
| R9 | The uncertainty statements do not distinguish a fixed-evaluator comparison from variability of the optimizer itself. | Name separate inferential units. | `sections/experiments.tex:20`; `sections/appendix.tex:619`, `:810`: fixed-evaluator original-input intervals and independent-search summaries/counts are separate. | Scoring repeats are not independent searches. Real run counts remain pending. |

## Round-2 corrections and round-3 verification

| ID | Reviewer comment (verbatim excerpt) | Response and manuscript change | Verification |
| --- | --- | --- | --- |
| R2.1 | the equation and pseudocode currently return to the newly updated best program when inheritance fails, whereas the inspected native implementation returns to the best program recorded before that candidate. | Corrected Equation 6 to use `W_(t+1)=B_t` on failed inheritance. Algorithm 1 saves `B_old`; corresponding prose uses the same pre-update state. See `sections/method.tex:65`, `:78`; `sections/appendix.tex:344`. | Round 3 checks both the native wrapper and main/appendix text. An accepted candidate with unknown local comparisons can update best while working returns to old best. A synthetic branch check is not a performance experiment. |
| R2.2 | equal access rules do not mean free sharing of ERA-generated traces | `sections/appendix.tex:746` now specifies each run's own accumulated history under the same access rules. | Resolved in round 3. Other arms do not receive free ERA traces. |
| R2.3 | "Without accepting a worse evaluator" is stronger than the actual invariant. | `sections/discussion.tex:4` now says "without lowering the recorded best development score". | Resolved in round 3. C45 does not guarantee unseen or downstream quality. |
| R2.4 | Adding "For complete executions" before defining the estimator would resolve this without another equation. | Added that restriction at `sections/method.tex:25`. | Resolved in round 3; missing outcomes still use coverage and bounds. |

## Remaining scientific requirements

- C27/C28 remain material empirical gaps: acquisition efficiency and continued-search benefits need actual matched-budget comparisons.
- Downstream C1/C2/C3 benefits require their own observations and human judgments; C3 remains design-only.
- Freeze baseline implementations, model/checkpoint feasibility, prices, budgets, and analysis before running comparisons.
- A future claim that history-only search "matches ERA" requires adequate precision or a prespecified equivalence criterion; failure to reject a difference is insufficient.
- An inheritance-specific causal claim requires a separate control; the current depth-first versus history-only contrast changes allocation and inheritance together.
- This reviewer cycle does not re-audit the author-edited Abstract or publication fields. The 40-reference bibliography is unchanged.

## Closing checks

`make check` passes structural, memory, simulation-provenance, landscape, and whitespace checks.
The compiled manuscript has 9 main-text pages and 35 total pages, with no reduction of body fonts or margins.
The parent visually checked the main pages and appendix contact sheets, with full-page inspection of the revised method and main displays.
The submission guard remains intentionally rejecting because simulated illustrations remain.
No empirical study, training, engineering-source change, commit, or push was performed in this review cycle.
