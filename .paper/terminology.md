# Manuscript terminology

Author instruction, 2026-09-20: one concept, one term; repeat the accurate term rather than rotate synonyms.
This glossary supersedes earlier terminology guidance in `.paper/style_overrides.md` and historical audit notes.
It applies to current manuscript prose, headings, captions, and figure labels.

| Concept | Preferred term | Boundary |
|---|---|---|
| Project and complete framework | IterEval | Tagline: iterative evaluator self-improvement from human feedback. Use for the complete framework and experimental system, not as a name for either component alone. |
| Paper title | Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks | The opening phrase expresses the search insight, not another method name. |
| Paper-level learning process | evaluator self-evolution | Use evaluator evolution once the context is clear. The title and first introduction use self-evolving evaluators. |
| Tested baseline in Abstract and Introduction | default evaluator-evolution setup | Introduce as the default evaluator-evolution setup we tested; then use default setup. Do not alternate with default iterative optimizer or default model-driven evolution setup for this same configuration. |
| Upstream method | disagreement-based preference mining | Use preference mining after the full name when the context is clear. No component acronym. Covers existing datasets and newly generated outputs; reuse compatible preferences or collect missing ones. |
| Selecting comparisons | sampling; sampling policy | Data mining is the broader process; sampling is its selection operation. |
| Collecting human judgments | annotation | Not a synonym for mining, which can reuse labels. Distinguish annotation units from annotation time. |
| Evaluation information from people | human feedback | Umbrella for H0–H3; do not alternate with supervision for the same object. |
| Preference labels | human preferences | Overall or dimensional preferences; not a name for all H2/H3 feedback. |
| The procedure being learned | evaluation procedure | What the evaluator inspects, computes, and uses to judge. |
| Editable executable implementation | evaluation program | Not evaluator program, evaluation policy, or judging logic as stylistic alternatives. |
| Complete evaluation system | evaluator | Evaluation agent only where agent behavior is relevant. |
| Search method | depth-first evaluator evolution | Use the search or our search when the referent is clear. No component acronym or falsification-guided, evidence-guided, or diagnostic-guided rebranding. |
| Persistent correction explored by the search | direction | Not hypothesis, idea, or correction problem as interchangeable names. |
| Testable rationale for a direction | hypothesis | Explains the expected correction; diagnostic results do not automatically verify it. |
| Proposed complete evaluation program | candidate | Distinguish from an edit or component. A proposed artifact is a candidate output, then simply output. |
| A modification to the evaluation procedure | revision | A revision produces a candidate; use candidate when discussing measured performance or acceptance. Attempt is a general description, not an alternative name for the candidate. |
| Concrete work on a direction | implementation | Do not rotate with realization or instantiation. A statistical realization is a distinct, permitted use. |
| Accepting a candidate | candidate acceptance | Not promotion or adoption for this decision. |
| Continuing work on a direction | direction continuation | Not direction persistence or hypothesis continuation. |
| Best accepted evaluation program, B | best program | Best evaluator is acceptable when referring to the full system outside state-update notation. |
| Program being edited, W | working program | Not working state or working version. |
| Choosing the next working program | program inheritance | Separate from candidate acceptance and direction continuation; failed inheritance can still leave the direction active. |
| Search-level checks | diagnostic results | Not ambiguous new evidence; artifact evidence refers to information used to evaluate outputs. |
| Numerical/structured outputs of existing evaluation sources | evaluation signals | A preference sign is not an evolution direction. Disagreement refers to conflicts among these signals; use evaluation error for mismatches with human preferences. |
| Evaluator judgment inconsistent with a human preference | evaluation error | Defined relative to the supplied preference, not proof of an objectively wrong judgment. Do not use disagreement with human preferences as a second meaning of disagreement. |
| Z, shared input to evolution | feedback table | Logical join of human feedback with artifact, signal, and execution records. Not human evidence or adaptation evidence table. |
| Sampling endpoint | sampling efficiency | Evaluate final held-out agreement at matched annotation units or time, not just disagreement counts. |
| Alternative adaptation methods | score calibration; evaluator fine-tuning | Do not alternate with scorer calibration or evaluator weight fine-tuning. |
| Downstream applications | output selection; critic-guided refinement; reward-guided training | C1 also measures evaluator alignment. Evaluator fine-tuning and C3 generator training are different. |

## Scope and exceptions

- Do not rename cited paper titles, citation keys, implementation identifiers, legacy figure paths, or cross-reference labels.
- Preserve historical revision entries and audit quotations; this glossary governs new writing.
- Ordinary verbs and genuinely different objects need not share a single word. Do not replace every occurrence of evidence with feedback or every candidate with output.
- Diagnosing incomplete implementation supports further work within the implemented eligibility and budget rules; it does not guarantee continuation or prove the direction useful.
- Retire IPM and ERA from current reader-facing text. Preserve legacy data keys and code identifiers, with explicit display-name mappings where needed.
- Motivate disagreement-based preference mining by lowering the relative priority of repetitive comparisons on which existing signals agree. Disagreement is the implemented ranking mechanism, not a guarantee of human information value; no detected conflict can also reflect ties or missing signals. Retain the random anchor and matched-human-cost test.
- Keep uncertainty and simulation disclosures unchanged. A vocabulary revision is not new empirical evidence.
- Revised LaTeX prose uses one complete sentence per source line, with blank lines between paragraphs.

`python3 scripts/check_terminology.py` checks known stale wording in the active TeX input tree.
It excludes references, comments, and structural identifiers; it is a regression check, not a substitute for reading context.
