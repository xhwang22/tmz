# Research plan-to-manuscript coverage

Revision basis: `docs/plans/p2e_v2_plan.md` in the source project, especially
sections 1–5; current ERA execution semantics additionally follow
`docs/era_algorithm.md`. This is a coverage map, not an implementation or result
completion claim. No private results are imported.

| Research requirement | Manuscript destination | Visual destination | Evidence boundary |
| --- | --- | --- | --- |
| Open-ended generation with an existing evaluation ecosystem (§§1–2) | Introduction; problem formulation | Fig1 overview | Scope, not universal applicability or existing labels |
| Human-preference alignment and executable evaluation standards (§§1–2.3) | Abstract; introduction; discussion | Fig1 feedback-to-evolution structure | Motivation and research question, not an achieved faithful representation of preferences |
| Parameter adaptation versus program evolution (§2.2; author clarification) | Introduction; C1; adaptation appendix | Tab12 adaptation choices | Fixed-interface restriction is not a general limit of tuning; no training or comparative result |
| Four domain families and all 22 standards (§2.4) | Problem; full domain appendix | Fig1 artifact gallery, Tab1 taxonomy, Figs2/4 all-domain C1 | Planned scope and complete synthetic coverage, not 22 completed experiments |
| Evaluation standard defines a domain (§2.4) | Problem; domain appendix | Tab1 criteria; Figs2/4 all 22 rows; Figs6/8/9 diagnostic rows | Shared procedure, not one universal scorer; eight-domain diagnostics do not stand for full coverage |
| Semantic space and versioned evaluation knowledge (§3.1) | Preference mining | Tab3 readiness audit | Mappings fixed before labels |
| Existing tools and independent metric reserve (§3.1) | Mining; data appendix | Tab4 information-access table | Reserved endpoints never enter evolution |
| Existing H0 is not an admission prerequisite (§3.2 patch) | Introduction; problem; mining | Fig1 two feedback routes; Tab2 provenance | Missing labels define data work, not the algorithm |
| Reused/new feedback are construction settings (§3.2 patch) | Mining; experiments; discussion | Separate columns/rows in quantitative displays; Tab2 | A domain may use both; not permanent domain categories |
| Direct/derived/material-only/new human data (§3.2) | Mining; annotation appendix | Tab2 provenance | Inputs alone are not human judgments |
| Agreement, abstention, independent new labels (§3.2 patch) | Annotation protocol; quantitative-display discussion | Fig6 three-denominator audit | Simulated raters provide no reliability evidence; new labels are not presumed better |
| H0/H1/H2/H3 (§3.3) | Problem; mining; annotation appendix | Fig1 evidence interface; Tab2; Fig8b fixture | Human dimensions are not inferred from H0 |
| Many-to-many mapping and shared signals (§3.4) | Mining | Tab3 source-independence requirements | Shared/mixed scores do not become independent votes |
| Same-dimension, overall–dimension and trade-off strata (§3.4) | Mining | Tab3 semantic readiness | Different constructs are not scorer contradictions |
| Random anchor, source dependence and readiness (§3.4) | Mining; annotation appendix | Fig5 matched-budget fixture; Tab3 | Sampling benefit remains a hypothesis |
| Adaptation evidence table Z (§3.5) | Mining | Fig1 common evidence interface | Human labels are proposal-only |
| Six-component executable program (§4.1) | ERA method | Fig3 runtime architecture | Fixed base model; illustrative artifact |
| Direction versus implementation; continuation (§4.2) | ERA method; algorithm appendix | Fig1 cycle; Tab5 search-allocation controls | Hypothesis is exploration unit, program is selection unit; utility unmeasured |
| EXHAUSTED, PAUSED and REFUTED (§§4.2,4.5) | ERA method; algorithm appendix | Algorithm1 outcome branches | Failure or nonsignificance is not refutation |
| Atomic edits and connected mechanism candidates (§4.3) | ERA method | Tab5 attribution design; Fig8a fixture | Bundle gain is not per-edit attribution; simulated contrasts are not causal evidence |
| Development, confirmation and component attribution (§4.4) | ERA; experimental design | Tab4 access; Tab5 ablations | Adaptive development is not test evidence |
| C1 alignment and fixed-pool selection (§5.1.2) | Core results design | Tab10, Figs2/4/7 simulated displays covering 22 domains | Pair-only data cannot support Best-of-N; denominator rules remain explicit |
| C2 fresh shared start and new blinded H (§5.1.3) | Core results design | Fig9 eight-domain diagnostic fixture; Tab8 empirical status | Fresh endpoints need new judgments in both construction settings; C2 inputs are distinct from C1 |
| C3 frozen rewards and LoRA+GRPO (§5.1.4) | Core results design; training appendix | Fig1d; Tabs6/8 | Planned only; no training authorized, run, or simulated |
| Corpus construction versus acquisition efficiency (§3.2 patch, §5.2) | Experiments; quantitative-display discussion | Fig5 random-controlled budget curves | New data alone do not establish sampling efficiency |
| Editable components, allocation and H granularity (§5.2) | Ablation studies | Tab5 controls; Fig8 fixture | Equal evidence/budgets; paired H comparison also accounts for human time |
| Trajectories, failure regimes, H efficiency and adapter fidelity (§5.3) | Analysis and studies | Tab7 reporting; Fig10 cost fixture | Observations required; assigned costs and schematic trajectories prove no efficiency |

The older draft's exclusions of upstream mining and the C3 research design are
superseded by this revision. Historical optimizer modes and debugging history
remain excluded from the scientific narrative.

The author's quantitative-display request changes the presentation, not the
evidence status. Seven redundant conceptual callouts were retired in favor of
eight active simulated charts. Main Figure 2 now gives all 22 C1 domains in
6/6/5/5 taxonomy order, with five method columns and paired intervals; appendix
Figure 4 adds ID/OOD detail. C1 has 11 synthetic cohorts per setting, while
annotation, component, and C2 detail remains an explicit eight-domain subset.
The retired diagrams remain editable archives.
All plan items above remain covered in text/tables. Toy effects, labels, cohort
assignments, and uncertainty must not be interpreted as plan execution.

## September 19 display update

The main atlas is replaced by the approved landscape composite with all 22 tasks:
ring composition, cost/agreement scatter, and four family bar panels. Its 2,880
synthetic OOD inputs are balanced by fixed hash to 720 per family. Full-cohort
paired ID/OOD effects remain in appendix Fig4. This is a layout allocation,
not changed domain scope, measured data readiness, or an effectiveness result.
