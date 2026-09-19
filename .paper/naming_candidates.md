# Naming candidates and collision screening

Screened: 2026-09-16. These are proposals, not an adopted project or method name.
The manuscript title remains unchanged; ERA remains the method name without an
invented expansion. No repository or source directory has been renamed.

## Shortlist

1. **SHIROE-Eval** — **S**elf-evolving **H**uman-**I**nformed **R**easoners for
   **O**pen-ended **E**valuation. The Easter egg is Shiroe (城惠) in *Log Horizon*.
   This is the closer semantic fit: evaluation agents evolve using human
   feedback, and the scope is explicitly open-ended. The name does not claim
   that their reasoning is a faithful explanation of human preferences.
2. **HIMARI-Eval** — **H**uman-**I**nformed **M**ultimodal **A**ssessment through
   **R**eflective **I**mprovement. The Easter egg is Himari (日鞠) in *Blue Archive*.
   This emphasizes feedback and the breadth of evaluated artifacts; the full
   paper title would still need to communicate agent self-evolution.

The `-Eval` suffix is part of each proposed public name, not an assertion that
the underlying character name is unused. Bare SHIROE already names an
[AI project-memory runtime](https://github.com/kanadhiayash/shiroe) and an
[agentic research manager](https://github.com/washwor1/Shiroe). Bare HIMARI has
unrelated software uses, including an [OIDC service](https://github.com/sorah/himari),
and a [Himari-ML repository](https://github.com/XNS-ivy/Himari-ML) described as
machine learning. SHIRO is also an existing
[reinforcement-learning method](https://arxiv.org/abs/2212.12786), a near-name
collision relevant to searchability even though it is not SHIROE-Eval.

## What was checked

- arXiv API: title searches for the bare names, followed by
  `all:"SHIROE-Eval" OR all:"HIMARI-Eval" OR all:"CHISE-Eval"`. The qualified-name
  query returned no entries. Stemming can return near-matches, so titles were
  inspected rather than treating raw counts as exact-name matches.
- GitHub public repository search: `"SHIROE-Eval" in:name is:public` and
  `"HIMARI-Eval" in:name is:public`, with `per_page=100`. Each returned zero
  repositories. Separate bare-name searches exposed the conflicts above;
  those broader searches reviewed the first 100 ranked results and were not
  exhaustive inventories of all repositories or their code.
- OpenAlex: `title.search:SHIROE` returned three soil/mycology titles with
  "shiroes"; `title.search:HIMARI` returned a voice pack and a literary study.
  Neither result set contained an evaluator or agent framework with that name.
- Ordinary web search was attempted as an additional check, but later
  DuckDuckGo requests returned HTTP 202 challenge pages. Those responses are
  not evidence of absence. Google Scholar automation was unavailable because
  its optional dependency was missing; DBLP returned an anti-bot page rather
  than search data. Neither source is counted as a completed clearance check.

Re-run the exact public-name searches before adopting a name:
[SHIROE-Eval on GitHub](https://github.com/search?q=%22SHIROE-Eval%22&type=repositories),
[HIMARI-Eval on GitHub](https://github.com/search?q=%22HIMARI-Eval%22&type=repositories).
The supported conclusion is **no exact qualified-name collision found within
these public checks**, not global uniqueness, trademark clearance, or absence
from unindexed/private work.

## Previously considered names that are occupied

- EVA: [EVA visual representation learning](https://arxiv.org/abs/2211.07636)
  and the more directly relevant [EVA-Score](https://arxiv.org/abs/2407.04969).
- SERA: [repository agents](https://arxiv.org/abs/2601.20789) and
  [SeRA self-reviewing alignment](https://arxiv.org/abs/2410.09362).
- ALICE: [active learning with natural-language explanations](https://arxiv.org/abs/2009.10259)
  and an [audio-language evaluation framework](https://arxiv.org/abs/2603.20433).
- VIOLET: [video-language transformers](https://arxiv.org/abs/2111.12681).
- FRIEREN: [video-to-audio generation](https://arxiv.org/abs/2406.00320).
- HERTA: [graph-neural-network training](https://arxiv.org/abs/2403.18142).
- SEELE: [Gaussian-splatting acceleration](https://arxiv.org/abs/2503.05168).
- HOMURA: [time-constrained LLM translation](https://arxiv.org/abs/2601.10187).
- ASUKA: [code-agent evaluation](https://arxiv.org/abs/2606.05920).
- KAEDE: [knowledge-aware question decomposition for KBQA](https://github.com/pvfeldt/KaeDe).
- CHISE: [character processing based on a character ontology](https://doi.org/10.1007/978-3-540-78159-2_14).

No papers from this naming check were added to the manuscript bibliography.
