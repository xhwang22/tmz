# Abstract and introduction citation audit — 2026-09-20

## Scope and outcome

This revision starts from the author's uncommitted abstract and introduction, not
the older committed prose. It adds citations and makes only the local wording
changes needed to attribute prior work accurately. Figures, methods, experiments,
Related Work, and the author's result sentences are unchanged. Nothing is pushed.

The abstract has two background citation groups (three works). The introduction
cites 13 distinct works. Five bibliography entries are new: FLASK, EvalLM, the
quality-criteria confusion study, AMPLe, and SkillOpt. The other eight were already
in the bibliography. The four previously requested arXiv papers remain in Related
Work; the query-specific-rubrics paper is additionally relevant to this introduction.

The workflow uses the academic-writing and citation-management guidance together
with the verified-citation workflow in ml-paper-writing. The user-recommended
`constructorfabric/reference-audit` is used as an actual CLI, not represented as
an installed writing skill: its `.cf-studio/config/SKILL.md` is a placeholder.
Identity screening, publication-field verification, and claim support are treated
as three separate checks.

## Research process

Discovery combined OpenAlex searches, reference-following, the existing September
19 audit, publisher/venue records, and targeted reading of primary full texts.
No paper was added from a remembered title alone. Search responses and downloaded
sources are cached under `build/citation-audit/intro-20260920/`; previously checked
full texts remain under `build/citation-audit/fulltext/`.

Searches covered:

- `EvalLM Interactive Evaluation User Defined Criteria`
- `FLASK fine grained language model evaluation alignment skill`
- `open ended evaluation context specific criteria human preferences`
- `"evaluation" "criteria drift"`
- `Active Preference Learning Large Language Models`, followed by title-filtered
  and quoted searches for `"active preference learning" "language"`
- `"query by committee"`
- `language model optimization scalar feedback textual feedback credit assignment`
  and `"textual feedback" "optimization"`
- `SkillOpt agent skill optimization`
- `Learning Query Specific Rubrics Human Preferences`, followed by the verified
  arXiv identifier because the broad search returned irrelevant matches.

Broad searches often returned unrelated papers. Those were discarded, not counted
as substantive evidence. Semantic Scholar search returned HTTP 429; OpenAlex and
primary records supplied the usable discovery route. A general-web attempt to
locate the original Query by Committee full text returned a JavaScript shell and
was not used as evidence.

Additional candidates screened but not inserted into this introduction:

- **Learning to Judge: LLMs Designing and Applying Evaluation Rubrics**, Siro et
  al., Findings of EACL 2026, pp. 6371–6389, DOI
  `10.18653/v1/2026.findings-eacl.335`. Official BibTeX/PDF and opening sections
  inspected. GER-Eval is explicitly a diagnostic framework, not a preference-trained
  rubric optimizer. It is relevant to a future Related Work expansion, but does not
  belong in the sentence listing human-feedback learning methods.
- **APRIL: Interactively Learning to Summarise by Combining Active Preference
  Learning and Reinforcement Learning**, official EMNLP 2018 record
  <https://aclanthology.org/D18-1445/>. Screened as historical background; the newer
  APL and AMPLe papers are more economical anchors for the present data-selection
  motivation. No APRIL-specific claim is made in the manuscript.
- **Prometheus**: the published ICLR 2024 paper uses synthetic rubric-conditioned
  training. It remains in Related Work but is removed from the introduction's
  human-feedback attribution group. Its existence and usefulness are not disputed.
- **Agent-as-a-Judge**, DSPy, TextGrad, ADAS, AFlow, and DGM: relevant to broader
  procedure design and optimization; not all are needed in this short introduction.
  Existing bibliography entries are preserved. The current author revision leaves
  Agent-as-a-Judge uncited; this pass does not remove it or manufacture a citation.
- **Query by Committee**: Crossref confirms the original 1992 workshop identity,
  pages and DOI. ACM full text was inaccessible (HTTP 403). No new theoretical
  claim or additional introduction citation is attached to it. Its existing
  citations in other sections are unchanged.

## Claim-to-source placement

| Manuscript point | Sources and inspected locations | Supported scope / boundary |
| --- | --- | --- |
| Evaluation dimensions depend on the task or individual instruction | FLASK, Introduction and §3; EvalLM, Introduction and formative-study motivation | Supports context-sensitive, multi-dimensional evaluation. The summary/webpage examples remain author illustrations, not reported case studies from these papers. |
| Metrics and model judges offer useful but imperfect human alignment | SummEval, evaluation study; ImageReward, §2 and comparisons; MT-Bench, judge biases and agreement; Hu et al., §§3–5, especially §§5.1–5.4 | Domain- and model-bounded findings, not a theorem that every automated evaluator fails. Hu et al. adds evidence about confusing quality dimensions, not just a generic leaderboard gap. |
| Judging examples is easier than specifying a complete evaluator | EvalGen, Introduction, §7.3 and §8.1 | Criteria drift, tacit criteria, and difficulty implementing criteria. Does not claim human judgments are complete, stable, or unambiguous. |
| Learning evaluator models from human feedback | ImageReward, §2 | Preference-trained reward/evaluator model; no longer attributed to Prometheus's synthetic-data recipe. |
| Learning or refining criteria | AutoCalibrate, §§2.1–2.3; query-specific rubrics, Introduction and §§3.2–3.4 | Human-labeled examples refine criteria; pairwise preferences train a rubric generator. Neither is described as full evaluator-program evolution. |
| Selecting evaluation functions | EvalGen, §§4.1–4.2 | Human grades select implementations of criteria. These are not necessarily pairwise labels. |
| Revising instructions from execution feedback | GEPA, Introduction and algorithm; SkillOpt, §§3.1–3.7 | Separate from the human-feedback sentence because these are general optimization mechanisms. Both can exploit more than a final scalar score. |
| Comparison selection affects feedback efficiency | APL, §3 and evaluation; AMPLe, §§3.2–3.3, §4.2 and §5 setup | Supports selective use of a limited comparison budget. Does not certify IPM, heterogeneous-signal disagreement, or offline subset-mining gains. |
| A preference label does not supply fine-grained reasons | FLASK, Introduction and Fig. 1; query-specific rubrics, Introduction | Supports the coarse-feedback premise. The following claim about multiple plausible revisions is the authors' reasoning; implementation depth and ERA gains still need their own evidence. |
| Default search redirection, ERA effectiveness and downstream gains | No external citation attached | These are observations or results of this paper, not findings that can be borrowed from another work. |

Two limited prose adjustments make attribution explicit: the prior-methods sentence
is separated into human-feedback learning and general instruction optimization;
the ambiguity paragraph now states the source-supported coarse-feedback premise
before drawing the paper's direction-selection inference. The mining paragraph's
opening sentence specifies what the active-learning citations support.

## Publication-field verification

For all 13 cited works, the cited version was checked against a primary record.
The local comparison report is `primary-field-checks.json` in the audit directory:
title, ordered authors, year, venue, pages, volume, DOI or arXiv identifier are
compared wherever present in both records. All compared fields match after
format/whitespace normalization. Missing formal venues are not filled by inference.
This is supplemented by PDF/landing-page checks, including proceedings track.

| Work | Correct cited publication | Primary record |
| --- | --- | --- |
| FLASK | ICLR **2024**, pp. 55361–55414; not the 2023 preprint year | [Official BibTeX](https://proceedings.iclr.cc/paper_files/paper/5286-/bibtex) and published PDF |
| EvalLM | **CHI 2024**, pp. 1–21; DOI `10.1145/3613904.3642216` | Publisher-deposited Crossref BibTeX and the CHI citation printed in [author PDF](https://arxiv.org/pdf/2309.13633v2) |
| Quality-criteria confusion | **ACL 2024, main-conference long papers**, pp. 9530–9570 | [ACL Anthology](https://aclanthology.org/2024.acl-long.516/) plus Crossref |
| AMPLe | **ACL 2025, main-conference long papers**, pp. 33145–33166 | [ACL Anthology](https://aclanthology.org/2025.acl-long.1590/) plus Crossref |
| SkillOpt | **arXiv:2605.23904v2 (2026)**; no formal venue verified | [arXiv](https://arxiv.org/abs/2605.23904v2), exported BibTeX and PDF |
| SummEval | **TACL 2021**, vol. 9, pp. 391–409; not an ACL conference paper | [Official BibTeX](https://aclanthology.org/2021.tacl-1.24.bib) |
| ImageReward | **NeurIPS 2023, main track**, vol. 36, pp. 15903–15935 | [Official BibTeX](https://proceedings.neurips.cc/paper_files/paper/19480-/bibtex) and track-marked landing page |
| MT-Bench / Judging LLM-as-a-Judge | **NeurIPS 2023, Datasets and Benchmarks track**, vol. 36, pp. 46595–46623 | [Official BibTeX](https://proceedings.neurips.cc/paper_files/paper/19631-/bibtex) and track-marked landing page |
| EvalGen | **UIST 2024**, pp. 1–14; DOI `10.1145/3654777.3676450` | Publisher-deposited [Crossref record](https://api.crossref.org/works/10.1145/3654777.3676450) and author PDF |
| AutoCalibrate | **LREC-COLING 2024**, pp. 2638–2656; not ACL/EMNLP | [Official BibTeX](https://aclanthology.org/2024.lrec-main.237.bib) |
| Query-specific rubrics | **arXiv:2602.03619v3 (2026)**; no formal venue verified | [arXiv](https://arxiv.org/abs/2602.03619v3), exported BibTeX and PDF |
| GEPA | **ICLR 2026**, pp. 8479–8565 | [Official BibTeX](https://proceedings.iclr.cc/paper_files/paper/6768-/bibtex) |
| Active Preference Learning | **ICML 2024**, PMLR 235, pp. 36577–36590 | [Official PMLR record and embedded BibTeX](https://proceedings.mlr.press/v235/muldrew24a.html) |

Important source decisions:

- FLASK's automatic index match is the 2023 preprint. The official ICLR 2024
  proceedings override that index's year/venue suggestion.
- EvalLM's ACM landing page returned 403, but its deposited metadata and author
  PDF independently agree on CHI 2024 and the DOI. Access failure is recorded.
- Two Crossref calls in the generic identity-screen script were rate-limited
  (EvalLM and AMPLe). Successful Crossref responses fetched earlier in this same
  audit and official PDFs/BibTeX are retained separately; the failed calls are not
  rewritten as successes.
- Query-specific rubrics lists **Jie Zhou twice** in its official metadata and v3
  PDF. The source author list is preserved; no invented deduplication is performed.
- SkillOpt §3.5 retains a rejected-edit buffer, and §3.6 retains slow/meta guidance.
  It must not be described as forgetting all failed attempts. GEPA also maintains
  complementary candidates. The manuscript's bounded observed-redirection wording
  is preserved rather than generalized into a property of all evolutionary search.

## Automated checks

Ran the pinned reference-audit version:

```bash
uv run --python 3.14 \
  --with 'reference-audit @ git+https://github.com/constructorfabric/reference-audit@c80461cbdd237b220a5bf5888ffd9a4068e51329' \
  reference-audit audit main.tex references.bib --no-llm --format json \
  --cache build/citation-audit/reference-audit-cache.db
```

The JSON/log are cached in `build/citation-audit/intro-20260920/`.

- **45 references:** 38 uniquely identified, 7 unresolved; zero no-match or
  multiple-match verdicts. All five new references were uniquely identified.
- The seven unresolved entries are GenEval, Pick-a-Pic, human-feedback
  summarization, ReAct, LoRA, DeepSeekMath, and APL. These repeat the prior audit's
  unresolved set; index failures are not hallucination findings. Of them, only APL
  is cited in this introduction, and its primary PMLR record and paper were checked.
- **44 cited, one uncited, zero missing citation keys.** Agent-as-a-Judge is
  currently unused after the author's introduction revision; it is preserved.
- The tool reports 13 missing TeX includes because it resolves figure paths from
  nested section files incorrectly. LaTeX successfully resolves the same inputs.
  No figure path is changed to satisfy this parser artifact.
- The separate primary-field check covers all 13 works actually used in the two
  edited sections; it found no compared-field mismatch.
- `make build/main.pdf` succeeded: 37 total pages, no undefined citations or
  references in the final LaTeX log.
- The full repository check is **not all-green**: the current main text is 10 pages
  against a 9-page initial-submission limit, and Agent-as-a-Judge is unused. Layout
  and unrelated bibliography cleanup are outside this citation pass.
- The terminology checker also flags the author's final contribution item,
  `preference acquisition`, against the established `preference mining` wording.
  It is unchanged in this citation-focused pass. Trailing whitespace in the two
  edited files was removed without changing wording.

Audit artifact hashes (SHA-256):

- Primary-field report: `c2bbdff7aed0324982d579551886b59c9d48ca637fafe77b4a401e3d7515362a`.
- reference-audit report: `aeb9976a573cb55f7eaaff406e67ce44a4dc85bbfe51cbe1d86516e733245d66`.

## Evidence caveat retained for the authors

Adding citations does not validate the author's new result sentences. Existing
paper memory still marks mining-efficiency and matched-budget ERA advantages as
evidence gaps, and the repository contains simulated reporting fixtures. The
bounded default-search observation has a separate internal audit; it is not proof
of ERA superiority or of uncertainty causing redirection. No new empirical data
were inspected here. Claims about sustained gains, held-out alignment, refinement,
and training rewards must be reconciled with actual experimental evidence before
submission. This scoped edit preserves the author's result prose and records the
gap instead of manufacturing external support for it.
