# Research plan-to-manuscript coverage

Revision basis: `docs/plans/p2e_v2_plan.md` in the source project, especially
sections 1–5; current ERA execution semantics additionally follow
`docs/era_algorithm.md`. This is a coverage map, not an implementation or result
completion claim. No private results are imported.

| Research requirement | Manuscript destination | Visual destination | Evidence boundary |
| --- | --- | --- | --- |
| Open-ended generation with an existing evaluation ecosystem (§§1–2) | Introduction; problem formulation | Fig1 overview | Scope, not universal applicability or existing labels |
| Human-preference alignment and executable evaluation standards (§§1–2.3) | Abstract; introduction; discussion | Fig1 feedback-to-evolution structure | Motivation and research question, not an achieved faithful representation of preferences |
| Parameter adaptation versus program evolution (§2.2; author clarification) | Introduction; C1; adaptation appendix | Tab7 adaptation choices | Fixed-interface restriction is not a general limit of tuning; no training or comparative result |
| Four domain families and all 22 standards (§2.4) | Problem; full domain appendix | Fig1 artifact gallery, Tab3 taxonomy, Figs4/5 all-domain C1 | Planned scope and complete synthetic coverage, not 22 completed experiments |
| Evaluation standard defines a domain (§2.4) | Problem; domain appendix | Tab3 criteria; Figs4/5 all 22 rows; Figs7/9/10 diagnostic rows | Shared procedure, not one universal scorer; eight-domain diagnostics do not stand for full coverage |
| Semantic space and versioned evaluation knowledge (§3.1) | Preference mining | Tab5 readiness audit | Mappings fixed before labels |
| Existing tools and independent metric reserve (§3.1) | Mining; data appendix | Tab6 information-access table | Reserved endpoints never enter evolution |
| Existing H0 is not an admission prerequisite (§3.2 patch) | Introduction; problem; mining | Fig1 two feedback routes; Tab4 provenance | Missing labels define data work, not the algorithm |
| Reused/new feedback are construction settings (§3.2 patch) | Mining; experiments; discussion | Separate columns/rows in quantitative displays; Tab4 | A domain may use both; not permanent domain categories |
| Direct/derived/material-only/new human data (§3.2) | Mining; annotation appendix | Tab4 provenance | Inputs alone are not human judgments |
| Agreement, abstention, independent new labels (§3.2 patch) | Annotation protocol; quantitative-display discussion | Fig7 three-denominator audit | Simulated raters provide no reliability evidence; new labels are not presumed better |
| H0/H1/H2/H3 (§3.3) | Problem; mining; annotation appendix | Fig1 evidence interface; Tab4; Fig9b fixture | Human dimensions are not inferred from H0 |
| Many-to-many mapping and shared signals (§3.4) | Mining | Tab5 source-independence requirements | Shared/mixed scores do not become independent votes |
| Same-dimension, overall–dimension and trade-off strata (§3.4) | Mining | Tab5 semantic readiness | Different constructs are not scorer contradictions |
| Random anchor, source dependence and readiness (§3.4) | Mining; annotation appendix | Fig6 matched-budget fixture; Tab5 | Sampling benefit remains a hypothesis |
| Adaptation evidence table Z (§3.5) | Mining | Fig1 common evidence interface | Human labels are proposal-only |
| Six-component executable program (§4.1) | ERA method | Fig3 runtime architecture | Fixed base model; illustrative artifact |
| Direction versus implementation; continuation (§4.2) | ERA method; algorithm appendix | Fig1 cycle; Tab11 search-allocation controls | Hypothesis is exploration unit, program is selection unit; utility unmeasured |
| EXHAUSTED, PAUSED and REFUTED (§§4.2,4.5) | ERA method; algorithm appendix | Algorithm1 outcome branches | Failure or nonsignificance is not refutation |
| Atomic edits and connected mechanism candidates (§4.3) | ERA method | Tab11 attribution design; Fig9a fixture | Bundle gain is not per-edit attribution; simulated contrasts are not causal evidence |
| Development, confirmation and component attribution (§4.4) | ERA; experimental design | Tab6 access; Tab11 ablations | Adaptive development is not test evidence |
| C1 alignment and fixed-pool selection (§5.1.2) | Core results design | Tab14, Figs4/5/8 simulated displays covering 22 domains | Pair-only data cannot support Best-of-N; denominator rules remain explicit |
| C2 fresh shared start and new blinded H (§5.1.3) | Core results design | Fig10 eight-domain diagnostic fixture; Tab2 empirical status | Fresh endpoints need new judgments in both construction settings; C2 inputs are distinct from C1 |
| C3 frozen rewards and LoRA+GRPO (§5.1.4) | Core results design; training appendix | Fig1d; Tabs10/2 | Planned only; no training authorized, run, or simulated |
| Corpus construction versus acquisition efficiency (§3.2 patch, §5.2) | Experiments; quantitative-display discussion | Fig6 random-controlled budget curves | New data alone do not establish sampling efficiency |
| Editable components, allocation and H granularity (§5.2) | Ablation studies | Tab11 controls; Fig9 fixture | Equal evidence/budgets; paired H comparison also accounts for human time |
| Trajectories, failure regimes, H efficiency and adapter fidelity (§5.3) | Analysis and studies | Tab8 reporting; Fig11 cost fixture | Observations required; assigned costs and schematic trajectories prove no efficiency |

The older draft's exclusions of upstream mining and the C3 research design are
superseded by this revision. Historical optimizer modes and debugging history
remain excluded from the scientific narrative.

The author's quantitative-display request changes the presentation, not the
evidence status. Seven redundant conceptual callouts were retired in favor of
eight active simulated charts. The main displays now prioritize C1 alignment/selection, downstream human outcomes, and two budget comparisons.
The approved 22-domain landscape and all other numerical illustrations are in the simulation appendix.
The retired diagrams remain editable archives.
All plan items above remain covered in text/tables. Toy effects, labels, cohort
assignments, and uncertainty must not be interpreted as plan execution.

## September 19 display update

The historical main atlas was replaced by the approved landscape composite with all 22 tasks:
ring composition, cost/agreement scatter, and four family bar panels. Its 2,880
synthetic OOD inputs are balanced by fixed hash to 720 per family. Full-cohort
paired ID/OOD effects remain in appendix Fig5. This is a layout allocation,
not changed domain scope, measured data readiness, or an effectiveness result.

## Current §5 organization (round 23)

| Plan requirement | Current placement | Evidence boundary |
| --- | --- | --- |
| Broad C1 alignment and selection | Main Table 1; detailed core appendix | Common cohorts, ID/OOD, per-domain and feedback-origin breakdowns; pair-only corpora cannot support selection |
| Focused C2 refinement | Main Table 2; detailed core appendix | Fresh shared y0, matched critics/revision, new blinded judgments and regressions |
| Representative-task C3 | Main Table 2; training appendix | IG1 priority, SV2 candidate, TG4 control; preflight, own rollouts, frozen rewards; no training executed |
| External outcomes | Table 9 | No pooling unrelated metrics; human and reserved external judgments remain separate |
| Equal-budget search and acquisition | Main Figure 2; Table 12 | Blank placeholders, no curves; all costs counted, existing-corpus labels hidden until selected |
| Mechanism, feedback, fidelity, efficiency | Analysis appendix | Evidence chains and paired interventions, not implicit causal credit |
| Simulated layouts | Appendix Figure 4 and following figures; Table 14 | Unchanged artificial fixtures, never observed or forecast results |

The Results section uses conditional ideal-result analysis; Discussion and Conclusion retain the unverified status.
