# Illustration provenance

- Selected asset: `output/imagegen/domain-panorama-final.png`, 3840×1280,
  RGB PNG, quality `high`. SHA-256 is recorded in `figure_assets.json`.
- Model: `gpt-image-2`; the user-selected deployment reported version
  `2026-04-21`. The route was not substituted with another image model.
- Service: the user-authorized Azure Foundry resource, through the compatible
  `/openai/v1/` generation and editing endpoints.
- Tooling: imagegen skill's bundled `image_gen.py` CLI, isolated Python 3.11,
  OpenAI SDK 3.14.1, Pillow. The source experiment environment was not changed.
- Credentials: a short-lived Microsoft Entra token was acquired at invocation
  time, used process-locally, and never written into the repository or output.
- Prompts: `prompts/domain-panorama.txt` and
  `prompts/domain-panorama-cleanup.txt`.
- Generation: four domain-family vignettes covering visual artifacts, images/3D,
  text, and automated research. The targeted edit removed invented text,
  pseudo-citations, and an unrequested decorative icon.
- Selection: only the reviewed final image is published. Rejected versions and
  the replaced overview are not active manuscript assets.
- Resolution: approximately 698 DPI at a full 5.5-inch text width.

The image is used only in Figure 1(a). Miniatures, including pictured chart
interfaces, are synthetic artwork, not measurements or experimental screenshots.
All authoritative labels, mathematical expressions, flow arrows, and remaining
figures are editable TikZ. The caption and AI use statement disclose the image's
status. Final author review remains required.

Prompts contain generic tasks and aesthetics only. No private examples, human
annotation records, observed metrics, credentials, or experiment logs were sent
to the image service. These prompts record figure preparation, not scientific
debugging history. Building the PDF uses committed assets and performs no API calls.

The previously used 3840×2160 overview and its prompts remain recoverable in git
history but are superseded by the four-family panorama plus native P2E diagram.
