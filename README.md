# 人类反馈驱动的评价系统进化：论文草稿

**Evolving Evaluation Systems from Human Feedback**

本仓库撰写人类反馈驱动的评价系统进化论文，目前不使用项目缩写。研究范围是开放式生成的评估系统，涵盖结构化视觉产物、图像与 3D、文本生成和自动科研，不限定为 slide generation。ERA 仅指证据引导评估器演化方法，不是项目名称，也不另造缩写全称；历史来源与计划文件名保持原样。

论文依照源码项目的 `docs/plans/p2e_v2_plan.md` 及其最新 §3.2 补丁，以“给定任务及其人类反馈，能否进化出更符合该任务评价标准的 evaluator”为主线。复用已有偏好与新收集偏好是两种数据构建设置，共用算法；同一领域可以兼有两者。现成 H0 决定需要补哪些数据工作，不决定算法或领域定义。标签来源、协议、一致性、弃权和结果分别报告，新标注不被预设为更可靠。新建数据集与证明分歧采样有效是不同结论，后者需要等预算随机采样对照。

当前使用原版 ICLR 2027 模板、匿名审稿模式。按作者要求加入了**明确标记的模拟数据图表**，供审阅报告设计、配色和排版；没有实证结果，模板的 “Under review” 页眉不表示已经投稿。源码仓库 [Auto-Evolve-Harness-for-Slide-Evaluation](https://github.com/Moore-Tian/Auto-Evolve-Harness-for-Slide-Evaluation) 保留历史名称，本轮没有修改、重命名该代码仓库或启动实验。

## 阅读

- [paper.pdf](paper.pdf)：编译预览，正文 9 页。
- [main.tex](main.tex)：主入口，Overleaf 选择此文件。
- [sections/](sections/)：正文和附录，新增独立的偏好挖掘章节。
- [figures/](figures/)：9 张图，3 张正文图、6 张附录图；其中 2 张概念图、7 张模拟定量图。
- [data/simulated/](data/simulated/)：13 个带逐行 `SIMULATED` 标记的 CSV 和哈希清单，不含真实标注或实验结果。
- [可视化参考与设计说明](.paper/visual_references.md)：指定的 post-training survey（2503.06072）、full-stack safety survey、Speculative RAG、MMMR 图例，以及本项目采用的具体表达方式。
- [完整覆盖映射](.paper/plan_coverage.md)：计划条目与正文、图表、证据边界的对应。
- [主张索引](.paper/claims.yml)、[图表索引](.paper/figures.yml)：后续写作与图文一致性校验的结构化记忆。
- [references.bib](references.bib)：33 条引文，核对来源见 [reference_sources.json](.paper/reference_sources.json)。

概念图保留总览与六组件运行机制。定量图包括配对效应森林图、标注预算曲线、一致性／弃权／共识面板、选择排名构成、消融热图与箱线散点、refinement 雨云分布与胜负构成，以及质量—成本散点。12 张表覆盖模拟 C1 数值、完整 22 领域、两类数据来源、就绪与访问条件、消融、训练控制、报告要求和参数适配对照。22 个领域是研究全景；图表中的 8 个模拟队列不代表实际标签可用性，也没有缩减研究范围。

论证主线遵循计划 §§1–2.3：开放任务中的人类偏好依赖语境和多维取舍，难以直接变成可解释、可执行的自动评价标准；现有指标与 judges 因而可能偏离人类判断。我们研究利用偏好数据推动评价 agent 自进化，将结构化偏好挖掘与评价程序进化连接起来。人类标准是目标，进化的是程序对该标准的显式近似；误判原因定位是支撑机制，而不是论文的首要问题。ERA 以机制假设为探索单位、完整程序为选择单位。这些方法定义不构成绩效证据。

“为什么不只调参”通过明确的对照回答：校准已有分数的权重／阈值、固定结构的评价器权重微调，以及固定 base model 的程序进化。附录 Table 12 和共享观察对照区分改变证据与改变解释方式，核算相同监督下的适配、选择和部署成本。不声称微调不能学习标准或工具使用，也不预设进化更省数据或更有效。显式规则和轨迹可供检查，不等于已经证明解释忠实。这些评价器对照不同于 C3 的生成器训练，本轮没有执行或模拟微调结果。

C1 检验固定候选池上的对齐与选择；C2 从共享的新生成输出出发比较 critic，两种构建设置都需要对新输出另收盲化人类判断；C3 设计冻结 reward 下的 LoRA + GRPO 对照。C3 仅为研究设计，没有执行训练，也没有生成模拟训练结果。附录中的实证状态表与模拟图表分开，横线表示未测量，不是零值。

## 编译和检查

需要 TeX Live 或同等环境，含 pdfLaTeX、BibTeX、TikZ、algorithm/algpseudocode、booktabs/tabularx/longtable、multirow、placeins 和 natbib。离线检查使用 Python 3 标准库及 Poppler 的 `pdfinfo`、`pdftotext`。

```bash
make
make check
```

重新生成模拟数据、矢量图和数值表（需要 NumPy、Matplotlib 和 TeX Gyre Heros 字体）：

```bash
make simulated
# 或使用隔离环境（重新生成后检查图表与清单）：
uv run --python 3.11 --with numpy==1.24.4 --with matplotlib==3.7.5 python scripts/render_simulated_results.py
make check
```

生成器固定种子为 `20260916`，不调用模型、不执行 ERA、不读取 benchmark 结果。数值、区间和成本仅用于布局示例，不能用于预测效果、功效分析或方法排名。本轮生成环境为 Python 3.8.10、NumPy 1.24.4、Matplotlib 3.7.5、fontTools 4.57.0；相同环境可确定性再生成。隔离环境中的字体处理依赖也可能改变 PDF 字节，因此跨环境再生成后需重新审阅版面和清单。

逐图视觉检查（额外需要 Pillow、`standalone.cls` 和 `pdftoppm`）：

```bash
make figures
# 或在独立环境中运行，不改项目依赖：
uv run --python 3.11 --with pillow python scripts/render_figures.py
```

生成 `build/figure-review/` 下的独立矢量 PDF、PNG 与 `contact-sheet.png`；
可向脚本传入 `overview`、`evaluator` 等图名，只重绘指定图。预览渲染不调用模型 API。

构建中间文件位于 `build/`，最终文件为 `paper.pdf`。已提交的矢量图可直接编译，不要求本地重新生成模拟数据，也不需要 Azure 登录或模型 API。Overleaf 上传 TeX、BibTeX、模板、`figures/`、`output/imagegen/` 即可。`.paper/*.yml` 使用 JSON 兼容的 YAML，便于标准库检查，仍可由 YAML 工具读取。

`make check` 检查引用、标签、9 页限制、溢出、图像哈希与排印分辨率、22 领域、主张状态、图表标题和正文引用，以及模拟数据的配对、缺失分母、数值表、一致性、弃权和成本汇总。结构与算术检查不代替学术审读或实证验证。

`python3 scripts/check_simulated_results.py --submission` 是投稿保护检查：当前应以状态码 2 拒绝通过，因为仍有模拟图表。只有替换为获准的真实测量、重算区间并重新审计主张，才能形成含实证结果的投稿稿；不能仅删除模拟标记。

## 配色、字体与图表

三张作者配色参考合并为海洋蓝、海玻璃绿、沙金与珊瑚色：`#376795`、`#7BC0CD`、`#51999F`、`#BFDFD2`、`#DBCB92`、`#FFE6B7`、`#ECB66C`、`#ED8D5A`。方法图中 ERA 保持珊瑚色、静态工具种子保持蓝色；排名、分组或有符号效应另有明确图例，不依赖颜色单独传达信息。三张参考图原文件保留在作者工作区，不自动提交，也不使用其中的数值或显著性标记。

正文保留 ICLR 的 Times 字体和正式标题层级；两张 TikZ 图局部使用 Helvetica 兼容字体，定量图使用 TeX Gyre Heros。图标题约 8.5 pt、轴标题 8 pt、刻度和图例约 7.3–7.5 pt，按 5.4 英寸原生宽度输出并检查文字边界。表格采用三线表、对齐的数值列和轻量行底色。实际 PDF 页面的图注、段落断页、图例留白和图标碰撞也纳入检查，没有修改官方模板的字号、边距或版芯。

GPT Image 2 的已验证调用路线是指定 Azure Foundry 资源的 `/openai/v1/`，不是不可用。现有[原图](output/imagegen/edit-source.png) → [加红杯、保留蓝碗](output/imagegen/edit-preserved.png) → [误删蓝碗](output/imagegen/edit-omission.png) 的素材链和提示、哈希完整保留。目前只有图 1 使用保留蓝碗的照片，宽 1.96 cm，约 1990 DPI；其余照片和旧概念图已退出正文。本轮图表由原生矢量绘图生成，没有新增模型调用。[image_generation.md](.paper/image_generation.md) 记录素材来源，用户指定的 API 使用文档在前轮已经更新。

所有定量显示都有逐图、逐表、逐行的模拟披露。配对效应使用共同完成的输入；数值表使用各方法完成的输入；排名构成保留未评分输入，避免分母混用。新建数据、采样有效性和组件有效性仍需不同实验证据。主张 C27/C28 保持待验证，不因模拟图表升级为结果。写作不收录调试流水账或历史中间方法。

## 后续作者工作

冻结实际实验域、数据、标注协议、模型、对照和预算；提供经授权的结果与新生成输出的盲化判断；完成作者信息、许可、伦理和 AI 使用声明。不得用 H0 推导出并不存在的 H1/H2，不能把模型解释写成人类理由。

本公开仓库含可识别的项目来源，不是匿名补充材料。投稿前需独立检查 PDF、代码链接、补充材料与元数据的匿名性。不得提交凭据、私有运行路径、真实样本标识、日志、生成评估器或未经授权的结果。

## 模板来源

`iclr2027_conference.sty` 与 `iclr2027_conference.bst` 原样取自
[ICLR/Master-Template](https://github.com/ICLR/Master-Template/tree/46ed6f4c6cef5b175dde23639e77d44c3463b230/iclr2027)，提交 `46ed6f4c6cef5b175dde23639e77d44c3463b230`。
未修改字体、页边距或版芯。初投稿正文上限为 9 页，参考文献、附录及规定声明不计入；提交前再次核对当年官方政策。
