# Illustration provenance

Updated 2026-09-16 for the reference-informed visual redesign. See
[visual_references.md](visual_references.md) for the inspected papers and
the specific communication choices adopted. Their figures were not copied,
traced, or uploaded to the image service.

## Active generated assets

All three images are 1536×1024 RGB PNG, generated with `gpt-image-2`, quality
`high`. The selected deployment reported model version `2026-04-21`; no other
image model was substituted. Exact hashes and input-image lineage are recorded
in [figure_assets.json](figure_assets.json).

| Asset in `output/imagegen/` | Operation and input | Manuscript use | Prompt in `.paper/prompts/` |
| --- | --- | --- | --- |
| `edit-source.png` | Generate a blue bowl on a pale stone table | Fig7(b), source | `edit-scene-source.txt` |
| `edit-preserved.png` | Edit source: add a red mug, preserve the bowl and scene | Fig1(a), Fig6(b), Fig7(b) candidate B | `edit-scene-preserved.txt` |
| `edit-omission.png` | Edit preserved candidate: remove only the bowl and its shadow | Fig7(b) candidate A | `edit-scene-omission.txt` |

The photographic comparison illustrates the instruction “Add a red mug.
Preserve the blue bowl.” All three images were inspected after generation.
The omitted bowl is circled by native TikZ, not an image-model annotation.
The scenes are constructed illustrations, not benchmark artifacts, generator
outputs under evaluation, human feedback, or measured results.

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

The source, omission, and preserved images print at 1.94 cm width in Figure 7(b):
approximately 2011 DPI. The preserved image prints at 1.96 cm in Figure 1(a)
(approximately 1991 DPI) and 1.68 cm in Figure 6(b) (approximately 2322 DPI).
The declared maximum width remains 3 cm, a conservative 1300-DPI budget rather
than the actual placement size. The checker requires at least 600 DPI, checks explicit
TeX widths against each asset's declared maximum, and verifies PNG dimensions
and SHA-256; it does not mistake a small photo for a full-page raster.

## Disclosure and privacy

All authoritative labels, mathematical expressions, evidence pointers, flow
arrows, and other diagrams are editable TikZ. Native webpage, text, and research
examples are also synthetic. The relevant captions and AI use statement disclose
their status. Reference figures and factual plots are never generated evidence.

Prompts contain invented scenes and generic aesthetics only. No private examples,
human annotation records, observed metrics, credentials, or experiment logs were
sent to the service. Building the PDF and figure previews uses committed assets
and makes no model API calls.

The author's blue/mint/cream/peach/rose palette and the expanded task gallery
were implemented in native TikZ in round 4. The three photographs, model
provenance, lineage, and hashes are unchanged; this round makes no new model calls.

The round-2 `domain-panorama-final.png` and its prompts remain an explicitly
archived asset, not an active manuscript graphic. Earlier overviews remain in
git history. Final author review is still required.
