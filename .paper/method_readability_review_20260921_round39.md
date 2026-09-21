# Core-first Method review — 2026-09-21, round 39

## Scope and process

The author identified excessive formalism around secondary mechanisms and an
underdeveloped core optimizer abstraction. The parent rewrote the single Method
source using academic-writing-skills and ml-paper-writing. The dedicated,
read-only method_readability_reviewer inspected implementation semantics,
reviewed the new draft and verified the final corrections.
No experiments, source-code changes, new citations, commit or push occurred.

## Revision dispositions

| Concern | Revision | Anchor |
| --- | --- | --- |
| Exploration/selection abstraction appears too late. | The opening states direction as exploration unit and complete program as selection unit, immediately followed by persistent state. | Overview and setup |
| Architecture and protocol obscure the optimizer. | Six-component space moves last; measurement sampling, repeats, ties and incomplete outcomes stay in Appendix F. | Revision space; Agreement estimator |
| Decorative equations add notation without constraints. | Retains only state, objective and acceptance/best-update blocks; removes mining, revision, diagnostic-update and continuation functions. | Equations 1–3 |
| Inheritance competes with acceptance/continuation as a third insight. | Describes inheritance in one paragraph as the next-working-program policy inside continuation. | Candidate acceptance and direction continuation |
| Accepted-but-not-inherited behavior is unexplained. | States the local-comparison requirement and preserves the pre-update best fallback without reversing acceptance. | Same paragraph; Appendix D |
| Direction is indistinguishable from generic reflection. | Specifies stable identifier, starting program and retained trial history; revision outcomes do not clear the active direction. Intent can be refined. | Choosing a direction; Algorithm 1 |
| Direction choice may imply a second mandatory model call. | Explicitly permits choice and first revision in one editing session. | Choosing a direction |
| Pauses look free in pseudocode. | Records pause observations and costs before clearing the direction; all sessions count under configured accounting. | Algorithm 1, pause branch |
| Replay handling omits reuse of measured candidates. | Obtains checking/local outcomes for valid changed candidates and reuses verified records for exact replays. | Algorithm 1, candidate branch |
| Appendix asserts a semantic stopping test absent from code. | Replaces required contradicted predictions with agent assessment supported by available diagnostics, not controller certification. | Appendix D and trajectory analysis |
| Mining is too prominent. | Compresses to two paragraphs: reverse-priority rationale, reuse/new-label routes, random anchor and matched-human-cost endpoint. | Preference mining |
| Algorithm float appears after Experiments begins. | Moves its source declaration earlier within depth-first evolution; rendered Algorithm 1 is on page 6, before Experiments on page 7. | Main Method |

The final reviewer response was:

> 最终复核通过，无实质问题。
>
> 持续方向已成为 Method 主线；inheritance 降为继续探索时的工作程序选择策略，未再喧宾夺主。正文与算法清楚保留了独立接受、诊断留存、旧 B 回退、显式暂停及换方向。附录与正文一致，没有硬性方向预算或自动语义判定的虚构。

The later algorithm-float relocation changed only source placement, not content.

## Verification

- The Method remains entirely in sections/method.tex; no duplicate algorithm.
- make all succeeds; no overfull boxes, undefined citations/references or
  multiply defined labels in build/main.log.
- Memory, terminology, simulation provenance, both landscape checks and
  git diff --check pass. C27/C28 remain empirical gaps.
- Final PDF pages 4–7 were visually inspected. The core state and selection
  distinction appear on page 4; the main algorithm is readable on page 6.
- PDF: 36 total pages, 10 main-text pages. Initial-submission limit remains
  exceeded by one page; 17 unused bibliography entries and the approved teaser's
  2.5–4.7-point label warning remain. check_paper.py is therefore not fully passing.
- Author-edited Abstract and Introduction, figure geometry/assets and numerical
  fixtures are unchanged. The overview caption alone reflects the revised
  acceptance/continuation hierarchy.

| Preserved file | SHA-256 |
| --- | --- |
| sections/abstract.tex | 6ac0b31defae6558594151fe54e40f95d26b79dba7c7ed91d833cac241738998 |
| sections/introduction.tex | 9b01acd31ef94d9e0bb9dbe213c6b4b7771303626a31bfaea15ca5027065a4d6 |
| figures/overview.tex | 833cb05a09f274b88f37ae0f8abc124611d39a117fc9721cd8e9473dfcf85bcd |

This review validates exposition and its inspected implementation correspondence,
not the author's empirical claims or the effectiveness of either method component.
