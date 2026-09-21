# Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks

IterEval — iterative evaluator self-improvement from human feedback.

论文采用 ICLR 2027 匿名审稿模板。当前是含**明确标记的模拟定量图表**的工作稿，
不是已完成实证验证的投稿稿。模板页眉不表示已经投稿。作者修改后的 Abstract /
Introduction 中的收益表述仍未得到实证验证；C27/C28 保持证据缺口状态。

## 阅读与当前图表规划

- [paper.pdf](paper.pdf)：37 页编译预览，正文 11 页，尚超出初投稿的 9 页限制。
- [main.tex](main.tex)：编译入口；Overleaf 选择此文件。
- [sections/](sections/)：正文与附录。
- [完整图表索引](.paper/figure_inventory.md)：13 张图、15 张表。
- [计划覆盖映射](.paper/plan_coverage.md)：研究问题、实验设计、图表及证据边界。
- [主张记忆](.paper/claims.yml) / [图表记忆](.paper/figures.yml)：写作与图文一致性校验。
- [术语约定](.paper/terminology.md)：IterEval 为完整框架，两个子方法不另设缩写。

| 正文展示 | 作用 | 文件 |
| --- | --- | --- |
| Figure 1 | image-editing 案例；保留作者认可的三栏布局和九处图像细节 | [正文 PDF](figures/teaser.pdf) · [作者三栏 SVG](figures/candidates/teaser-v6-paper-wording/teaser.svg) |
| Figure 2 | 原拟物化 overview：任务、偏好挖掘、环形进化流程、下游应用 | [overview.tex](figures/overview.tex) |
| Figure 3 | C1 任务分类、偏好一致性与 Best-of-4、22 个任务的 OOD 汇总 | [PDF](figures/simulated/c1_landscape.pdf) · [SVG](figures/simulated/c1_landscape.svg) |
| Table 1 | 完整 ID/OOD 对齐与选择对照；数值仍待测 | [Results](sections/results.tex) |

Figure 1 保留作者更新的 SVG 文字、几何与九张嵌入图，方法色改为湖绿色。
正文直接使用该三栏版本，不再使用此前重排的 teaser-print.tex。
九处照片在正文宽度下均不低于 300 DPI；文字与路径保留矢量。
小标签在 5.4 英寸宽度下约 2.5–4.7 pt，是现有版本的可读性限制，
不能因此擅自重排作者认可的布局。

Figure 2 恢复原有四面板、拟物图标、照片、圆角卡片和环形进化流程。
只调整局部标签换行和箭头间距，不替换为泳道或扁平状态机。
接受候选、继承程序和继续方向的区别，以及停止后换方向的可能性保留在图注和方法中。

方法块使用湖绿 `#62AAA5` 和深色 `#477D79`，与正文性能图呼应；红色只用于错误状态。
Figure 3 的布局、数据和绘图产物未改。原 [landscape_outcomes.pdf](figures/simulated/landscape_outcomes.pdf)
保留为附录 Figure 6。运行结构、预算占位分别是附录 Figure 4、5；其余附录图顺延，
表号不变。三张概念图、一张预算占位和九张模拟定量图均不构成效果证据。

## 方法与实验边界

两个子方法统一为 **disagreement-based preference mining** 和
**depth-first evaluator evolution**。前者降低现有信号反复一致的比较的采样优先级，
保留随机锚点；从现成数据集或新产物中选比较，复用兼容的人类偏好或补收缺失标签。
信号一致不保证正确，分歧也不保证有信息量。

后者以 direction 为继续探索的单位、完整 evaluation program 为选择单位。
候选接受、程序继承和方向继续是不同决定；base model 权重固定。
公式表达实现中的更新与选择规则，不声称收敛、泛化保证或自动语义证伪。

研究范围为四族 22 个任务。C1 检验对齐和固定池选择；C2 从共享新输出出发比较
critic-guided refinement，需要新收盲化判断；C3 为冻结 reward 下的生成器训练设计，
没有执行或模拟训练。程序进化、校准与 evaluator fine-tuning 的对照不同于 C3。

[data/simulated/](data/simulated/) 保留全量模拟记录、旧图均衡子集及正文 C1 汇总。
本次图表重排没有修改 30 份已跟踪 CSV 或任何定量图产物。
复用／新收偏好是数据构建设置，不是固定领域分类或真实标签可用性的证明。

## 编译与检查

需要 TeX Live（pdfLaTeX、BibTeX、TikZ、algorithm、longtable 等）、TeX Gyre 字体、
Python 3、NumPy 和 Poppler。普通编译不调用模型 API，不需重新生成图片或模拟数据。

```bash
make
make check
```

目前编译、图表来源、术语、论文记忆和模拟数值检查通过，无 overfull box 或未定义引用。
`make check` 的结构检查仍报告正文超页和 17 条未使用的文献；不表示可直接投稿。
`python3 scripts/check_simulated_results.py --submission` 必须拒绝当前模拟工作稿。

逐图预览（需要 Pillow 和 `standalone.cls`）：

```bash
python3 scripts/render_figures.py teaser overview evaluator budget_tests
```

预览输出在 `build/figure-review/`。正文通过 `teaser.tex` 直接引用作者三栏版本的
`teaser.pdf`，不使用已否决的 `teaser-print.tex`。重新导出：

```bash
uv run --with cairosvg python scripts/render_teaser.py
python3 scripts/check_teaser.py
```

`make simulated` 重建全量模拟图；`python3 scripts/render_c1_landscape.py` 重建正文 C1
汇总图。重新生成后需复核数值、字体、版面与清单，不能只更新哈希以通过检查。
配色设计历史见 [.paper/palette_candidates.md](.paper/palette_candidates.md)，当前方法色
及图号以 [style_overrides.md](.paper/style_overrides.md) 和图表索引为准。

## 文献、来源与投稿准备

[references.bib](references.bib) 共 52 条记录，当前引用 35 条，保留作者指定的四篇
2026 年论文。来源及出版处核验见 [reference_sources.json](.paper/reference_sources.json)、
[citation_audit.md](.paper/citation_audit.md) 和 [相关工作审查](.paper/related_work_audit_20260920.md)。
本轮没有改动文献元数据、Abstract 或 Introduction 的论证文本（仅更新图引用和图注）。

工程来源为 [Auto-Evolve-Harness-for-Slide-Evaluation](https://github.com/Moore-Tian/Auto-Evolve-Harness-for-Slide-Evaluation)，
其历史仓库名不限制论文任务范围。本轮只修改论文仓库，没有启动实验或改动工程实现。
Teaser 图像、偏好与路径均为构造例子，不是实际标注或优化轨迹。

官方模板来自 [ICLR/Master-Template](https://github.com/ICLR/Master-Template/tree/46ed6f4c6cef5b175dde23639e77d44c3463b230/iclr2027)，
未修改模板文件、字号或页边距。标题自然排成两行，摘要不含引用。

投稿前仍需替换模拟数据、验证收益主张、精简正文、审查引用、完成作者与伦理声明，
并独立检查匿名性。本公开仓库含项目来源，不是匿名补充材料；不得上传凭据、私有运行
路径、未经授权的样本、日志、生成评价器或实验结果。
