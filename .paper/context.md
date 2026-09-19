# Paper context

Updated: 2026-09-19. Status: method and study design with author-requested,
explicitly simulated quantitative displays; confirmatory results pending.
The abstract/introduction include a bounded qualitative development observation.

## Title and scope

**Evolving Evaluation Systems from Human Feedback for Open-Ended Tasks**

The paper currently has no project acronym. ERA names only the evidence-guided
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

The author approved the revised argument: alignment difficulty, the gap between
preference feedback and an executable evaluation procedure, why agent evolution
is a useful candidate approach, then two connected learning obstacles.
Acquisition reduces annotation of easy comparisons and recurring patterns;
falsification-guided depth-first evolution develops directions beyond an initial
unsuccessful implementation.
The search principle is to separate accepting a candidate from continuing its
direction, rather than assuming immediate gain determines the value of further work.
The paper-level question remains learning an evaluation procedure from human
feedback, not generic feedback efficiency. Acquisition and evolution address
connected difficulties without claiming a new two-stage theory.
The revised introduction explains rejection/redirection in the tested iterative
optimizer configuration, then motivates continuation through interacting evaluation
steps. A direction specifies an intended improvement; its hypothesis states a
testable prediction, and a candidate is a complete evaluator implementation.
One unsuccessful implementation is insufficient to reject a direction, but can
still be negative evidence. Consensus among signals is not correctness.
Use human feedback consistently as the umbrella term and human preferences only
for preference judgments. Detailed adaptation controls stay in Experiments and
the appendix, with a short alternative-method comparison at the end of the introduction.
GEPA, Meta-Harness, and DGM guide the argument structure, not borrowed findings.
Parameter-adaptation comparisons remain in the introduction and experiments;
provenance protocols and detailed study-arm/domain lists do not belong in this
abstract. The short simulation notice remains, without inventing a results
sentence or implying validated interpretability. C42 records the framing claim.

The shared question is whether an evaluator can evolve toward a task's human
evaluation standard given that task and its human feedback. Reusing existing
preferences and collecting new preferences are two data-construction settings,
not different algorithms or permanent domain classes. A domain may use both.
Existing H0 is not an admission requirement. Its availability determines the
missing data work, not the algorithm. Label provenance, annotation protocols,
agreement, abstention, and results must be reported separately; newly collected
labels are not inherently more reliable.

The same wrong ordering may arise from missing observations, unused evidence,
or inappropriate interpretation and priorities. Human evidence helps locate
these evaluation gaps and supplies a selection standard; an ordering alone does
not identify its cause. The acquisition procedure inventories domain evaluation knowledge,
freezes signal–dimension mappings, uses a random reliability anchor, separates
three semantic disagreement strata, and acquires structured H0–H3.
H1 is central. H0-only instantiations do not possess uncollected H1/H2.
The evidence table Z connects feedback, artifacts, source signals, routes,
tool output, uncertainty, and cost to ERA.

ERA evolves observation and judgment through (A, K, V, T, Pi, G) with a fixed
base model. Pointwise scoring excludes opponents and labels. At least three
complete scores per artifact precede the median comparison. The hypothesis is
the unit of exploration; the complete program is the unit of selection.
Connected changes instantiate a mechanism hypothesis, not an empirical finding.
Proposal evidence, sealed Train measurement, and allocation are separate.
Working and best programs differ. Evidence-bound continuation, protection guards,
terminal Val, independent Test/OOD, and component attribution remain explicit.

Parameter adaptation is a substantive alternative. The planned C1 controls add
fixed-structure evaluator fine-tuning and score calibration. An additional
shared-observation comparison freezes (A,T,Pi) and restricts ERA to (K,V,G),
separating changed observations from changed interpretation. Fine-tuning can
learn criteria or tool use under suitable interfaces; the control is not a
general capability claim. Supervision, development access, and adaptation and
deployment costs are accounted for. ERA's explicit criteria and traces permit
inspection, not an automatic claim of faithful explanation. No advantage over
parameter adaptation is asserted, no tuning results are simulated, and no
training is run. Evaluator tuning is distinct from C3 generator training.

## Hypotheses and studies

Disagreement acquisition may improve final evaluator alignment at equal human
cost; depth-first continuation may produce more sustained gains than restarting
proposals at equal search resources. Both remain unverified (claims C27/C28).
The inspected default pointwise workflow shows rejection, incumbent retention,
and redirection (C43); related themes can recur without continuation of the
rejected implementation. Accepted improvements also occurred.
This observation is not a universal characterization of RSI, an explanation of
all limited gains, or proof that ERA/DFS outperforms alternatives.
Building a preference corpus does not establish acquisition
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

Current structure: 2 main figures, 8 appendix figures, 12 tables, 33 verified
bibliographic identities, and 44 claim records. The overview and pointwise
runtime remain conceptual; eight figures and Table 10 use simulated reporting
fixtures. The complete PDF is 30 pages; the main text remains within 9 pages.
Official ICLR body fonts, margins, and heading rules are unchanged.

Main Figure 2 is now the approved v20 landscape composite: balanced task ring,
cost/agreement scatter and four family bar panels in one row, covering all 22
tasks. Its 2,880 OOD inputs are selected by fixed hash without reading outcomes,
with 720 per family. Statistics are recomputed on this synthetic subset, not
copied from the full-cohort appendix. Filled/open marks indicate illustrative
reused/new feedback, not label readiness. Pale family ramps subordinate the
baselines to ERA's common lake-green accent; Source Sans 3 and Source Serif 4
are embedded. C44 records only the allocation. The old atlas stays archived.
Appendix Figure 4 retains full-cohort paired ID/OOD effects, Figure 8 component
detail, and Figure 9 C2. The subset exports, vector assets and independent
bootstrap/coordinate audit are documented in data/simulated/landscape/README.md.
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
limits. All five acquisition policies retain equal-width lines and individual
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
Revised abstract/introduction prose and captions use one sentence per source
line, with blank lines only between paragraphs; PDF wrapping remains automatic.
The main overview now uses scoped TeX Gyre Heros, regular-weight action labels,
consistent card insets, and correctly scaled pictograms on the same native
canvas. Its caption and scientific content are unchanged. Qualified framework
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

Freeze execution scope, data permissions, real supervision, models, budgets,
contrasts, human protocols, analysis, authorship, and disclosures.
Add empirical outputs only from authorized source-traceable measurements.
