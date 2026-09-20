# Paper context

Updated: 2026-09-20. Status: method and study design with author-requested,
explicitly simulated quantitative displays; confirmatory results pending.
The introduction includes a bounded qualitative development observation.
The latest author-edited abstract retains ERA's method principle and adds an explicit
hypothesis about alignment and sustained improvement, followed by downstream tests
of output selection, critic-guided refinement, and reward-guided training on
representative tasks. These effects are not reported as verified results.
Its broader wording about existing evolution methods does not extend the scope of that observation.

## Title and scope

**Evolving Evaluation Systems from Human Feedback for Open-Ended Tasks**

The paper currently has no project acronym. ERA names only the depth-first
evaluator evolution method; do not invent an expanded acronym. The author has
retired P2E from the active paper, not from archival history or source filenames.
The historical source-repository name does not restrict the paper to slides.
Do not rename that repository or local source directory.

The complete scope contains 22 domains in four families: structured visual
artifacts; image generation and understanding, including 3D; text generation;
automated research. A domain shares dimensions, priorities, a decision rule, and
a human protocol. A common procedure is instantiated per standard, not deployed
as one universal judge. Panorama inclusion does not imply readiness or results.

## Scientific argument

The central difficulty is aligning automated evaluation with human preferences
on open-ended tasks. Human standards are contextual and involve trade-offs.
A preference records a judgment without fully specifying the criteria and
evidence needed to judge new outputs. Following the source plan's §§1–2.3,
the response is to use preference data to drive an evaluation agent's
self-evolution. The human standard remains the target; its explicit
approximation in the evaluator is what evolves. Do not lead with error-diagnosis
ambiguity as though that were the main problem.

The author approved the revised argument: open-ended evaluation is difficult
because quality depends on task-specific criteria and trade-offs; preferences
provide concrete judgments without specifying an executable evaluation procedure.
Agent evolution is a candidate approach to learning that procedure, with two
connected learning obstacles.
Informative Preference Mining (IPM) lowers the sampling priority of comparisons on which existing signals agree;
depth-first evaluator evolution develops directions beyond an initial
unsuccessful implementation.
The search principle is to separate accepting a candidate from continuing its
direction, rather than assuming immediate gain determines the value of further work.
The paper-level question remains learning an evaluation procedure from human
feedback, not generic feedback efficiency. IPM and evolution address
connected difficulties without claiming a new two-stage theory.
The revised introduction explains rejection/redirection in the tested iterative
optimizer configuration, then motivates continuation through interacting evaluation
steps. A direction specifies an intended improvement; its hypothesis states a
testable prediction, and a candidate is a complete evaluator implementation.
One unsuccessful implementation is insufficient to reject a direction, but can
still be negative evidence. Consensus among signals is not correctness.
Follow `terminology.md`, which supersedes all earlier naming guidance.
Use human feedback consistently as the umbrella term and human preferences only
for preference judgments. Detailed adaptation controls stay in Experiments and
the appendix, with a short alternative-method comparison at the end of the introduction.
Preferences are introduced as a form of human feedback. Disagreement refers to
conflict among existing evaluation signals; diagnostic results refer to search-level
implementation checks, distinct from evidence gathered about an artifact.
The data-mining-to-evolution link is explicit: acquire informative preferences,
then turn the problems they reveal into working evaluation-procedure changes.
The observation of rejection/redirection motivates the explicit design principle
that rejecting a candidate need not end work on its direction. It does not
establish that immediate gain governed the optimizer's continuation decisions.
The research question precedes the literature bridge, and data mining references
follow the allocation rule they support. The two linked steps are introduced
once, without adding a separate feedback-waste theory or expanding the overview.
GEPA, Meta-Harness, and DGM guide the argument structure, not borrowed findings.
The introduction's literature bridge cites AutoCalibrate for feedback-driven
criteria refinement and EvalGen for evaluation-function selection, Agent-as-a-Judge for tool-based
evidence gathering, and active preference learning alongside query-by-committee
for selective data mining. These establish relevant prior capabilities, not ERA
novelty or effectiveness. These sources use verified published records.
Related Work now includes all four author-requested 2026 preprints: query-specific
rubrics, Benchmark2, skill extraction/consumption, and the reward-hacking survey.
They support distinct comparisons, not ERA's effectiveness claims.
The citation audit checks identities, publication fields and cited scope separately.
DGM is updated to ICLR 2026 and RewardBench to Findings of NAACL 2025.
Official proceedings/PDF conflicts are resolved field by field; index matches
never override the primary record without review. See citation_audit.md for
the 40-entry venue inventory, verification dates and remaining limitations.
Parameter-adaptation comparisons remain in the introduction and experiments;
provenance protocols and detailed study-arm/domain lists do not belong in this
abstract. The short simulation notice remains; unverified effects are expressed
as a hypothesis and downstream tests, not reported findings or validated
interpretability. C42 records the framing claim.

The shared question is whether an evaluator can evolve toward a task's human
evaluation standard given that task and its human feedback. Reusing existing
preferences and collecting new preferences are two data-construction settings,
not different algorithms or permanent domain classes. A domain may use both.
Existing H0 is not an admission requirement. Its availability determines the
missing data work, not the algorithm. Label provenance, annotation protocols,
agreement, abstention, and results must be reported separately; newly collected
labels are not inherently more reliable.

The same wrong ordering may arise from missing observations, unused evidence,
or inappropriate interpretation and priorities. Human feedback helps locate
these evaluation gaps and supplies a selection standard; an ordering alone does
not identify its cause. The data mining design inventories domain evaluation knowledge,
freezes signal–dimension mappings, uses a random reliability anchor, separates
three semantic disagreement strata, and supplies available H0–H3 feedback.
The implemented miner supplies structural priorities and source-group records;
human-reliability qualification is a separate, still unverified step.
H1 is central. H0-only settings do not possess uncollected H1/H2.
The feedback table Z connects feedback, artifacts, source signals, routes,
tool output, uncertainty, and cost to ERA.

ERA evolves observation and judgment through (A, K, V, T, Pi, G) with a fixed
base model. Pointwise scoring excludes opponents and labels. Full development
and terminal validation request at least three executions per artifact before
median comparison, with completeness checked separately. The direction is
the unit of continued exploration; the complete program is the unit of selection.
Connected changes implement a direction's proposed correction, not an empirical finding.
Proposal evidence, sealed Train measurement, and allocation are separate.
Working and best programs differ. Diagnostic results for direction continuation, protection guards,
terminal Val, independent Test/OOD, and component attribution remain explicit.
The Method now follows executable evaluation and measurement, error-to-candidate
revision, independent best/working updates, and failure interpretation and freeze.
Default synthesis hides structured specialist scores, ratings, and scales while
retaining findings, reasons, and scopes. Patch sessions require actual edits,
intent, and inspected Train references; expectations and checks are optional.
Program inheritance distinguishes accepted, undamaged, and unaccepted damaged
candidates; the last needs fresh, uncredited progress and preserved protection
cases. Exact recorded-field changes, not semantic claims, can earn such progress.
The controller does not automatically judge a direction unhelpful.
Diagnostic results support further implementation or motivate ending a direction;
pausing or budget exhaustion leaves its value unresolved. Terminal Val never reranks the Train shortlist.
The detailed implementation/exemplar audit is in method_implementation_audit.md.

Parameter adaptation is a substantive alternative. The planned C1 controls add
fixed-structure evaluator fine-tuning and score calibration. An additional
shared-observation comparison freezes (A,T,Pi) and restricts ERA to (K,V,G),
separating changed observations from changed interpretation. Fine-tuning can
learn criteria or tool use under suitable interfaces; the control is not a
general capability claim. Human feedback, development access, and adaptation and
deployment costs are accounted for. ERA's explicit criteria and traces permit
inspection, not an automatic claim of faithful explanation. No advantage over
parameter adaptation is asserted, no tuning results are simulated, and no
training is run. Evaluator tuning is distinct from C3 generator training.

## Hypotheses and studies

IPM may improve final evaluator alignment at equal human
cost; depth-first continuation may produce more sustained gains than restarting
proposals at equal search resources. Both remain unverified (claims C27/C28).
The inspected default pointwise workflow shows rejection, incumbent retention,
and redirection (C43); related themes can recur without continuation of the
rejected implementation. Accepted improvements also occurred.
This observation is not a universal characterization of RSI, an explanation of
all limited gains, or proof that ERA/DFS outperforms alternatives.
Building a preference corpus does not establish sampling
efficiency, which requires a separate matched-budget random-sampling control.
C1 assesses alignment and fixed-pool selection. C2 uses fresh shared initial
outputs and new blinded human rankings. C3 specifies frozen-reward LoRA + GRPO,
with own-policy online rollouts and matched resources; it is design-only.
The three experimental parts are core results, ablations, and analysis.
The External Metric Reserve never enters evolution, critique, reward, or selection.

## Narrative and evidence contract

Use formal paper prose, not debugging or method-version history. Mining and the
C3 research design are in scope, superseding the older draft's exclusions.
Optional teacher branches, historical optimizer names, private records, training
execution, and unmeasured gains remain out of scope.

The September 19 rewrite draws a qualitative motivation from inspected private
development records; `search_observation_audit.md` records its scope and hashes.
No private numerical results, sample IDs, prompts, logs, or generated evaluators
were imported. The source working tree was already dirty and was not modified.
Source documentation supports specifications, not performance or causality.
Use claims.yml and figures.yml for subsequent audits; gap claims are hypotheses,
never findings. Memory claim IDs C1/C2/etc. are a separate namespace from the
paper's study labels C1/C2/C3.

Current structure: 2 main figures, 10 appendix figures, 15 tables, 40 verified
bibliographic identities, and 48 claim records.
Main Figure 2 is the adapted C1 landscape on page 8, alongside the ID/OOD
alignment-and-selection main table. Its original 5.4 × 3.57-inch layout,
family palettes and Source fonts are retained.
The ring is a taxonomy of 22 tasks, the scatter links seed/ERA agreement
and Best-of-4 family means, and all 110 bars share method-complete OOD
cohorts within each domain across the five shown methods.
The new summaries derive only from unchanged existing synthetic input records.
All 3,520 requested inputs are retained in provenance; failed scoring counts
as failed selection. C48 supports only these denominator/arithmetic facts.
The new data and audit are in data/simulated/c1_landscape/.
No new experiment, simulated observation, C2/C3 outcome, or efficacy claim is added.
The budget placeholder is appendix Figure 4 and downstream placeholders are
Table 8; main-text interpretations remain conditional.
The main text remains nine pages using unchanged ICLR typography.

The historical landscape remains unchanged as appendix Figure 5.
Its 2,880 OOD inputs are selected by fixed hash, 720 per family, and differ
from the full-cohort main Figure 2. Figure 6 retains full-cohort paired
ID/OOD effects, Figure 10 component detail, and Figure 11 C2.
The subset exports and audit remain in data/simulated/landscape/README.md.
Annotation, component, and C2 diagnostics retain their eight-domain scope.
C1 tables, selection, and cost profiles now use 11 domains per setting.

Three isolated candidates follow the author's reference images and their
labeled HEX values. Use their five colors as coordinated ensembles, not only
as opposing pairs. The provisional reference-1 method mapping is static judge
blue #74A9C5, static tools/seed mint #C2E5CF, prompt optimization cream #EDDDAB,
program search peach #F2B8AE, and ERA rose #DD7389. Metric-only references stay
neutral. Family, H-level, policy, rank, and outcome plots have their own explicit
legends; settings use position, labels, or hatching where color has another role.
The component heatmap spans all five colors with cream at zero and fixed ±6
limits. All five data mining policies retain equal-width lines and individual
percentile bands. Reference 2 supplies a cool-to-warm alternative; reference 3
supplies teal/apricot. No final palette choice is assumed.

Neutral ink and dark numerals preserve the source fills. Density fills use
88% source color; darker companions serve fine strokes and small diagram
labels only. Charts use TeX Gyre Heros on native 5.4-inch canvases; the diagrams
use scoped Helvetica-compatible typography. GPT Image 2 supplies only the
existing disclosed overview photograph; this pass makes no model/image calls.
`visual_references.md` retains inspected paper versions and design choices.
The old eight C1 cohorts' group records, summaries, and exported intervals,
and all seven diagnostic-only CSVs, are preserved. Fourteen C1 cohorts are
added for complete layout coverage, not to report completed experiments.
Aggregate C1 tables, selection, and cost summaries consequently change.

Candidate previews stay under `build/reference-palettes/`. Each uses the
same 14 CSVs and numerical table as the canonical assets, with identical
scales and geometry. Checks cover 110 atlas values, 22 paired intervals, and
29 small-text/background contrast pairs per candidate. Source boards,
vector PDFs, and grayscale proofs remain local review materials; original
reference JPEGs are not redistributed. The historical main-figures preview
filename now contains the main atlas plus an appendix diagnostic proof.
Figure/caption/claim links are synchronized.
The September 19 pass rewrites the abstract and introduction, aligns the method's
depth-first terminology, and preserves the title and empirical-gap status.
Revised manuscript prose and captions use one sentence per source
line, with blank lines only between paragraphs; PDF wrapping remains automatic.
The main overview now uses scoped TeX Gyre Heros, regular-weight action labels,
consistent card insets, and correctly scaled pictograms on the same native
canvas. Its caption now makes existing-dataset mining and the two search decisions explicit. Qualified framework
name proposals and the limits of their collision checks are recorded in
`naming_candidates.md`; none has been adopted in the manuscript.

## Simulation contract

`scripts/render_simulated_results.py` generates 14 CSV files, eight vector PDFs,
a numerical TeX table, and `data/simulated/manifest.json`. Every data row is
marked SIMULATED; charts, captions, the title page, and PDF metadata disclose the
status. The fixtures do not execute ERA, use actual labels, estimate expected
performance, establish method rankings, or simulate C3 or evaluator tuning.
`c1_cohorts.csv` covers all 22 domains (11 per setting); `cohorts.csv` retains
the eight diagnostic cohorts (four per setting). These assignments do not
assert real label availability. Construction settings are not domain identities.

`scripts/check_simulated_results.py` checks provenance, hashes, arithmetic,
paired denominators, coverage, annotation outcomes, and the evidence boundary.
C1 table means use method-complete groups; paired effects use joint completeness;
selected-rank shares retain every input, including failed scoring. C37/C38 support
only fixture provenance and arithmetic, never effectiveness. The submission
gate intentionally fails until simulated displays are replaced by authorized
measurements and all associated claims are audited.

## Remaining author decisions

Freeze execution scope, data permissions, available human feedback, models, budgets,
contrasts, human protocols, analysis, authorship, and disclosures.
Add empirical outputs only from authorized source-traceable measurements.

## Current plan-aligned revision (round 23)

C1 is broad across ready domains; C2 prioritizes SV4, IG1, and TG1; C3 prioritizes IG1 with SV2 as a second candidate and TG4 as a control.
C3 requires target-policy reward diagnostics and remains design-only.
Existing datasets supply mining candidates as well as reusable labels; acquisition replay hides unselected human labels.
The appendices now run from foundations through adaptation, detailed core reporting, C3, ablations, analysis, simulation fixtures, and the experiment manifest.

SkillOpt §§3.1–3.7 supply an exposition model: define the optimized object and score, then state updates and deployment boundaries.
The Method adds a population preference-alignment target, its complete-cohort estimator, an acceptance predicate, and independent best/working updates.
C45 records only the nondecreasing recorded-development-score invariant; no generalization, convergence, or automated-refutation theorem is asserted.
Implementation contracts stay in the algorithm appendix.
The working abstract and all bibliography entries are preserved.

Final verification: 9 main-text pages, 34 PDF pages; `make check` passes structural,
memory, simulation, landscape, and whitespace checks.
The main pages and appendix contact sheets were visually reviewed; the C3 result
paragraph stays together on page 8 and the budget figure starts page 9.
The submission guard still exits with code 2 because simulated fixtures remain.
The landscape manifest updates only its display ID and the checker hash after
wording changes; numerical data and figure-asset hashes are unchanged.
No commit or push was performed in this round.

## Independent reviewer revision (round 24)

The author requested a reviewer subagent and repeated iteration on Method, Experiments, Results, and Discussion.
Three passes are complete; `reviewer_comments.md` maps every first- and second-round issue to a manuscript change and the third-round disposition.
The reviewer found no remaining writing/definition blocker in those sections, not unconditional acceptance of the paper.

The method now uses an input-weighted stochastic objective and distinguishes the native canonical-pair development proxy.
Best acceptance, working-state inheritance, and direction allocation have distinct rules.
Failed inheritance returns to the pre-update best even when the candidate updates best; the equation, pseudocode, and implementation now agree.
Agent-proposed actions and controller eligibility are separated from semantic refutation.

Experiments define the history-only control, the combined allocation/inheritance contrast, and frozen-price model-and-tool search budgets.
Label efficiency is separated from measured human-time efficiency, and fixed-evaluator uncertainty from independent-search variability.
Main tables specify equal-domain aggregation, eligible cohorts, and ID/OOD regression contrasts.
Discussion interprets opportunity cost, alternative explanations, and the distinct C1/C2/C3 requirements instead of repeating a risk checklist.

Final checks: 9 main-text pages, 35 total PDF pages; `make check` passes.
Main and appendix layouts were visually checked; source prose retains one sentence per line where revised.
Claims and captions are synchronized (47 claims, 11 figures, 15 tables).
C27/C28, downstream benefits, and exact executable comparator configurations remain unresolved evidence/design requirements.
The submission guard still rejects the simulated draft.
The author-edited Abstract and all 40 bibliography entries were preserved, not re-certified by this focused review.
No experiments, training, engineering-source edits, new image generation, commit, or push occurred.


## Main-text landscape restoration (round 25)

The author explicitly requests the attractive landscape layout in the main text.
Figure 2 now uses full-cohort C1 agreement and selection instead of the old balanced-subset cost illustration.
The original figure and every original numerical record remain intact.
The independent checker covers 110 bars and intervals, eight family points, complete/all-input denominators, geometry, hashes, fonts, and visible disclosures.
The paper has 9 main pages and 36 total pages; no template scaling or body-font change was needed.
C27/C28 remain empirical gaps; C3 is not run or simulated.
No abstract, Method, bibliography, engineering-source, commit, or push change is part of this task.

## Whole-manuscript terminology consistency (round 26)

`terminology.md` is the current naming authority and supersedes conflicting terminology in earlier rounds above.
Round 26 used disagreement-based data mining; the current name is Informative Preference Mining (IPM), including mining existing datasets and reusing compatible preferences.
ERA remains depth-first evaluator evolution.
Keep candidate acceptance, program inheritance, and direction continuation distinct; use best program and working program for B and W.
Reserve candidate for a proposed evaluation program and use output for an artifact being evaluated; preference sign does not mean an evolution direction.
Human feedback, human preferences, evaluation procedure, evaluation program, diagnostic results, artifact evidence, and feedback table Z retain their separate definitions.
`make check` now includes an active-TeX terminology regression check that preserves legacy paths and citation identifiers.
The author-edited abstract, 40 references, numerical records, and both landscape assets are unchanged; C27/C28 remain gaps.
The manuscript remains 9 main pages and 36 total pages. No experiments, engineering changes, commit, or push occur in this round.

## IPM and Method argument (round 27)

The upstream method is Informative Preference Mining (IPM), not disagreement-based data mining.
Lead with lowering the relative sampling priority of repeated comparisons on which existing signals agree, then define comparable signs and the implemented structural priority.
The score is twice the count of within-dimension conflicts plus overall--dimension conflicts plus a cross-dimensional trade-off indicator.
It estimates neither information gain nor human reliability; zero conflict may reflect ties or missingness, and consensus can hide shared errors.
The random anchor is selected before ranking and charged to the same budget, with human qualification still separate from the implemented ranking.
Existing datasets and new outputs supply the same feedback table through compatible preference reuse or missing-label annotation.
ERA proceeds through objective/measurement, directions/candidates, acceptance/inheritance, and direction continuation.
Preserve the pre-update best-program fallback and all inheritance prerequisites; direction continuation can use retained diagnostics even when the rejected candidate cannot be inherited.
The author-edited abstract, citations, empirical gaps, numerical assets, and landscape layouts are unchanged.
