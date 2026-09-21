# Figure 2c — action-cycle review candidate

## Scope and approved scheme

One generated review image following the author's approval of the action-cycle
layout. Preserve the four-panel envelope, a/b/d illustrations and lake-green
style; replace c's internal organization. This is not a manuscript replacement
or a GitHub push.

The main row is Propose direction → Revise program → Evaluate candidate →
Diagnose. The short green return targets Revise; the longer gray return targets
Propose. Candidate acceptance independently branches from Evaluate to B above.
Only B feeds downstream applications after search. The checking set is a small
evaluation input. No repeated candidate trajectory is requested.

Current layout: `overview-panel-c-layout.md`. The earlier two-round wireframe
is superseded and was not used as a generation input.

## Method grounding

Checked against `sections/method.tex`: selection and direction continuation
are separate; diagnostics retain observations separately from interpretation;
working-parent choice remains conservative rather than unconditional candidate
inheritance. Ending a direction is an explicit, recorded agent decision, not a
certified rejection or a guaranteed local-budget commitment. The diagram must
not imply measured improvement or a minimum revision depth. Detailed guards,
parent choice and terminal-validation policy remain caption/Method material.

## Generation provenance

- Skill: imagegen, previously authorized fallback CLI/API route.
- Unmodified CLI: `/home/azureuser/.codex/skills/.system/imagegen/scripts/image_gen.py`.
- Endpoint: `http://127.0.0.1:8811/v1`.
- Requested deployment: `gpt-image-2`; not independent verification of the
  provider's upstream model identity.
- Input: `output/imagegen/overview-panel-c-method-20260921-v10.png`.
- Input SHA-256: `26997e298482e86c2ac7458e35245c721e6d374b5e4c6b1d60c3e4d10eedc6df`.
- Prompt: `prompts/overview-panel-c-action-cycle-v11.txt`.
- Output: `output/imagegen/overview-panel-c-action-cycle-20260921-v11.png`.
- Settings: high quality, auto size, PNG, no augmentation, one image.
- First attempt: HTTP 404, no image. One unchanged retry submitted.
- Retry completed in 100.3 seconds.
- v11 SHA-256: `d06811621125cd7f8d8b1452ee7f4b2958a37274a961aac834a3bdb98de07d3c`.

## V11 review and targeted correction

The four-action row and different green/gray return destinations are visible.
Acceptance originates at Evaluate, and B has a locked output after search.
The a/b/d pictorial composition is broadly preserved. Three defects remain:
the active-direction field includes Propose; an old black downstream distributor
has no source; and the checking-set input lacks a connector. These are diagram
errors, not changes to the Method.

One targeted edit keeps all node positions and artwork while moving the field's
left edge, removing the obsolete distributor, and adding the checking-input
arrow. Prompt: `prompts/overview-panel-c-action-cycle-v12-fix.txt`.
Input: v11; output: `output/imagegen/overview-panel-c-action-cycle-20260921-v12.png`.
Same model, endpoint, CLI and settings. The v11 intermediate will be archived
with v10; only the latest candidate stays in the output directory.

## Delivered V12 and inspection

- Targeted edit: first request returned HTTP 404; unchanged retry completed
  in 143.4 seconds. Output is a 1630 × 965 PNG (1,320,439 bytes).
- SHA-256: `f3169240b9af4d0fb3f4ea9d892082e701793c36014a16afa03da45a5190bf40`.
- The active-direction field now excludes Propose and contains Revise,
  Evaluate, Diagnose and the short return. Green returns to Revise; gray
  returns to Propose, without a crossing.
- Checking has a small input arrow into Evaluate. Acceptance independently
  leads from Evaluate to B; its output passes a lock marked After search and
  enters the downstream group. The obsolete black distributor is removed.
- The a/b/d layout and pictorial style are broadly preserved, not certified
  pixel-identical: the generative edit slightly redraws details and changes
  the canvas width by one pixel.
- This is a schematic review candidate, not a print-approved or integrated
  figure. Parent choice, resource exits, fixed-model status, aggregate-only
  checking access and observation/interpretation distinctions need the
  accompanying Method/caption. No measured gain or guaranteed depth is shown.

V10 and the intermediate v11 were moved to the external local archive at
`/home/azureuser/muzhao/tmz-figure-archive/20260921/overview/panel-c/`.
Their sizes and checksums are in `manifest.json`; destination hashes were
verified before removing the source paths. Protected references retain their
previous hashes. Output retains only v12 as the current panel-c candidate.
No manuscript assets were replaced and no GitHub push was performed.

## Review checklist

Verify all four main actions and their reading order, both return destinations,
an acceptance edge originating at Evaluate, B-only downstream output, field
boundary excluding Propose, readable labels, and preservation of a/b/d.
Record deviations explicitly before handing off. Keep the newest candidate
in output and archive superseded v10 with checksum verification, retaining
the approved references and source prompts.
