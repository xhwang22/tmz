# Independent reviewer audit — round 2

Date: 2026-09-19.
Scope: revised Method, Experiments, conditional Results, Discussion, and the relevant algorithm, measurement, comparator, and reporting appendices.
This report reviews the current shortened draft, not only the first revision submitted for review.
It excludes the already scheduled paper-memory synchronization and layout pass.
The reviewer has not edited manuscript text, implementation, figures, data, or bibliography.
The only additional diagnostic was a synthetic, non-networked call to the existing inheritance function with bytecode writing disabled.
The subsequent targeted recheck is recorded in `reviewer_round3_20260919.md`; the findings below describe the round-2 snapshot before those final corrections.

## Overall judgment

The first revision resolves most substantive writing and experimental-identification issues.
The method now separates candidate acceptance, candidate inheritance, and direction allocation; the text also stops attributing semantic refutation to the controller.
The input-weighted stochastic objective and the weighted missing-outcome bounds are now mutually consistent for a complete eligible cohort.
The comparator contract identifies what each arm changes and explicitly limits the history-only versus depth-first contrast to the combined allocation-and-inheritance policy.
The revised Discussion interprets alternative outcomes instead of merely listing risks.
I would not request another broad rewrite.

One implementation-alignment correction remains important: the equation and pseudocode currently return to the newly updated best program when inheritance fails, whereas the inspected native implementation returns to the best program recorded before that candidate.
This difference is observable when a candidate is accepted on development measurements but is ineligible for inheritance because local comparisons are unknown.
Two short wording clarifications would also remove avoidable ambiguity about diagnostic-history access and the meaning of a "worse" evaluator.

## Round-1 issue status

| Round-1 issue | Current status | Remaining qualification |
| --- | --- | --- |
| R1: operational allocation and termination | Substantially resolved | Agent-requested diagnostics, submission, and pause are now distinct from controller guards and scientific interpretation of refutation. |
| R2: shared eligibility before inheritance branches | Resolved in the predicate prose | The now-explicit possibility of acceptance without inheritance exposes the old-best/new-best update mismatch described below. |
| R3: stochastic objective and grouping weights | Resolved in substance | The complete-execution domain of the displayed estimator can be stated in a few words. |
| R4: comparator and budget definitions | Substantially resolved | The history-access rule should say each run's own history; exact configurations and prices correctly remain pending. |
| R5: labels versus human effort | Resolved | Equal original-input units establish label efficiency; human-effort claims require measured annotation time. |
| R6: Discussion as interpretation | Resolved in substance | Limit the first sentence to recorded development agreement; the revised history-only interpretation now includes the necessary independent-proposal comparison. |
| R7: display estimands and downstream regression | Resolved | The shortened Table 1 caption no longer calls marginal cell intervals paired intervals; Table 2 has separate ID/OOD ERA-minus-seed regression differences. |
| R8: central scientific comparisons visible | Resolved | Acquisition and continuation are explicitly named, with resource-matched interpretation. |
| R9: fixed-evaluator uncertainty versus optimizer variability | Resolved | Fixed-replicate input-group intervals and independent-search variability are separately specified. |

## Required correction: fallback uses the pre-update best program

Severity: major implementation-alignment issue, small textual repair.
Snapshot anchors: `sections/method.tex:65`–`:75`; `sections/appendix.tex:343`–`:347`, `:392`, and `:397`.

The method currently gives

```
B_(t+1) = C if accepted, else B_t
W_(t+1) = C if inherited, else B_(t+1).
```

However, native `harness_evolution/multidomain/example_search.py:1588` computes inheritance using `best.id` before installation of the candidate.
`revision_control.py:233`–`:259` first excludes unknown local or development evidence, even when `selected_for_exploration` is true, and returns the supplied `best_id` if inheritance is denied.
`example_search.py:535`–`:546` subsequently updates `best` but sets `working` from this already recorded `next_parent_id`; its consistency check explicitly passes `record["best_before_id"]`.
The development-promotion predicate at `example_search.py:1539`–`:1547` does not require all local diagnostic comparisons to be known.
Consequently, acceptance and failed inheritance are not mutually exclusive.

A synthetic direct call to the real inheritance function confirmed the relevant branch:

```
selected_for_exploration = True
complete_development_execution = True
comparable_development_execution = True
local boundaries unknown = 1
best_id = "seed"

=> keep_candidate = False
=> next_parent_id = "seed"
```

No model or dataset was invoked and no source file was changed.
This checks the controller branch, not the frequency of that branch in actual runs.
The same branch was subsequently verified through the native `patch_revision_v1` wrapper, which delegates the underlying eligibility decision through `intervention_revision` to `revision_control`.

Minimal repair if the manuscript describes the current implementation:

- Set the fallback of `W_(t+1)` to `B_t`, not `B_(t+1)`.
- In the pseudocode, save the pre-update best or update the working state before overwriting the best reference.
- State once that the fallback uses the pre-candidate best; a new direction can still start from the subsequently updated best.
- Make the corresponding appendix "returns to the best" statements unambiguous.

There is no need to alter the runtime merely to simplify the paper equation.
The recorded-best monotonicity statement remains true with this correction.

## Clarification: equal access rules do not mean free sharing of ERA-generated traces

Severity: moderate design ambiguity, one-sentence repair.
Snapshot anchor: `sections/appendix.tex:744`.

"History-only proposals ... can inspect the same accumulated diagnostic history as ERA" can mean either the same information-access rule or literally the same traces produced by an ERA run.
These are different experiments.
Runs following different programs normally generate different histories, and giving one arm another arm's diagnostic outputs without accounting for their generation cost would compromise the resource comparison.

Suggested wording:

> History-only proposals also edit the current best program and retain their own accumulated diagnostic history under the same access rule as ERA, but neither prioritize an active direction nor inherit an unaccepted program.

If a checkpoint-fork study is intended instead, specify the common frozen prefix, post-fork budgets, and how the prefix cost is accounted for.
The present end-to-end comparison does not need that additional design.

## Clarification: bound "worse" to the recorded selection quantity

Severity: moderate claim precision, a few words.
Snapshot anchor: `sections/discussion.tex:4`.

"Without accepting a worse evaluator" is stronger than the actual invariant.
An accepted evaluator can have a higher repeatedly inspected development score while having lower unseen agreement or different downstream behavior.
The Method already correctly states that its invariant is not a guarantee of unseen agreement.

Suggested wording:

> ERA permits further implementation without lowering the best recorded development agreement, but continuation has an opportunity cost.

The following Discussion sentence now requires history-only proposals to improve over independent proposals before suggesting that retained diagnostics may explain gains.
That additional condition resolves the original attribution problem.
If future results use "matches ERA" as a substantive equivalence claim, they will need sufficiently precise uncertainty or an explicit equivalence criterion; a nonsignificant difference alone is not equivalence.
This is a future interpretation guard, not a request to insert a new test into the current placeholders.

## Optional precision: state the complete-execution domain of the estimator

Severity: minor.
Snapshot anchor: `sections/method.tex:25`.

The displayed median and binary agreement indicator require complete executions.
The next sentence correctly delegates missing outcomes to coverage and bounds, but the equation's domain is implicit.
Adding "For complete executions" before defining the estimator would resolve this without another equation.

The appendix weighting itself is correct: predetermined weights sum to one, observed weighted successes contribute `K`, and unobserved mass is `1-M`, giving the identification bounds `[K, K+1-M]`.
These bounds must remain distinct from sampling confidence intervals, as the present text specifies.
The native canonical-pair development quantity is now explicitly called a proxy rather than silently equated with every within-group preference.

## Checks that did not reveal a new substantive defect

- The objective includes execution randomness for the fixed finite-repeat scoring procedure rather than asserting access to a population median.
- Pair dependence induced by shared artifacts and input groups is acknowledged in the statistical appendix.
- Complete, comparable observations are a common prerequisite for all inheritance branches; exact trace-field changes are not called verified causal mechanisms.
- The controller is not presented as an automatic semantic-falsification oracle.
- The comparison contract explicitly says that allocation and inheritance change together in the history-only versus depth-first contrast.
- The primary search budget is frozen-price model-and-tool cost, with attempts and other resource counts separately reported rather than simultaneously forced equal.
- The annotation analysis distinguishes acquired labels, historical replay, and measured human time.
- Main-table reporting uses fixed-replicate, equal-domain summaries on common eligible cohorts and requires eligible-domain counts.
- C2 and C3 distinguish relative preference from absolute change against the original output or base policy, and C3 remains design-only.
- Discussion does not infer critic or reward usefulness merely from average preference agreement.
- The conditional Results retain an explicit unmeasured-placeholder notice and do not turn ideal outcomes into observed findings.

## Evidence boundary unchanged

This writing revision does not close empirical gaps C27 or C28, establish downstream benefits, or prove that abandoned directions in the motivating optimizer would have succeeded if continued.
The comparative runs, newly needed human judgments, frozen baseline configurations, and trainable-backbone feasibility remain future evidence requirements.
No new theorem, causal guarantee, automatic refutation procedure, or measured result should be introduced to make the wording appear more complete.

## Recommended next step

Make the fallback correction and the two short clarifications, then perform a targeted final check of the equation, pseudocode, and matching appendix statements.
The other reviewed content is ready for the parent's memory and layout synchronization; another broad content rewrite is not warranted by this review.
