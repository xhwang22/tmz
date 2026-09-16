# Manuscript style

- Use formal, direct academic prose with a scientific argument. Do not narrate
  debugging, historical runs, infrastructure work, or abandoned intermediate methods.
- Distinguish specifications, hypotheses, implementation availability, and findings.
  Plans and synthetic examples are not empirical evidence.
- P2E names the broader project. ERA names only the evaluator revision method.
  Use the broad open-ended-generation title and retain the four-family scope.
- Domain means a shared evaluation standard, not an artifact modality.
  Do not imply one scorer transfers universally across 22 domains.
- H0 = overall; H1 = dimension preference and core supervision; H2 = structured
  error/severity/localization; H3 = optional human rationale. H0-only data remain
  useful but cannot be relabeled as H1/H2. Model reasoning is not human rationale.
- Include upstream preference mining and the C3 design, but do not describe any
  parameter-training execution or training benefits without new authorization
  and evidence. Leave optional teacher variants and historical optimizer modes out.
- Keep many-to-many signal mappings and source dependence explicit. Mixed signals
  are not multiplied into independent votes. Different constructs can trade off.
- Use median artifact scores followed by strict comparison, not majority voting.
- Separate proposal Train, sealed Train aggregates, terminal Val, and Test/OOD.
  Independent reserved metrics never become tools, critics, rewards, or selectors.
- Separate a direction from its implementation, working from best program,
  continuation from promotion, and exhaustion from scoped refutation.
- Bound causal language to controlled paired attribution; connected-bundle gains
  do not establish each component's independent contribution.
- Keep caveats near relevant claims without repeating draft-status notices in
  every paragraph. Avoid promotional novelty claims and universal dismissals
  of existing program optimizers.
- Figures should use distinct visual forms for distinct relationships: artifact
  gallery and feedback loop, matrix, routed architecture, revision branches,
  matched study lanes, worked examples, access timeline, and factor synthesis.
  Use GPT Image 2 only for disclosed synthetic vignettes; exact labels, flows,
  and equations remain native TikZ. No fabricated performance curves or counts.
- Adopt inspected reference principles, not copied artwork: concrete editable
  objects from Self-Refine, a task-centered revision loop from Eureka, semantic
  information paths from TextGrad, and separate task/model/data views from SAM.
  Record figure/page/source and the mapping in `visual_references.md`.
- Avoid a default of repeated pastel cards. Use whitespace, dark section anchors,
  aligned examples, localized evidence, and semantic color. Candidate letters,
  hatching, and line patterns must also work without color. Principal labels
  remain 8–9 pt and subordinate labels about 7 pt at native manuscript size.
- Shared palette, panel markers, candidate tokens, and component styles live in
  `figures/visual_style.tex` and `preamble.tex`. Review standalone figures and
  final manuscript pages; a successful TeX build does not detect label collisions.
