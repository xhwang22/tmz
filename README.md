# Dive Deeper, Branch Later: Self-Evolving Evaluators across Open-Ended Tasks

IterEval — iterative evaluator self-improvement from human feedback.

ICLR 2027 匿名模板工作稿，**当前正文 10 页，完整 PDF 34 页**。
Fig1(b) 已横向铺开三列内容，Table1/Fig3 的浮动页间距已收紧；正文仍超出初稿 9 页限制。
当前定量展示是理想情景的 aggregate assignments，不是实测结果。
图内不加模拟横幅，图注、首页和元数据保留来源说明。模板页眉不表示已经投稿。
作者编辑的 Abstract / Introduction 未改，其中的效果主张仍有证据缺口。

## 当前文件与图表

- [paper.pdf](paper.pdf)：最新编译稿；[main.tex](main.tex) 为编译入口。
- [实验填充总计划](.paper/experiment_fill_plan.md)：逐项实验、完整图表清单与执行先后。
- [22 域 baseline 执行书](.paper/baseline_execution.md)：给执行 agent 的数据规模、评分底座、优化器、预算与验收要求；[逐域数据文档/指标入口](.paper/baseline_domain_data.md)。最新执行范围是全部 22 域，不再限于四个优先域。
- [baseline / 数据源 / 出版字段审计](.paper/experiment_literature_audit.md)。
- [占位数值唯一入口](data/ideal_scenario/scenario.json)与[替换说明](data/ideal_scenario/README.md)。
- [真实记录空模板](data/experiment_templates/README.md)：保持空白；实际结果另建版本化目录。
- [当前图表索引](.paper/figure_inventory.md)、[主张记忆](.paper/claims.yml)、[图表记忆](.paper/figures.yml)。
- [术语约定](.paper/terminology.md)：IterEval 是完整框架，子方法不另设缩写。

| 正文展示 | 分工 | 文件 |
| --- | --- | --- |
| Fig. 1 | 上方案例带、下方左右对照；保留原分支画法及九处图像 | [teaser.pdf](figures/teaser.pdf) |
| Fig. 2 | 三面板：偏好挖掘、持续方向与诊断、下游应用 | [overview.pdf](figures/overview.pdf) |
| Table 1 | 七方法最终 held-out agreement、selection、regret、coverage | [results.tex](sections/results.tex) |
| Fig. 3 | 原环形 taxonomy、部署成本与质量、各域增益 | [landscape.pdf](figures/ideal_scenario/landscape.pdf) |
| Fig. 4 | 发展曲线、四个内部控制、方向结局 | [search.pdf](figures/ideal_scenario/search.pdf) |
| Table 2 | C2 新输出盲评、条件 C3 的结果槽位 | [results.tex](sections/results.tex) |

附录有 3 张图（A1–A3）和 19 张表（A1–A19），全部输入要求见填充计划。
Fig3 保留原 5.4 × 3.57 inch 紧凑构图、四家族色与湖绿，不再重排。
它重用 Table1 的底层数值来展示任务差异和部署代价，不构成独立证据。
只有四个优先域在当前情景中赋值，其余任务以横杠标明未纳入。

Fig1 保留上方案例带、下方左右对照及原分支拓扑，画布为 1840 × 880。
默认搜索底板从 516 加宽到 780 个局部单位，三列分支间距从 168 增至 264；
单行标题、1.1 倍截图及更舒展的诊断文字填充面板。右侧几何不变，不加渐变，不改九处图像及裁剪。
Fig2 未改。Fig1 印刷字号约 4.6–6.8 pt，照片 305–741 PPI；小标签及 Fig2 部分低分辨率图标的限制仍保留。
IterEval 的占位 agreement 从 81.0 调至 78.0，Best-of-N 从 66.0 调至 62.0，
regret 从 .158 调至 .192；相关曲线、成本、下游结果和正文宏同步。这不是实测结果的更改。
原 [landscape_outcomes.pdf](figures/simulated/landscape_outcomes.pdf) 和
[data/simulated/](data/simulated/) 都未改，现作为历史资源，不是当前正文数据。

## 方法与实验边界

两个子方法是 disagreement-based preference mining 和 depth-first evaluator evolution。
前者降低现有信号重复一致的比较的采样优先级，保留随机锚点；
既能复用兼容标签，也能给已有或新生成的输出补收人类偏好。

进化以 direction 为继续探索单位、完整 evaluation program 为选择单位。
程序的 parent choice 是 continuation 内部策略，不另立第三个核心概念。
方向 ID 不保证语义连续性，agent 结束方向的理由也不是自动验证的。

主测试使用**各域独立、未见原始输入/source groups**，不要求 OOD。
每个域分别适配；22 个任务是候选范围，不是已完成覆盖。
优先 SV4 网页、IG1 详细 caption、TG1 摘要、AR1 研究创意。

主表：固定 judge、Seed、learned signal fusion、SkillOpt、全程序 GEPA、
Meta-Harness、IterEval。保留官方优化器的原生历史和搜索能力；
SkillOpt 另与 text-only IterEval 做同编辑空间比较。
四个内部控制分别识别 parent retention、相同 parent 下的 direction priority、
以及 history，不能混为一项收益。

C1 测 agreement 与固定池 selection。C2 需新输出和新盲评；
C3 是独立授权后的冻结 reward 训练，不因填入理想数值而成为已执行实验。
没有捏造真实轨迹、rater 记录、独立搜索结果、置信区间或许可。

## 编译、替换与检查

需要 TeX Live、TeX Gyre、Python 3、NumPy、Matplotlib 和 Poppler。
正常编译不调用模型 API。

```bash
make ideal
make
make check
```

`make ideal` 从唯一 JSON 生成图、数值表和正文宏。
普通 `make` 也会在已登记的情景源或生成脚本变动后更新生成物。
检查包括引用/图号、9 页限制、来源哈希、跨表数字、偏好率和证据边界。
检查通过不代表实验证实。

```bash
python3 scripts/check_ideal_scenario.py --submission
```

当前门禁必须失败。真实数据请另存版本化目录，依据空模板生成原始记录与
可审计汇总，再接入现有布局；同时更新分母、区间、provenance 和结果解释。
不要给理想情景改标签冒充实测，也不要将其数值填入真实记录。

历史图的重建脚本只用于历史资源维护，不用来生成本轮实测结果。
图稿预览使用稳定路径，不累积重复版本。

Fig1 的 SVG 排版与导出可单独重建（导出需要 CairoSVG）：

```bash
python3 scripts/layout_teaser.py
uv run --with cairosvg python scripts/render_teaser.py
python3 scripts/check_teaser.py
make
```

当前结构检查会如实报告正文超出 9 页；其余来源、数字及图形检查不替代该门禁。

## 来源与发布边界

当前 40 条参考文献全部被引用，保留作者指定的四篇 2026 年论文。
出版字段及来源见实验文献审计和
[reference_sources.json](.paper/reference_sources.json)。
未使用条目保存在 [.paper/archive/](.paper/archive/)。

工程来源为
[Auto-Evolve-Harness-for-Slide-Evaluation](https://github.com/Moore-Tian/Auto-Evolve-Harness-for-Slide-Evaluation)。
本次发布保留此前已整理的论文修订、实验规划和 22 域执行文档，并更新 Fig1 与编译稿。
没有修改工程实现，也没有运行实验、标注或训练；旧候选图和运行缓存不纳入发布。

官方模板来自
[ICLR/Master-Template](https://github.com/ICLR/Master-Template/tree/46ed6f4c6cef5b175dde23639e77d44c3463b230/iclr2027)；
字号、页边距及模板文件不变。
投稿前还需真实证据、声明和匿名审查。公开论文仓库不等同于匿名补充材料，
不得放入凭据、私有运行路径或未经授权的样本和日志。
