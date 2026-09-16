# Revised manuscript review

Review date: 2026-09-16. This checklist is not author sign-off or submission approval.

## Content and scope

- The title is **P2E: Evolving Evaluation Systems for Open-Ended Generation**.
  P2E names the project; ERA is its evaluator evolution method. The historical source
  repository and local source directory were not renamed or modified.
- The paper follows a scientific argument, not debugging history or a sequence
  of intermediate methods. The user-selected P2E plan supplies the complete
  research scope; current ERA documentation supplies the execution semantics.
  Their roles are recorded in `plan_coverage.md` and `source_provenance.md`.
- All 22 candidate domains in four families appear in the domain table.
  The overview uses a compact gallery of concrete artifacts and distinct
  quality criteria. The quantitative panels retain domain identities across
  eight illustrative cohorts without reducing the 22-domain research scope.
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

- Nine figures comprise an overview, a pointwise evaluator architecture, and
  seven quantitative displays. Three are in the main text and six in the
  appendix. The charts use paired-effect forests, acquisition curves, an
  annotation audit, selected-rank composition, a heatmap with box/strip plots,
  raincloud distributions with outcome bars, and a quality–cost scatter.
  Editable TikZ and Python sources produce vector text, geometry, and marks.
  Redundant conceptual illustrations are no longer in the manuscript.
- The author-requested post-training survey (2503.06072), full-stack safety
  survey, Speculative RAG, and MMMR visuals were inspected, alongside the earlier
  Self-Refine, Eureka, TextGrad, and Segment Anything references. All three
  author color references inform the shared ocean/sea-glass/sand/coral palette.
  P2E is coral and the static tool-augmented seed is blue; reused preferences
  are teal and newly collected preferences are warm peach. Rank, outcome, and
  signed-effect encodings have their own explicit legends. Labels, markers,
  line patterns, and hatching supplement color. Softly tinted groups, original
  pictograms, and curved flows remain in the diagrams. Source versions and
  design choices are recorded in `visual_references.md`; no reference figure
  was copied, traced, or sent to an image-generation service.
- Eleven tables cover simulated C1 outcomes, domains, annotation provenance,
  readiness, information access, ablations, training controls, reporting
  requirements, pending empirical downstream outcomes, simulated cohorts,
  and the experiment manifest. Every figure and table has a manuscript
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
  right-aligned; narrow prose columns are left-aligned. The final experiment
  manifest fits beneath the cost figure rather than occupying an isolated page.
  Short annotation, attribution, and training-protocol paragraphs are kept
  intact so large floats do not interrupt individual sentences across pages.
- The official Times body and ICLR heading rules are unchanged. Diagram `phv`
  typography is locally scoped; charts use TeX Gyre Heros on native 5.4-inch
  canvases, with 8.5 pt titles, 8 pt axes, 7.3–7.5 pt tick/legend labels, and
  6.8 pt fixture-disclosure notes. All PDF fonts are embedded, without Type 3
  fallbacks. Chart bounds and actual manuscript placements are checked.
- Thirty-eight claim records, nine figure records, eleven table records, and the
  revision history pass the repository's offline consistency checks.
  Claims also pass the upstream Draft 2020-12 JSON Schema with zero errors.
  The upstream skill's advertised validation script was absent; the schema
  was preserved unmodified and validated with modern `jsonschema` instead.
  Structural validity does not establish empirical support.

## Simulation provenance and limits

- The author authorized simulated data for visual and reporting design.
  Thirteen CSV files, seven chart PDFs, one numerical TeX table, and a manifest
  are generated from seed 20260916. Simulation is disclosed on the title page,
  in relevant prose, in every chart and caption, in every data row, and in PDF
  metadata. No actual model, evaluator evolution, human annotation, or C3
  training was run. Costs are assigned rather than measured.
- The independent simulation checker verifies hashes, paired metrics,
  completeness denominators, annotation outcomes, acquisition budgets,
  numerical table cells, canonical LF file endings, and the claim boundary. Table means use
  method-complete groups; paired contrasts use joint completeness; selected-rank
  shares retain all inputs, including failures. Intervals describe toy data,
  not experimental uncertainty or expected method performance.
- Regeneration in the same environment reproduces all 22 checked asset hashes
  exactly: 13 CSVs, the manifest, seven PDFs, and the numerical table.
  Claims C37/C38 support fixture provenance and arithmetic only. C27/C28 remain
  gaps with no empirical evidence artifacts.
- `scripts/check_simulated_results.py --submission` passes its simulation audit
  and then intentionally exits 2 with `SUBMISSION BLOCKED`. Replacing fixtures
  with authorized measurements and re-auditing claims is required before submission.

## Build and references

- The full local build succeeds with pdfLaTeX and BibTeX; `make check` passes.
- Main text is 9 pages; the complete PDF is 26 pages including statements,
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

## Still required

Authors must approve the framing, select and freeze the experimental manifest,
replace all simulated fixtures with authorized measurements and new annotation
where needed, re-audit claims, finalize disclosures and author information,
and perform the final submission audit.
The public repository itself contains identifying project provenance and is not
an anonymous supplement.
