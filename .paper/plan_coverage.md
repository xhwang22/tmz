# Research plan-to-manuscript coverage

Current display allocation (round 36): main Fig1 constructed teaser; Fig2 method overview; Fig3 C1 landscape; main Tab1 comparator matrix. Thirteen figures and fifteen tables. The top table uses current numbers; dated historical sections below retain their original numbers.

Revision basis: `docs/plans/p2e_v2_plan.md` in the source project, especially
sections 1–5; current evolution execution semantics additionally follow
`docs/era_algorithm.md`. This is a coverage map, not an implementation or result
completion claim. No private results are imported.

| Research requirement | Manuscript destination | Visual destination | Evidence boundary |
| --- | --- | --- | --- |
| Open-ended generation with an existing evaluation ecosystem (§§1–2) | Introduction; problem formulation | Fig2 overview | Scope, not universal applicability or existing labels |
| Human-preference alignment and executable evaluation standards (§§1–2.3) | Abstract; introduction; discussion | Fig2 feedback-to-evolution structure | Motivation and research question, not an achieved faithful representation of preferences |
| Parameter adaptation versus program evolution (§2.2; author clarification) | Introduction; C1; adaptation appendix | Tab6 adaptation choices | Fixed-interface restriction is not a general limit of tuning; no training or comparative result |
| Four domain families and all 22 standards (§2.4) | Problem; full domain appendix | Fig3a taxonomy, Tab2 criteria, Figs6/7 all-domain C1 | Planned scope and complete synthetic coverage, not 22 completed experiments |
| Evaluation standard defines a domain (§2.4) | Problem; domain appendix | Tab2 criteria; Figs6/7 all 22 rows; Figs9/11/12 diagnostic rows | Shared procedure, not one universal scorer; eight-domain diagnostics do not stand for full coverage |
| Semantic space and versioned evaluation knowledge (§3.1) | Preference mining | Tab4 readiness audit | Mappings fixed before labels |
| Existing tools and independent metric reserve (§3.1) | Mining; data appendix | Tab5 information-access table | Reserved endpoints never enter evolution |
| Existing H0 is not an admission prerequisite (§3.2 patch) | Introduction; problem; mining | Fig2 two feedback routes; Tab3 provenance | Missing labels define data work, not the algorithm |
| Reused/new feedback are construction settings (§3.2 patch) | Mining; experiments; discussion | Separate columns/rows in quantitative displays; Tab3 | A domain may use both; not permanent domain categories |
| Direct/derived/material-only/new human data (§3.2) | Mining; annotation appendix | Tab3 provenance | Inputs alone are not human judgments |
| Agreement, abstention, independent new labels (§3.2 patch) | Annotation protocol; quantitative-display discussion | Fig9 three-denominator audit | Simulated raters provide no reliability evidence; new labels are not presumed better |
| H0/H1/H2/H3 (§3.3) | Problem; mining; annotation appendix | Fig2 evidence interface; Tab3; Fig10b fixture | Human dimensions are not inferred from H0 |
| Many-to-many mapping and shared signals (§3.4) | Mining | Tab4 source-independence requirements | Shared/mixed scores do not become independent votes |
| Same-dimension, overall–dimension and trade-off strata (§3.4) | Mining | Tab4 semantic readiness | Different constructs are not scorer contradictions |
| Random anchor, source dependence and readiness (§3.4) | Mining; annotation appendix | Fig8 matched-budget fixture; Tab4 | Sampling benefit remains a hypothesis |
| Feedback table Z (source plan: adaptation evidence table, §3.5) | Mining | Fig2 common feedback interface | Human labels are proposal-only |
| Six-component executable program (§4.1) | Depth-first evaluator evolution | Fig4 runtime architecture | Fixed base model; illustrative artifact |
| Direction versus implementation; continuation (§4.2) | Depth-first evaluator evolution; algorithm appendix | Fig2c pictorial evolution loop and separate decisions; Tab11 search-allocation controls | Direction is exploration unit, program is selection unit; utility unmeasured |
| Source plan's EXHAUSTED, PAUSED and REFUTED terminology (§§4.2,4.5) | Current direction-continuation and termination rules | Algorithm1 agent actions and resource limits | Historical terms, not implemented semantic outcome classes; the controller does not automatically judge a direction unhelpful |
| Atomic edits and connected mechanism candidates (§4.3) | Depth-first evaluator evolution | Tab11 attribution design; Fig10a fixture | Bundle gain is not per-edit attribution; simulated contrasts are not causal evidence |
| Development, confirmation and component attribution (§4.4) | Evolution; experimental design | Tab5 access; Tab11 ablations | Adaptive development is not test evidence |
| C1 alignment and fixed-pool selection (§5.1.2) | Core results design | Tab14, Figs6/7/10 simulated displays covering 22 domains | Pair-only data cannot support Best-of-N; denominator rules remain explicit |
| C2 fresh shared start and new blinded H (§5.1.3) | Core results design | Fig12 eight-domain diagnostic fixture; Tab8 empirical status | Fresh endpoints need new judgments in both construction settings; C2 inputs are distinct from C1 |
| C3 frozen rewards and LoRA+GRPO (§5.1.4) | Core results design; training appendix | Fig2d assessment cards; Tabs10/8 | Planned only; no training authorized, run, or simulated |
| Corpus construction versus sampling efficiency (§3.2 patch, §5.2) | Experiments; quantitative-display discussion | Fig8 random-controlled budget curves | New data alone do not establish sampling efficiency |
| Editable components, allocation and H granularity (§5.2) | Ablation studies | Tab11 controls; Fig11 fixture | Equal evidence/budgets; paired H comparison also accounts for human time |
| Trajectories, failure regimes, H efficiency and adapter fidelity (§5.3) | Analysis and studies | Tab7 reporting; Fig13 cost fixture | Observations required; assigned costs and schematic trajectories prove no efficiency |

The older draft's exclusions of upstream mining and the C3 research design are
superseded by this revision. Historical optimizer modes and debugging history
remain excluded from the scientific narrative.

The author's quantitative-display request changes the presentation, not the
evidence status. Seven redundant conceptual callouts were retired in favor of
nine active simulated charts. Main Figure 3 restores the approved landscape design with C1 alignment and selection; main Table 1 retains the full comparator matrix.
The original balanced-subset landscape remains unchanged in the simulation appendix.
Downstream placeholders and the blank budget figure are in their respective appendices, with main-text interpretation retained.
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


## Main-text landscape restoration (round 25)

Main Figure 2 adapts the approved landscape to plan §5.1.2: task taxonomy, C1 agreement versus Best-of-4 selection, and all 22 task-level agreement panels.
Main Table 1 retains the full ID/OOD comparator specification; it is not populated with synthetic numbers.
Appendix Table 8 holds downstream placeholders, and Figure 4 reserves matched-budget comparisons.
The original balanced-subset figure remains Figure 5; full-cohort paired effects are Figure 6.
C37/C48 support simulation provenance and denominator arithmetic only, not empirical gains.
The new exports retain 3,520 requested OOD inputs; bars use the five-method completeness intersection within each domain, while selection counts incomplete scoring as failure.
A new independent checker validates all 110 bars/intervals and eight family points, with original records and assets unchanged.
C27/C28 remain empirical gaps, and no C2/C3 outcome is added.
