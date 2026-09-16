# Manuscript style

- Use formal, direct academic prose with a scientific argument. Do not narrate
  debugging, historical runs, infrastructure work, or abandoned intermediate methods.
- Distinguish specifications, hypotheses, implementation availability, and findings.
  Plans and synthetic examples are not empirical evidence.
- Use the unbranded title "Evolving Evaluation Systems from Human Feedback for
  Open-Ended Tasks".
  Do not use P2E as the current paper/project name. ERA names only the evaluator
  evolution method; do not invent an expanded acronym. Historical provenance
  and source filenames are not renamed. Retain the four-family scope.
- Lead with the source plan's problem: automated evaluation struggles to align
  with task-dependent human preferences. An observed preference records a
  judgment without fully specifying the criteria and evidence for new outputs.
  Preference-data-driven evaluation-agent self-evolution is the response.
  The author-approved abstract order is alignment difficulty, the gap between
  preference feedback and an executable evaluation procedure, agent evolution,
  and cross-task validation. Error diagnosis supports this argument; it is not
  the paper's central problem. Explain acquisition and evolution through their
  roles in that argument. Keep parameter-fitting contrasts, search-state
  mechanics, data-provenance protocols, and lists of domains or study arms out
  of the abstract. Human standards remain the target, not objects the agent
  invents. Executable programs do not establish complete or faithful explanations.
- Explain parameter adaptation fairly. Fixed-structure evaluator fine-tuning
  changes the mapping from observations to judgments; calibration changes
  existing numerical decision rules. ERA changes the explicit program with a
  fixed base model. Fine-tuning can also learn criteria or tool use when its
  interface permits them. Do not assert that it is incapable, data-inefficient,
  or inferior. Include a shared-observation control and account for resources.
  Evaluator fine-tuning is distinct from C3 generator training. Neither is run.
  Inspectable criteria/traces do not establish faithful reasoning or alignment.
- Domain means a shared evaluation standard, not an artifact modality.
  Do not imply one scorer transfers universally across 22 domains.
- H0 = overall; H1 = dimension preference and core supervision; H2 = structured
  error/severity/localization; H3 = optional human rationale. H0-only data remain
  useful but cannot be relabeled as H1/H2. Model reasoning is not human rationale.
- Reusing existing preferences and collecting new preferences are two
  data-construction settings for the same task-plus-human-feedback problem.
  A domain can use both; existing H0 is not a domain-admission requirement.
  Preserve separate provenance, protocols, agreement, abstention, and results.
  Newly collected labels are not presumed superior. Corpus construction does
  not establish sampling efficiency; require a matched-budget random control.
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
  Mechanism hypotheses are the units of exploration; complete programs are
  the units of selection. Alignment, useful critique, and useful reward under
  optimization are separate capabilities that require separate evidence.
- Bound causal language to controlled paired attribution; connected-bundle gains
  do not establish each component's independent contribution.
- Keep caveats near relevant claims without repeating draft-status notices in
  every paragraph. Avoid promotional novelty claims and universal dismissals
  of existing program optimizers.
- Prefer quantitative displays over redundant conceptual diagrams. Retain the
  overview and pointwise runtime; use paired-effect forest plots, budget curves,
  an annotation audit, rank composition, an annotated heatmap with box/strip
  plots, raincloud distributions, and quality–cost scatter for distinct questions.
  Chart variety must follow the quantity, not decoration. Avoid unnecessary 3D,
  radial charts, heavy frames, and decorative significance markers.
- The author explicitly authorized simulated data for reporting/layout review.
  This is an exception for transparently labeled fixtures, never permission to
  fabricate evidence. Disclose simulation in the title-page notice, section,
  image, caption, each data row, and manifest. Effects, intervals, costs, cohort
  assignments, and artificial raters are neither observations nor predictions.
  Retain null/negative contrasts; do not manufacture a uniformly winning method.
  No simulated C3 training. Never upgrade C27/C28 based on these fixtures.
  Use GPT Image 2 only for disclosed illustrative bitmaps; exact labels, flows,
  equations, axes, and quantitative marks remain native vector graphics.
- The author's requested references take priority: the post-training survey
  (2503.06072), full-stack safety survey, Speculative RAG, and MMMR. Adopt airy
  grouping, illustrated roles, curved information paths, and a diverse task
  gallery, not their artwork, data, or results. Earlier Self-Refine, Eureka,
  TextGrad, and SAM examples remain secondary references for evidence alignment.
  Record figure/page/source and the mapping in `visual_references.md`.
- Reconcile all three author references through blue #376795, sky #7BC0CD,
  teal #51999F, mint #BFDFD2, sand #DBCB92, cream #FFE6B7, peach #ECB66C, and coral
  #ED8D5A. Dark ink #303C43 and darker companion colors keep small text readable.
  ERA is coral and the static tool-augmented seed is blue. Setting comparisons
  use teal for reused preferences and peach for new preferences. Where color
  instead encodes ranks, signed effects, or outcomes, state that mapping in the
  legend/caption. Keep labels, shapes, line patterns, and hatching as redundant
  cues. Preserve softly tinted surfaces and original pictograms in diagrams.
- Keep ICLR body fonts, margins, and heading rules unchanged. Figures use
  Helvetica-compatible typography: scoped `phv` in TikZ and TeX Gyre Heros in
  Matplotlib. Main chart titles are 8.5 pt, axis labels 8 pt, tick/legend labels
  about 7.3–7.5 pt; 6.8 pt is reserved for fixture-disclosure notes. The native
  chart canvas is 5.4 inches wide and is not silently cropped or reduced.
  Use aligned numeric columns, booktabs rules, light row emphasis, and readable
  row spacing. Inspect complete pages as well as individual charts for orphaned
  text, detached captions, icon collisions, excessive whitespace, and font
  embedding; a successful compilation alone is insufficient.
- Show domain diversity through concrete artifacts and different quality
  criteria, not modality names alone. The overview, complete 22-domain table,
  and per-domain quantitative panels share a procedure while retaining distinct
  evaluation standards. Eight toy cohorts are display choices, not scope cuts.
- Shared palette, panel markers, candidate tokens, and component styles live in
  `figures/visual_style.tex` and `preamble.tex`. Review standalone figures and
  final manuscript pages; a successful TeX build does not detect label collisions.
