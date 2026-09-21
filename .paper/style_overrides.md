# Manuscript style

## Method language and implementation limits (2026-09-21, round 40)

- Preserve round39's core-first structure; make local edits, not a new framework.
  Give a short complete cycle before Algorithm 1 so its actions are introduced.
- Use evaluation program for the editable object and evaluator for the system.
  Prefer propose, revise, evaluate, accept, continue/end, update and return.
  Avoid search opportunity, allocation ends, eligible C and support a pause.
- Keep acceptance and continuation as the two high-level decisions. Describe
  the next working program as a conservative parent choice within continuation;
  retain the actual pre-update best fallback and incomplete-local-data edge.
- Distinguish recorded executions and outcomes from agent interpretations and
  unresolved questions. Neither a model explanation nor a changed trace field
  is a verified causal account.
- A direction's error and intended correction guide revisions. The implementation
  preserves the identifier/history, not immutable semantics. Ending requires an
  explicit recorded action but no verified reason category or minimum depth.
  Do not invent stronger semantic or continuation gates in prose.
- Separate offline label-access budgets from new annotation counts and time.
  Count random-anchor labels within the corresponding budget; ranking-derived
  pairs do not create independent annotation units.
- Preserve author-edited Abstract/Introduction and all artwork. Update only the
  overview caption for terminology; keep detailed checks in the appendix.

## Core-first Method hierarchy (2026-09-21, round 39)

- Keep Method in one TeX source. Use Overview and setup, brief disagreement-based
  preference mining, depth-first evaluator evolution, then Revision space.
- Open with direction as exploration unit and complete program as selection unit.
  Define persistent best/working programs, direction and diagnostic state before
  the six-component architecture or detailed measurement protocol.
- Keep only state, objective and acceptance/best update as main equations.
  Explain the direction lifecycle in the main algorithm; avoid decorative
  functions for prose operations.
- The high-level distinction is candidate acceptance versus direction continuation.
  Program inheritance is a working-program policy within continuation, not a
  third equal-level contribution. Preserve the actual pre-update fallback.
- Direction identity/history persist, while its intent may be refined. Pause
  reasons are model assessments, not controller-certified semantic conclusions.
  Preserve resource accounting for pauses and verified-record reuse for replays.
- This hierarchy supersedes the three-subsection and joint-update exposition
  guidance in rounds 37–38 below. Figure geometry and assets remain protected.

## Preserve the approved figure layouts (2026-09-21, round 36)

The author rejected the round-35 redesign of both main figures.
Figure 1 must directly print the approved three-column author-v6 SVG export,
including its wording, search trees and all nine images. Change method colors
to lake green only; do not substitute teaser-print.tex or reflow its panels.
Figure 2 retains the original four-panel pictorial overview: artifact cards,
mining cards, icon-led circular evolution loop and downstream assessment cards.
Keep its native canvas, pictograms, photographs, rounded surfaces and panel
positions. Fix local text/arrow collisions only; do not replace it with a
flat flowchart, strips, lanes or a state-machine diagram.
Small teaser labels are a documented readability limit, not authorization to
redesign. Method details remain in the caption and algorithm.
This instruction supersedes the rejected layout guidance below.

## Superseded layout guidance (2026-09-20, round 35)

Main Figure 1 is the author-v6 image-editing teaser; Figure 2 is the method
overview; Figure 3 is the existing C1 landscape. Keep Table 1 in the main text.
The ten appendix figures follow these three; table numbering is unchanged.
Use lake green `#62AAA5` and dark companion `#477D79` for method blocks and
search paths, matching the main performance figure. Reserve red for error
statuses, not method identity. This supersedes older rose-method instructions.
Preserve the updated three-column teaser SVG as an editable reference. Its
paper-specific native-size layout stacks the task above the breadth/depth
comparison, uses at least 7-point labels, and reuses the same three photos.
Illustrative success on one pair is not candidate acceptance or measured gain.
The overview must show repeated revisions, a possible direction switch, and
separate acceptance, inheritance, and continuation decisions; fallback uses
the pre-update best program without discarding diagnostic history.

## Title layout and abstract citations (2026-09-20)

Keep the abstract citation-free; retain literature support in the Introduction and Related Work.
Preserve the exact approved title with title-local ragged-right alignment and natural wrapping into two lines. The author rejected the forced three-line layout; do not restore manual breaks after the colon or Evaluators.
Keep the official title font, size, margins, and template file unchanged; do not stretch word spacing or leave Tasks alone on a line.

## Current terminology precedence (2026-09-20, round 32)

Follow `terminology.md` for current wording; it supersedes conflicting terms in all earlier notes below.
Use IterEval for the complete framework, with the tagline "iterative evaluator self-improvement from human feedback".
Use the title "Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks".
The two components are disagreement-based preference mining and depth-first evaluator evolution, without component acronyms.
Introduce the framework with "We present IterEval, a framework for self-evolving evaluators across open-ended tasks."
These instructions supersede the earlier unbranded-title requirement and IPM/ERA names below; historical records and implementation identifiers remain unchanged.
Motivate preference mining from reducing the priority of repetitive comparisons on which signals agree; do not assert that disagreement guarantees useful human feedback or that zero conflict establishes simplicity.
Keep candidate acceptance, program inheritance, and direction continuation distinct.
Use human feedback, human preferences, evaluation procedure, and evaluation program for their defined objects, not as stylistic substitutes.
Diagnostics support continued implementation; do not restore falsification-guided or another guided method name.
Historical audit quotations and revision entries retain their original wording.

## General constraints and earlier guidance

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
  Directions are the units of continued exploration; their hypotheses explain
  the intended correction, and complete programs are the units of selection.
  Alignment, useful critique, and useful reward under
  optimization are separate capabilities that require separate evidence.
- Bound causal language to controlled paired attribution; connected-bundle gains
  do not establish each component's independent contribution.
- Keep caveats near relevant claims without repeating draft-status notices in
  every paragraph. Avoid promotional novelty claims and universal dismissals
  of existing program optimizers.
- The current main displays are Figure 1 (overview), Figure 2 (the revised C1
  landscape), and Table 1 (C1 alignment/selection). Preserve Figure 2 in the
  main text at its native size. The budget placeholder is appendix Figure 4,
  and C2/C3 placeholders are appendix Table 8. The original landscape is
  appendix Figure 5; preserve its assets, data, palette and provenance.
  Full-cohort paired effects are Figure 6, components Figure 10, and refinement
  Figure 11. Do not confuse the historical balanced subset with the new full-
  cohort C1 display. Keep placeholder results visibly unmeasured; ideal analysis
  uses conditional language rather than fictional findings. Do not shrink
  official typography to fit new tables or formulas.
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

## Landscape composite style (updated 2026-09-20)

The author-approved v20 landscape remains unchanged as appendix Figure 5.
Its adapted version is main Figure 2; both use the following palette and layout.
Keep the four-quarter task ring, upper-right scatter and four family
bar panels in one row. Baselines use pale family ramps; ERA uses one lake-green
accent. Keep Source Sans 3 / Source Serif 4 and the native 5.4 × 3.57-inch canvas.
The original 2,880 synthetic inputs are a fixed-hash subset, not the full cohorts.
Main Figure 2 instead uses all jointly complete OOD inputs per task for agreement,
and all requested inputs for Best-of-4, counting failed scoring as failed selection.
Its ring denotes taxonomy, not sample proportions; its scatter links agreement
and selection rather than assigned cost. Retain every simulation disclosure.
Do not retune data to improve visual rankings. Full-cohort paired effects remain
in Figure 6. The historical landscape and underlying observations are unchanged.

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

## Argument focus (2026-09-19, round 19)

- Open with why open-ended evaluation is difficult: task-specific criteria and
  trade-offs. Introduce limitations of existing evaluators after that problem.
- Let the preference/procedure gap lead directly to the research question.
  Place prior work after the question or capability it supports, without
  deleting the verified references or expanding their attributed scope.
- Keep one explicit acquisition-to-evolution bridge. Do not add repeated
  definitions of two stages, two failures, and wasted feedback.
- State the observed rejection/redirection pattern directly, then state that
  rejecting a candidate need not end work on its direction as a design principle.
  Do not turn this principle into a verified causal rule of the tested optimizer.
- Preserve agreement rather than resolved judgments as the acquisition proxy,
  and program evolution as a research choice rather than a necessary alternative
  to score fitting or fine-tuning. Sentence focus should follow the argument,
  not a mechanical requirement to place every new concept in the subject.

## Method exposition and implementation boundary (2026-09-19, round 20)

- Use GEPA, Meta-Harness, and DGM as structural exemplars, with SkillOpt as an
  auxiliary terminology reference. Explain the executable evaluator and its
  measurement, then error-driven candidate changes, acceptance versus
  continuation, and failure interpretation. Do not borrow their results or
  characterize their search policies as uniformly greedy.
- Keep pointwise execution central. A complete program is the selection unit;
  a direction is the continued-exploration unit. Put detailed access checks,
  optional declarations, attribution controls, and pseudocode in the appendix.
  Use one complete sentence per source line in revised Method and acquisition prose.
- Ground mechanisms in the inspected native patch implementation. Structured
  specialist scores are hidden from default synthesis; proposal expectations
  are optional. Accepted, undamaged, and unaccepted damaged candidates have
  distinct working-state eligibility. Exact recorded-field changes are not
  automatically verified semantic explanations.
- Distinguish scoped refutation as an evidence standard from the controller's
  implemented continuation and pausing decisions. Do not claim an automatic
  semantic-refutation oracle. Terminal Val never reranks the Train shortlist
  or drives another edit; budget exhaustion does not refute a direction.
- Describe acquisition's implemented structural conflict ranking separately
  from still-unverified human-reliability qualification. Do not restore the
  unimplemented reliability-weighted formula or inherit a model-pilot anchor
  fraction as the human-study setting. Preserve absent feedback levels.

## SkillOpt-style formal exposition (round 23)

Use stable objects, an explicit objective and measured estimate, and state-update equations before low-level implementation checks.
SkillOpt is an exposition reference, not evidence for ERA and not an algorithm to copy.
Distinguish the recorded development selection invariant from unknown population performance.
Keep diagnostic continuation, working-state inheritance, and semantic refutation distinct; a rejected working state can still supply diagnostic history.
No theoretical guarantee is added beyond what follows from the stated update rules.

## Algorithm-first Method (2026-09-21, round 37)

- Related Work leads directly to Section 3, IterEval. Use Overview and setup,
  a short disagreement-based preference mining subsection, and a substantially
  longer depth-first evaluator evolution subsection. Do not restore separate
  Scope, Motivation, or Design Principles sections.
- Intro motivates the search principle; Method defines the optimizer. Follow
  direction choice, revision, measurement/diagnosis, then acceptance, inheritance,
  continuation and switching. Explain each design's purpose where it first appears.
- Explicit direction and diagnostic state summarize the persisted implementation.
  Do not present a mathematical state variable as a new learned representation,
  guaranteed diagnosis or automatic semantic test.
- Keep native six-component interfaces, detailed ranking, repeated measurement,
  diagnostic declarations and resource-policy caveats in the appendix unless
  needed to understand the state transition. Do not copy another optimizer's
  hard update budgets into a description of our advisory edit counts.

## Single-source Method and reading order (2026-09-21, round 38)

- Keep the complete Method in `sections/method.tex`; do not restore the separate
  `problem.tex` and `mining.tex` inputs. Preserve existing cross-reference labels.
- Explain the feedback table before using its proposal subset in revision.
  Keep candidate acceptance next to the best/working update, followed by
  inheritance eligibility and direction continuation.
- Use one concrete trace-to-revision example to explain diagnostic results.
  Detailed record schemas, damage checks and budget caveats belong in the
  appendix; their removal from the main flow cannot weaken the actual rules.
