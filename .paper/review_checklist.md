# Revised manuscript review

Review date: 2026-09-17. This checklist is not author sign-off or submission approval.

## Content and scope

- The title is **Evolving Evaluation Systems from Human Feedback for Open-Ended Tasks**.
  No current project acronym is used; ERA names only the method. The historical source
  repository and local source directory were not renamed or modified.
- The paper follows a scientific argument, not debugging history or a sequence
  of intermediate methods. The user-selected research plan supplies the complete
  research scope; current ERA documentation supplies the execution semantics.
  Their roles are recorded in `plan_coverage.md` and `source_provenance.md`.
- The abstract follows the author-approved argument: preference-alignment
  difficulty on open-ended tasks, the gap between a preference outcome and a
  procedure for judging new outputs, feedback-driven agent evolution, and
  cross-task validation. Structured acquisition and evaluation-failure
  hypotheses support that argument. Parameter-fitting contrasts, search-state
  mechanics, provenance protocols, and domain/study-arm lists are removed from
  the abstract. The introduction retains evaluator fine-tuning and calibration
  comparisons, including a shared-observation control. No superiority or
  faithful-reasoning claim is inferred from an explicit program. Evaluator
  tuning and C3 generator training remain distinct and unexecuted.
- All 22 candidate domains in four families appear in the domain table.
  The overview uses a compact gallery of concrete artifacts and distinct
  quality criteria. Main Figure 2 and expanded Figure 4 show all 22 C1 domains
  in 6/6/5/5 taxonomy order. C1 summaries use 11 domains per setting; annotation,
  component, and C2 details retain eight explicitly labeled diagnostic domains.
  This is not a claim of readiness, transfer, or 22 completed experiments.
- Reusing existing preferences and collecting new preferences are two
  data-construction settings for the same task-plus-human-feedback problem.
  A domain can use both, and existing H0 is not an admission prerequisite.
  Provenance, annotation protocols, agreement, abstention, and results remain
  separate. Newly collected labels are not presumed more reliable. Building
  a corpus does not establish sampling efficiency; a matched-budget random
  sampling comparison is required for that separate claim.
- Semantic mapping, source dependence, three disagreement strata, H0–H3,
  evidence table Z, six-component ERA, and C1/C2/planned C3 are covered.
  Experimental design retains core results, ablations, and analysis as its
  three principal parts.
- Human H1/H2 are not inferred from H0; model reasoning is not human rationale.
  A random reliability anchor precedes the frozen targeted acquisition policy.
- Complete artifact scores precede median comparison. Proposal evidence,
  sealed Train aggregates, terminal Val, and Test/OOD remain distinct.
  The pre-search External Metric Reserve cannot enter evolution or selection.
- A direction is distinct from its implementation; best and working programs
  have separate roles. Complete measurement is required for both promotion
  and continuation. Resource exhaustion and scoped refutation are not equated.
  The argument now treats observation and judgment as objects of evolution,
  hypotheses as units of exploration, and complete programs as units of selection.
- C1 has fixed candidate pools and complete rankings. C2 uses fresh shared
  initial outputs and new blinded judgments. C3 includes an unchanged Base
  reference and two frozen-reward training arms with their own online rollouts.
  No parameter training was performed.
- No private results, sample identifiers, run records, or generated evaluators
  were imported. Empirical outcomes remain unmeasured. Claims C27/C28 are
  recorded as empirical gaps and retained only as hypotheses, not findings.

## Figures, tables, and memory

- Ten figures comprise an overview, a pointwise evaluator architecture, and
  eight quantitative displays. Two are in the main text and eight in the
  appendix. Main Figure 2 combines a balanced task ring, cost/agreement scatter,
  and four family bar panels on a shared 0–100% scale. The 2,880-input synthetic
  OOD subset is separate from the full-cohort appendix. Figure 4 gives
  all-domain ID/OOD intervals. Figure 8 contains the bounded mechanism and
  feedback-detail diagnostics; C2 remains separate in Figure 9.
  The charts also use expanded paired-effect intervals, acquisition curves, an
  annotation audit, horizontal selected-rank ribbons, a heatmap with split
  violins and raw points, rainclouds with a diverging preference balance and
  separate abstentions, and aligned cost/agreement profiles.
  Editable TikZ and Python sources produce vector text, geometry, and marks.
  Redundant conceptual illustrations are no longer in the manuscript.
- The author-requested post-training survey (2503.06072), full-stack safety
  survey, Speculative RAG, and MMMR visuals were inspected, alongside the earlier
  Self-Refine, Eureka, TextGrad, and Segment Anything references. All three
  author color references each supply one isolated palette candidate using
  their labeled HEX values. The author rejected the preceding four invented
  directions. Reference 1's blue/mint/cream/peach/rose colors are provisional;
  references 2 and 3 supply blue/orange and teal/apricot alternatives.
  No final author choice is assumed. The complete method ensemble uses blue
  for static judge, mint for static tools/seed, cream for prompt optimization,
  peach for program search, and rose for ERA; metric-only anchors stay gray.
  Family, H-level, policy, rank, and outcome encodings have explicit legends.
  Four H levels use four colors, with settings encoded by side and hatching.
  All five acquisition policies have equal-width lines and individual bands.
  The component heatmap uses the full five-color sequence with cream at zero.
  Labels, markers,
  line patterns, and hatching supplement color. Softly tinted groups, original
  pictograms, and curved flows remain in the diagrams. Source versions and
  design choices are recorded in `visual_references.md`. Local source thumbnails
  appear only in the review board, not the paper; no reference artwork was traced
  or sent to an image-generation service.
- Twelve tables cover simulated C1 outcomes, domains, annotation provenance,
  readiness, information access, ablations, training controls, reporting
  requirements, pending empirical downstream outcomes, simulated cohorts,
  the experiment manifest, and parameter-adaptation alternatives. Every figure and table has a manuscript
  callout. Exact captions for both figures and tables match structured memory.
- Only the previously generated 1536×1024 preserved photograph remains active,
  in Figure 1. It prints at 1.96 cm, about 1990 DPI; the declared maximum 3 cm
  width provides about 1300 DPI. The source photograph, alternative edit,
  panorama, and unused conceptual figures remain archived. Prompts, model
  provenance, input lineage, and asset hashes are preserved. This round makes
  no new model calls. Captions and the AI use statement distinguish constructed
  examples and artificial preferences from observations and human studies.
- `make figures` produces isolated vector PDFs, PNGs, and a contact sheet
  without model calls. Diagram labels, arrows, the title page, result tables,
  domain-table continuation, algorithm, and appendix layouts are reviewed
  both in isolation and in the final manuscript. Numerical table columns are
  right-aligned; narrow prose columns are left-aligned. The full C1 numerical
  table remains in the appendix, now summarizing 11 C1 domains per setting.
  The landscape composite occupies the top of main page 8, with its caption
  and Results discussion immediately below. The mechanism figure is an appendix
  diagnostic. Official body settings are unchanged; no new forced page break
  or whole-figure shrinkage is used.
  The parameter-adaptation paragraph stays together below the overview instead
  of being split across the first page and the figure on the second page.
  Short annotation, attribution, and training-protocol paragraphs are kept
  intact so large floats do not interrupt individual sentences across pages.
- The official Times body and ICLR heading rules are unchanged. Diagram
  Helvetica-compatible typography (`qhv`/`phv`) is locally scoped; charts use TeX Gyre Heros on native 5.4-inch
  canvases, with 8.5 pt titles, 8 pt axes, 7.3–7.5 pt tick/legend labels, and
  6.8 pt fixture-disclosure notes. All PDF fonts are embedded, without Type 3
  fallbacks. Chart bounds and actual manuscript placements are checked.
- Forty-two claim records, ten figure records, twelve table records, and the
  revision history pass the repository's offline consistency checks.
  The prior upstream Draft 2020-12 JSON Schema audit reported zero errors;
  this round changes only display links, not claim text or evidence status.
  The upstream skill's advertised validation script was absent; the schema
  was preserved unmodified and validated with modern `jsonschema` instead.
  Structural validity does not establish empirical support.

## Simulation provenance and limits

- The author authorized simulated data for visual and reporting design.
  Fourteen CSV files, eight chart PDFs, one numerical TeX table, and a manifest
  are generated from seed 20260916. Simulation is disclosed on the title page,
  in relevant prose, in every chart and caption, in every data row, and in PDF
  metadata. No actual model, evaluator evolution, human annotation, or C3
  training was run. Costs are assigned rather than measured. The 22 C1 cohort
  assignments and eight diagnostic assignments are illustrative; R/N labels
  do not assert actual availability or permanently partition the domains.
- The independent simulation checker verifies hashes, paired metrics,
  completeness denominators, annotation outcomes, acquisition budgets,
  numerical table cells, canonical LF file endings, and the claim boundary. Table means use
  method-complete groups; paired contrasts use joint completeness; selected-rank
  shares retain all inputs, including failures. Intervals describe toy data,
  not experimental uncertainty or expected method performance.
- The original eight-domain C1 group rows, summaries, and exported intervals
  are unchanged, as are all seven diagnostic-only CSVs. Fourteen C1 cohorts
  are added and aggregate tables, selection, and costs recomputed. All 14
  current CSVs and the numerical table match byte-for-byte across the three
  palette candidates. All 110 atlas values and 22 paired effects are checked
  against canonical CSVs; candidate outputs cannot overwrite canonical assets.
  Twenty-nine checked small-text/background pairs exceed 4.5:1 in every palette,
  with grayscale proofs and redundant labels/positions/shapes retained.
  Claims C37/C38 support fixture provenance and arithmetic only. C27/C28 remain
  gaps with no empirical evidence artifacts.
- `scripts/check_simulated_results.py --submission` passes its simulation audit
  and then intentionally exits 2 with `SUBMISSION BLOCKED`. Replacing fixtures
  with authorized measurements and re-auditing claims is required before submission.

## Build and references

- The full local build succeeds with pdfLaTeX and BibTeX; `make check` passes.
- Main text is 9 pages; the complete PDF is 30 pages including statements,
  references and appendices. US Letter format and anonymous PDF author metadata.
- The two official ICLR files match their upstream SHA-256 hashes exactly.
- All 33 references are cited; no undefined citations, duplicated keys or
  unresolved cross-references.
- The prior bibliography validation recorded 33 valid entries and zero errors;
  bibliography metadata was not changed or revalidated online in this round.
  Its 25 recommended-field warnings concern page ranges for online ICLR papers
  and volume/pages/DOI fields for explicitly cited arXiv preprints. Those fields
  were not invented to silence generic warnings.
- No overfull boxes, undefined citations/references, font-size substitutions,
  or unresolved rerun warnings remain. Nonfatal underfull-box notices concern
  page justification and bibliography spacing.
- Private-path and credential-pattern scans passed for publication sources.
  Repository documentation remains intentionally identifiable and is not an
  anonymous submission supplement.

## Approved argument revision (round 16, 2026-09-19)

- Abstract and introduction follow the preference-to-procedure argument, with more space devoted to the observed search problem than to acquisition mechanics.
  Candidate acceptance and direction continuation remain separate decisions; the observation is bounded to the inspected optimizer configuration.
  Human feedback, human preferences, evaluation procedure, evaluation program, candidate, direction and hypothesis retain distinct meanings.
- Revised prose uses one complete sentence per source line, without forced PDF line breaks.
  The abstract is one paragraph, the introduction ends on page 2, and the main text remains 9 pages in a 30-page PDF.
  The official ICLR typography and margins are unchanged.
- Claims and revision memory are synchronized; 44 claim records, 10 figure records and 12 table records pass the repository checks.
  C27 and C28 remain empirical gaps; simulated displays do not support acquisition or search superiority.
  The approved landscape composite remains Figure 2 on page 8, with balanced synthetic subset provenance distinct from the appendix cohorts.

## Still required

Authors must approve the framing, select and freeze the experimental manifest,
replace all simulated fixtures with authorized measurements and new annotation
where needed, re-audit claims, finalize disclosures and author information,
and perform the final submission audit.
The public repository itself contains identifying project provenance and is not
an anonymous supplement.
