# P2E plan-to-manuscript coverage

Revision basis: `docs/plans/p2e_v2_plan.md` in the source project, especially
sections 1–5; current ERA execution semantics additionally follow
`docs/era_algorithm.md`. This is a coverage map, not an implementation or result
completion claim. No private results are imported.

| Research requirement | Manuscript destination | Visual destination | Evidence boundary |
| --- | --- | --- | --- |
| Open-ended generation with an existing evaluation ecosystem (§§1–2) | Introduction; problem formulation | End-to-end overview | Scope, not universal applicability |
| Four domain families and all 22 standards (§2.4) | Problem; full domain appendix | Panorama and domain table | Planned scope, not 22 completed experiments |
| Evaluation standard defines a domain (§2.4) | Problem; domain appendix | Domain contrast examples | A modality is not a domain |
| Semantic space and versioned evaluation knowledge (§3.1) | Preference mining | Signal–dimension matrix | Mappings fixed before labels |
| Existing tools and independent metric reserve (§3.1) | Mining; data appendix | Access-boundary diagram | Reserved endpoints never enter evolution |
| Direct/derived/material-only/new human data (§3.2) | Mining; annotation appendix | Data provenance table | Inputs alone are not human judgments |
| H0/H1/H2/H3 (§3.3) | Problem; mining; annotation appendix | Feedback ladder; annotation example | Human dimensions are not inferred from H0 |
| Many-to-many mapping and shared signals (§3.4) | Mining | Conflict matrix | Shared/mixed scores do not become independent votes |
| Same-dimension, overall–dimension and trade-off strata (§3.4) | Mining | Three conflict panels | Different constructs are not scorer contradictions |
| Random anchor, source dependence and readiness (§3.4) | Mining; annotation appendix | Readiness table | Sampling benefit is a hypothesis |
| Adaptation evidence table Z (§3.5) | Mining | Evidence-record diagram | Labels are proposal-only |
| Six-component executable program (§4.1) | ERA method | Evaluator architecture | Fixed base model |
| Direction versus implementation; continuation (§4.2) | ERA method | Branching search diagram | Continuation benefit is unmeasured |
| EXHAUSTED, PAUSED and REFUTED (§§4.2,4.5) | ERA method; algorithm appendix | Direction outcomes | Failure or nonsignificance is not refutation |
| Atomic edits and connected mechanism candidates (§4.3) | ERA method | Component graph and attribution matrix | Bundle gain is not per-edit attribution |
| Development, confirmation and component attribution (§4.4) | ERA; experimental design | Data boundary; ablation table | Adaptive development is not test evidence |
| C1 alignment and fixed-pool selection (§5.1.2) | Core results design | C1 panel; ID/OOD results templates | Pair-only data cannot support Best-of-N |
| C2 fresh shared start and new blinded H (§5.1.3) | Core results design | C2 controlled branches | New outputs require new judgments |
| C3 frozen rewards and LoRA+GRPO (§5.1.4) | Core results design; training appendix | C3 arms; outcome template | Planned only; no training authorized or run |
| Mining efficiency, editable components, allocation and H granularity (§5.2) | Ablation studies | Controlled-ablation matrix | Equal human and computation budgets |
| Trajectories, failure regimes, H efficiency and adapter fidelity (§5.3) | Analysis and studies | Analysis and reporting tables | Regimes require observations, not labels assigned a priori |

The older draft's exclusions of upstream mining and the C3 research design are
superseded by this revision. Historical optimizer modes and debugging history
remain excluded from the scientific narrative.
