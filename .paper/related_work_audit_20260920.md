# Related Work: organization and citation audit — 2026-09-20

## Scope

Rewrites `sections/related_work.tex` in response to the author's objection to its
organization. The previous headings mixed evaluator types, generic optimizers,
and downstream domains. The revised section compares what existing approaches
change, what feedback they use, and which part of our research question remains.
The abstract, introduction, methods, experiments, figures, and empirical claim
statuses are unchanged. No experiments, training, commit, or push were performed.

The project plan's Sections 2.2–2.3 and the ERA plan's Section 8 informed the
structure, not the truth of every limitation in their tables. Current manuscript
terminology takes precedence over older plan names.

## Current organization: three headings

Round 28 initially separated model learning, criteria refinement, and agentic
evaluation. The author's follow-up requested fewer headings and noted that the
standalone reward-hacking paragraph looked appended solely to include a citation.
Round 29 merged those three evaluator routes but still read as a catalogue.
Round 30 follows the author's request to organize each passage around its
relationship to our work, using citations to support the comparison rather than
giving every method a miniature introduction.

| Paragraph | Comparison object | Relation to our work |
|---|---|---|
| Learning evaluation procedures from human feedback | Why improve the evaluator; weights, criteria, or executable procedure as the updated object | Uses reward hacking to motivate learning the evaluation procedure from human feedback, then compares learned judges, criteria learning, and evolving verifiers without claiming tool use or explicit rules are new. |
| Continuing directions in program evolution | History retention, direction continuation, and program inheritance | Compares SkillOpt's rejected-edit history and acceptance gate to ERA's separate working/best programs. Compares SkillHEX's test-time branch selection without training/validation sets to development-cohort evaluation and depth-first direction allocation. |
| Mining preferences for evaluator evolution | Shared selective-feedback principle; learning versus measurement objective | Places IPM within active preference learning, distinguishes its learning objective from Benchmark2 test-set construction, and explains reuse of existing preferences and the evaluator-improvement endpoint. |

Round 31 changes the reward-hacking citation's role in response to the author.
It now opens the evaluator-learning comparison: improving a generator against an
imperfect objective can exploit evaluation errors, motivating improvement of the
evaluation procedure itself from human feedback. It no longer serves only as a
downstream-validation caveat. The source's discussion of reward overoptimization
and iterative reward-model updates was rechecked. This is motivation for studying
evaluator learning, not proof of its necessity as the only remedy or of ERA's
effectiveness. It does not claim our offline method implements policy–evaluator
co-training or prevents reward hacking.

The updated SkillOpt comparison was checked against its abstract and Section 3.5;
the SkillHEX comparison was checked against its abstract, problem setting, and
PUCT-style selection description. SkillLens supports the distinction between
generating procedural knowledge and using it successfully, not a claim that its
experiments validate ERA's diagnostics. Peripheral per-paper descriptions were
removed; the source bibliography and verified publication fields are unchanged.

## Four author-required papers

| Work | Primary record | Use and boundary |
|---|---|---|
| Reward-hacking survey | https://arxiv.org/abs/2604.13602 | Optimization can exploit an imperfect evaluation objective; motivates improving the evaluation procedure from human feedback, not a claim that ERA is the only remedy or prevents reward hacking. |
| SkillLens | https://arxiv.org/abs/2605.23899 | Extraction and consumption are distinct capabilities, with average gains and negative transfer. SkillLens is the authors' project name (PDF p. 1 links `aka.ms/SkillLens`), not a replacement bibliography title. |
| Query-specific rubrics | https://arxiv.org/abs/2602.03619v3 | Human-preference-trained rubric generation for DeepResearch and subsequent use as a training reward. Does not establish our cross-domain gains. |
| Benchmark² | https://arxiv.org/abs/2601.03986 | Selective test-set construction based on ranking consistency, discriminability, and capability alignment. Distinguish measuring models from selecting feedback to improve an evaluator. |

All four retain verified 2026 arXiv-preprint status. No conference acceptance is
inferred from an ACL-like PDF template or an indexing service. The query-rubrics
author list retains the two occurrences of Jie Zhou in the official source.

## Added references and publication-field checks

Seven new references were selected from the project's routes and targeted
OpenAlex searches. Publisher/arXiv BibTeX was downloaded before adding entries.
Full texts were read for the attributed claims, separately from metadata checks.

| Key | Verified record | Publication fields |
|---|---|---|
| `shankar2024spade` | https://doi.org/10.14778/3685800.3685835 and https://www.vldb.org/pvldb/vol17/p4173-shankar.pdf | **Proceedings of the VLDB Endowment**, 17(12), 4173–4186, 2024; journal article. |
| `ke2024critiquellm` | https://aclanthology.org/2024.acl-long.704/ | **ACL 2024, Volume 1: Long Papers**, 13034–13054. |
| `park2024offsetbias` | https://aclanthology.org/2024.findings-emnlp.57/ | **Findings of EMNLP 2024**, 1043–1067; not main-conference EMNLP. |
| `verga2024poll` | https://arxiv.org/abs/2404.18796 | Verified 2024 preprint; no formal venue verified. |
| `luo2026harnessbank` | https://arxiv.org/abs/2607.13683v2 | Verified 2026 preprint; no formal venue asserted. |
| `feng2026skillhex` | https://arxiv.org/abs/2608.05628 | Verified 2026 preprint; no formal venue asserted. |
| `chen2026webgrader` | https://arxiv.org/abs/2608.06474 | Verified 2026 preprint; no formal venue asserted. |

Two author-record discrepancies required explicit treatment:

- CritiqueLLM's current ACL and Crossref records name **Andrew Feng**; its PDF
  displays **Zhuoer Feng**. The bibliography follows the current publisher record,
  with the difference documented rather than silently altering the author list.
- OffsetBias's ACL/Crossref fields invert the third author's given/family names.
  The published PDF and downloaded arXiv BibTeX both give **Meiying Ren**. The
  entry uses `Ren, Meiying` on that basis while retaining the official Findings
  venue, year, pages, and DOI.

The provenance manifest `.paper/reference_sources.json` records sources and
claim boundaries. Cached downloads and the primary-field comparison are under
`build/citation-audit/related-20260920/` (ignored build artifacts).

## Claims deliberately not carried over from the project table

- Trained judges are not characterized as scalar-only or incapable of critique.
  Prometheus and CritiqueLLM are counterexamples; Self-Taught Evaluators iterate.
- EvalGen is interactive and explicitly discusses iteration and criteria drift.
- SPADE derives assertions from developers' prompt edits and selects them with
  labeled outputs. It is not characterized as ignoring failure information.
- OffsetBias addresses identified biases; this does not establish that it can
  never generalize beyond them.
- PoLL uses pooling, but that does not prove every ensemble lacks a mechanism
  for learning conditional source reliability.
- WebGrader already evolves evidence-using verifier skills and validates them
  before grader freeze. Agentic judges are not universally static.
- SkillOpt retains rejected-edit history; HarnessBank retains diverse harnesses.
  SkillHEX already has hypothesis-driven executable tests, persistent branches,
  and PUCT-style exploration/exploitation. ERA is not framed as the first method
  to diagnose failures, retain directions, or revise multiple components.
- SkillHEX's verifier-based experiments are a specific contrast, not a claim
  that all architecture search requires deterministic tasks. WebGrader also uses
  semantic judgment; describing it as wholly deterministic would be inaccurate.
- Explicit components permit inspection, not automatic causal attribution.
  Neither IPM sampling gains nor ERA superiority follow from this literature.

AHE, AgentOptimizer, and Split-and-Merge were not added from ambiguous short
names. Selective coverage is intentional; the section is not a reproduction of
every row or every representative in the project plan.

## Verification and remaining checks

The academic-writing, citation-management, and ML-writing skills governed the
methodological organization and the separation of identity, publication-field,
and claim-support checks. The user-recommended `reference-audit` was run as its
CLI at commit `c80461cbdd237b220a5bf5888ffd9a4068e51329`, with `--no-llm`.
Its placeholder SKILL.md is not represented as an installed writing skill.

The automatic screen found 46 unique identity matches among 52 entries, with
six unresolved entries, zero missing citation keys, and 13 uncited entries.
All seven additions and all four required preprints matched unique identities.
This is **not** a clean full-bibliography certification: the tool encounters
rate limits, can prefer an old preprint over the published version, and emits
13 false missing-include warnings for repository-root-relative figure inputs.
Successful LaTeX compilation resolves those inputs.

In particular, its DGM suggestion points to an unrelated/republication-style
record. The actual ICLR 2026 proceedings BibTeX controls the entry, not that
automatic suggestion. Agent-as-a-Judge retains its verified ICML 2025/PMLR 267
record rather than the 2024 preprint year returned by an index. Existing published
metadata checks for GEPA, DSPy, FLASK, and AutoCalibrate are also preserved.

An additional local field comparison checks **12 records**: the seven additions,
four required preprints, and DGM's official proceedings. There are zero remaining
differences from the selected primary records, after the documented OffsetBias
author correction. It explicitly checks publication type and venue for published
papers and prevents assigning a conference venue to the verified preprints.

The PDF compiles, terminology and whitespace checks pass, and no undefined
citations or overfull boxes remain in the final LaTeX pass. Full repository checks
are not all green:

- Main text remains **10 pages**, exceeding the initial-submission limit of 9;
  it was already 10 pages before this revision. Typography was not reduced.
- Removing unrelated citation lists leaves **13 unused bibliography entries**.
  They remain in the source library rather than being deleted to silence a check.
- Claim memory for C1/C27/C28/C42/C43 and Figure 1's caption is already stale
  relative to the author-edited abstract/introduction. Neither those sources nor
  their memory records were modified by this Related Work revision.

The paper remains a working draft with unresolved empirical claims. Literature
citations and this rewrite do not validate the author's result sentences.

### Round 29 checks

The three-heading revision retains all four author-required citations and changes
no bibliography entry or publication field. It reuses the primary-record checks
above rather than claiming a new full-bibliography certification. Compilation,
the terminology regression check, and whitespace checks pass. The PDF remains
37 pages with 10 main-text pages, so the existing initial-submission page-limit
issue is unresolved. Abstract, introduction, figures, and empirical status are
unchanged.

### Round 30 checks

The section now leads with shared goals and specific methodological differences.
All four required citations remain; no new citation or publication-field change
was introduced. Design statements were checked against the current Method and
claim memory, including separate candidate acceptance, program inheritance, and
direction continuation. C27/C28 remain empirical questions, not literature-backed
findings. Terminology and whitespace checks pass, and the rebuilt PDF has no
undefined citations or overfull boxes. The PDF has 36 total pages and 10 main-text
pages. The existing page-limit and stale-memory issues outside Related Work are
not claimed resolved.
