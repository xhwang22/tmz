# Conceptual illustration provenance

- Model/deployment: `gpt-image-2` (OpenAI); the deployment listing reported model
  version `2026-04-21` on 2026-09-16.
- Service: the user-designated Azure Foundry resource, through its Azure OpenAI
  compatible `/openai/v1/` image generation and image editing APIs.
- Mode: the imagegen skill's bundled CLI, explicitly authorized API/model route.
- Runtime: isolated Python 3.11 and OpenAI SDK 3.14.1. The source experiment
  environment was not modified. Credentials were acquired at invocation time,
  remained process-local, and are not stored in the repository.
- Asset: `output/imagegen/overview-final.png`, 3840 by 2160, PNG, quality `high`.
  At the 5.5-inch print width its effective resolution is approximately 698 DPI.
  Exact asset hash and generation settings are in `figure_assets.json` and are
  verified by `make check`.
- Generation prompt: `prompts/overview.txt`.
- Focused edit prompts: `prompts/overview-correction.txt` and
  `prompts/overview-final-correction.txt`.

The prompts specify the same scientific structure as the text: human overall
preferences guide ERA's revision method; the six-component evaluation program
uses a fixed base model; sealed development supplies aggregate feedback to
revision; a frozen evaluator receives one artifact without preference labels.
The figure does not claim that one learned scorer transfers across standards.
Artifact miniatures are illustrative, not benchmark examples or measurements.

The image and arrows require author review alongside the manuscript before
submission. The caption and AI use statement disclose the generated illustration.
The exact evaluator and data-access diagrams remain editable TikZ sources.

Only the selected final image is published. Prompts record figure preparation,
not the history of scientific experiments or intermediate research methods.
Building the paper consumes the committed image and makes no model API calls.
No endpoint credential, private artifact, empirical trace, or observed result
was supplied in these image prompts.
