# Visual references and redesign brief

Reviewed 2026-09-16. These sources inform visual communication, not this paper's
empirical claims. Original figures are neither reproduced nor traced in the
manuscript, and were not uploaded to the image-generation service.

## Primary references requested by the author

| Reference inspected | Primary source | Transferable design choice | Application in this paper |
| --- | --- | --- | --- |
| *A Survey on Post-training of Large Language Models*, arXiv 2503.06072v3; Figs. 1/2/5/8/12, PDF pp. 6/7/15/19/26 | [Versioned paper](https://arxiv.org/pdf/2503.06072v3) | Pale rounded groups, original role pictograms, airy cycles, and matched lanes distinguish processes without heavy borders. | Gentle grouping and a dominant ERA cycle in the overview; C1/C2/C3 remain compact assessment lanes. |
| *A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment*, arXiv 2504.15585v4; Figs. 11/12, PDF pp. 27/28 | [Versioned paper](https://arxiv.org/pdf/2504.15585v4) | Illustrated nested structures show which objects and roles belong to each stage. | Explicit evidence, human-feedback, evaluator, and independent-assessment roles with small original pictograms. |
| *Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting*, ICLR 2025, arXiv 2407.08223v2; Fig. 1, PDF p. 2 | [Versioned paper](https://arxiv.org/pdf/2407.08223v2) | Role-specific icons and restrained curved arrows make one method flow visually dominant. | Separate observing from judging; keep the central evolution cycle legible before reading the caption. |
| MMMR author site, `data_overview.png` and `data_summary.png`; linked arXiv 2505.16459v4, Fig. 2, PDF p. 3 | [Author site](https://mmmr-benchmark.github.io/), [versioned paper](https://arxiv.org/pdf/2505.16459v4) | A task gallery communicates diversity through recognizable artifacts and an organized taxonomy. | Four-family artifact gallery and complete 22-domain table; quantitative panels retain named domain rows. The larger panorama and four worked cases are now archived. |

The MMMR site retains the title *MMMR: Benchmarking Massive Multi-Modal Reasoning
Tasks*. The inspected linked PDF is titled *MMLU-Reason: Benchmarking Multi-Task
Multi-modal Language Understanding and Reasoning* (v4, 2025-07-02). This distinction
records the source actually inspected rather than silently treating the titles
as identical. No task examples, dataset totals, or measured plots were reused.

## Secondary references from the preceding round

| Reference inspected | Primary source | Transferable design choice | Application in this paper |
| --- | --- | --- | --- |
| Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback*, Fig. 2, p. 3, arXiv v2 (2023) | [Paper](https://arxiv.org/pdf/2303.17651), [author site](https://selfrefine.info/) | Readable candidate text, specific feedback, and the modified object share a spatial alignment. | Annotated summary in the runtime diagram; the extended image-edit comparison is archived. |
| Ma et al., *Eureka: Human-Level Reward Design via Coding Large Language Models*, Fig. 2, p. 2 | [Author-hosted paper](https://eureka-research.github.io/assets/eureka_paper.pdf), [project](https://eureka-research.github.io/) | Concrete task/code artifacts sit inside a legible feedback cycle. Color distinguishes paths with different roles. | Give ERA the dominant visual area; separate proposal, measurement, and retained program state. |
| Yuksekgonul et al., *TextGrad: Automatic “Differentiation” via Text*, Fig. 1, p. 3, arXiv v1 (2024) | [Paper](https://arxiv.org/pdf/2406.07496), [author site](https://textgrad.com/) | A common information-flow language connects graphs, source-code edits, images, and task examples. | Keep conceptual structure vector-native, use a consistent evidence accent, and include tangible examples from different families. |
| Kirillov et al., *Segment Anything*, Fig. 1, ICCV 2023 | [CVF paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Kirillov_Segment_Anything_ICCV_2023_paper.pdf) | Task, model, and data are separate views; small real images clarify the objects manipulated by the method. | Distinguish acquisition, pointwise runtime, and independent studies; include synthetic artifact views with exact overlays. |

## Design brief

The overview should explain the research mechanism before the reader reads its
caption. Four domain families remain visible, but a generic gallery must not
occupy most of the figure. The dominant objects are evaluator disagreement,
structured human evidence, the editable program, and independent assessment.

### Three author color references

| Local reference, preserved outside the commit | Adopted principle | Current use |
| --- | --- | --- |
| `color_reference.jpg` | Soft blue/mint/sand/peach/rose family; color should not overpower data | Light surfaces, quiet grid lines, dark text; no copied example values |
| `color_reference_1.jpg` | Blue-to-warm progression; show distributions and individual observations | Blue static seed versus coral ERA; box/strip plots and raw-value overlays; no copied significance annotations |
| `color_reference_2.jpg` | Ocean blue, sea glass, sand, and coral with restrained contrast | Main shared palette and rank/outcome composition; no decorative radial plot |

The working palette reconciles these references: blue `#376795`, sky `#7BC0CD`,
teal `#51999F`, mint `#BFDFD2`, sand `#DBCB92`, cream `#FFE6B7`, peach `#ECB66C`,
and coral `#ED8D5A`. Ink is `#303C43`; darker companion colors carry small text
and outlines. The author-owned reference images are not manuscript assets and
are not automatically redistributed. Their plotted values are never used.

### Quantitative visual language

- Keep just two conceptual figures: the overview and pointwise runtime. The
  seven retired diagrams remain editable archives; their scientific definitions
  remain in the text, algorithm, and tables.
- Give each quantity a suitable visual form: forest plots for paired effects;
  matched-budget curves for acquisition; interval/lollipop/composition panels
  for annotation; stacked columns for selected ranks; heatmap plus box/strip
  plots for component and feedback comparisons; rainclouds plus outcome bars
  for refinement; scatter for quality–cost trade-offs. Avoid chart variety that
  obscures a comparison, 3D effects, ornamental frames, or decorative p-values.
- ERA remains coral and the static tool-augmented seed blue across method plots.
  Reused/new preference settings use teal/peach when setting identity is encoded
  by color. Rank and outcome plots have their own explicitly labeled ordinal
  mappings. Markers, dash patterns, hatching, zero references, and direct labels
  provide cues independent of color.
- Keep four-family diversity in concrete artifacts, the full 22-domain table,
  and named domain rows. Eight toy cohorts exercise the displays without
  claiming that these domains have particular labels or that one judge covers
  them universally. Reused/new preferences are construction settings.
- The author authorized simulated data to review chart design. Each CSV row,
  image, and caption is explicitly marked; the generator uses no observed
  benchmark values, annotators, models, or ERA implementation. Null/negative
  contrasts remain visible. The displays are not predicted effects, a power
  analysis, or evidence of any method's superiority. C27/C28 remain gaps.

### Typography and page composition

- Keep official ICLR Times body text, headings, margins, and the nine-page main
  limit unchanged. Diagram sans-serif is scoped to `phv`; charts use TeX Gyre
  Heros with embedded fonts. No body-wide font substitution is introduced.
- Render quantitative charts on a true 5.4-inch canvas. Titles are 8.5 pt,
  axis labels 8 pt, ticks/legends 7.3–7.5 pt, and disclosure notes 6.8 pt.
  Labels are bounds-checked before export; readable text is not sacrificed to
  automatic tight cropping. Native vector marks remain sharp when enlarged.
- Align numeric table columns, balance label and metric widths, and use booktabs
  rules with light row emphasis. Keep long prose columns left-aligned. Float
  placement should keep explanations near charts without isolated short tables.
- Review full-size figures and whole manuscript pages, including the title,
  main results, domain-table continuation, and appendix chart pages. Check icon
  overlap, arrow paths, legend padding, caption detachment, paragraph splits,
  and avoidable whitespace. An error-free build does not establish visual quality.

## Image-generation brief

Use the explicitly requested `gpt-image-2` deployment through the user's Azure
Foundry resource and the imagegen skill's bundled CLI. Generate a controlled
photographic scene, then make targeted edits that preserve camera and scene
identity. This creates legible illustrative candidates, not benchmark outputs.
Keep all authoritative text, callouts, equations, routing, and annotations in
TikZ. Prompts contain only invented objects and generic aesthetic instructions.

The existing lineage illustrates “Add a red mug. Preserve the blue bowl.” The
source has the bowl alone; the preserved candidate adds a mug, and a later edit
removes the bowl. Only the preserved candidate remains active, as the overview's
image-family vignette. The source and omission images are archived with their
prompts and hashes. They are constructed illustrations, not collected human H.
This quantitative/typographic round uses native TikZ and vector plotting,
reuses the disclosed photograph, and makes no new image-generation API calls.
