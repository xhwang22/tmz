# Illustration provenance

Updated 2026-09-17 for the palette-candidate and main-text composition pass. See
[visual_references.md](visual_references.md) for the inspected papers and
the specific communication choices adopted. Their figures were not copied,
traced, or uploaded to the image service.

## Current use and preserved lineage

The three scene images are 1536×1024 RGB PNG, generated with `gpt-image-2`, quality
`high`. The selected deployment reported model version `2026-04-21`; no other
image model was substituted. Exact hashes and input-image lineage are recorded
in [figure_assets.json](figure_assets.json).

| Asset in `output/imagegen/` | Operation and input | Manuscript use | Prompt in `.paper/prompts/` |
| --- | --- | --- | --- |
| `edit-source.png` | Generate a blue bowl on a pale stone table | Archived source; not referenced by the current manuscript | `edit-scene-source.txt` |
| `edit-preserved.png` | Edit source: add a red mug, preserve the bowl and scene | Fig1(a), synthetic image-family vignette | `edit-scene-preserved.txt` |
| `edit-omission.png` | Edit preserved candidate: remove only the bowl and its shadow | Archived omission example; not referenced by the current manuscript | `edit-scene-omission.txt` |

The preserved lineage illustrates the instruction “Add a red mug. Preserve the
blue bowl.” All three images were inspected after generation. The earlier
three-image comparison and its native TikZ annotation are now archived. The
active photo is a constructed illustration, not a benchmark artifact,
generator output under evaluation, human feedback, or measured result.

## Verified generation route

- Service: the user-authorized Azure Foundry resource, using the **resource-level**
  `/openai/v1/` base URL and `/images/generations` / `/images/edits` APIs.
  The project URL is resource context, not the base URL of these verified calls.
- Tooling: imagegen skill's bundled, unmodified `image_gen.py` CLI via
  `uv run --python 3.11 --with openai --with pillow`; OpenAI SDK 3.14.1 and
  Pillow 12.3.0. The source research environment was not modified.
- Authentication: `az account get-access-token` with resource
  `https://cognitiveservices.azure.com`. A short-lived Entra token is held only
  in the command's `OPENAI_API_KEY`; the SDK sends Bearer authentication.
  The token is neither printed nor written to disk or this repository.
- Commands: `generate` or `edit`, `--model gpt-image-2`, the recorded
  `--prompt-file`, `--size 1536x1024 --quality high --no-augment`, explicit
  `--out`; editing additionally supplies the recorded `--image`.
- Generation completed in 97.7 seconds, the mug edit in 103.3 seconds, and the
  omission edit in 97.9 seconds. These are preparation timings, not service
  guarantees or scientific experiment measurements.

The preserved image prints at 1.96 cm in Figure 1(a), approximately 1991 DPI.
The declared maximum width remains 3 cm, a conservative 1300-DPI budget rather
than the actual placement size. The checker requires at least 600 DPI, checks explicit
TeX widths against each asset's declared maximum, and verifies PNG dimensions
and SHA-256; it does not mistake a small photo for a full-page raster.

## Disclosure and privacy

All authoritative labels, mathematical expressions, evidence pointers, and flow
arrows in conceptual diagrams are editable TikZ. Quantitative marks, axes, and
labels are vector PDFs produced by `scripts/render_simulated_results.py`, not
by an image model. Webpage, text, and research vignettes are constructed too.
The relevant captions and AI use statement distinguish illustrations and
simulated data from observations. Reference artwork supplies no evidence.

Prompts contain invented scenes and generic aesthetics only. No private examples,
human annotation records, observed metrics, credentials, or experiment logs were
sent to the service. Building the PDF and figure previews uses committed assets
and makes no model API calls.

The present round uses three complete vector-chart palettes based on the
author's labeled color references, provisionally retaining reference 1's
blue/mint/cream/peach/rose ensemble. The main C1 atlas now covers all 22 domains;
the unchanged eight-domain annotation/component/C2 diagnostics are explicitly
bounded appendix details.
Original reference thumbnails appear only in local review boards; they are
not manuscript assets or inputs to an image-generation service.
Eight explicitly simulated quantitative figures use 14 CSVs. Fourteen C1
domains were added for coverage; original C1 records/intervals and diagnostic
data are preserved. This is not evidence of 22 executed evaluations.
The photograph files, model
provenance, lineage, and hashes are unchanged; this round makes no new model
calls. The working Azure route was already recorded in the author-requested
API guide outside this paper repository.

The round-2 `domain-panorama-final.png` and its prompts remain an explicitly
archived asset, not an active manuscript graphic. Earlier overviews remain in
git history. Final author review is still required.

## September 19 chart insertion

Main Figure 2 now uses the approved native-vector v20 landscape composition.
It is not an image-model output. PDF/SVG/PNG and balanced synthetic exports live
under figures/simulated/landscape_outcomes.* and data/simulated/landscape/.
Earlier atlas descriptions above are historical. No new image calls were made.
