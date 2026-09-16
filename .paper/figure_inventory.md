# Figure and table inventory

The structured caption and claim mapping is in `figures.yml`.
All nine figures are conceptual or explicitly synthetic; none contains observed
performance. Exact structure is native TikZ. Three controlled GPT Image 2 photos
illustrate source and candidates in Figure 7(b); one is reused in Figures 1(a)
and 6(b). The author's blue/mint/cream/peach/rose palette is shared across figures.
They are not empirical results. Design sources and the redesign rationale are
recorded in `visual_references.md`.

| ID | Source | Purpose |
| --- | --- | --- |
| Fig1 | figures/overview.tex | Concrete four-family gallery, human evidence, dominant ERA loop, C1/C2/C3 |
| Fig2 | figures/preference_mining.tex | Signal–dimension matrix, three semantic strata, H0–H3 and Z |
| Fig3 | figures/evaluator.tex | Worked pointwise summary example: artifact → observations → findings → fusion |
| Fig4 | figures/direction_search.tex | Direction versus connected edits, best/working state, four outcomes |
| Fig5 | figures/downstream.tex | Matched lanes for fixed-pool C1, shared-start C2, planned Base / own-rollout C3 |
| Fig6 | figures/domain_panorama.tex | Four-family task gallery with domain-specific evidence and quality criteria |
| Fig7 | figures/annotation_examples.tex | Webpage omission, photographic image edit, summary span, and research-plan examples |
| Fig8 | figures/data_boundaries.tex | Access timeline, one-way freeze boundary, independent metric reserve |
| Fig9 | figures/semantic_synthesis.tex | Finding groups, contradictions, and synthetic anchor interpolation |

| ID | Label | Purpose / status |
| --- | --- | --- |
| Tab1 | tab:ablations | Main controlled ablation families; design |
| Tab2 | tab:results | Per-domain C1 ID/OOD outcomes; unmeasured |
| Tab3 | tab:downstream-results | C2 and planned C3 contrasts; unmeasured |
| Tab4 | tab:domains | Complete 22-domain panorama; scope, not readiness |
| Tab5 | tab:human-provenance | Direct, adapted, material-only, and new annotations |
| Tab6 | tab:readiness | Knowledge, independence, artifacts, feedback and source audits |
| Tab7 | tab:full-ablations | Full condition and inference matrix; design |
| Tab8 | tab:training | Planned LoRA + GRPO controls; no training execution |
| Tab9 | tab:reporting | Required outcomes and interpretation limits |
| Tab10 | tab:manifest | Configuration fields to freeze; unresolved values marked TBD |

Numbers shown in diagrams are identifiers, planned design values, or synthetic
arithmetic, never study measurements. Figure 9's 50, 75, 100 anchors and lambda
0.4 illustrate a specified scale; 50 + 0.4 × 25 = 60 is not a scored example.
Figures 1, 2, 3, 6, and 7 explicitly disclose their constructed cases or preferences.

`make figures` produces individual vector PDFs, PNG previews, and a contact sheet
under `build/figure-review/`. This is an offline visual-review workflow, separate
from image generation. Inspect the manuscript at its final 5.5-inch text width.

Do not add decorative metric plots to fill placeholders. Empirical plots require
authorized analysis artifacts, explicit units/denominators, and uncertainty.
