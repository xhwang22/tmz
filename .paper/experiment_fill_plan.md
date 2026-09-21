# IterEval 实验填充总计划

2026-09-21。状态：写作与实验设计完成，数值未测；不表示已经运行 baseline、人工标注或训练。

本文件取代旧计划里“每个 domain 必须有 OOD test”和旧模拟图的实验分工。实现仓库未改。论文 C1/C2/C3 study ID 与 claims.yml 的 claim ID 不同。

最新执行补充：按用户要求，baseline 范围扩大为主计划中的全部 22 域。具体数量、方法、预算、数据入口与缺口见[22 域执行书](baseline_execution.md)和[逐域数据清单](baseline_domain_data.md)。这是执行计划变更，不表示其余域已经有结果；现有四域理想图仍是占位，未在此修改。

## 0. 当前占位稿与唯一替换入口

正文 9 页，附录/声明/参考文献另计。Abstract、Introduction、Fig1 和 Fig2 未改。
Fig3 已恢复原环形 taxonomy、四家族配色、湖绿色及 5.4 × 3.57 inch 紧凑布局，不再是空槽位。

- **唯一占位数值源**：`data/ideal_scenario/scenario.json`。这是理想情景的 aggregate assignments，不含实际 votes、rollouts、独立 runs 或统计推断。
- **统一生成**：`make ideal` 生成主表、数值附录表、Fig3/Fig4/Fig.A2，以及 `numbers.tex` 正文宏；`make` 编译。修改源数据后普通 `make` 也会更新已登记的生成物。
- **一致性检查**：`make check` 核对来源哈希、均值、差值、计数分母、偏好率、跨图表终点和正文数字。不能把检查通过解释为实验证实。
- **呈现约定**：图内没有模拟横幅；图注、首页和 PDF metadata 保留真实来源说明。后续不用为移除横幅重新调整图的布局。
- **真实替换**：原始记录另存版本化目录，保留此情景作为 archive；从真实 `summary_estimates.csv` 接入同一图表布局，更新 manifest/数据读取器并重新审核所有结果句。不要给此 JSON 改标签冒充实测，也不要把占位值复制到真实 CSV。
- **提交门禁**：`python3 scripts/check_ideal_scenario.py --submission` 在当前稿件必须失败。真实证据就绪后才能更新门禁和来源说明。

逐项完成顺序仍见第 8 节。轨迹、执行许可、独立指标、统计区间等不能靠 aggregate 情景填充，继续保留待填。

## 1. 主线和范围

- C1：域内学习 evaluator，在独立、未见原始输入上测 agreement 和 selection。
- C2：冻结 evaluator 改写新输出，重新盲评；不能沿用旧 output 的偏好。
- C3：冻结 evaluator 作 reward，训练 generator 后重新盲评。是条件实验，仍需独立训练授权。
- 核心机制：同样成本下，持续方向是否比“有历史但没有方向优先”的搜索更有用。
- 支撑机制：降低重复一致比较的采样优先级是否改善最终 evaluator，不是证明“分歧必然有价值”。
- 跨任务指分别适配多个标准，不是单 evaluator 的 universal transfer。
- 不要求 OOD，但保留独立 held-out、source-group 去重、防泄漏。可选分布变化必须保持评价标准。

SV4 网页规格生成、IG1 详细 caption、TG1 摘要、AR1 研究创意可以先启动，但全部 22 个 domain 都进入 baseline 执行任务。数据、许可或人工标签不足的域保留补齐任务/阻塞，不能静默删去或按结果选择入组。目标数量不等于已经具备数据或完成实验。

## 2. Baseline 与归因

| 主表行 | 保留的机制 / 改动面 | 待完成 |
|---|---|---|
| Fixed model judge | 同 backbone，固定 prompt，无额外工具 | prompt、尺度、token cap |
| Seed evaluator | 完整未进化的 tool-using evaluator | 冻结六组件、依赖与资源 |
| Learned signal fusion | 固定多信号上的正则 pairwise logistic ranker | features、训练归一化、missing policy、超参 |
| SkillOpt | 官方 skill/text 编辑，reject buffer 与已选定 meta update | Pin 版本；不能用自改程序进化 fork 代表原生方法 |
| GEPA (program adaptation) | 官方 engine + 完整 program，原生 population/reflective search | adapter、授权 traces；不能降成 prompt-only |
| Meta-Harness | 官方 harness-code 搜索，全历史代码/分数/traces | 匹配 proposer transport，不改搜索决策 |
| IterEval | 原生 direction、diagnostics、parent rule | 冻结实现、预算与开发选择 |

代码存在≠本项目跑通≠已复现。来源与出版字段见 [调研审计](experiment_literature_audit.md)。

四个内部搜索条件，不是已发表 baseline 的替身：

1. Full IterEval。
2. Active direction + best-parent：保留方向与诊断，拒绝后从 best 再改。
3. History-only + best-parent：保留历史，每轮从 best 提新方向。
4. No-history + best-parent：进一步去掉此前失败历史。

1−2 检验 intermediate parent；2−3 在相同 parent policy 下检验方向优先；3−4 检验 history。1−3 是合并效果，不能宣称只改变一个机制。

另需 SkillOpt vs text-only IterEval，完全相同文本字段、证据和编辑约束。Full IterEval 与 SkillOpt 的差距不能单独证明 optimizer 更好。

## 3. 正文展示分工

| 编号 / 稳定 label | 问题 | 必需数据 / 状态 |
|---|---|---|
| Fig. 1 / fig:teaser | 为什么值得深入 | 现有构造案例保留；不填经验数字 |
| Fig. 2 / fig:overview | 方法是什么 | 现有配色布局保留；不重画 |
| Table 1 / tab:main-alignment | 最终比谁好多少 | 7方法×独立 runs；Pair、BoN、Reg、coverage、eligible-domain counts；待填 |
| Fig. 3 / fig:c1-landscape | 哪里好，部署代价如何 | 原环形版式已恢复，理想数值已填；待替换真实 deploy cost 与 paired Δ |
| Fig. 4 / fig:budget-tests | 深搜如何有用 | 外部优化器发展曲线；内部消融的 post-search held-out checkpoints；direction outcomes |
| Table 2 / tab:downstream-results | 下游输出是否改善 | C2 fresh blind votes/regressions；C3 条件行 |

Table 1 是 absolute final leaderboard；Fig. 3 重用其底层记录，但展示 paired heterogeneity 和部署成本，不再画全部方法的绝对分数。它们不是两份独立证据。Fig. 4 是搜索预算维度，不能用 cost-quality scatter 替代。

Fig. 3 已沿用原 landscape 的四家族色、湖绿色方法色与紧凑 composite 质感。原 landscape_outcomes.pdf 和两个 landscape 数据版本均未删除或修改；旧 synthetic OOD 数据不能改名冒充本次实测。当前只为四个优先域赋值，其余 18 个任务以横杠明确不在情景内。

## 4. 全部附录图表

| 编号 | 稳定 label | 填充内容 / 完成条件 |
|---|---|---|
| Table A1 | tab:domains | 22 候选定义；不是实验完成数 |
| Table A2 | tab:data-sources | exact version、资产/偏好角色、权限；目前是经来源核对的候选 |
| Table A3 | tab:readiness | 标准、source groups、splits、H0–H3、N、adapter、许可 |
| Table A4 | tab:human-provenance | 实际 source 的 direct/derived/new 路线与预算单位 |
| Table A5 | tab:annotation-results | votes、rater count、agreement denominator、abstention、minutes、consensus |
| Table A6 | tab:access | 规则已写；补 split hashes、访问日志和防泄漏审核 |
| Table A7 | tab:adaptation | 合约已写；补 official commit、wrapper diff、smoke checks |
| Table A8 | tab:cost-results | mining/search/deployment 分账；tokens、calls、latency、failures |
| Fig. A1 | fig:runtime | 六组件概念图保留，不填模拟结果 |
| Table A9 | tab:domain-results | 每域/route/N 全部7方法，Top、H1、coverage、missing bounds、runs |
| Table A10 | tab:full-ablations | 合约已写；补条件实现标志、适用域和预算 |
| Table A11 | tab:search-results | 四控制和 text-only；paired effects、runs、attempts、cost、end reasons |
| Fig. A2 | fig:acquisition | 复用标签 budget / 新标 person-minute / 四格 interaction |
| Table A12 | tab:mining-results | 核心2×2与补充 uncertainty/cross-model/instability；每 budget 一组 |
| Table A13 | tab:component-results | 兼容组件干预，H0→H1→H2/H3，label adapter fidelity |
| Fig. A3 | fig:trajectory | 固定规则抽真实轨迹；成功若不存在则不编，保留失败/耗尽 |
| Table A14 | tab:downstream-detail | C2 no-critic/Seed/IterEval/y0；C3 Base/两 reward；W/T/L、validity、regressions |
| Table A15 | tab:external-endpoints | 独立指标版本、protected attributes；无适用 metric 记 N/A |
| Table A16 | tab:training | 条件 C3 preflight、配置、reward hash、checkpoint、quality/safety |
| Table A17 | tab:optional-results | AFlow、fine-tuning、OOD、N sweep、reopening、扩展 C3 |
| Table A18 | tab:reporting | 全部 display 导航、状态、输入 |
| Table A19 | tab:manifest | run manifest、统计方案、证据来源、发布许可 |

定义/合约表无需强填数值；实测表必须追溯真实源记录。A9 的 domain block 要为每个入组 domain 实例化，不能只填一个代表例。

## 5. 填表前冻结

完成 [run manifest 模板](../data/experiment_templates/run_manifest.template.json)，不能把 null 当默认值：

- quality standard、允许证据、原始 input/source 分组及近重复阈值；
- source/license、proposal/sealed Train、terminal Val、final Test；
- endpoint 的固定 domain set、selection 的统一 N；
- baseline commits、原生变体、同 backbone/proposer、seed、部署 cap；
- mining signals、dependence groups、anchor、H detail、每组 pair 标签数；
- search cost cap、计价日期、tools、checkpoints、独立搜索数；
- primary contrasts、最小有意义效应、cluster units、bootstrap、multiplicity；
- C2 no-critic 与新标流程；C3 preflight 与独立授权。

当前建议 5 independent searches、R≥3 scoring repeats、20/50/100/200 group budgets、25/50/75/100% cost checkpoints，都是待发展数据可行性核对的设计值，不是已执行事实。不能把 test 选成“只有高分歧”的子集。

## 6. 原始记录到图表

[CSV 空表头](../data/experiment_templates/README.md) 没有预填数据。

| 文件 | 最小单位 | 供给 |
|---|---|---|
| input_groups.csv | source-group / 原始 input | readiness、splits、cluster inference |
| human_judgments.csv | annotator × exact output pair | H0/H1、rater audit、C2/C3、time |
| human_rankings.csv | 排序组里的 output × annotator | BoN、regret、top-region；不从 pair-only 伪造 |
| artifact_scores.csv | evaluator × output × repeat | C1、coverage、missing bounds |
| search_events.csv | action / candidate / measurement | cost checkpoints、direction、parent、失败 |
| costs.csv | 实际 model/tool call | budget matching、部署成本 |
| downstream_outputs.csv | input × arm × output | C2/C3 lineage 与盲评 join |
| summary_estimates.csv | 明确定义的 estimand/contrast | 图表最终数字，必须关联 raw records/analysis hash |

同一 output hash 固定复用分数；同 source 派生输出不能跨 split；不同 N/route/run 不得悄悄并成更多独立样本。

## 7. 统计和措辞

主表取独立 search 平均，不挑最好 seed。固定 evaluator 的 paired input bootstrap 与 optimizer-run variation 分开；联合区间保留两层。直接估计 paired difference，不用两根 error bar 是否重叠判断。

Pair 主比较使用固定共同完整 cohort，并报请求分母 coverage/missing bounds。选择失败主分析按 BoN=0、Reg=1，另报 complete-case sensitivity。人类不可判断是另一类缺失。

真实结果按四句填：endpoint/比较对象 → effect/interval/n_groups/n_runs → 域差异/成本/失败 → 证据允许的结论。当前按作者要求预写理想情景的条件解释；替换时必须依据真实效果重写，不能保留必胜结论。

Agreement 好而 BoN 不变、history-only 持平、human-time 优势消失、C3 reward 好而人评不好，正文/附录均已有解释边界。作者编辑的 Abstract/Introduction 含结果式句子，真实数据到位前仍为 claim gaps，不因这次重写自动获得支持。

## 8. 执行顺序

1. 冻结优先域可用子集与许可，完成 A2/A3/A5/A6。
2. 验证7种接口、计费和小规模评分，完成 A7/manifest，再考虑大规模运行。
3. 固定 H，独立搜索→locked C1，填 A8/A9→Table 1→Fig. 3。
4. 四搜索控制，填 A11→Fig. 4，并导出真实 trajectory。
5. random/mined、核心2×2、label/time curves，填 A12→Fig. A2。
6. 兼容组件、反馈细节、转换分析，填 A13；无法运行的干预明记原因。
7. C2 新输出与盲评，填 A14/A15→Table 2。
8. 单独决定 C3 授权；未完成就保留 design-only，不写训练收益。
9. 按真实结果改 Abs/Intro/Results/Discussion/Conclusion，再全篇 claim audit。

本次没有运行实验或训练，也没有提交、推送 GitHub。
