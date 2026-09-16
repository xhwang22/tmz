# Figure and table inventory

The structured caption and claim mapping is in `figures.yml`.
All eight figures are conceptual or explicitly synthetic; none contains observed
performance. Exact structure is native TikZ. The sole generated raster is used
in Figure 1(a), not as an empirical result.

| ID | Source | Purpose |
| --- | --- | --- |
| Fig1 | figures/overview.tex | Four families → preference mining → ERA → C1/C2/C3 |
| Fig2 | figures/preference_mining.tex | Signal–dimension matrix, three semantic strata, H0–H3 and Z |
| Fig3 | figures/evaluator.tex | Six-component pointwise evaluator, sourced findings and fusion |
| Fig4 | figures/direction_search.tex | Direction versus connected edits, best/working state, four outcomes |
| Fig5 | figures/downstream.tex | Fixed-pool C1, fresh-shared-start C2, planned own-rollout C3 |
| Fig6 | figures/annotation_examples.tex | Synthetic summary, image-edit, and research-plan annotation examples |
| Fig7 | figures/data_boundaries.tex | Proposal/Train/Val/Test access and independent metric reserve |
| Fig8 | figures/semantic_synthesis.tex | Finding groups, contradictions, and synthetic anchor interpolation |

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
arithmetic, never study measurements. Figure 8's 50, 75, 100 anchors and lambda
0.4 illustrate a specified scale; 50 + 0.4 × 25 = 60 is not a scored example.
Figures 2 and 6 explicitly disclose their constructed preferences.

Do not add decorative metric plots to fill placeholders. Empirical plots require
authorized analysis artifacts, explicit units/denominators, and uncertainty.
