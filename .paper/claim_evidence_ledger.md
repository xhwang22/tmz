# Claim–evidence ledger

The authoritative current sentence-level memory is `claims.yml`.
Its artifact paths are relative to this paper repository. Specification evidence
shows what the method defines, not that the method works. The source plan and
current ERA documentation are identified in `source_provenance.md`; the
plan-to-manuscript map is `plan_coverage.md`.

## Allowed inference

| Claim family | Manuscript / evidence | Allowed status |
| --- | --- | --- |
| Preference-supervised evaluation-agent evolution and domain standard | Introduction, problem, Fig1, Tab1 | Research question and scope, not achieved alignment or universal transfer |
| Preference outcomes versus criteria and evidence for new outputs | Abstract, introduction, problem; C42 | Problem framing, not a claim that all human preferences can be recovered or explained |
| Two feedback-construction settings; no H0 admission prerequisite | Problem/mining, Fig1, Tab2; C33/C34 | Shared algorithm with separately reported data provenance |
| New labels are not presumed more reliable | Annotation protocol, Fig6, Tab2; C35 | Reporting requirement; simulated raters supply no reliability evidence |
| Semantic mapping, dependence, three strata | Mining, Tab3 | Acquisition design, not validated information efficiency |
| H0–H3 and evidence table Z | Problem/mining, Figs1/3, Tab2 | Protocol; availability must be reported per source |
| Six components, fixed model, pointwise access | Problem/method, Fig3, Tab4 | Method specification, not immunity to leakage |
| Evolution of observation and judgment; hypothesis/program units | Method, Figs1/3, Tab5; C31/C32 | Procedural definitions, not evidence of improved judgment |
| Directions, connected edits, best/working, outcomes | Method, Algorithm1, Tab5 | Search procedure; utility requires controlled ablation |
| Train/Val/Test and metric reserve | Method/mining, Tab4 | Access contract; adaptive development is not final evidence |
| Optional semantic synthesis | Method/appendix | Defined grouping and anchor arithmetic, not semantic accuracy |
| C1/C2/C3 and controlled ablations | Experimental design, Tabs5–8/11 | Study design; no measured effect; C3 design-only |
| External human standard; automated program changes | Method; C39 | Self-evolution definition, not self-definition of human preferences |
| Fine-tuning/calibration alternatives and shared-observation control | Experiments, adaptation appendix, Tab12; C40 | Planned evaluator comparison; no superiority, data-efficiency, or cost result; distinct from C3 |
| Explicit criteria and traces versus faithful explanation | Adaptation appendix; C41 | Inspection affordance and evidential boundary, not validated interpretability |
| Corpus construction versus acquisition efficiency | Experiments, Fig5, Tab5; C36 | Separate matched-budget random-sampling comparison required |
| Annotation efficiency and sustained gains from depth-first continuation | Introduction; C27/C28 | Material empirical gaps; retain as open comparisons only |
| Default pointwise rejection, incumbent retention, and redirection | Introduction; search_observation_audit.md; C43 | Bounded qualitative development observation, not universal RSI behavior or proof of the DFS remedy |
| Simulated display provenance | Generator, manifest, CSVs, PDFs; C37 | Supported only as artificial reporting examples, not effects |
| C1 denominators | C1/selection CSVs and arithmetic checker; C38 | Supported only as arithmetic consistency of toy displays |

The round-14 abstract maps its preference/procedure distinction to C42 and its
learning object and external human target to C1/C31/C39.
The observed default rejection/redirection maps to C43, whose source audit
explicitly preserves accepted improvements and the limits of the evidence.
The acquisition design maps to C4–C8, continuation versus adoption to C14/C15/C32,
and the cross-domain study design to C2/C3/C21/C22/C33/C34.
Its opening alignment motivation is supported by the literature cited in the introduction.
The final simulation notice maps to C37.
No sentence asserts the acquisition or depth-first advantages recorded as gaps in C27/C28.
C28 now expresses the author-approved continuation hypothesis; the prior coordinated-component formulation remains in revision history.

## Numerical audit

| Token or quantity | Trace | Meaning |
| --- | --- | --- |
| ERA, H0–H3, C1/C2/C3 | Definitions in problem, introduction and experiments | Method name and level/study identifiers |
| 22 domains; four families of 6/6/5/5 | Tab1, full domain IDs; Figs1/2/4 | Full planned scope and synthetic C1 coverage, not readiness or completed experiments |
| Two construction settings | Mining; Fig1; Tab2 | Reused/new feedback, not permanent domain classes |
| Six components | Eq. program; Fig3 | (A, K, V, T, Pi, G), not an effect size |
| Three semantic strata | Mining; Tab3 | Within-dimension, overall–dimension, trade-off |
| At least 3 repeats | Eq. measurement; Appendix measurement | Fixed measurement requirement, not observed reliability |
| Default N=4; top-two | C1 design and measurement appendix | Planned candidate-pool and ranking endpoints |
| 95% intervals | Experimental design, Figs2/4/6; bootstrap code | Planned interval level; displayed intervals resample toy input groups only |
| H budgets 20, 50, 100, 200 | Ablation paragraph; Tab5; acquisition.csv | Matched-budget design; plotted outcomes are assigned toy responses |
| Two development / three final annotators | Annotation appendix | Planned independent annotation protocol |
| 50, 75, 100; lambda=0.4; result 60 | Semantic-synthesis appendix and anchor equation | Synthetic scale arithmetic, not a performance result |
| 22 C1 cohorts, 11 per setting; eight diagnostic cohorts | c1_cohorts.csv; Tab9/cohorts.csv; manifest | Full C1 layout coverage and bounded diagnostic subset; assignments do not assert label availability |
| 160 groups; four candidates; three repeats | c1_groups.csv, manifest | Toy generator settings, not experimental sample sizes |
| Seven methods in Tab10/Fig10; five in Fig2; four in Fig7 | C1 summary, selected-rank and cost CSVs | Reporting fixtures, not evaluated implementations; Fig2 is a fixed non-metric subset |
| 1,000 bootstrap replicates | Generator, manifest, Appendix J | Resampling variation in fixtures, not uncertainty about ERA |
| Five policies; 12 runs; 10-unit anchor; 10–90% bands | Fig5, acquisition.csv | Matched toy inputs; run percentiles are not confidence intervals |
| Three raters; two-of-three consensus; four outcomes | Fig6, annotation_groups.csv, annotation_summary.csv | Artificial votes, with valid-pair / requested-rating / input-group denominators |
| Four cumulative H levels; conditional component differences | Fig8, component_effects.csv, granularity.csv | Paired synthetic group contrasts in eight diagnostic domains, not independent search runs or additive causal effects |
| C2 tie threshold 0.15; regression threshold −0.8 | Fig9; refinement_groups.csv; generator/checker | Arbitrary latent units, not universal human thresholds |
| Relative deployment-cost units | Fig10, cost_summary.csv | Assigned costs, not timed calls or measured compute |
| Main-text balanced C1 composite: 22 tasks, 2,880 inputs, 720/family | Fig2; C44; data/simulated/landscape/ | Fixed-hash synthetic subset; 120/task in six-task families, 144/task in five-task families; not empirical prevalence |
| 110 bars/intervals and 120 cost/agreement points | Fig2b--c; method-summaries.csv, displayed-macros.csv, check_landscape_results.py | Method-complete agreement; all-input assigned cost; ten equally weighted 11-domain means; marginal intervals are not paired contrasts |
| Tab10 values; Fig4 effects; Fig7 rank shares | C1/selection CSVs and check_simulated_results.py | Method-complete, jointly complete, and all-input denominators respectively; the balanced Fig2 subset is audited separately above |
| Dashes in empirical downstream status | Tab8 | Unmeasured, not zero; no C3 fixtures |

No claim of measured accuracy, selection, refinement, training gain,
statistical significance, annotation efficiency, superiority to existing
optimizers, causal diagnosis, or completed multi-domain evaluation is supported
by this draft. Do not convert plan targets, available code, or synthetic tests
into evidence for such claims. The simulated displays are author-authorized
layout examples, not a simulation study of ERA or a forecast. C27/C28 retain
`gap` status and empty evidence lists. C37/C38 do not alter that boundary.

## Argument revision audit (2026-09-19, round 16)

The abstract and introduction now progress from contextual evaluation standards
to the gap between human feedback and an executable evaluation procedure.
Acquisition and evolution are connected parts of this problem, not a new theory
of feedback efficiency. No experimental claim has been promoted.

| Revised statement | Evidence/claim | Disposition |
| --- | --- | --- |
| Human feedback does not specify a complete evaluation procedure | C42; problem definition and cited evaluator literature in Introduction | Framing, not a claim that all human standards are recoverable |
| Program evolution changes evidence gathering and judgment | C12/C31/C39; Method specification | Method capability, not an advantage over fine-tuning |
| Acquisition allocates fewer annotations to agreement cases, with a random anchor | C7 and Mining protocol | Design; consensus is not correctness |
| Tested optimizer returned to the best evaluator after unsuccessful candidates | C43; search_observation_audit.md | Bounded observation; does not characterize all RSI methods or prove why gains stalled |
| Connected evaluation steps motivate further implementation | C13/C32; Method example and continuation specification | Rationale; the summary-omission example is illustrative, not a new observed result |
| Candidate acceptance and direction continuation are distinct | C15/C16/C17/C32; Method selection and refutation rules | Design; failure remains evidence, and continuation requires new information |
| Better acquisition at equal human cost; better continuation at equal search cost | C27/C28 | Open comparisons, not findings; quantitative displays remain simulated |

Terminology is synchronized in the edited sections. Human feedback is the
umbrella; human preferences are preference judgments. A direction states an
intended improvement, its hypothesis predicts a testable change, and a candidate
is a complete evaluator implementation. Detailed provenance and adaptation
controls remain in their existing sections rather than the early introduction.
