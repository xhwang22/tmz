# Claim–evidence ledger

The authoritative current sentence-level memory is `claims.yml`.
Its artifact paths are relative to this paper repository. Specification evidence
shows what the method defines, not that the method works. The source plan and
current ERA documentation are identified in `source_provenance.md`; the
plan-to-manuscript map is `plan_coverage.md`.

## Allowed inference

| Claim family | Manuscript / evidence | Allowed status |
| --- | --- | --- |
| Preference-supervised evaluation-agent evolution and domain standard | Introduction, problem, Fig1, Tab2 | Research question and scope, not achieved alignment or universal transfer |
| Preference outcomes versus criteria and evidence for new outputs | Abstract, introduction, problem; C42 | Problem framing, not a claim that all human preferences can be recovered or explained |
| Two feedback-construction settings; no H0 admission prerequisite | Problem/mining, Fig1, Tab3; C33/C34 | Shared algorithm with separately reported data provenance |
| New labels are not presumed more reliable | Annotation protocol, Fig5, Tab3; C35 | Reporting requirement; simulated raters supply no reliability evidence |
| Semantic mapping, dependence, three strata | Mining, Tab4 | Acquisition design, not validated information efficiency |
| H0–H3 and evidence table Z | Problem/mining, Figs1/4, Tab3 | Protocol; availability must be reported per source |
| Six components, fixed model, pointwise access | Problem/method, Fig4, Tab5 | Method specification, not immunity to leakage |
| Evolution of observation and judgment; hypothesis/program units | Method, Figs1/4, Tab6; C31/C32 | Procedural definitions, not evidence of improved judgment |
| Directions, connected edits, best/working, outcomes | Method, Algorithm1, Tab6 | Search procedure; utility requires controlled ablation |
| Train/Val/Test and metric reserve | Method/mining, Tab5 | Access contract; adaptive development is not final evidence |
| Optional semantic synthesis | Method/appendix | Defined grouping and anchor arithmetic, not semantic accuracy |
| C1/C2/C3 and controlled ablations | Experimental design, Tabs6–9/11 | Study design; no measured effect; C3 design-only |
| External human standard; automated program changes | Method; C39 | Self-evolution definition, not self-definition of human preferences |
| Fine-tuning/calibration alternatives and shared-observation control | Experiments, adaptation appendix, Tab12; C40 | Planned evaluator comparison; no superiority, data-efficiency, or cost result; distinct from C3 |
| Explicit criteria and traces versus faithful explanation | Adaptation appendix; C41 | Inspection affordance and evidential boundary, not validated interpretability |
| Corpus construction versus acquisition efficiency | Experiments, Fig3, Tab6; C36 | Separate matched-budget random-sampling comparison required |
| Annotation efficiency and coordinated-evolution usefulness | Introduction; C27/C28 | Material empirical gaps; retain as hypotheses only |
| Simulated display provenance | Generator, manifest, CSVs, PDFs; C37 | Supported only as artificial reporting examples, not effects |
| C1 denominators | C1/selection CSVs and arithmetic checker; C38 | Supported only as arithmetic consistency of toy displays |

The round-7 abstract maps its preference/procedure distinction to C42, its
learning object and external human target to C1/C31/C39, structured acquisition
to C4–C8, coordinated changes and separate-feedback assessment to
C12/C14/C15/C32, and the cross-task study design to C2/C3/C21/C22. Its opening
alignment motivation is supported by the literature cited in the introduction.
The final simulation notice maps to C37. No sentence asserts the acquisition or
evolution advantages recorded as gaps in C27/C28.

## Numerical audit

| Token or quantity | Trace | Meaning |
| --- | --- | --- |
| ERA, H0–H3, C1/C2/C3 | Definitions in problem, introduction and experiments | Method name and level/study identifiers |
| 22 domains; four families | Tab2, full domain IDs; Fig1 | Planned panorama only |
| Two construction settings | Mining; Fig1; Tab3 | Reused/new feedback, not permanent domain classes |
| Six components | Eq. program; Fig4 | (A, K, V, T, Pi, G), not an effect size |
| Three semantic strata | Mining; Tab4 | Within-dimension, overall–dimension, trade-off |
| At least 3 repeats | Eq. measurement; Appendix measurement | Fixed measurement requirement, not observed reliability |
| Default N=4; top-two | C1 design and measurement appendix | Planned candidate-pool and ranking endpoints |
| 95% intervals | Experimental design, Figs2/5; bootstrap code | Planned interval level; displayed intervals resample toy input groups only |
| H budgets 20, 50, 100, 200 | Ablation paragraph; Tab6; acquisition.csv | Matched-budget design; plotted outcomes are assigned toy responses |
| Two development / three final annotators | Annotation appendix | Planned independent annotation protocol |
| 50, 75, 100; lambda=0.4; result 60 | Semantic-synthesis appendix and anchor equation | Synthetic scale arithmetic, not a performance result |
| Eight cohorts; 160 groups; four candidates; three repeats | Tab10, cohorts.csv, c1_groups.csv, manifest | Toy generator settings, not experimental sample sizes |
| Seven methods in Tab1/Fig9; four in Fig6 | C1 summary, selected-rank and cost CSVs | Reporting fixtures, not evaluated implementations |
| 1,000 bootstrap replicates | Generator, manifest, Appendix J | Resampling variation in fixtures, not uncertainty about ERA |
| Five policies; 12 runs; 10-unit anchor; 10–90% bands | Fig3, acquisition.csv | Matched toy inputs; run percentiles are not confidence intervals |
| Three raters; two-of-three consensus; four outcomes | Fig5, annotation_groups.csv, annotation_summary.csv | Artificial votes, with valid-pair / requested-rating / input-group denominators |
| Four cumulative H levels; conditional component differences | Fig7, component_effects.csv, granularity.csv | Paired synthetic group contrasts, not independent search runs or additive causal effects |
| C2 tie threshold 0.15; regression threshold −0.8 | Fig8; refinement_groups.csv; generator/checker | Arbitrary latent units, not universal human thresholds |
| Relative deployment-cost units | Fig9, cost_summary.csv | Assigned costs, not timed calls or measured compute |
| Tab1 values; Fig2 effects; Fig6 rank shares | C1/selection CSVs and check_simulated_results.py | Method-complete, jointly complete, and all-input denominators respectively |
| Dashes in empirical downstream status | Tab9 | Unmeasured, not zero; no C3 fixtures |

No claim of measured accuracy, selection, refinement, training gain,
statistical significance, annotation efficiency, superiority to existing
optimizers, causal diagnosis, or completed multi-domain evaluation is supported
by this draft. Do not convert plan targets, available code, or synthetic tests
into evidence for such claims. The simulated displays are author-authorized
layout examples, not a simulation study of ERA or a forecast. C27/C28 retain
`gap` status and empty evidence lists. C37/C38 do not alter that boundary.
