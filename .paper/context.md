# Paper context

Updated: 2026-09-16. Status: method and study design; empirical results pending.

## Title and scope

**P2E: Evolving Evaluation Systems for Open-Ended Generation**

P2E means Preference-Guided Evaluator Evolution, the broader research project.
ERA names the evidence-guided evaluator evolution method within P2E; do not
invent an expanded acronym. The historical source-repository name does not
restrict the paper to slides. Do not rename that repository or local source directory.

The complete scope contains 22 domains in four families: structured visual
artifacts; image generation and understanding, including 3D; text generation;
automated research. A domain shares dimensions, priorities, a decision rule, and
a human protocol. A common procedure is instantiated per standard, not deployed
as one universal judge. Panorama inclusion does not imply readiness or results.

## Scientific argument

The same wrong ordering may arise from missing observations, unused evidence,
or inappropriate interpretation and priorities. Human evidence helps locate
these evaluation gaps and supplies a selection standard; an ordering alone does
not identify its cause. P2E inventories domain evaluation knowledge,
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

## Hypotheses and studies

Disagreement acquisition may improve annotation efficiency; coordinated evolution
may address observation/routing/interpretation failures. Both remain unverified.
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

Current structure: 5 main figures, 4 appendix figures, 10 tables, 33 verified
bibliographic identities. Figure 6 expands the four families into representative
tasks and their distinct quality criteria; Figure 7 gives one feedback example
per family. Figures are conceptual; matrices and annotation examples are
explicitly synthetic. The ICLR main-text limit remains 9 pages.

The author-selected five-color palette is blue #74A9C5, mint #C2E5CF, cream
#EDDDAB, peach #F2B8AE, and rose #DD7389. Figures use pale rounded groups, original
outlined pictograms, curved flows, and dark readable labels. The requested
post-training/safety surveys, Speculative RAG, and MMMR inform the visual
language; `visual_references.md` records the inspected versions and panels.

## Remaining author decisions

Freeze execution scope, data permissions, real supervision, models, budgets,
contrasts, human protocols, analysis, authorship, and disclosures.
Add empirical outputs only from authorized source-traceable measurements.
