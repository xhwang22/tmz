# 实验设计的文献与实现审计

核查日期：2026-09-21。用于选择基线、界定可比较对象和数据角色；不是复现报告，也不是穷尽所有文献的系统综述。主来源为官方论文/会议出版页、作者仓库 README 和接口说明。已发表版本优先；没有确认出版处时保持 arXiv，不能凭项目年份填会议。元数据逐项来源见 reference_sources.json。

## 1. 核心 baseline 的位置与实际能力

| 方法 | 出版记录与一级来源 | 对实验的直接约束 | 尚待本项目完成 |
|---|---|---|---|
| SkillOpt | [arXiv:2605.23904](https://arxiv.org/abs/2605.23904)，2026；[Microsoft 官方代码](https://github.com/microsoft/SkillOpt) | 文本/skill 优化；保留 reject buffer、历史及选定 meta/slow update。不是无记忆重启。用 text-only IterEval 做同空间对照 | pin 论文对应 variant，区别后续 SkillOpt-Sleep；共享模型/证据/预算；smoke test |
| GEPA | [ICLR 2026 正式出版页](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0e9e708b6f48e14fd0ac29e167413f76-Abstract-Conference.html)；[官方代码](https://github.com/gepa-ai/gepa)；arXiv:2507.19457 | 当前 program-capable / optimize_anything 接口可以优化完整程序。保留 reflective mutation、population/Pareto selection 和选定 merge policy；不称 prompt-only | pin API/commit，完整 program adapter、可见反馈和工具计费 |
| Meta-Harness | [arXiv:2603.28052](https://arxiv.org/abs/2603.28052)，2026；[官方代码](https://github.com/stanford-iris-lab/meta-harness) | 编码 agent 可查看此前程序/分数/traces。不是只从 incumbent 出发。官方有 text classification/TerminalBench 示例；README 明确清理版可运行不等于逐项复现论文结果 | proposer transport 与相同模型匹配、artifact interface、日志访问控制；不能把默认 Claude 环境当已匹配 |
| Fixed model judge | 本项目固定参照条件，不冒称新发表算法 | 同 backbone，固定评分 prompt，pointwise；无额外工具，所以不是与 full IterEval 同观测的机制消融 | prompt、尺度、资源、重复评分 |
| Seed evaluator | 本项目原生未进化程序 | 原始六组件、工具和路由固定；可同时作 C1/C2/C3 参照 | freeze seed hash、运行时依赖 |
| Learned signal fusion | 本项目明确实现的常规 preference predictor | 正则化 pairwise logistic ranker，固定 features，用其 pointwise linear score 排序；单分数单调校准不能宣称提升 ranking | 训练归一化、正则选择、missing policy；不在 Test 上选择 |

官方 SkillOpt 在实现仓库中的历史审计 SHA：79124b37e9a6371e13b753f8bcd7adb1e493ade1。它只是已读版本，不自动成为本次运行版本；运行前仍需冻结。各方法已有代码≠跨模态接口已经适配成功。任何匹配失败保留为 readiness 状态，不填零分或假结果。

## 2. 可选优化路线与不作为必测行的原因

| 工作 | 一级来源 / 出版状态 | 与 IterEval 的关系与取舍 |
|---|---|---|
| AFlow | [官方实现](https://github.com/FoundationAgents/AFlow)，[arXiv:2410.10762](https://arxiv.org/abs/2410.10762)，ICLR 2025 | 第一优先可选 workflow-search baseline。官方 BaseBenchmark 支持定制评分接口；多模态适配仍需验证。不能等同于 IterEval 内部的 history-only control |
| ADAS | [官方实现](https://github.com/ShengranHu/ADAS)，[arXiv:2408.08435](https://arxiv.org/abs/2408.08435)，ICLR 2025 | 自动架构设计路线；与 GEPA、Meta-Harness 有实验覆盖重叠，非每域强制 |
| DGM | [官方实现](https://github.com/jennyzzt/dgm)，[arXiv:2505.22954](https://arxiv.org/abs/2505.22954)，ICLR 2026 | archive 与经验检验的重要先例；原生代码任务环境与本文不同，不能把移植成本隐去 |
| AgentOptimizer | [arXiv:2402.11359](https://arxiv.org/abs/2402.11359) | 函数/工具作为可优化对象的先例，不据名称判定它只能改 prompt；未新增为主表必跑项 |
| SkillHEX | [arXiv:2608.05628](https://arxiv.org/abs/2608.05628) | 相关 harness/skill evolution；本次未确认可直接运行的官方适配，保留 related work |
| HarnessBank | [arXiv:2607.13683](https://arxiv.org/abs/2607.13683) | 论文说明代码随接收发布；未确认本次可用官方实现，不伪造 reproduction |
| WebGrader | [arXiv:2608.06474](https://arxiv.org/abs/2608.06474) | Web 功能/验证相关，不直接覆盖主观多维视觉质量 |
| Evaluator fine-tuning | Prometheus / CritiqueLLM / Auto-J 等既有条目和来源 | 训练 judge 可以产出 critique，不概括成只能 scalar。仅在共同开放权重和相同观测条件下作补充对照；不能拿不同 backbone 的现成强 judge 归因于优化机制 |

C3 的 GRPO 是下游 generator 训练，不是 evaluator fine-tuning；不能互相替代。
同样，SkillOpt 的论文效果不是本文同预算比较的预期值。

## 3. 数据资源：到底提供什么

| 数据/研究 | 一级来源与出版处 | 能复用的东西 | 不能直接声称的东西 |
|---|---|---|---|
| SummEval | [Yale-LILY README](https://github.com/Yale-LILY/SummEval)，TACL 2021 | 原文关联、系统摘要、coherence/consistency/fluency/relevance 人工评分。README 给出100 articles ×16 summaries；每摘要 crowd/expert ratings | 维度评分不是自动存在的总体 H0；转换规则与偏好构念须验证。同 article 派生输出必须同组 |
| DOCCI | [项目](https://google.github.io/docci/)，[Springer 出版页](https://link.springer.com/chapter/10.1007/978-3-031-73027-6_17) | 图像、详细人工描述、相关图像/实体信息，CC BY4.0。可作 IG1 输入和参照材料 | 没有现成“多个生成 caption 的偏好”；仍需生成/恢复输出再标注。arXiv 正确编号2404.19753 |
| Research ideas / AI-Researcher | [作者代码与数据](https://github.com/NoviScl/AI-Researcher)，[ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ea94957d81b1c1caf87ef5319fa6b467-Abstract-Conference.html) | 研究创意和专家评分/reviews，主题级 grouping，可能提供符合构念的排序信号 | expert scores 不能不经审计就变成完整 N-way 排序；不能从 report rubric 推出 ideation 适用性 |
| Design2Code | [作者 README](https://github.com/NoviScl/Design2Code)，NAACL 2025 正式版本 | 截图、HTML、生成输出及 human pairwise/direct assessment 链接，支持 SV2 reconstruction；484-page benchmark | 不是 specification-to-web 的 SV4 数据；截图相似不等于功能满足。许可与当前资产可下载性须冻结 |
| Pick-a-Pic / PickScore | [官方 README](https://github.com/yuvalkirstain/PickScore)，NeurIPS 2023 | 文生图人类成对偏好，可用于 IG2；需固定 v1/v2、图像资产和训练重叠 | 不是 caption 偏好；URL-only 图片可能失效。本次部分 Hugging Face 请求401，不能宣称所有资产下载可用 |
| ImageReward | [官方 README](https://github.com/THUDM/ImageReward)，NeurIPS 2023 | 文生图 preference/reward 资源；benchmark 每 prompt 的多图排序可供资格审计 | 不是 image-to-text 评分器；作为优化信号的 reward 不能同时是独立 test metric；检查训练污染 |

SV4 目前没有在这次调研中确认可直接替代目标任务的现成偏好库，保留新输出/新标注路线。上述资源都是候选，不是22域数据已就绪。领域标准、group、assets、版本、许可、label provenance 和转换忠实性仍需 A2/A3/A5 逐项填写。

## 4. 必须保留的四篇相关工作

| arXiv ID | 本文承担的作用 | 不外推的结论 |
|---|---|---|
| [2604.13602](https://arxiv.org/abs/2604.13602) / reward hacking | 说明离线一致性不够，优化 reward 后需要独立 human endpoints 与 exploitation probes | 不当作 IterEval 已能防 reward hacking 的证据 |
| [2601.03986](https://arxiv.org/abs/2601.03986) / Benchmark² | benchmark/evaluator 质量与学习的相关路径，支持区分被优化信号和独立测量 | 不据此宣称本项目测试集天然无偏或具普适标准 |
| [2605.23899](https://arxiv.org/abs/2605.23899) / SkillLens | 从经验到可用技能的相关演化路线 | 不把现成 text/skill 优化框架说成无历史 |
| [2602.03619](https://arxiv.org/abs/2602.03619) / query-specific rubrics | query-specific 评价标准；[作者公开 rubric model](https://huggingface.co/fdu-lcz/rubric_generator) | 对象是 DeepResearch reports，不自动是 research ideas |

四条保留既有引用和已审计 metadata，未虚构会议出版字段。
新增的 Meta-Harness 也保持 arXiv；已发表的 GEPA/DOCCI/研究创意采用正式出版记录。

## 5. 本次出版字段纠错与最终检查

- DOCCI 的会议名称是 Computer Vision -- ECCV 2024，但 Springer 官方引用年份为2025；Crossref online date 2024-11-26、项目2024写法和 publisher citation year不同。按 [官方 BibTeX](https://citation-needed.springer.com/v2/references/10.1007/978-3-031-73027-6_17?format=bibtex&flavour=citation) 使用2025，页291–309、DOI10.1007/978-3-031-73027-6_17，完整12作者依官方顺序。
- 研究创意论文 ICLR2025 的官方 BibTeX 页94003–94092；这不是凭常见页长猜测。[官方导出](https://proceedings.iclr.cc/paper_files/paper/781-/bibtex)。
- GEPA 正式版是 ICLR2026，不能按2025 arXiv首次发布时间写成2025 conference。
- Design2Code 正式版 NAACL2025，不能因旧 README 的 arXiv2024 就覆盖出版处。
- OffsetBias 的既有记录是 Findings of EMNLP2024，不是 main conference；未用的条目移入 archive，出处记录一起保存。
- Self-Refine / LoRA / DeepSeekMath 用于下游设计，不据其效果推算本文收益。
- 活跃 bibliography 的引用、出处记录和未使用条目由本地 checker核对；结构检查不能替代 full-text inference，也不能证明实验可运行。

## 6. 仍待确认的项目，不写成“调研已经解决”

所有七种接口的共同模型运行、完整数据许可/下载、跨源污染、能支持统一 N 的独立组数、专家标注成本、最终统计功效和实际搜索成本均未完成。调研确认的是研究路径和候选资源，不是执行结果。确认失败时收窄 admitted cohort，并在看结果前固定；不可悄悄替换失败 baseline。

