# Paper context

Updated: 2026-09-16. Status: method-and-protocol skeleton, not an empirical report.

## Scope and audience

Working title: **Learning to Evaluate Structured Artifacts from Human Preferences**.
Audience: ICLR readers interested in model-based evaluation, preference learning,
and optimization of language-model programs.

Research project: **Preference-Guided Evaluator Evolution**. ERA is only the
revision method, not the project name. The source repository retains its
historical Auto-Evolve-Harness-for-Slide-Evaluation name; do not mistake that
path for the research scope or rename the repository without authorization.
The project concerns learning evaluators under different evaluation standards.
Slides, webpages and other structured artifacts are candidate applications,
not a slide-only task followed by assumed transfer. Reuse of the revision method
does not imply that one learned scorer works across all domains; a shared
artifact format alone does not define a shared evaluation standard.

Central question: can overall human preferences guide useful revisions to how an
executable evaluator obtains evidence, applies criteria, and synthesizes quality?
The working hypothesis is that program revision can address some errors left by
prompt-only adaptation. This is not yet a demonstrated conclusion.

## Narrative contract

Follow a conventional paper argument: motivation, related work, formulation,
method, controlled evaluation, results, limitations. Do not narrate debugging,
historical search runs, abandoned variants, infrastructure repairs, or successive
internal algorithm versions. Implementation history is not a contribution.

Main method: pointwise evaluator; six editable components; evidence-guided
revision; separate proposal, measurement and allocation; protected data boundaries.
Numerical versus semantic synthesis is an explicit method choice and comparison.

Out of scope for this draft: optional teacher-annotation branches, upstream
disagreement mining, internal study names, historical optimizer variants,
parameter-training experiments, and claims about arbitrary multi-agent systems.

## Evidence status

Public method documentation and selected implementation modules support the
method description. They do not demonstrate performance, generalization,
causality, or sample efficiency. No experiment results were imported.

The source working tree contained pre-existing uncommitted changes. Source HEAD
alone is therefore not a complete snapshot of the method consulted.
See `source_provenance.md` and `claim_evidence_ledger.md`.

## Next author decisions

Freeze datasets, permissions, supervision, models, budgets, comparison interfaces,
primary contrasts, annotation procedures and final author information.
Replace result placeholders only with permitted, source-traceable measurements.
After the draft and figures stabilize, a paper-memory-builder pass can promote
the lightweight ledger to `.paper/claims.yml` and `.paper/figures.yml`.
