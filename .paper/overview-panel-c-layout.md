# Historical Figure 2c — action-cycle layout

Superseded on 2026-09-21 by the author-requested
[three-panel layout review](overview-three-panel-layout.md). The author found
the generated action cycle too generic and the domain panorama too large.
The original design record below is retained for provenance, not as an active
four-panel constraint.

Cleanup note: the old `build/overview-panel-c-layout/` preview was deleted on
2026-09-21; its editable SVG was retained in the
[build source archive](build-cleanup-20260921.md). The current proof is under
`build/overview-layout-current/`.

Status at drafting: author-approved scheme for one generated review candidate,
2026-09-21. Not a manuscript replacement or a GitHub push. This supersedes the
two-round study below and its `build/overview-panel-c-layout/plan.svg` / `plan.png`.
Those wireframes are historical, not inputs to the new generation.

## Current scheme: one action row, two return destinations

Human feedback → Propose direction → Revise program → Evaluate candidate → Diagnose.

Only Revise, Evaluate and Diagnose belong to the pale-green active-direction
field. Below the action row, two nested, noncrossing return paths differ by
destination:

- Short green return: Diagnose → Revise program; retain the direction and use
  its diagnostics for another revision.
- Long gray return: Diagnose → Propose direction; end the direction and propose
  another when resources permit.

Above the row, candidate acceptance branches from Evaluate candidate to Best
program B. Better checking agreement and the guards update B; otherwise B stays
unchanged. Selection does not control the continuation return. The checking set
is a small input to evaluation, not a separate process stage. Only B connects
to downstream applications, frozen after search.

Preserve the four-panel envelope, a/b/d's pictorial artwork, and lake-green style.
No repeated candidates, component inventory, example case, large footer, decision
diamond, or circular enclosure. The b input ends at Propose direction, not at a
group boundary. Both returns have visible arrowheads at their own destinations.

Semantic limits remain: the green return retains direction and diagnostics, not
necessarily candidate code; parent choice follows the Method's conservative rule.
Observed execution/outcome records differ from agent interpretation and questions.
Checking releases aggregates. The agent records its decision to end a direction;
the controller does not certify semantic consistency or reason sufficiency.
No minimum depth, successful next revision, or hard local-budget commitment is
implied. A new direction starts from the current best program; resources can stop
search without refuting a direction. Terminal validation does not rerank or
reopen search. The base model stays fixed and no efficacy claim is added.

Review gates: correct return destinations; no crossings; acceptance originates at
Evaluate; only B feeds d after search; active-direction field excludes Propose;
readable labels and preserved a/b/d composition.

Prompt: `prompts/overview-panel-c-action-cycle-v11.txt`.

---

# Historical rejected two-round study (not current)

Status: design for author review, 2026-09-21. No image generation, manuscript
replacement, or push. The previous v10 raster is rejected as too crowded.
This is a single layout study, not a new finished-art series.

## What the panel should communicate

The same direction and its diagnostic history can support successive revisions,
while candidate acceptance separately updates the best program. A direction can
also end. The panel illustrates these method rules, not measured gains.

Figure 1 carries the concrete case and breadth/depth comparison. Figure 2c should
show the optimizer's organization without repeating that case or the algorithm's
full protocol. Preserve the four-panel envelope and the a/b/d illustrations.

## Spatial composition

Use the existing roughly 840-by-630 panel proportions. The wireframe is only a
spatial test; simple glyphs are placeholders for the established pictorial art.

- Header: one title, no separate model-robot card or component inventory.
- Left 54%: one borderless, pale-green field headed Active direction d.
  Two complete candidate-program icons repeat vertically. Between them a
  diagnostic notebook distinguishes observed changes from the next question.
  A smaller repeated notebook follows the second candidate. A green path connects
  revisions and diagnostics; it does not encode unconditional code inheritance.
- Middle 10%: clear connector space. Two candidate-measurement links merge into
  one dashed collector and enter one checking-set icon. No other object belongs
  in this gutter. The collector means the same checking procedure for each
  candidate, not a delayed joint evaluation after two revisions.
- Upper/right 32%: Checking set above Best program B. Only the conditional
  acceptance arrow joins these. The output leaves B laterally, with a small lock
  on the connector rather than a separate Freeze box.
- Lower/right: a small New direction folder, outside the green field and below
  the acceptance cluster. Its gray incoming link originates after diagnosis,
  crosses the field edge, and is labeled End d. It must not connect to the
  acceptance collector or to the downstream output.
- Remaining width is outside margin. Keep the lower connector below the end of
  the dashed collector. No stepped enclosure, inner swimlane boxes, or loop.

The core reading order is top-to-bottom. Rightward links mean either candidate
measurement (dashed, upper region) or ending a direction (gray, lower region).
Their different positions and labels distinguish them without relying on color.

## Boundary connections

The existing b-to-c Human feedback arrow terminates at c's outer group boundary,
not at the last candidate or the continuation dots. It denotes input to the
whole optimizer. Detailed proposal/checking access is specified in the caption;
do not route an extra long wire up the left side of the search path.

The c-to-d connection starts from Best program B, passes a lock, and enters d as
a group. A single group connector is sufficient for the three applications.
The lock means freezing after search, not freezing each accepted intermediate
candidate. No candidate or New direction has a direct downstream connector.

## Objects and labels

Keep the main label set short:

- Active direction d
- Candidate C1; Candidate C2
- Observed change; Next question (diagnostic notebook marked z)
- Revise again; Diagnose again; Continue d
- Candidate acceptance; Checking set; Better + checks; Best program B
- End d; New direction

No full example sentences, formulas, observed scores, success crosses/checkmarks,
repeated checking clipboards, explanatory footer slogan, or six-component strip.
Reuse the same program glyph for candidates and B. Use one notebook design for
diagnostics and one folder design for a new direction; do not make every object
a new boxed card. Final artwork may use subtle folds/shadows, not nested panels.

## Caption responsibilities and semantic limits

Explain the following once in the caption rather than as tiny in-image text:

1. The two rounds are illustrative. A direction can end at an earlier round;
   no minimum depth or guaranteed successful second candidate is implied.
2. Green arrows carry revision/diagnostic progression. The working parent follows
   the Method's conservative rule; C1 is not necessarily the code parent of C2.
3. Observed execution/outcome records differ from the agent's interpretations
   and next questions. Checking releases aggregates, not detailed checking cases.
4. Acceptance requires improved checking agreement and the validity, coverage,
   and regression guards. Otherwise B is unchanged.
5. Ending a direction is recorded agent judgment, not automatic refutation.
   When resources permit, a new direction begins from the current best program.
   Search can also end for resource reasons; this does not refute a direction.
6. The base model stays fixed; the editable object is the complete evaluation
   program. The output is frozen after search and terminal checks.

These map to the current paper-memory specifications C15, C16, C17 and C31.
No efficacy claim is introduced; the C28 evidence gap remains unchanged.

## Review gates before rendering finished art

- At thumbnail size, the green within-direction path is dominant.
- The same complete-program shape repeats, so these are revisions, not separate
  evaluator components in a fixed pipeline.
- Measurement and direction-exit links never cross.
- No acceptance edge controls the green continuation edge.
- New direction is unambiguously outside the active-direction field.
- Short incoming/outgoing group connectors do not masquerade as stage links.
- Preserve actual whitespace. If a label does not fit at about 7 pt in the
  full-width paper figure, shorten it or move it to the caption; do not shrink it.
- This study tests only c's proportions. Full-figure and paper-size readability
  still need checking before integration. Existing a/b/d tiny labels are not
  declared fixed by this c-only study.

Wireframe source: `build/overview-panel-c-layout/plan.svg`.
Preview: `build/overview-panel-c-layout/plan.png`.
