# Visual references and redesign brief

Reviewed 2026-09-16. These sources inform visual communication, not P2E's
empirical claims. Original figures are neither reproduced nor traced in the
manuscript, and were not uploaded to the image-generation service.

## Primary references requested by the author

| Reference inspected | Primary source | Transferable design choice | P2E application |
| --- | --- | --- | --- |
| *A Survey on Post-training of Large Language Models*, arXiv 2503.06072v3; Figs. 1/2/5/8/12, PDF pp. 6/7/15/19/26 | [Versioned paper](https://arxiv.org/pdf/2503.06072v3) | Pale rounded groups, original role pictograms, airy cycles, and matched lanes distinguish processes without heavy borders. | Shared illustrated style, dominant ERA cycle, matched C1/C2/C3 lanes, and gentler visual hierarchy. |
| *A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment*, arXiv 2504.15585v4; Figs. 11/12, PDF pp. 27/28 | [Versioned paper](https://arxiv.org/pdf/2504.15585v4) | Illustrated nested structures show which objects and roles belong to each stage. | Explicit evidence, human-feedback, evaluator, and independent-assessment roles with small original pictograms. |
| *Speculative RAG: Enhancing Retrieval Augmented Generation through Drafting*, ICLR 2025, arXiv 2407.08223v2; Fig. 1, PDF p. 2 | [Versioned paper](https://arxiv.org/pdf/2407.08223v2) | Role-specific icons and restrained curved arrows make one method flow visually dominant. | Separate observing from judging; keep the central evolution cycle legible before reading the caption. |
| MMMR author site, `data_overview.png` and `data_summary.png`; linked arXiv 2505.16459v4, Fig. 2, PDF p. 3 | [Author site](https://mmmr-benchmark.github.io/), [versioned paper](https://arxiv.org/pdf/2505.16459v4) | A task gallery communicates diversity through recognizable artifacts and an organized taxonomy. | New four-family domain panorama with representative tasks, domain-specific criteria, and one feedback case per family. |

The MMMR site retains the title *MMMR: Benchmarking Massive Multi-Modal Reasoning
Tasks*. The inspected linked PDF is titled *MMLU-Reason: Benchmarking Multi-Task
Multi-modal Language Understanding and Reasoning* (v4, 2025-07-02). This distinction
records the source actually inspected rather than silently treating the titles
as identical. No task examples, dataset totals, or measured plots were reused.

## Secondary references from the preceding round

| Reference inspected | Primary source | Transferable design choice | P2E application |
| --- | --- | --- | --- |
| Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback*, Fig. 2, p. 3, arXiv v2 (2023) | [Paper](https://arxiv.org/pdf/2303.17651), [author site](https://selfrefine.info/) | Readable candidate text, specific feedback, and the modified object share a spatial alignment. | Annotated summary and image-edit examples; highlight the exact error rather than a generic document icon. |
| Ma et al., *Eureka: Human-Level Reward Design via Coding Large Language Models*, Fig. 2, p. 2 | [Author-hosted paper](https://eureka-research.github.io/assets/eureka_paper.pdf), [project](https://eureka-research.github.io/) | Concrete task/code artifacts sit inside a legible feedback cycle. Color distinguishes paths with different roles. | Give ERA the dominant visual area; separate proposal, measurement, and retained program state. |
| Yuksekgonul et al., *TextGrad: Automatic “Differentiation” via Text*, Fig. 1, p. 3, arXiv v1 (2024) | [Paper](https://arxiv.org/pdf/2406.07496), [author site](https://textgrad.com/) | A common information-flow language connects graphs, source-code edits, images, and task examples. | Keep conceptual structure vector-native, use a consistent evidence accent, and include tangible examples from different families. |
| Kirillov et al., *Segment Anything*, Fig. 1, ICCV 2023 | [CVF paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Kirillov_Segment_Anything_ICCV_2023_paper.pdf) | Task, model, and data are separate views; small real images clarify the objects manipulated by the method. | Distinguish acquisition, pointwise runtime, and independent studies; include synthetic artifact views with exact overlays. |

## Design brief

The overview should explain the research mechanism before the reader reads its
caption. Four domain families remain visible, but a generic gallery must not
occupy most of the figure. The dominant objects are evaluator disagreement,
structured human evidence, the editable program, and independent assessment.

- Use the author's uploaded five-color reference: blue `#74A9C5`, mint
  `#C2E5CF`, cream `#EDDDAB`, peach `#F2B8AE`, and rose `#DD7389`. Its sample
  performance plots supply no data for this paper. The local reference image
  itself is not a manuscript asset and is not redistributed.
- Blue/mint/cream/peach distinguish the four domain families; rose connects
  them to shared evaluator evolution. Elsewhere, mint marks acquired evidence,
  cream marks human judgment, and rose marks evolution or a labeled error.
  Darker companion inks keep labels readable; direct labels, hatching, and
  candidate letters carry meaning independently of color.
- Use softly tinted rounded groups, original outlined pictograms, restrained
  curved arrows, and whitespace. Avoid heavy dark headers and saturated blocks.
  This author-selected palette and illustrated style supersede the preceding
  round's saturated-accent brief.
- Use actual short sentences, candidate photographs, evidence pointers, and
  editable components instead of stacks of unlabeled paper icons.
- Assign different grammars to different relationships: gallery + feedback
  loop, annotated matrix, routed architecture, evolution branches, matched
  experiment lanes, domain panorama, worked comparisons, data-access boundary,
  and finding-to-factor graph.
- Make domain diversity substantive: show slides/web/charts, image synthesis/
  editing/3D, summaries/grounded answers/translation, and research ideas/
  ablations/reports. Give each a different quality criterion. The method and
  feedback schema are shared; the evaluation standards are not universal.
- Keep the principal labels at approximately 8–9 pt at manuscript width;
  subordinate labels may be 7–7.5 pt. Inspect final-size PDF renders, not just
  large standalone figures.
- No decorative performance curves, invented wins, or implied empirical
  trajectories. Every constructed example is disclosed in its caption.

## Image-generation brief

Use the explicitly requested `gpt-image-2` deployment through the user's Azure
Foundry resource and the imagegen skill's bundled CLI. Generate a controlled
photographic scene, then make targeted edits that preserve camera and scene
identity. This creates legible illustrative candidates, not benchmark outputs.
Keep all authoritative text, callouts, equations, routing, and annotations in
TikZ. Prompts contain only invented objects and generic aesthetic instructions.

The existing example is: “Add a red mug. Preserve the blue bowl.” The source has the
bowl alone. Candidate B adds the mug and retains the bowl. Candidate A retains
the mug but removes the bowl. All judgments about these images in the paper
are constructed demonstrations of the feedback schema, not collected human H.
The present palette/domain-diversity round reuses these disclosed assets and
edits native TikZ only; it makes no new image-generation API calls.
