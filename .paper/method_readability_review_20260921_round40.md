# Method refinement — 2026-09-21, round 40

## Scope

The author requested local simplification after accepting the core-first Method
structure. The parent used academic-writing-skills and ml-paper-writing for the
revision. The dedicated method_readability_reviewer independently inspected the
implementation and reviewed the revised prose read-only. This is a writing and
implementation-correspondence review, not an empirical validation.

## Dispositions

| Comment | Change | Boundary |
| --- | --- | --- |
| Algorithm actions appear before explanation. | Four sentences describe the cycle before Algorithm 1. The algorithm uses end and defines the submitted candidate explicitly. | No new algorithm stage. |
| Direction is not operational enough. | The error and intended correction guide revisions; identifier, starting program and trials define the recorded continuity. | The controller does not enforce invariant semantic intent. |
| Ending a direction is an unconstrained exit. | Main text names the explicit action and instruction; appendix states exactly what the parser checks. | No verified reason category, mandatory depth, or exhaustion-of-tests guarantee exists. This remains an implementation limitation, not a resolved algorithmic guarantee. |
| Inheritance competes with the two core decisions. | Describe a conservative parent rule within continuation; remove program inheritance from main prose and caption. | Preserve pre-update best fallback, including accepted candidates with incomplete local measurements. |
| Observations and interpretations are mixed. | Separate execution/case outcomes from agent explanations and questions in diagnostic state; use a testable tool-output example. | A trace change does not establish semantic correctness or causal explanation. |
| Human budget conflates reused and new labels. | Match label-access budgets for existing datasets and annotation counts for new labels; report time separately. Define original-input groups and dependent ranking-derived pairs in the appendix. | No measured human-time saving is claimed. |
| Editable scope appears too late. | Preview observations, criteria, tools, routing and evidence combination in the opening. | Full component list remains last. |
| Heterogeneous terminology impedes reading. | Use evaluation program, best/working program, continue/end, and candidate acceptance consistently. Update glossary and appendix terminology. | Native pause and legacy source identifiers remain where necessary. |

## Implementation findings

- patch_revision.py preserves direction_id while allowing updated intent.
- revision_session.py instructs an unresolved question and why no different test
  is ready; pause maps to a no_change submission with a nonempty reason.
- Parent choice requires additional local comparisons beyond candidate acceptance.
  The fallback remains the pre-update best, not necessarily the newly accepted best.
- Mining's structural ranking does not prove information value or human effort
  savings. Original label access and new annotation are distinct resources.

No implementation files, model calls, empirical runs, citations, author-edited
Abstract/Introduction, figure geometry or quantitative fixtures are changed.
The overview caption alone is updated. C27/C28 remain empirical gaps.

## Final review and verification

The substantive review found no blocking Method defect and requested four small
wording corrections. They remove intrinsic-easiness language, cover the initial
direction in the cycle overview, scope branching to the ordinary loop, and use
ending terminology in appendix trajectory analysis. All are applied.

The reviewer's final targeted verification confirmed all four corrections and
the matching C49/C50 memory, with no remaining blocking discrepancy in scope.

- `make all` passes; PDF has 36 total pages and 10 main-text pages.
- No overfull boxes, undefined references/citations or multiply defined labels.
- Memory, terminology, simulation, both landscape and whitespace checks pass.
- Final PDF pages 4–7 visually inspected; the cycle and direction definition
  precede the rendered Algorithm 1, which remains before Experiments.
- `check_paper.py` still fails on the existing nine-page initial limit and
  17 unused bibliography records. The approved teaser retains its documented
  2.5–4.7-point label warning; no artwork changes were authorized or made.
- Abstract, Introduction and overview-source hashes remain identical to round39.
  All four implementation hashes in method_implementation_audit.md also match.
- No commit or push performed. The existing dirty worktree is preserved.
