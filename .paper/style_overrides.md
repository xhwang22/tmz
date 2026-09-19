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
  overview and pointwise runtime. Main Figure 2 shows every one of the 22 C1
  domains in fixed 6/6/5/5 taxonomy order: five OOD method columns with printed
  values and common-scale micro-bars, followed by paired ERA-minus-seed intervals.
  Method color is categorical, not a score heatmap. Keep all-domain ID/OOD
  intervals in appendix Figure 4. The mechanism/feedback-detail display is
  appendix Figure 8; C2 is separate in Figure 9. Keep the C1 numerical table and
  acquisition curves in the appendix. Use paired-effect interval tables, budget
  curves, an annotation audit, horizontal rank ribbons, an annotated heatmap
  with split violins and raw points, rainclouds with diverging preference bars,
  and aligned cost/agreement profiles for distinct questions. Keep abstentions
  separate from either winner in preference balances; all-input denominators
  remain unchanged. Cost connectors pair settings, not evolution steps.
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
- Use the three supplied color references independently; the author rejected
  the previous four invented palette directions. `palette_candidates.md`
  records exact labeled HEX values and source-to-role mappings. The provisional
  manuscript uses reference 1: blue #74A9C5, mint #C2E5CF, cream #EDDDAB,
  peach #F2B8AE, and rose #DD7389. Alternatives follow reference 2's blue/orange
  and reference 3's teal/apricot sequences. Do not add purple or copper fills,
  or arbitrarily deepen the primary blue. No final author choice is assumed.
  Use white paper and neutral ink #25272B; small numerals use #202226.
  Use the complete five-color ensemble for the five non-metric methods:
  static judge blue, static tools/seed mint, prompt optimization cream,
  program search peach, and ERA rose. Metric-only references stay gray.
  Where color instead encodes families, H levels, policies, ranks, or outcomes,
  state that mapping explicitly. Settings use left/right position and sparse
  hatching in split violins, not another competing color scale.
  Keep labels, shapes, line patterns, and hatching as redundant
  cues. Preserve softly tinted surfaces and original pictograms in diagrams.
  Keep source base fills intact; use dark numerals instead of deepening fills
  for white labels. Density fills use 88% source color over white. The heatmap
  uses the complete five-color sequence, cream at zero, and fixed ±6 limits. Derive
  darker companions only for fine strokes and small diagram labels; do not
  add chromatic plot headings. In split violins, label halves left/right.
  All five acquisition policies use equal-width strokes and individual bands.
  Audit grayscale proofs and 29 small-text contrast pairs in each palette.
  Palette previews stay in `build/` and must match all 14 CSVs and the numerical
  table byte for byte; changing colors cannot change any simulated observation.
  Check all 110 atlas values and 22 paired intervals against canonical CSVs.
- Keep ICLR body fonts, margins, and heading rules unchanged. Figures use
  Helvetica-compatible typography: scoped TeX Gyre Heros (`qhv`) in the main
  overview, `phv` in the runtime diagram, and TeX Gyre Heros in Matplotlib.
  The overview uses 8.5 pt panel headings, 7.4 pt card headings/body labels,
  7 pt notes, and an 11 pt ERA label. Reserve bold for headings and ERA;
  keep action labels regular. Retain explicit card insets, consistent row
  spacing, and the figure-local `transform shape` setting so pictograms respect
  their specified scales. Do not shrink the entire figure to hide crowding.
  Main chart titles are 8.5 pt, axis labels 8 pt, tick/legend labels
  about 7.3–7.5 pt; 6.8 pt is reserved for fixture-disclosure notes. Component
  sublabels and setting labels use 7 pt with explicit spacing. The native
  chart canvas is 5.4 inches wide and is not silently cropped or reduced.
  Separate bold panel letters from regular-weight headings; use fine header
  rules, direct endpoint labels, quiet row guides, and aligned estimates.
  The compact simulation badge and its companion notice remain visible and
  text-extractable in every quantitative figure.
  Use aligned numeric columns, booktabs rules, light row emphasis, and readable
  row spacing. Inspect complete pages as well as individual charts for orphaned
  text, detached captions, icon collisions, excessive whitespace, and font
  embedding; a successful compilation alone is insufficient.
- Show domain diversity through concrete artifacts and different quality
  criteria, not modality names alone. The overview, complete 22-domain table,
  and per-domain quantitative panels share a procedure while retaining distinct
  evaluation standards. Main C1 and expanded alignment must show all 22 tasks,
  not just four family averages. C1 summaries use 11 domains per setting.
  Eight-domain annotation/component/C2 details are explicitly bounded diagnostic
  subsets; neither full nor subset fixtures imply empirical completion.
  R/N tags are synthetic construction assignments, not verified label availability.
- Shared palette, panel markers, candidate tokens, and component styles live in
  `figures/visual_style.tex` and `preamble.tex`. Review standalone figures and
  final manuscript pages; a successful TeX build does not detect label collisions.

## Latest composite-preview color direction (2026-09-17)

For the UNI-style integrated review figure, the author's latest instruction
supersedes the earlier five-hue method mapping: keep ERA as a single chromatic
accent and the four baselines as a subordinate, single-hue light-to-dark ramp.
Choose those hues to harmonize with the task ring; do not restore five equally
prominent colors per bar group. Apply the same mapping to bars, scatterplots,
and their shared key. Keep the ring's four family hues and its clockwise
light-to-dark progression within each family. These are categorical colors,
not performance encodings. Preview approval does not replace manuscript assets.

## Approved writing direction (2026-09-19)

- In revised LaTeX prose, put one complete sentence on each source line, with a blank line between paragraphs.
  Do not wrap sentences at an arbitrary character width or insert forced PDF line breaks.
  Apply this to the abstract, introduction, and their captions now; preserve unrelated sections until they are revised.
- Use the approved chain: difficulty of human-aligned open-ended evaluation, preference/procedure gap, why agent evolution is a useful candidate approach, acquisition and optimization obstacles, then the method principle and its empirical tests.
  GEPA, Meta-Harness, and DGM guide argument structure, not borrowed results or a claim that all prior optimizers are greedy.
- Explain acquisition by reducing redundant annotation of easy comparisons and recurring patterns, not by claiming the agent knows which samples intrinsically deserve human judgment.
  Consensus is not truth; preserve the random anchor and compare final evaluator gains at equal human cost.
- Motivate depth-first search with observed default rejection/redirection, not an imagined generic generalization failure.
  Distinguish a direction's initial implementation from its attainable value.
  Separate adopting a candidate from continuing its direction; refutation requires evidence against the hypothesis, while resource exhaustion is not refutation.
  These are design principles, not proof that DFS is necessary in every task or already superior.
- Keep pointwise scoring as the main interface and avoid reciting the pairwise development chronology.
  Give mining and depth-first evolution distinct roles in the same learning problem, without a component inventory in the abstract.
- Keep C27/C28 as explicit open comparisons.
  A qualitative development observation may motivate the method, but must not turn simulated displays or unsuccessful confirmatory comparisons into favorable results.

## Inserted landscape composite (2026-09-19)

The author-approved v20 landscape figure now replaces the atlas in main Fig2.
This supersedes earlier atlas and five-hue-method instructions for Fig2 only.
Keep the four-quarter task ring, right cost/agreement scatter and four family
bar panels in one row. Baselines use pale family ramps; ERA uses one lake-green
accent. Keep Source Sans 3 / Source Serif 4 and the native 5.4 × 3.57-inch canvas.
The selected 2,880 synthetic inputs are a fixed-hash subset, not the full appendix
cohorts; document that distinction and retain all simulation disclosures.
Do not retune data to improve visual rankings. Full-cohort paired effects remain
in Fig4, not Fig2. Other chart styles are unchanged in this integration pass.

## Approved argument refinement (2026-09-19)

- Keep learning human-aligned evaluation procedures as the paper-level question.
  Feedback efficiency connects acquisition and evolution but does not replace
  that question. Do not brand them as a new two-stage theory or rigid pipeline.
- Give ERA more explanatory space than acquisition. Introduce the observed
  rejection/redirection pattern, then why interacting evaluation steps can
  require further implementation, then candidate acceptance versus continuation.
  Bound the observation to the tested optimizer configuration.
- One unsuccessful implementation is insufficient to reject its direction;
  it is not devoid of negative evidence. Unfinished implementation alone does
  not justify indefinite continuation. Budget exhaustion is not refutation.
- Consensus does not establish correctness. Use agreement among existing signals,
  not claims that those signals already understand or resolve human judgments.
- Use human feedback as the umbrella term and human preferences for preference
  judgments. Use preference acquisition for the process and disagreement-based
  preference acquisition for this allocation. Avoid cycling through supervision,
  feedback, and preferences as stylistic substitutes.
- An evaluation procedure describes what the evaluator does; an evaluation
  program is its editable implementation. A candidate is a complete evaluator
  version. A direction specifies an intended improvement; its hypothesis states
  a testable prediction. Use implementation rather than rotating synonyms.
- Move detailed adaptation controls and annotation provenance out of the early
  introduction. Preserve them in Methods/Experiments and the appendix.
  Keep the abstract a single paragraph and revised source one sentence per line.
- Do not remove simulation disclosures or turn planned comparisons into completed
  studies to make the prose sound more conclusive.

## Argument compression and terminology (2026-09-19, round 17)

- Make the acquisition-to-evolution link explicit: obtain informative preferences,
  then turn the problems they reveal into working evaluation-procedure changes.
  Keep learning human-aligned evaluation as the research question; do not recast
  the paper as a generic claim about feedback efficiency.
- Introduce preferences as the form of human feedback used here. This does not
  exclude the richer H2/H3 feedback defined in Methods or change pointwise scoring.
- Reserve disagreement in the revised abstract/introduction for conflict among
  existing evaluation signals. Use errors revealed by human feedback for mismatch
  between the evaluator and human preferences.
- Use diagnostic results for search-level implementation checks; keep artifact
  evidence distinct. Do not use an ambiguous new evidence to bridge the levels.
- Explain that immediate-gain-based acceptance can also curtail further work,
  but do not elevate observed rejection/redirection into an enforced baseline
  stopping rule, universal first-attempt abandonment, or proof of useful directions.
- Consensus is an acquisition proxy, not proof that a comparison is resolved
  correctly or intrinsically easy. Preserve random checks for shared blind spots.
- End the introduction with the learning problem and the roles of the two stages,
  followed by a compact evaluation scope. Reduce repeated planned/protocol wording
  without changing unmeasured comparisons into completed empirical studies.
- Add prior work only at the claim it supports. AutoCalibrate refines criteria,
  not only scores; Agent-as-a-Judge gathers evidence but does not establish
  feedback-driven evaluator evolution. Active preference learning motivates
  selective acquisition, not this paper's human-cost or alignment gains.
  Prefer verified published metadata and record each new citation's claim scope.

## Citation identity, publication and claim support (2026-09-19, round 18)

- Check identity, publication fields and cited claim support separately. A valid
  DOI or an exactly-one index match does not certify the venue or the sentence.
- Verify journal/booktitle, publication year, volume, issue, pages, DOI and version
  where applicable. Distinguish main proceedings, Findings, workshops and preprints.
  Never infer a formal venue from a paper's topic, author reputation or a search snippet.
- Resolve conflicting index/BibTeX/PDF metadata field by field against the original
  publication artifact; retain the conflicting values and decision in the audit.
  Do not overwrite published author names or titles with a preprint/index variant.
- Cite unconfirmed publication status explicitly as a verified arXiv preprint;
  do not invent missing pages, volume, DOI or acceptance. Preserve verification
  tiers and dates, including author-side comments versus proceedings records.
- Include the four requested papers in their relevant Related Work discussions,
  with their actual scope. Benchmark construction, skill utility, learned rubrics
  and reward-hacking taxonomy do not prove our acquisition or search advantages.
- Keep citation checks reproducible and report unresolved matches, source anomalies
  and parser limitations. Do not describe a mixed-result audit as all passed.
