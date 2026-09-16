# Paper context

Updated: 2026-09-16. Status: method and study design with author-requested,
explicitly simulated quantitative displays; empirical results pending.

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

The author approved the abstract's argument before this rewrite: alignment
difficulty, the gap between preference feedback and an executable evaluation
procedure, feedback-driven agent evolution, and cross-task validation. Structured
acquisition and coordinated changes are supporting method mechanisms.
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

Disagreement acquisition may improve annotation efficiency; coordinated evolution
may address observation/routing/interpretation failures. Both remain unverified
(claims C27/C28). Building a preference corpus does not establish acquisition
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

No empirical results, sample IDs, logs, or generated evaluators were imported.
The source working tree was already dirty and was not modified.
Source documentation supports specifications, not performance or causality.
Use claims.yml and figures.yml for subsequent audits; gap claims are hypotheses,
never findings. Memory claim IDs C1/C2/etc. are a separate namespace from the
paper's study labels C1/C2/C3.

Current structure: 3 main figures, 6 appendix figures, 12 tables, 33 verified
bibliographic identities, and 42 claim records. The overview and pointwise
runtime remain conceptual; seven figures and Table 1 use simulated reporting
fixtures. Figure 1 and the complete domain table preserve four-family diversity.
The ICLR main-text limit remains 9 pages; official body typography is unchanged.

The three author color references inform an ocean/sea-glass/sand/coral palette:
blue #376795, sky #7BC0CD, teal #51999F, mint #BFDFD2, sand #DBCB92, cream #FFE6B7,
peach #ECB66C, and coral #ED8D5A. Charts use TeX Gyre Heros at 7–8.5 pt on a native
5.4-inch canvas; the two diagrams use scoped Helvetica-compatible typography.
Native vector plots carry the quantitative encodings. GPT Image 2 supplies only
the existing, disclosed overview photograph; this round makes no image calls.
`visual_references.md` retains inspected paper versions and design choices.

## Simulation contract

`scripts/render_simulated_results.py` generates 13 CSV files, seven vector PDFs,
a numerical TeX table, and `data/simulated/manifest.json`. Every data row is
marked SIMULATED; charts, captions, the title page, and PDF metadata disclose the
status. The fixtures do not execute ERA, use actual labels, estimate expected
performance, establish method rankings, or simulate C3. Toy assignments cover
eight illustrative cohorts across both settings; they do not assert real label
availability. The full scientific scope remains 22 domains.

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
