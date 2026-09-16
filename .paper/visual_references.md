# Visual references and redesign brief

Reviewed 2026-09-16. These sources inform visual communication, not P2E's
empirical claims. Original figures are neither reproduced nor traced in the
manuscript, and were not uploaded to the image-generation service.

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

- Use dark ink, a white canvas, and restrained but saturated accents. Large
  pale rounded panels are not the default container.
- Color carries meaning: blue = artifacts / candidate A; coral = candidate B
  or a localized issue (always explicitly labeled); amber = human feedback;
  teal = acquired evidence; violet = program revision. Text and line styles
  carry the same distinction in grayscale.
- Use actual short sentences, candidate photographs, evidence pointers, and
  patch components instead of stacks of unlabeled paper icons.
- Assign different grammars to different relationships: gallery + feedback
  loop, annotated matrix, routed architecture, branching revision path,
  matched experiment lanes, worked comparisons, data-access boundary, and
  finding-to-factor graph.
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

The example is: “Add a red mug. Preserve the blue bowl.” The source has the
bowl alone. Candidate B adds the mug and retains the bowl. Candidate A retains
the mug but removes the bowl. All judgments about these images in the paper
are constructed demonstrations of the feedback schema, not collected human H.
