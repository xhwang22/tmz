# Claim–evidence ledger

The authoritative current sentence-level memory is `claims.yml`.
Its artifact paths are relative to this paper repository. Specification evidence
shows what the method defines, not that the method works. The source plan and
current ERA documentation are identified in `source_provenance.md`; the
plan-to-manuscript map is `plan_coverage.md`.

## Allowed inference

| Claim family | Manuscript / evidence | Allowed status |
| --- | --- | --- |
| Broad P2E scope and domain standard | Introduction, problem, Tab4, Fig1 | Research scope, not universal evaluation or transfer |
| Semantic mapping, dependence, three strata | Mining, Fig2, Tabs5–6 | Acquisition design, not validated information efficiency |
| H0–H3 and evidence table Z | Problem/mining, Fig6, Tab5 | Protocol; actual availability must be reported per run |
| Six components, fixed model, pointwise access | Problem/method, Fig3 | Method specification, not immunity to leakage |
| Directions, connected edits, best/working, outcomes | Method, Fig4, Algorithm1 | Search procedure; utility requires ablation |
| Train/Val/Test and metric reserve | Method/mining, Fig7 | Access contract; adaptive development is not final evidence |
| Optional semantic synthesis | Method/appendix, Fig8 | Defined grouping and anchor arithmetic, not semantic accuracy |
| C1/C2/C3 and controlled ablations | Experimental design, Fig5, Tabs1–3/7–10 | Study design; no measured effect |
| Annotation efficiency and connected-revision usefulness | Introduction hypotheses | Material empirical gaps; never assert as findings |

## Numerical audit

| Token or quantity | Trace | Meaning |
| --- | --- | --- |
| P2E, ERA, H0–H3, C1/C2/C3 | Definitions in problem, introduction and experiments | Names and level/study identifiers |
| 22 domains; four families | Tab4, full domain IDs | Planned panorama only |
| Six components | Eq. program; Fig3 | (A, K, V, T, Pi, G), not an effect size |
| Three semantic strata | Mining; Fig2 | Within-dimension, overall–dimension, trade-off |
| At least 3 repeats | Eq. measurement; Appendix measurement | Fixed measurement requirement, not observed reliability |
| Default N=4; top-two | C1 design and measurement appendix | Planned candidate-pool and ranking endpoints |
| 95% intervals | Experimental design and measurement appendix | Planned interval level, not an observed confidence interval |
| H budgets 20, 50, 100, 200 | Ablation paragraph; Tab7 | Matched-budget study conditions |
| Two development / three final annotators | Annotation appendix | Planned independent annotation protocol |
| 50, 75, 100; lambda=0.4; result 60 | Fig8 and anchor equation | Explicitly synthetic arithmetic, not a performance score |
| Dashes in results | Tabs2–3 | Unmeasured, not zero |

No claim of measured accuracy, selection, refinement, training gain,
statistical significance, annotation efficiency, superiority to existing
optimizers, causal diagnosis, or completed multi-domain evaluation is supported
by this draft. Do not convert plan targets, available code, or synthetic tests
into evidence for such claims.
