# Method rewrite: exemplars and implementation

## Semantic and language boundaries (2026-09-21, round 40)

This local revision retains round39's state and selection equations. It adds a
complete verbal cycle before Algorithm 1, removes inheritance as a branded third
decision, and separates execution records from agent interpretations. Main text
uses evaluation program and continue/end a direction consistently. Existing-label
budgets are not described as newly performed human work.

The independent reviewer rechecked the current source. patch_revision.py:230–275
preserves direction_id, while revision intent can change. revision_session.py:57–87
asks for an unresolved question and why no different test is ready; :404–407 maps
the pause reason to a no_change record. No parser rule fixes semantic intent or
requires a sufficient reason category, exhaustive testing, or minimum depth.
These limitations are now explicit; no hard continuation contract is invented.

revision_control.py:227–259 still requires known local/checking comparisons for
the next candidate parent. example_search.py preserves pre-update best fallback,
including an accepted candidate whose local comparison is incomplete. The prose
reduces terminology, not these implementation conditions.

The four inspected source hashes below remain unchanged. The implementation,
author-edited Abstract/Introduction, figure assets, numerical fixtures and
empirical status are not changed. No new citations or venue metadata are added.

## Core-first optimizer exposition (2026-09-21, round 39)

The Method now begins with persistent (B, W, d, z) and the selection/exploration
distinction. Only state, objective and acceptance/best update remain displayed.
Algorithm 1 moves to the main text; the six-component revision space moves last.
Program inheritance remains implemented but is explained within continuation.
No controller, data, model, or empirical result is changed.

The dedicated reviewer rechecked the native path and verified the rewritten
draft after two corrections: pause costs are recorded before the next direction,
and diagnostic interpretation is not presented as an enforced semantic stop test.
Direction choice and the first revision can share one editing session.
The ordinary loop omits optional compression modes; it is not a complete listing
of every configurable branch.

Implementation anchors inspected for this cycle:

- patch_revision.py:230–237 preserves the active direction identifier; :266–274
  permits updates to the plan/intent, so persistence is not immutable semantics.
- example_search.py:1057–1119 supplies the installed parent, latest trial and
  same-direction history to the next session. Rejection or failed inheritance
  does not itself clear direction identity.
- revision_session.py:57–87 and :380–439 define investigation, submission,
  repair and pause. A pause is recorded as no_change, not a free search reset.
- example_search.py:709–723 and :1156–1158 clear a paused plan and restart
  from best. The agent's reason is not certified as semantically sufficient.
- example_search.py:1569–1606 reuses verified measurements for exact replays
  and applies checking-based selection. The pseudocode does not count replayed
  scores as independent new measurements.
- revision_control.py:227–250 retains the complete/comparable local-and-checking
  prerequisites for inheritance. example_search.py:475–482 and :584–588 preserve
  the pre-update best fallback, including accepted-but-not-inherited candidates.
- example_search.py:1047–1051 distinguishes advisory cumulative edits in the
  default policy from enforced run/session/execution limits.

The source HEAD remains 5814194eb4469e302438b20d6cf368a3d6928cfc with existing
uncommitted work. Current inspected file hashes:

| Source path | SHA-256 |
| --- | --- |
| harness_evolution/multidomain/revision_control.py | bea3de6852661922e3af2824253d04d7b7c5ef905fcf43bd34b7081a5cbebfe2 |
| harness_evolution/multidomain/example_search.py | 001723e8d29ac8a5ba793908ae21bf32a7a26db28e3bfaec1622681002baadaa |
| harness_evolution/multidomain/patch_revision.py | ec4658faf3945f90f91296c75c4dbd5ccb2efe6648e28f56dec949749cabc5bb |
| harness_evolution/multidomain/revision_session.py | 912cc3731fa9fd1909e61902f056be5af62b80ca23ca60f8f2d07b8e4eb4f881 |

These are source checks, not evidence of optimization benefit.
See method_readability_review_20260921_round39.md for the final review.

## Source consolidation and readability review (2026-09-21, round 38)

The main Method now has one source, `sections/method.tex`. The source-only merge
preserved the extracted PDF text exactly before any prose revision. Two dedicated
reviewer passes and a final verification then checked the revised reading order
against the semantics recorded below. The feedback table is introduced before
its proposal subset, acceptance is adjacent to the joint best/working update,
and a constructed trace example explains how diagnosis informs another revision.
Technical details moved to the appendix retain their original conditions.

The review corrected two easily confused implications: failed inheritance does
not imply failed acceptance, and default direction continuation is not
unconditional continuation. Both decisions still use the pre-update best program.
Repeated checking data remain development data; terminal validation cannot rerank
or reopen search. There is no new hard direction-edit budget, automatic semantic
verification rule, empirical claim, or change to the engineering implementation.
See `method_readability_review_20260921.md` for review dispositions and checks.

## Persistent-state and algorithm-order revision (2026-09-21, round 37)

The author's latest direction replaces the three separate formulation, mining,
and evolution sections with Section 3, IterEval. Overview and setup states the
inputs, editable program, objective and data boundaries. Preference mining is a
short interface; the core follows one cycle rather than retelling the insight.
SkillOpt's cached Method §§3.1–3.7 was read as a structural reference. GEPA, DGM
and AgentOptimizer are author-supplied exposition examples, not evidence that
their algorithms universally abandon rejected directions. No new citation or
publication-field claim is introduced.

The active state (B, W, d, z) abstracts existing best/working programs, the
persistent direction plan, and diagnostic history. Revise and Update expose
their data dependencies, not newly implemented operators or learned parameters.
The record binds intent and actual edits to the tested candidate and its true
parent. Available proposal observations include repaired, unchanged, regressed
and unknown outcomes; checking Train remains aggregate-only. Optional expected
orderings and exact-field checks are not a required complete diagnostic schema.
An exact-field change does not verify a semantic explanation.

Inspected anchors in the engineering repository:

- revision_session.py:28–85: proposal-only investigation, actual installed
  parent versus last trial, intended versus observed behavior, tools/submit/
  repair/pause actions, and optional expectations/checks.
- revision_control.py:214–259: common completeness/comparability requirements,
  acceptance/no-damage/fresh-progress inheritance branches, protected cases,
  and previously credited repairs. The pre-update best remains the fallback.
- example_search.py:900–1176: retained direction plans and histories, choosing
  further investigation/revision or pausing, and edit-guidance policy handling.
  The proposal's max_steps is not a maximum direction depth.
- docs/era_algorithm.md: default edit counts, replacement fractions and
  cumulative direction edits are advisory. There is no default cumulative
  API/token cap to import into the main equations. Configured search and
  session bounds plus execution limits remain separate constraints.

The core therefore distinguishes candidate acceptance, program inheritance,
and direction continuation. Resource exhaustion is unresolved, not refutation.
Terminal Val remains a frozen-shortlist assessment, not an adaptive acceptance
gate. The direction allocation is an implemented policy, not a convergence or
semantic-refutation theorem. C27/C28 remain evidence gaps.

Engineering HEAD remains 5814194eb4469e302438b20d6cf368a3d6928cfc; its dirty
worktree contains the inspected changes. SHA-256 identifies this read-only
inspection, not a frozen experiment:

| Path relative to engineering repository | SHA-256 |
| --- | --- |
| harness_evolution/multidomain/revision_session.py | 5bb56884633bef98e01e0111a14a4ca1c730ef03b7e8733d2c20b1e51f10a8e2 |
| harness_evolution/multidomain/revision_control.py | bea3de6852661922e3af2824253d04d7b7c5ef905fcf43bd34b7081a5cbebfe2 |
| harness_evolution/multidomain/example_search.py | 001723e8d29ac8a5ba793908ae21bf32a7a26db28e3bfaec1622681002baadaa |
| docs/era_algorithm.md | e6ec62203c2ae3098328a1829d29539db985311e767e5bb9fc38b87db67d0c62 |

No engineering files, model calls, numerical results, figure assets or captions
were changed. The author's pre-existing Abstract edits and Introduction were
preserved. Historical audit entries below describe earlier revisions.

Inspected and revised on 2026-09-19.
The writing exemplars guide exposition; the source implementation governs algorithmic statements.
This audit supplies no new performance evidence and leaves C27/C28 unverified.

## Structural references

| Exemplar | Verified identity and publication status | Use in this rewrite |
| --- | --- | --- |
| GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning | arXiv:2507.19457v2; ICLR 2026 in the existing citation audit | Define the executable object and measurement before explaining trace-driven changes. |
| Meta-Harness: End-to-End Optimization of Model Harnesses | arXiv:2603.28052v1; official `stanford-iris-lab/meta-harness` repository; only preprint status verified here | State the central design choice, show the search loop, and move interfaces and detailed checks to the appendix. |
| Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents | arXiv:2505.22954v3; ICLR 2026 in the existing citation audit | Separate executing the evaluator from modifying it; motivate exploration before describing state maintenance. |
| SkillOpt: Executive Strategy for Self-Evolving Agent Skills | arXiv:2605.23904v2; official `microsoft/SkillOpt` repository; only preprint status verified here | Keep object names and stage order stable; do not import optimization metaphors or its empirical conclusions. |

GEPA §§2–3.1 and DGM §3 and Appendices C.2/C.4 were read from the local full-text audit cache.
Meta-Harness §3/Algorithm 1 and SkillOpt §§3.1–3.7 were read from their official arXiv full texts in this turn.
GEPA retains Pareto candidates, DGM retains nonoptimal valid agents, and Meta-Harness does not impose one fixed parent-selection rule.
None is characterized as universally abandoning every unsuccessful direction.
The paper's development observation remains limited to the tested configuration recorded in `search_observation_audit.md`.

The four papers separately requested for Related Work remain included: arXiv:2604.13602, 2601.03986, 2605.23899, and 2602.03619.
Their role is contextual comparison, not evidence for ERA's performance or structural templates for its Method.
Their verified preprint status and publication-field checks remain in `citation_audit.md`; no bibliography entry or venue field changed in this rewrite.

## Implementation-to-text checks

Source paths below are relative to the engineering repository named in `source_provenance.md`.
The observed default is native ERA with a tool-driven patch session; legacy branches are not silently combined with it.

| Manuscript statement | Implementation anchor | Scope and limitation |
| --- | --- | --- |
| Pointwise runtime reads one artifact and permitted task context | `harness_evolution/multidomain/runtime.py`; `domain_adapters/base.py` | Pair preferences supervise external diagnosis and measurement, not the deployed scorer. |
| Default synthesis hides structured specialist scores, ratings, and scales | `harness_evolution/multidomain/semantic_fusion.py:174–212` | Findings, reasons, and specialist scopes remain; prose can still contain value judgments. |
| A patch contains actual edits, intent, and inspected Train references | `harness_evolution/multidomain/patch_revision.py:64–91`; `revision_session.py:28–82` | Expected orderings and intermediate checks are optional, not a mandatory complete hypothesis packet. |
| Connected edits form one complete candidate | `harness_evolution/multidomain/mechanism.py:102–128` | Partially assembled versions are not separately measured; bundle gain does not establish each component's effect. |
| Best-evaluator acceptance differs from working-state inheritance | `harness_evolution/multidomain/example_search.py`; `revision_control.py:214–259` | Complete/comparable measurements are required; accepted or undamaged candidates need not earn the extra allowance for an unaccepted damaged candidate. |
| New progress can justify retaining a damaged intermediate candidate | `revision_control.py:238–249`; `intervention_revision.py:331–376`; `patch_revision.py:269–286` | Root-error repairs cannot be recredited; only an exact, previously uncredited recorded-field change earns mechanical progress, not a semantic expectation. |
| Failed attempts inform subsequent implementation, but automatic semantic refutation is absent | `era_search.py:380–394`; `revision_control.py:251–259` | The controller records `mechanism_refuted=False`; scoped refutation remains a research evidence standard, not an implemented oracle. |
| Edit-character counts are guidance | `harness_evolution/multidomain/edit_budget.py:232–284` | Permissions, interface validity, fixed-model and execution constraints still apply. |
| Development is adaptively reused; terminal Val does not rerank or guide edits | `harness_evolution/multidomain/era_search.py:270–293,397–454` | Original-input/artifact separation is implemented; source-level near-duplicate review remains a broader study requirement. |
| Acquisition currently ranks structural conflicts | `harness_evolution/multidomain/mining.py:140–264` | Priority is twice the count of within-dimension conflicts plus overall–dimension conflicts plus a trade-off indicator; no learned human-reliability weights. |
| Human qualification is distinct from an implemented structural queue | `mining.py:329–338`; `fresh_web_mining.py:65,167,215` | Model-annotated pilot anchors are not human reliability; no pilot fraction is promoted to the main human-acquisition configuration. |
| Acquisition and evaluation aggregate repeated scores differently | `harness_evolution/multidomain/mining_runner.py:147–172`; `orchestrator.py:130–142` | Acquisition takes the median of same-repeat score differences; evaluator measurement compares separately aggregated artifact scores. |

The source plan's §§3–4 define the broader acquisition and falsification standards.
Its header explicitly distinguishes those standards from completed implementation and evidence.
The new prose preserves both levels and does not claim a sampling benefit, a depth-first advantage, or complete cross-domain human annotation.

## Source identity

Engineering HEAD: `5814194eb4469e302438b20d6cf368a3d6928cfc`.
The engineering worktree contains newer uncommitted changes; HEAD alone does not identify the inspected implementation.
No engineering files, experiments, models, or private data were modified or launched.
These SHA-256 values identify selected inspected files, not a frozen experiment:

| Source path | SHA-256 |
| --- | --- |
| `harness_evolution/multidomain/mining.py` | `cdf63b53ab06fe280bab1c25ad3e1dd738d9961fcb848c3bfe77df699398af50` |
| `harness_evolution/multidomain/mining_runner.py` | `a097ea3cfb8b066b72f40ce2d37ced3253c7d5bc45052372cd1bd3e9a98aa959` |
| `harness_evolution/multidomain/semantic_fusion.py` | `e1a24a1db9c3e1e0d4f1d46b581c027e6b4248f950f43417b30f3d0b9fa68a40` |
| `harness_evolution/multidomain/patch_revision.py` | `de3c9163576baddb95ab5da9fbb292bcad5185401a9d5f346c4e2d399fa317ce` |
| `harness_evolution/multidomain/intervention_revision.py` | `df143e61fb79d1a5319053247296bf890bea5ad8dfa8493e785529865e30db58` |
| `harness_evolution/multidomain/revision_control.py` | `bea3de6852661922e3af2824253d04d7b7c5ef905fcf43bd34b7081a5cbebfe2` |
| `harness_evolution/multidomain/revision_session.py` | `f66d14b39d6c21dc5065e95eeae32adfdc663cecd32e7d33da8b68941e4a1c3d` |
| `harness_evolution/multidomain/era_search.py` | `2aa88f2331984ef9d357f2f7c0d63f3ab285541ff267aa75416bdad2afd26c26` |
| `harness_evolution/multidomain/example_search.py` | `1105def8a5489b6558a0088f9b441a77f8bc7b1fd5b0df83b1280b7c6019e34a` |
| `docs/era_main_search.md` | `afdb02ef36572230007904fe4c789a98888e3a7b5fe6335f2912a8d930cec58a` |
| `docs/plans/p2e_v2_plan.md` | `442b9e5f3350d994b1c60f354ad0837ff90e200a5a974a7c3139e22d668855f9` |

## Formal-exposition pass (2026-09-19, round 23)

SkillOpt's official full text, https://arxiv.org/html/2605.23904v2, §§3.1–3.7, was reread for this author-requested pass.
Its object/measurement/update/gate/deployment progression informs the Method; its textual learning rate, slow/meta update, and empirical findings are not imported.
No bibliography entry or publication-venue field is changed; only verified preprint status is used for this exemplar.

The population objective states the desired agreement of median pointwise scores on a domain's strict-preference distribution.
The estimator is explicitly restricted to complete cohorts; missingness retains the existing coverage/bounds policy.
The acceptance predicate combines strict recorded development gain with existing completeness, comparability, coverage, and stratum guards.
The two update equations summarize best-program acceptance and working-program inheritance; they are not new controller behavior.
The nondecreasing development-score invariant (C45) holds for the recorded measurements used by selection, not an independently remeasured or unseen score.
No convergence, positive expected improvement, causal identification, or automatic semantic-refutation guarantee is claimed.
Detailed progress credits and damage/protection checks remain in the unchanged algorithm contract.

## Independent reviewer corrections (2026-09-19, round 24)

Three reviewer passes are recorded in `reviewer_round1_20260919.md` through `reviewer_round3_20260919.md`; responses are in `reviewer_comments.md`.
The equation now includes finite-repeat execution randomness and equal original-input weighting, with a uniform strict pair within each input.
This reporting target is not silently equated with the native sealed-development proxy: `era_search.partition_train:291–314` selects one canonical pair per input.
Coverage and missing-outcome bounds use predetermined input/pair weights; the complete-execution estimator does not drop failures and call the remainder an unconditional estimate.

The state-order check found a real paper/implementation mismatch.
`example_search.py:1588` passes the pre-update `best.id` into inheritance.
Its completion step updates best and then restores working from the recorded `next_parent_id`, checking against `best_before_id` (`:535–548`).
Thus a candidate can be accepted on development measurements but fail inheritance because local comparisons are unknown.
Equation 6 now returns working to the old `B_t` in that case, and Algorithm 1 saves `B_old` explicitly.
The reviewer verified this branch through both the core function and native `patch_revision.inheritance_decision` with a synthetic record, not a dataset or model call.
This branch correspondence says nothing about the frequency or benefit of continuation.

`revision_session.py:28–86` exposes tools, submit, repair, and pause actions; the agent proposes diagnostics and further work.
`revision_control.py:214–259` enforces common known/complete/comparable prerequisites before inheritance branches.
`patch_revision.py:305–307` makes damage review advisory rather than requiring a separate model review.
Native intermediate checks use per-repeat exact changes; semantic expectations remain unverified.
The manuscript now separates those mechanical conditions from direction allocation and scientific refutation.

The engineering HEAD is still `5814194eb4469e302438b20d6cf368a3d6928cfc`, with pre-existing uncommitted changes.
The following hashes identify files inspected for this reviewer cycle; they supplement, not replace, the earlier snapshot above.
No source edits or empirical execution were performed by this review.

| Source path | SHA-256 at round-24 close |
| --- | --- |
| `harness_evolution/multidomain/revision_control.py` | `bea3de6852661922e3af2824253d04d7b7c5ef905fcf43bd34b7081a5cbebfe2` |
| `harness_evolution/multidomain/example_search.py` | `2616be465314aabd5bb0bc8cf4012e068944f4827c5d89ef7d85cfec7ac5d9c2` |
| `harness_evolution/multidomain/patch_revision.py` | `2d64dc6120e9c4f3a7738e76a0df3814e3a11f0b6dba3ab7b971d760ffa64ce1` |
| `harness_evolution/multidomain/revision_session.py` | `4e53d1620e79e646a3563c534d5ef2098256045b18580538c0a3522680259c17` |
| `harness_evolution/multidomain/era_search.py` | `2c1b95b5247a3a3423901229accd2233b21bdfef05b5cf6ea2874822018b11c8` |
| `harness_evolution/multidomain/intervention_revision.py` | `39cf7b7e0cb247911cf0b2ecb1298929d1e69abf41d651607fbe6ab4d4d77eff` |

## IPM reverse-selection exposition (2026-09-20, round 27)

The author selected Informative Preference Mining (IPM) and requested the Method be argued from reducing low-value repetition rather than presuming disagreement valuable.
The revised opening therefore lowers the priority of comparisons on which existing evaluation signals agree, while treating information value as an empirical question.
The implementation is unchanged: `mining.py:100–285` ranks structural conflicts, breaking ties by pair identifier, with a separately sampled random anchor.
The main text now displays the existing priority equation; it does not introduce a hard filter, entropy estimate, or learned reliability weights.
Within-dimension conflicts use opposing cross-source signals, including when a group has internal conflict; the group-consensus abstention rule applies to dimension aggregation for trade-offs.
Overall--dimension conflict is signal-level opposition, not necessarily a conflict between group consensuses.
Missingness and ties can yield zero priority, so zero priority does not establish agreement or simplicity.
The full human-qualification protocol and matched-human-cost benefit remain unverified.
The repeated-signal margin in `mining_runner.py:147–172` remains the median of same-repeat pair differences, distinct from the evaluator's median-then-compare measurement.

The ERA rewrite preserves the objective, estimator, acceptance and inheritance equations, and the pre-update best fallback.
`revision_control.py:214–265` still requires known, complete, comparable local and development comparisons before inheritance branches.
Direction continuation can retain diagnostic history even when program inheritance fails; diagnostics do not constitute an automatic semantic decision about the direction.
No engineering source, numerical fixture, model execution, annotation, or training is changed.
The three source hashes for `mining.py`, `mining_runner.py`, and `revision_control.py` were rechecked and match the original Source identity table above.
