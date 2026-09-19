# Citation audit — 2026-09-19

## Outcome and scope

All four author-requested papers are cited in `sections/related_work.tex` and included in `references.bib`.
The bibliography now contains 40 cited entries.
The four additions are explicitly arXiv preprints: a formal journal or conference publication was not verified.
Absence of a verified venue is not proof that a paper has never been accepted.

This audit separates three questions:

1. **Identity:** do the identifier, title and authors refer to the intended paper?
2. **Publication fields:** does the chosen version have the stated venue, year, volume, pages and DOI?
3. **Claim support:** does the paper's actual text support the particular sentence citing it?

An automatic identity match does not answer the other two questions.
The source ledger records the original September 16 verification and the September 19 incremental checks separately; unchanged entries are not represented as newly re-certified.

## Workflow and tools

- Applied the installed `citation-management` metadata/validation workflow and `academic-writing-skills` claim-scope and non-defensive writing rules.
- Consulted the hallucination-prevention workflow in `ml-paper-writing`, from [Orchestra-Research/AI-research-SKILLs](https://github.com/Orchestra-Research/AI-research-SKILLs/tree/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/ml-paper-writing), pin `773a52944ba4747a18bd4ae9ade53fff041adcbc`. Used source retrieval and claim verification, not unsubstantiated statistics or another conference template.
- Actually ran the author-requested [constructorfabric/reference-audit](https://github.com/constructorfabric/reference-audit/tree/c80461cbdd237b220a5bf5888ffd9a4068e51329), pin `c80461cbdd237b220a5bf5888ffd9a4068e51329`. It is a Python CLI package; its repository `SKILL.md` is only a placeholder, not a complete writing skill.
- Retrieved official arXiv BibTeX/landing pages/PDFs, official proceedings/BibTeX, ACL Anthology and PMLR records, and relevant publisher DOI metadata. Secondary indexes were used for screening, not as final authority in conflicts.
- Added a read-only identity-screening script, `scripts/audit_citation_sources.py`, which caches public responses and their hashes. It does not rewrite bibliography entries or certify claim support.
- Refreshed C27 verbatim via the `paper-memory-builder` workflow after prose compression; its empirical gap status is unchanged.

Reproduction from the repository root:

```bash
uv run --python 3.14 \
  --with 'reference-audit @ git+https://github.com/constructorfabric/reference-audit@c80461cbdd237b220a5bf5888ffd9a4068e51329' \
  reference-audit audit main.tex references.bib \
  --no-llm --format json \
  --cache build/citation-audit/reference-audit-cache.db \
  > build/citation-audit/reference-audit-final.json \
  2> build/citation-audit/reference-audit-final.log

uv run --python 3.11 --with bibtexparser==1.4.3 \
  python scripts/audit_citation_sources.py
make check
```

The external CLI's LLM/abstract-based `--check-citations` feature was not used as a substitute for reading the cited method/results sections.
Raw public responses, downloaded papers and generated reports stay in ignored `build/citation-audit/`; durable decisions and source URLs are recorded here and in [reference_sources.json](reference_sources.json).

## The four additions and their supported roles

| Paper | Location checked | Role in Related Work | Boundary |
| --- | --- | --- | --- |
| [2604.13602 — Reward Hacking in the Era of Large Models](https://arxiv.org/abs/2604.13602v1) | §2; mechanisms and defenses in §§3–7 | Survey framework for proxy optimization: objective compression, optimization amplification, evaluator–policy co-adaptation | The framework is the survey's synthesis, not proof of inevitability or evidence that ERA prevents reward hacking |
| [2601.03986 — Benchmark²](https://arxiv.org/abs/2601.03986v1) | §§3.1–3.4; §4 and Table 2 | Benchmark quality through ranking consistency, discriminability and capability alignment; selective test-set construction | Benchmark construction is distinct from selecting comparisons for human annotation; this does not establish our equal-human-cost acquisition benefit |
| [2605.23899 — From Raw Experience to Skill Consumption](https://arxiv.org/abs/2605.23899v1) | §3; §4.2 and Table 1; §5 | Experience, skill extraction and consumption; reported average gains, negative transfer and extraction/consumption differences | Consumer-dependent skill utility is not evidence for ERA's implementation diagnosis or the superiority of continuation |
| [2602.03619 — Learning Query-Specific Rubrics](https://arxiv.org/abs/2602.03619v3) | §§3.2–3.4; §4 | Preference-trained query-specific rubric generators and their use as DeepResearch report-training rewards | Learning rubrics is not the same claim as evolving the evaluator's evidence-gathering procedure |

All four received `exactly_one` identity matches in the external audit (OpenAlex for the survey, Benchmark² and rubrics; Semantic Scholar for skill consumption).
The rubric paper's official arXiv BibTeX and v3 PDF list **Jie Zhou twice**.
Both occurrences are preserved with a bibliography comment and provenance note; deduplication requires clarification, not an assumption.

## Publication-field decisions and conflicts

| Entry | Decision | Basis |
| --- | --- | --- |
| DGM | Changed arXiv 2025 to **ICLR 2026**, volume 2026, pp. 104223–104294; retained stable key `zhang2025dgm` | Official ICLR BibTeX/proceedings. The external audit instead matched a conflicting journal record, “SuperIntelligence - Robotics - Safety & Alignment,” DOI `10.70777/si.v2i3.15063`, volume 2, year 2025. Do not copy that record into this entry |
| RewardBench | Changed arXiv 2024 to **Findings of NAACL 2025**, pp. 1755–1797, DOI `10.18653/v1/2025.findings-naacl.96` | Official ACL Anthology. This is **not** the main NAACL proceedings. The citation key remains stable |
| GEPA | ICLR 2026, volume 2026, pp. 8479–8565; **Alex Dimakis** | Official published metadata differs from preprint author name Alexandros G. Dimakis |
| AFlow | ICLR 2025, volume 2025, pp. 34040–34077; **XiongHui Chen** | Official published BibTeX |
| ADAS | Added volume 2025, pp. 21344–21377 | Official ICLR 2025 BibTeX |
| DSPy | Added volume 2024, pp. 54928–54958; retained **Self-Improving Pipelines** title and full PDF author names | Official hosted PDF differs from index/BibTeX title **State-of-the-Art Pipelines** |
| Prometheus | Added volume 2024, pp. 29927–29962; retained **Jamin Shin** and **Seongjin Shin** | Official hosted PDF differs from index names Jay Shin / Ryan S Shin and malformed index BibTeX |
| JudgeBench | Added volume 2025, pp. 63277–63303; retained **William Y. Tang** and **Raluca Ada Popa** | Official hosted PDF uses fuller names than index |
| OPRO | Added volume 2024, pp. 12028–12068 | Official ICLR 2024 BibTeX |
| PPTAgent | Retained pp. **14402–14418** | Official ACL BibTeX differs from Crossref's 14413–14429 |
| Human-feedback summarization | Retained published title **Learning to summarize with human feedback** | Published record differs from arXiv title using “from” |
| GenEval | Retained **Hannaneh Hajishirzi** | Published author spelling differs from arXiv |
| SummEval | Retained correctly escaped author accents | `bibtexparser.convert_to_unicode` caused an author-token mismatch; that parser output is not grounds for changing the source bibliography |

Proceedings volume/page ranges above are copied from the official records, not inferred from PDF page counts.
For a conflict, resolve the affected field against the appropriate original publication artifact and document both readings.
Do not silently combine metadata from different versions.

## Venue inventory for all 40 entries

**A** means a proceedings, publisher or registered publisher DOI record supports the venue.
**B** means the venue is supported by an author-side publication comment or official project citation; a direct proceedings record remains desirable.
**P** means a verified arXiv record, without a verified formal venue.
Dates are per-entry verification dates, not a claim that every source was fetched again today.
The source ledger holds full authors and additional field-level notes.

| Citation key | Venue and year retained | Verification tier | Recorded date | Primary sources |
| --- | --- | --- | --- | --- |
| `agrawal2026gepa` | International Conference on Learning Representations, 2026 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2507.19457v2) [2](https://proceedings.iclr.cc/paper_files/paper/6768-/bibtex) [3](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html) |
| `fabbri2021summeval` | Transactions of the Association for Computational Linguistics, 2021 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2007.12626v4) [2](https://aclanthology.org/2021.tacl-1.24.bib) |
| `ghosh2023geneval` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2310.11513v1) [2](https://papers.nips.cc/paper_files/paper/2023/hash/a3bf71c7c63f0c3bcb7ff67c67b1e7b1-Abstract-Datasets_and_Benchmarks.html) |
| `hu2025adas` | International Conference on Learning Representations, 2025 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2408.08435v2) [2](https://shengranhu.com/ADAS/) [3](https://proceedings.iclr.cc/paper_files/paper/2066-/bibtex) [4](https://proceedings.iclr.cc/paper_files/paper/2025/hash/36b7acf6f6010652b3f2a433774a66fe-Abstract-Conference.html) |
| `khattab2024dspy` | International Conference on Learning Representations, 2024 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2310.03714v1) [2](https://github.com/stanfordnlp/dspy) [3](https://proceedings.iclr.cc/paper_files/paper/4781-/bibtex) [4](https://proceedings.iclr.cc/paper_files/paper/2024/file/f1cf02ce09757f57c3b93c0db83181e0-Paper-Conference.pdf) |
| `kim2024prometheus` | International Conference on Learning Representations, 2024 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2310.08491v2) [2](https://proceedings.iclr.cc/paper_files/paper/4064-/bibtex) [3](https://proceedings.iclr.cc/paper_files/paper/2024/file/803485352e61e3ebf41221e4776c9fd4-Paper-Conference.pdf) |
| `kim2024prometheus2` | Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, 2024 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2405.01535v2) [2](https://aclanthology.org/2024.emnlp-main.248.bib) |
| `kirstain2023pickapic` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2305.01569v2) [2](https://papers.nips.cc/paper_files/paper/2023/hash/73aacd8b3b05b4b503d58310b523553c-Abstract-Conference.html) |
| `lambert2024rewardbench` | Findings of the Association for Computational Linguistics: NAACL 2025, 2025 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2403.13787v2) [2](https://aclanthology.org/2025.findings-naacl.96.bib) [3](https://aclanthology.org/2025.findings-naacl.96/) |
| `liu2023geval` | Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2303.16634v3) [2](https://aclanthology.org/2023.emnlp-main.153.bib) |
| `madaan2023selfrefine` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2303.17651v2) [2](https://papers.nips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html) |
| `ouyang2022instruct` | Advances in Neural Information Processing Systems, 2022 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2203.02155v1) [2](https://papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) |
| `pptagent2025` | Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, 2025 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2501.03936v3) [2](https://aclanthology.org/2025.emnlp-main.728.bib) |
| `presentbench2026` | arXiv preprint arXiv:2603.07244, 2026 | P: verified preprint; formal venue unverified | 2026-09-16 | [1](https://arxiv.org/abs/2603.07244v1) |
| `pryzant2023protegi` | Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2305.03495v2) [2](https://aclanthology.org/2023.emnlp-main.494.bib) |
| `rafailov2023dpo` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2305.18290v3) [2](https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html) |
| `shankar2024evalgen` | Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology, 2024 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2404.12272v1) [2](https://doi.org/10.1145/3654777.3676450) |
| `shinn2023reflexion` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2303.11366v4) [2](https://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html) |
| `si2025design2code` | Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 2025 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2403.03163v3) [2](https://aclanthology.org/2025.naacl-long.199.bib) |
| `stiennon2020summarize` | Advances in Neural Information Processing Systems, 2020 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2009.01325v3) [2](https://papers.nips.cc/paper_files/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html) |
| `tan2025judgebench` | International Conference on Learning Representations, 2025 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2410.12784v2) [2](https://proceedings.iclr.cc/paper_files/paper/1874-/bibtex) [3](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf) |
| `wang2024selftaught` | arXiv preprint arXiv:2408.02666, 2024 | P: verified preprint; formal venue unverified | 2026-09-16 | [1](https://arxiv.org/abs/2408.02666v2) |
| `xu2023imagereward` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2304.05977v4) [2](https://papers.nips.cc/paper_files/paper/2023/hash/33646ef0ed554145eab65f6250fab0c9-Abstract-Conference.html) |
| `yang2024opro` | International Conference on Learning Representations, 2024 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2309.03409v3) [2](https://proceedings.iclr.cc/paper_files/paper/5223-/bibtex) [3](https://proceedings.iclr.cc/paper_files/paper/2024/hash/3339f19c5fcee3ad74502947a32be9e6-Abstract-Conference.html) |
| `yao2023react` | International Conference on Learning Representations, 2023 | B: author-side publication statement | 2026-09-16 | [1](https://arxiv.org/abs/2210.03629v3) |
| `yuksekgonul2025textgrad` | Nature, 2025 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2406.07496v1) [2](https://doi.org/10.1038/s41586-025-08661-4) [3](https://github.com/zou-group/textgrad) |
| `zhang2020bertscore` | International Conference on Learning Representations, 2020 | B: author-side publication statement | 2026-09-16 | [1](https://arxiv.org/abs/1904.09675v3) |
| `zhang2025aflow` | International Conference on Learning Representations, 2025 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2410.10762v4) [2](https://raw.githubusercontent.com/FoundationAgents/AFlow/main/README.md) [3](https://openreview.net/forum?id=z5uVAKwmjf) [4](https://proceedings.iclr.cc/paper_files/paper/2345-/bibtex) |
| `zhang2025dgm` | International Conference on Learning Representations, 2026 | A: proceedings/publisher record | 2026-09-19 | [1](https://arxiv.org/abs/2505.22954v3) [2](https://proceedings.iclr.cc/paper_files/paper/6883-/bibtex) [3](https://proceedings.iclr.cc/paper_files/paper/2026/hash/aa5f5e6eb6f613ec412f1d948dfa21a5-Abstract-Conference.html) |
| `zheng2023judging` | Advances in Neural Information Processing Systems, 2023 | A: proceedings/publisher record | 2026-09-16 | [1](https://arxiv.org/abs/2306.05685v4) [2](https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html) |
| `hu2022lora` | International Conference on Learning Representations, 2022 | B: author-side publication statement | 2026-09-16 | [1](https://raw.githubusercontent.com/microsoft/LoRA/main/README.md) [2](https://arxiv.org/abs/2106.09685) |
| `shao2024deepseekmath` | arXiv preprint, 2024 | P: verified preprint; formal venue unverified | 2026-09-16 | [1](https://arxiv.org/abs/2402.03300) |
| `seung1992committee` | Proceedings of the Fifth Annual Workshop on Computational Learning Theory, 1992 | A: proceedings/publisher record | 2026-09-16 | [1](https://doi.org/10.1145/130385.130417) [2](https://api.crossref.org/works/10.1145/130385.130417) |
| `liu2024autocalibrate` | Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), 2024 | A: proceedings/publisher record | 2026-09-19 | [1](https://aclanthology.org/2024.lrec-main.237/) [2](https://aclanthology.org/2024.lrec-main.237.bib) [3](https://aclanthology.org/2024.lrec-main.237.pdf) [4](https://lrec.elra.info/lrec2024-main-0237) [5](https://api.crossref.org/works/10.63317/3posqwchnb6g) |
| `zhuge2025agentjudge` | Proceedings of the 42nd International Conference on Machine Learning, 2025 | A: proceedings/publisher record | 2026-09-19 | [1](https://proceedings.mlr.press/v267/zhuge25a.html) [2](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhuge25a/zhuge25a.pdf) |
| `muldrew2024activepreference` | Proceedings of the 41st International Conference on Machine Learning, 2024 | A: proceedings/publisher record | 2026-09-19 | [1](https://proceedings.mlr.press/v235/muldrew24a.html) [2](https://raw.githubusercontent.com/mlresearch/v235/main/assets/muldrew24a/muldrew24a.pdf) |
| `wang2026rewardhacking` | arXiv preprint arXiv:2604.13602, 2026 | P: verified preprint; formal venue unverified | 2026-09-19 | [1](https://arxiv.org/bibtex/2604.13602) [2](https://arxiv.org/abs/2604.13602v1) [3](https://arxiv.org/pdf/2604.13602v1) |
| `qian2026benchmark2` | arXiv preprint arXiv:2601.03986, 2026 | P: verified preprint; formal venue unverified | 2026-09-19 | [1](https://arxiv.org/bibtex/2601.03986) [2](https://arxiv.org/abs/2601.03986v1) [3](https://arxiv.org/pdf/2601.03986v1) |
| `huang2026skillconsumption` | arXiv preprint arXiv:2605.23899, 2026 | P: verified preprint; formal venue unverified | 2026-09-19 | [1](https://arxiv.org/bibtex/2605.23899) [2](https://arxiv.org/abs/2605.23899v1) [3](https://arxiv.org/pdf/2605.23899v1) |
| `lv2026queryrubrics` | arXiv preprint arXiv:2602.03619, 2026 | P: verified preprint; formal venue unverified | 2026-09-19 | [1](https://arxiv.org/bibtex/2602.03619) [2](https://arxiv.org/abs/2602.03619v3) [3](https://arxiv.org/pdf/2602.03619v3) |

## Automatic results and unresolved limits

The final external run reports **40 entries, 40 cited, 0 uncited and 0 cited-but-missing**.
Its identity verdicts are **33 exactly-one, 7 unresolved, 0 none and 0 multiple**.
These are automated candidate-matching outcomes, not a certification of all fields.
The tool's separate `entries_with_issues` count is 12; it is not the unresolved-identity count.
Its hard field errors are the DGM volume and PPTAgent pages, both resolved here
against primary publication records as documented above, not by accepting the index values.

The seven unresolved entries are GenEval, Pick-a-Pic, human-feedback summarization, ReAct, LoRA, DeepSeekMath and Active Preference Learning.
Their original-source records are listed above; unresolved index/network status is not evidence that the papers are fictitious.
Direct Semantic Scholar calls returned HTTP 429 in this session, some OpenReview requests returned 403, and DBLP requests met a bot page.
No unrelated search hit was accepted as a replacement.

The CLI reports **11 missing includes** because it resolves valid figure input paths relative to nested source directories rather than the document root.
The LaTeX build and repository structural checks find these files.
Do not “repair” legitimate input paths to satisfy this parser.

Additional boundaries:

- Query-by-committee's DOI identity and publication fields were verified, but its ACM full text was inaccessible (403); a full-text check of the foundational acquisition claim remains pending.
- Self-Taught Evaluators and DeepSeekMath have no verified formal venue in this audit. They remain preprints, as do PresentBench and the four additions.
- ReAct and BERTScore retain author-side arXiv publication comments; LoRA retains the authors' official repository citation. They are tier B, not silently upgraded to proceedings verification.
- The identity-screen script compares metadata strings, not scientific claims. Its accent conversion, preprint/published title changes and author aliases can create false mismatches.
- Full-text checks covered the four additions and targeted introduction claims (including AutoCalibrate, EvalGen, Agent-as-a-Judge, Active Preference Learning, GEPA and DGM); this is not a fresh full-text claim audit of every sentence attached to all 40 references.
- No citation establishes C27/C28. Equal-cost acquisition and search advantages remain empirical gaps; quantitative displays remain explicitly simulated.

## Manuscript checks

`make check` passes structural, memory, simulation and landscape checks: 40 cited entries, 44 claim records, 9 main-text pages and 31 total pages.
Revised prose remains one sentence per source line.
No figure content, base typography, page margins, private experimental records or empirical result status changed.
Pages 1–3 and 10–14 are rendered into `build/round18-visual/` and visually checked for source/figure layout, readable bibliography entries, correct venue rendering and clipping.
The final bibliography page contains the last entry before the appendix starts on a new page; template spacing and font sizes are unchanged.
