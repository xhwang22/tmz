# Visual references and redesign brief

Source figures reviewed 2026-09-16; palette and composition update 2026-09-17.
These sources inform visual communication, not this paper's
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
| `color_reference.jpg` | Its five labeled blue/mint/cream/peach/rose colors; white paper and dark labels | Candidate A, provisional manuscript treatment: `#74A9C5 #C2E5CF #EDDDAB #F2B8AE #DD7389` |
| `color_reference_1.jpg` | Its labeled blue-to-orange progression; distributions and individual observations | Candidate B: `#72BCD5 #AADCE0 #FFE6B7 #F7AA58 #EF8A47`; no copied significance annotations |
| `color_reference_2.jpg` | Its labeled mint/teal/sand/apricot palette | Candidate C: `#4198AC #BFDFD2 #DBCB92 #ECB66C #ED8D5A`; no decorative radial plot |

The author rejected the four round-10 directions and asked for closer use of
the supplied references. Each current candidate is confined to one reference's
labeled swatches, without arbitrary purple, copper, or deeper-blue base fills.
`palette_candidates.md` records all source HEX sequences and role mappings.
Each method comparison uses the five colors together, in the order static
judge, static tools/seed, prompt optimization, program search, and ERA.
Use white paper, neutral ink `#25272B`, dark numerals `#202226`, source-colored
marks, and only light source tints for larger surfaces. Colored plot headers
are removed. Darker companions are confined to fine strokes, points, and small
diagram labels; they preserve source hue through sRGB scaling. This is a review
candidate, not a final author-approved identity. Local original thumbnails and
source hashes are included in `build/reference-palettes/` for comparison only.
The originals are not manuscript assets and are not automatically redistributed;
their plotted values and significance annotations are never used.

### Quantitative visual language

- Keep just two conceptual figures: the overview and pointwise runtime. The
  seven retired diagrams remain editable archives; their scientific definitions
  remain in the text, algorithm, and tables.
- Give the main text an all-domain C1 atlas: every one of the 22 tasks, grouped
  6/6/5/5 in taxonomy order, with five method columns and aligned paired effects.
  Printed percentages and 0–100% micro-bars share a quantitative scale; column
  colors identify methods, not scores. Show positive, near-zero, and negative
  contrasts. Expanded ID/OOD intervals, the C1 table, acquisition curves, and
  mechanism/feedback-detail panels belong in the appendix. C2 stays separate:
  shared task names do not establish shared C1/C2 input groups or correlation.
  Eight quantitative figures use 14 CSVs. Fourteen C1 domains are added while
  the original eight C1 records/intervals and diagnostic data remain intact.
- Give each quantity a suitable visual form: paired-effect interval tables
  with aligned signed means; matched-budget curves with endpoint labels;
  interval/bar/composition panels for annotation; slim horizontal rank ribbons;
  a heatmap plus split violins with raw observations for component and feedback
  comparisons; rainclouds plus a diverging preference balance for refinement;
  aligned cost and agreement profiles sharing named method rows. Abstentions
  occupy a separate numeric column, with the same all-input denominator as
  wins and ties. Cost connectors pair settings for one evaluator; they are not
  a search trajectory or a Pareto frontier. Avoid chart variety that
  obscures a comparison, 3D effects, ornamental frames, or decorative p-values.
- Candidate A uses the complete blue/mint/cream/peach/rose method ensemble;
  static tools/seed is mint, ERA rose, and metric-only anchors neutral.
  Family, feedback-level, policy, rank, and outcome mappings are explicitly
  labeled where those quantities use color. Four H levels use four colors,
  not an invented fifth level. The component heatmap uses all five with cream
  at zero; all five acquisition policies retain equal-width lines and bands.
  Markers, dash patterns, sparse hatching, zero references, and direct labels
  provide cues independent of color; split-violin settings use left/right.
- Keep four-family diversity in concrete artifacts, the full 22-domain table,
  and all 22 named C1 domain rows. Annotation, component, and C2 detail retains
  eight clearly labeled diagnostic domains. Neither scope claims actual labels,
  completed experiments, or universal transfer. Reused/new preferences are
  construction settings; R/N tags are illustrative, not permanent domain classes.
- The author authorized simulated data to review chart design. Each CSV row,
  image, and caption is explicitly marked; the generator uses no observed
  benchmark values, annotators, models, or ERA implementation. Null/negative
  contrasts remain visible. The displays are not predicted effects, a power
  analysis, or evidence of any method's superiority. C27/C28 remain gaps.

### Typography and page composition

- Keep official ICLR Times body text, headings, margins, and the nine-page main
  limit unchanged. The main overview uses scoped TeX Gyre Heros (`qhv`), matching
  the charts; the runtime diagram retains `phv`. Fonts are embedded, and no
  body-wide font substitution is introduced.
- The overview's typography pass retains its 13.7 by 8.1 cm native canvas,
  palette, four artifact families, two feedback settings, ERA loop, and three
  assessment roles. Use regular-weight action labels, aligned card text, and
  explicit padding for the human-evidence and assessment cards. Local
  `transform shape` restores the intended pictogram sizes; separate curved
  paths from text. This is a presentation change, not new scientific content.
- Render quantitative charts on a true 5.4-inch canvas. Titles are 8.5 pt,
  axis labels 8 pt, ticks/legends 7.3–7.5 pt, and disclosure notes 6.8 pt.
  A bold 9 pt panel letter, regular-weight title, and fine rule establish a
  common header. White space, restrained row guides, white-edged markers, and
  direct numeric labels carry the hierarchy; heavy frames are unnecessary.
  Numerals on source fills use #202226 ink; colored method blocks do not need
  white labels or arbitrary darkening. Setting and component sublabels
  are 7 pt; component columns retain clear inter-label gaps.
  A pale-accent simulation badge and companion notice remain visible in every
  quantitative figure. The original eight C1 records and intervals and all
  diagnostic-only CSVs remain intact; the 22-domain C1 aggregates are recomputed.
  Each palette candidate uses identical data, denominators, scales, and geometry.
  Labels are bounds-checked before export; readable text is not sacrificed to
  automatic tight cropping. Native vector marks remain sharp when enlarged.
- `make palettes` verifies exact source-to-role mapping and 29 text/background
  contrast pairs per candidate, including diagrams, badges, and heatmaps, and
  exports grayscale proofs. Direct values, signed effects,
  separate ID/OOD panels, and explicit left/right split-violin labels complement color;
  a contrast check is not a universal color-vision accessibility certification.
  All 14 CSVs and the numerical table match the canonical fixtures byte for
  byte; all 110 main-atlas values and 22 paired effects are checked.
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

## Main composite integration (2026-09-19)

The approved v20 UNI-style landscape composition supersedes the atlas guidance
above for main Figure 2: task composition ring, cost/agreement scatter and four
family bar panels in one row. It retains the source-derived family colors in
Microsoft spatial order, light baseline ramps and a common lake-green ERA accent.
Source Sans 3 / Source Serif 4 are embedded; no new imagery is generated.
Exact PDF/SVG/PNG and numerical exports are published with a separate balanced
synthetic-subset manifest. The full-cohort atlas remains a historical asset,
not an active main-text figure. Raw author reference JPEGs are not redistributed.
