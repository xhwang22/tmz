# Independent reviewer audit — round 1

Date: 2026-09-19.
Scope: Method, experimental design, conditional Results, and Discussion, cross-checked against Introduction, acquisition, the algorithm/statistics appendices, the claim/figure memory, and the engineering plan.
This is a writing-and-identification audit, not a new experiment or a verification of empirical gains.
No manuscript, implementation, data, bibliography, or figure was edited by this reviewer.

## Overall judgment

The candidate-acceptance versus direction-continuation distinction is a coherent methodological premise.
The draft also correctly distinguishes pointwise scoring from preference feedback, adaptive development from final assessment, and C1 agreement from C2/C3 usefulness.
However, the present formalization is clearest about the ordinary best-candidate gate and least explicit about the allocation decision that constitutes the central contribution.
The experiments name the right comparisons, but several comparison factors and estimands remain too unspecified to support their intended interpretations.
The Discussion is a three-sentence risk checklist rather than an interpretation of the method's conditions of usefulness.
I would request substantial revision of these points before treating the writing as stable.
I would not request more equations merely to make the method appear theoretical.

Empirical claims remain a separate blocker: C27 and C28 are material evidence gaps, not prose defects that a reviewer-editing cycle can close.
The explicit placeholder and simulation disclosures are appropriate and must remain.

## Priority findings

| ID | Severity | Exact current anchors | Issue | Revision type |
| --- | --- | --- | --- | --- |
| R1 | Major | `sections/method.tex:60`, `:78`–`:87`; `sections/appendix.tex:350`, `:393`–`:397`; `sections/introduction.tex:43`–`:48` | The central direction-allocation rule is not operationally stated; inherited candidate state, continued direction, and semantic refutation are still easy to confuse. | Clarify implemented policy and its limits; do not invent a refutation oracle. |
| R2 | Major | `sections/method.tex:69`–`:72`; `sections/appendix.tex:383`–`:389` | Promotion is described as sufficient for inheritance, although the inspected controller first requires known, complete, comparable inheritance evidence. | Correct method/prose precision from existing implementation. |
| R3 | Major | `sections/method.tex:11`–`:30`; `sections/appendix.tex:440`–`:460` | The objective omits execution randomness, and pair-weighted estimation differs from the input-weighted reporting definition. | Define the stochastic target and weighting convention. |
| R4 | Major | `sections/experiments.tex:14`–`:16`, `:48`–`:49`; `sections/results.tex:27`–`:37`; `sections/appendix.tex:737`–`:789` | Comparator names and matched-budget statements do not define executable comparisons or isolate direction continuation. | Supply a compact comparison contract; mark unchosen configurations pending. |
| R5 | Major | `sections/experiments.tex:50`–`:51`; `sections/mining.tex:35`–`:39`; `sections/appendix.tex:791`–`:795` | Equal annotation units are not necessarily equal human effort, and replaying a historical corpus does not measure current annotation time. | Separate label-efficiency and measured human-effort claims. |
| R6 | Major | `sections/discussion.tex:4`–`:6` | Discussion supplies neither the benefit/boundary of depth-first allocation nor interpretation across C1/C2/C3. | Replace the checklist with conditional mechanism synthesis and limitations. |
| R7 | Moderate | `sections/results.tex:10`–`:14`, `:49`–`:59`; `sections/appendix.tex:602`–`:607` | Main displays do not visibly encode all the estimands their captions promise, especially per-arm/per-split regressions. | Clarify table units and companion breakdowns before measurements are inserted. |
| R8 | Moderate | `sections/experiments.tex:4`, `:45`–`:53`; `sections/results.tex:95`–`:108` | The two central scientific hypotheses read as late auxiliary ablations, while the main opening emphasizes only evaluator and downstream quality. | Add a short question-to-comparison map without renumbering C1/C2/C3. |
| R9 | Moderate | `sections/experiments.tex:25`; `sections/appendix.tex:466`–`:483`, `:769`–`:770` | The uncertainty statements do not distinguish a fixed-evaluator comparison from variability of the optimizer itself. | Name the inferential unit for each result; retain unfinished run counts as pending. |

## Detailed recommendations

### R1 — State the implemented direction policy, not just the state-update algebra

The equations distinguish best program B and working program W, which is useful.
But the reader still cannot reconstruct when the current direction receives another attempt, when it is revised from B instead of W, or who decides to pause.
The pseudocode's “Continue the direction with its diagnostics, or pause it” leaves the distinctive operation as an unexpanded instruction.
The no-refutation-oracle caveat at Method line 86 is correct, but it arrives after the Introduction has stated that ERA checks the hypothesis and that contradicting results can end the direction.

Suggested repair:

- Introduce three different outputs once: candidate acceptance updates B; inheritance determines the next editable program W; direction allocation determines whether the next opportunity remains with the same correction problem.
- State which decision is model-proposed and which conditions the controller enforces in the current native patch workflow.
- State that returning W to B need not erase the direction or its diagnostic record.
- Give concrete current stopping categories, such as a proposed pause or actual resource/execution limits, without equating them to scientific refutation.
- Describe falsification as the diagnostic standard motivating this allocation, unless the current implementation actually enforces a semantic refutation decision.
- Do not import compulsory prediction packets or legacy continuation-review fields that the native patch workflow does not require.

This should be possible in a short paragraph and a more explicit pseudocode line, without another theorem.
The score monotonicity sentence can remain as a limited invariant, but it should not occupy the rhetorical role of the theoretical contribution.
The scientific question is whether spending further attempts on a diagnosed direction pays off under equal resources; a monotone stored maximum cannot answer it.

### R2 — Put the shared inheritance eligibility before its three branches

The inspected `revision_control.py` computes `keep = not unknown and (promoted or not damaged or exploratory)`.
Its unknown condition includes missing/comparability failures in local diagnostic evidence and parent/best comparisons, not merely the final development score.
Therefore “Accepted candidates qualify for inheritance” is too unconditional as currently written.
An accepted candidate is not licensed to bypass all inheritance checks merely by satisfying the acceptance predicate.

Suggested repair:

State a common eligibility requirement first, then describe promoted, undamaged, and damaged candidates.
For a damaged unaccepted candidate, retain the distinctions between new root-relative repair, a previously uncredited exact trace-field change, and preserved protection cases.
Do not rename an exact field change as verified semantic progress.
The appendixed operational definitions can carry the detailed unknown/damage cases; the main text needs only enough specificity to make the implication correct.

### R3 — Define what randomness and what observational unit J represents

The displayed probability samples only `(x,y+,y-)` from the domain distribution, but the compared scores are finite-R medians of stochastic model executions.
As written, the target is either conditional on an unstated execution realization or missing an expectation over execution randomness.
Calling the sample expression an estimate of J does not resolve that choice.

There is also a weighting difference.
The Method averages indicators over pairs, while Appendix line 457 says that global agreement first averages within original-input groups.
These coincide only under specific equal-pair-count conditions, and not in general with varying candidate counts, human ties, incomplete ranks, or mixtures of pair-only and ranked data.

Suggested repair:

- Specify that the primary target is overall human preference agreement for a frozen R-repeat scoring procedure.
- Include execution randomness in the target, or explicitly condition on a frozen execution protocol and explain the remaining sampling target.
- State the default reporting estimand as original-input average agreement if that is the intended contract.
- Explain why the development cohort's canonical pair per original input, if used, reduces to the simpler pair average rather than silently implying all reports use that formula.
- Retain completion coverage and missing-outcome bounds separately from statistical confidence intervals.
- State how reused artifact scores induce dependence between pairs; do not imply repeated scores or all pairs are independent tasks.

No new statistical claim is required.
This is a definition/alignment repair, not a request for a convergence theorem.

### R4 — Define comparators by what changes, not only by labels

“Prompt optimization,” “Program search,” and “history-only proposals” name families, not reproducible baselines.
The manuscript cites several methods that do not share one greedy search policy, so a reader cannot safely infer the experimental comparator from the Introduction.
“Best single metric” also needs a selection rule that excludes Test/OOD labels.

The search ablation is especially important.
Independent, history-only, and direction depth-first rows can differ in parent choice, diagnostic history, observation access, candidate construction, number of local probes, and implementation inheritance.
Without stating which factor changes between rows, a positive difference cannot specifically support direction continuation.
Matching proposal opportunities and matching total cost are not equivalent when diagnostics and candidate runtimes vary.

Suggested repair:

- Add an appendix comparison contract giving each row's parent rule, retained information, diagnostic access, editable components, continuation rule, and terminal selection rule.
- Separate named external optimizer implementations from internal controlled allocation ablations.
- Identify the frozen comparator used in the qualitative motivation when it becomes an experimental arm, rather than presenting that observation as evidence about the whole optimizer family.
- Select the best metric and calibrate any ensemble using Train-only information, then freeze them.
- Declare one primary resource-matching rule for Figure 2a; report attempt count, tokens, tool calls, and wall-clock/currency costs as separate measurements.
- If the precise backbone or trainable checkpoint has not been chosen, leave it explicitly pending rather than claiming an already-executable common-base fine-tuning comparison.

This audit does not require all the broad C1 baselines to be frozen during prose revision.
It does require the manuscript to distinguish defined comparisons from names awaiting a concrete implementation.

### R5 — Preserve the difference between annotation-unit efficiency and human-time efficiency

A targeted disagreement group can take longer to judge than a random group, even with the same number of outputs and the same requested H levels.
Counting both as one original-input unit establishes equal query budget, not equal labor cost.
The main experiment currently fixes N_H in units, while Results line 101 speaks of “less human effort.”

Suggested repair:

Use “annotation units” for the primary replay/sample-count comparison and reserve the human-effort statement for a measured annotation-time analysis.
For new annotation, report time, number of raters, adjudication, abstention, and H-level workload alongside units; ideally show the endpoint against both units and time.
For reused preferences, do not invent annotation times or treat historical acquisition as newly incurred labor.
Keep replay label efficiency separate unless original cost records are actually available and comparable.
Charge anchors consistently and state whether the random arm's anchor is simply part of its uniformly sampled budget.
The anchor may qualify signals, but the current human-reliability thresholds and policy remain unverified; this is already correctly disclosed in the appendix and should not be compressed away.

### R6 — Discuss when the method should and should not help

The current Discussion has only three sentences, each listing risks or safeguards.
It does not advance the reader's understanding beyond the experimental protocol.
It also fails to acknowledge the main trade-off of the method: continuation can develop an underimplemented idea, but can also spend scarce resources on a poorly chosen one.

Suggested structure, using conditional language while results are pending:

1. Implementation depth and opportunity cost: continued work is potentially useful when multiple evaluation steps must change together; one-step fixes or clearly contradicted hypotheses may favor broader search.
2. Interpret patterns across experiments: C1 improvement without C2 benefit would show that preference agreement does not ensure actionable critiques; C2 success with C3 failure would be compatible with useful local advice but a reward vulnerable to policy shift or exploitation.
3. Interpret acquisition and evolution together without asserting synergy: better sample selection cannot compensate for an optimizer that does not realize corrections, and more persistent optimization cannot recover preference distinctions missing from its feedback.
4. Limitations: shared evaluator blind spots, adaptive development selection, nonautomatic semantic refutation, and task/policy-specific downstream evidence.

Do not assert these outcomes have occurred.
The purpose is to make the expected contrasts interpretable, not to rehearse another unmeasured positive result.
A compact two-paragraph Discussion can do this; the detailed safety checklist already exists elsewhere.

### R7 — Make table cells correspond to one estimand

Table 2's caption promises regressions for each arm and split, but its body has one “Regressions” column for each domain.
The intended cell could therefore represent ERA, Seed, a difference, an ID/OOD average, or a tuple.
This ambiguity should be fixed while the values are still pending.

Table 1 says domains and feedback-setting breakdowns appear in the appendix, but the appendix currently specifies future reporting rather than supplying a complete pending per-domain results table.
The main table also lacks an explicit equal-domain aggregation definition in its caption, although the appendix asks for equal-domain summaries separately by feedback setting.

Suggested repair:

- Define each Table 2 regression cell as a specific contrast, or use a compact paired-arm/split layout with the full breakdown in a clearly identified companion display.
- State Table 1's aggregation weight, scope, and treatment of pair-only corpora in its caption or a near-table note.
- Do not combine different domain sets across Pair/Top/BoN/Reg without displaying their counts and eligibility rules.
- Keep coverage/missingness visible when real results are inserted; high conditional accuracy alone can mask differential execution failure.

The method claim does not require adding every metric to the nine-page main table.
It requires making the chosen main summaries unambiguous.

### R8 — Give the central tests a visible role in the experimental argument

The main study order C1 → C2 → C3 matches the plan and should remain.
But the present opening “We test evaluator quality and its use in improving generated outputs” omits why the paper's two proposed mechanisms should work.
Acquisition and search comparisons appear only under “Ablation studies,” after a comparatively long C3 design.

Suggested repair:

Add one compact opening sentence stating that C1–C3 test utility, while matched acquisition and search comparisons test how any improvement is obtained.
Name the decisive contrasts explicitly: disagreement versus random at fixed feedback detail and evolution resources; depth-first versus a history-matched restart comparator at fixed feedback and search resources.
Do not rename the study labels or create a fourth downstream claim.
No interaction/synergy claim is currently justified; a factorial acquisition-by-search study would be useful only if such a stronger claim is introduced.

### R9 — Name the inferential unit before promising a 95% interval

Input-group resampling estimates uncertainty over evaluation tasks for a fixed frozen evaluator.
Independent search runs estimate optimizer variability.
The current appendix recognizes the difference, but the main table's intervals and the search table's “grouped intervals over independent searches” do not say which uncertainty is represented or how the two are combined.

Suggested repair:

State whether Table 1 is a fixed-run or across-run result and which unit is paired across methods.
For the search experiment, report independent run counts and between-run summaries separately from within-run input-group intervals, or prespecify a hierarchical analysis.
Do not choose a numeric seed count solely for writing completeness; it remains a design/resource choice.
Keep scoring repeats distinct from independent search replicates.

## Evidence gaps that prose cannot close

| Gap | Existing memory | Consequence | Acceptable disposition now |
| --- | --- | --- | --- |
| Equal-cost acquisition improves the final evaluator. | C27, `status: gap` | Neither a constructed dataset nor disagreement yield establishes the claimed efficiency. | Keep as a hypothesis; retain pending comparison and measured-cost requirement. |
| Depth-first continuation improves sustained unseen agreement. | C28, `status: gap` | A monotone development maximum and motivating trace observation are insufficient. | Keep as a hypothesis; require controlled equal-resource independent searches. |
| The motivating rejected-direction pattern explains limited gains. | C43 supports a bounded qualitative observation only. | The observation cannot identify causality or the attainable value of abandoned directions. | Preserve bounded wording; prepare a permissible public evidence summary only with author authorization. |
| C2/C3 downstream benefits. | Design records and placeholder tables only. | C1 agreement cannot substitute for new blinded judgments on new outputs. | Keep all interpretations conditional; C3 remains unrun. |
| Automatic semantic refutation. | Method audit explicitly records its absence. | The algorithm cannot be described as automatically distinguishing hypothesis failure from implementation failure with verified correctness. | State the diagnostic standard and the implemented control policy separately. |
| Trainable shared-backbone fine-tuning comparison and precise baseline budgets. | Manifest/configurations remain pending. | Feasibility and fairness are not demonstrated by table labels. | Mark the unresolved configuration rather than inventing a baseline implementation. |

## What should survive revision

- The author's abstract, reference inventory, one-sentence-per-source-line rule, and official nine-page template.
- Pointwise deployed evaluation with paired human feedback used outside the scorer.
- A complete program as candidate, a correction direction as the continued-search object.
- Separate B and W state updates, with the limited stored-score invariant.
- Explicit limitations on semantic checks and refutation.
- C1 → C2 → C3 ordering, including fresh shared C2 outputs and own-policy C3 rollouts.
- Existing-corpus mining/replay and missing H levels remaining absent.
- All placeholder and simulation disclosures and the distinction between future ideal analysis and observed results.

## Round-2 acceptance criteria for the writing

The next review should be able to answer these questions from the revised manuscript without guessing implementation behavior:

1. What exactly is optimized, what randomness is averaged, and what is one statistical observation?
2. What conditions update B, what conditions update W, and what keeps the direction active?
3. Which decisions are controller-enforced, model-proposed, or retrospective scientific interpretation?
4. What differs between each central search/acquisition comparator, and what resource is held fixed?
5. What does each main-table cell mean, including regressions and incomplete executions?
6. What result patterns would support the method, limit it, or point to a different explanation?

These writing criteria do not convert the empirical gaps into established claims.
