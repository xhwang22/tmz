# Method readability review — 2026-09-21

## Scope and process

The author requested a single Method TeX file and a dedicated reviewer subagent
to improve fluency, clarity and reading order through repeated revision.
`/root/method_readability_reviewer` completed two substantive review passes and
a targeted final verification. The reviewer was read-only; manuscript edits and
compilation were performed by the parent agent. No experiments, model inference
for research results, engineering edits, commit or push were performed.

The Method now resides entirely in `sections/method.tex`. `main.tex` includes
only that Method source after Related Work. The source-only consolidation
preserved extracted PDF text exactly before the subsequent prose edits
(SHA-256 `03a71a4fee1c06ea436409040ddb337c42ed1afed416621105867d69fe65e482`).

## Review dispositions

The concerns below are paraphrases of the review, not verbatim quotations.
Anchors name current source paragraphs rather than obsolete line numbers.

| ID | Concern | Current anchor | Revision and verification |
| --- | --- | --- | --- |
| R1.1 | Implementation caveats interrupt the execution story. | Overview/setup; Appendix D and F | Main text now defines the object, objective and data access, then follows one iteration. Full measurement, diagnostic and resource details remain in the appendix. |
| R1.2 | Candidate acceptance and the best-program update are separated. | Accepting a candidate and choosing the next working program | Acceptance and the joint best/working update are contiguous, followed by inheritance eligibility. The pre-update best fallback is unchanged. |
| R1.3 | The path from human feedback to the revision input is unclear. | Mining, final paragraph; Revising within a direction | Introduces the feedback table Z as the join of selected human preferences and corresponding records before defining its proposal subset. |
| R1.4 | Diagnostics need a concrete connection to the next revision. | Measuring and diagnosing a candidate | Adds a constructed example: a tool detects missing content, but the final judgment ignores the finding, motivating a revision to how that finding is used. This is not a reported observation or performance result. |
| R2.1 | Failed inheritance must not be described as candidate rejection. | Continuing or switching directions | States that failed inheritance returns the next revision to the pre-update best while retaining diagnostic results. Acceptance can still have updated best. |
| R2.2 | Continued allocation must be described as the default, not unconditional. | Continuing or switching directions | Adds "By default" and preserves agent pause/switch decisions and resource termination. |
| R2.3 | Reused checking data must not be presented as held-out test evidence. | Overview/setup, final paragraph | Explicitly identifies checking data as development data; terminal validation cannot rerank or trigger edits. |
| R3.1 | "Both" incorrectly refers to ties and missing signals. | Mining, second paragraph | Replaces it with "The random anchor and targeted pairs both count toward b_H." |

Final reviewer verdict, before applying the last referent correction:

> 最终复审基本通过，优化语义和阅读顺序均已保留。
>
> 仅剩一处新引入的指代问题：“Both count toward \(b_H\)”紧接 ties/missing signals，容易被理解成二者占用预算。改为：
>
> The random anchor and targeted pairs both count toward \(b_H\).
>
> 除此之外，没有阻碍收尾的问题。

The requested correction is present in the final source.

## Preserved semantics

- Fixed base model; pointwise output scoring with no opponent or human label in
  evaluator execution.
- Separate best program, working program, persistent direction and diagnostic
  state; no invented learned state or semantic-verification oracle.
- Distinct acceptance, inheritance and continuation decisions. Inheritance
  retains the common complete/comparable local-and-checking prerequisites and
  the accepted/no-damage/fresh-progress branches.
- Pre-update best fallback, including the accepted-but-not-inheritable case.
- Aggregate-only checking data, frozen terminal validation and post-freeze tests.
- Advisory edit counts, not an invented cumulative direction-edit budget.
- Resource exhaustion leaves a direction unresolved; it is not refutation.
- Recorded best-development agreement is not a guarantee of unseen performance.

## Verification and remaining issues

- `make all` succeeds; no overfull boxes, undefined citations/references or
  multiply defined labels in `build/main.log`.
- Memory, terminology, simulation-provenance, both landscape audits and
  `git diff --check` pass. The active tree has 27 TeX sources; memory retains
  52 claims and empirical gaps C27/C28.
- PDF pages 4–7 were rendered and visually inspected. Equations, paragraphs and
  captions are readable without changing body typography or figure geometry.
- `check_paper.py` still fails on 17 unused bibliography records and 10 main-text
  pages against the 9-page initial-submission limit. The full PDF has 38 pages.
  The approved teaser retains its known 2.5–4.7-point label warning.
- Author-modified Abstract, Introduction and overview source hashes are unchanged:

| File | SHA-256 |
| --- | --- |
| `sections/abstract.tex` | `6ac0b31defae6558594151fe54e40f95d26b79dba7c7ed91d833cac241738998` |
| `sections/introduction.tex` | `9b01acd31ef94d9e0bb9dbe213c6b4b7771303626a31bfaea15ca5027065a4d6` |
| `figures/overview.tex` | `833cb05a09f274b88f37ae0f8abc124611d39a117fc9721cd8e9473dfcf85bcd` |

Figure captions/assets and quantitative fixtures are unchanged. This review
does not validate the author's result claims or update publication metadata.
