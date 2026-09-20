# Wording audit

## Authority and scope

Reviewed the recent author/assistant naming instructions, including the explicit naming request
at 2026-09-20 20:31 UTC and the latest completed turn at 21:06 UTC. Cross-checked
the current repository at `bafe259` against `.paper/terminology.md`,
`.paper/context.md`, the relevant entries in `.paper/claims.yml` and
`.paper/figures.yml`, and `sections/problem.tex`, `sections/method.tex`, and
`sections/introduction.tex`. The manifest records these files' hashes.

This follows the academic-writing-skills figure/text-consistency workflow:
paper-specific terminology takes precedence, and figure language stays within
the evidence status recorded in shared paper memory.

## Text changes

| Figure text | Revision and reason | Source |
|---|---|---|
| ERA | IterEval: depth-first evaluator evolution. Framework followed by the component shown; not a renamed component acronym. | Author instruction; terminology glossary |
| Default search | Default setup, with “Try a different direction.” Keeps the illustration bounded to the manuscript's default evaluator-evolution setup; does not claim formal BFS. | Introduction; C43 |
| Deepen one idea | Continue one direction. Uses the defined unit of continued exploration. | Method, Directions and candidates; C32 |
| Initial program | Initial evaluation program. | Terminology; problem formulation |
| Task: rank image edits | Task: evaluate image edits; “Each edit is scored separately.” A displayed ordering follows separate pointwise scores, not direct pairwise execution. | Problem equation; Method, Objective and measurement |
| Reference: A / Evaluator picks B | Human prefers A / Scores favor B. Specifies the preference–evaluation mismatch within the constructed example. | Problem formulation; C42 |
| Add street-layout comparison | Compare layout with the source. The comparison is with permitted source context, not the competing output. | Pointwise execution boundary |
| Drift terminology | Detect layout changes → Penalize layout changes → Scale the penalty by severity. Makes the same direction's successive implementation changes explicit. | Method's observation–importance–scoring example; C31/C32 |
| Still picks B / Now picks A | Still favors B / Now favors A. These are per-example score orderings, not candidate acceptance flags. | Method, acceptance and measurement |
| Nodes are program revisions | Nodes are complete evaluation programs. A revision produces a candidate; the node is not an isolated edit. | Method, Directions and candidates; C32 |
| Additional short line in panel c | Candidate acceptance and program inheritance are checked separately. Complements “Continue one direction” without turning continuation into automatic acceptance or inheritance. | Method; C15/C16/C47 |

## Evidence boundaries

The images, preference for A, intermediate outcomes, and final corrected
ordering remain constructed. They are not a real annotation, observed trace,
equal-budget comparison, or measured benefit. The visible disclosure says
“Illustrative search paths.” C27/C28 remain material evidence gaps; no gain
claim is imported from the author-edited Abstract/Introduction.

One corrected example cannot establish an improved development-cohort score,
pass the candidate-acceptance guards, or establish generalization. Accordingly,
the green result badge is not renamed “accepted.” The current continuous
central branch illustrates eligible program inheritance along one direction;
it is not a claim that all failed candidates are inherited. In the actual
method, a direction can continue from the pre-update best program when
inheritance fails. Those fallback mechanics belong in the method, not a new
branch redesign in this text-only teaser revision.

The default panel is a shallow-switching sketch motivated by the bounded C43
observation, not proof of a universal default stopping rule or a strict
breadth-first algorithm. No efficacy, human-cost, convergence, or downstream
reward-training claim is introduced.

## Validation and handoff

Builder checks cover symmetry, equal spacing, node/card centering, text bounds
and overlap, embedded images, the absence of flat-style effects, and the
manuscript terminology regression rules applied to visible figure text.
The exported preview was visually inspected. The figure-side wording profile
and source hashes support future updates without changing the manuscript.

No canonical integration, shared claim-memory edits, experiments, commit,
or push is performed by this revision.
