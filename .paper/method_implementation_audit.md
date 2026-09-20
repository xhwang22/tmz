# Method rewrite: exemplars and implementation

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
