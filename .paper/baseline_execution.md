# IterEval：22 域 baseline 实验执行书

日期：2026-09-21。状态：**待执行的冻结方案，不是实验结果，也不表示数据已经齐备。**

## 0. 可以直接交给执行 agent 的任务

> 请按本文件和[逐域数据与基础指标清单](baseline_domain_data.md)执行 IterEval baseline 实验。范围是 P2E plan §2.4 的全部 22 个域（SV1–SV6、IG1–IG6、TG1–TG5、AR1–AR5），不是只做原来的四个优先域。先逐域核验数据、标签来源、独立划分、许可、rubric 与可运行指标，再适配 baseline，最后运行、统计和导出。每域目标是 200 proposal + 100 checking + 100 validation + 200 independent test 个 source groups；核心优化器跑 5 个 seed。具体模型、预算、重复次数及缺失处理见下文。必须交付 22 行 readiness 和完整 method × domain × seed 状态表。数据缺失的域要补数据/标签或明确报告外部阻塞，不得默默省略、用代理标签冒充人类偏好，或根据收益决定是否保留某域。不得读 Test 来调方法，不得修改 Abstract/Introduction/图，不得启动 C3 参数训练，不得自动推送原始数据或 GitHub。付费资源和新增人工标注须在已有授权内执行；没有授权时，先完成所有可做的准备并列出所需资源。

本文件中的数量是**默认执行目标**。执行前写入 manifest 并核验；若容量、许可或预算无法满足，不可自行把小样本 pilot 改名正式实验。

## 1. 必读文档与冲突优先级

项目路径：论文 `/home/azureuser/muzhao/tmz`；实现 `/home/azureuser/muzhao/Auto-Evolve-Harness-for-Slide-Evaluation`；历史数据 `/home/azureuser/muzhao/auto_eval_harness`。

1. [P2E 主计划](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_plan.md)：§2.4 定义全部域；§3 定义反馈与 mining；§5.0 定义接入交付物，§5.1 区分 C1/C2/C3。
2. [新版逐域知识与数据审计](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md)：**数据语义主入口**。每域包含任务边界、维度、现成 scorer、数据与 H 缺口；本执行书的配套清单逐域深链到这里。
3. [逐 TD 数据收集方案](../../auto_eval_harness/docs/plans/p2e_v2_td_data_collection.md)、[数据源审计](../../auto_eval_harness/docs/plans/p2e_v2_data_source_audit.md)、[下载清单](../../auto_eval_harness/docs/plans/p2e_hard_domain_download.md)：找本地文件、恢复 assets、核对 source keys，不沿用旧的四域优先/替补限制。
4. [人工偏好协议](../../auto_eval_harness/docs/plans/metric_informed_human_preference_protocol.md)：H0/H1/H2、随机参照与盲化；人工标注任务包仍需按当前 domain contract 冻结。
5. 实现仓库 [AGENTS.md](../../Auto-Evolve-Harness-for-Slide-Evaluation/AGENTS.md)、[ERA 主搜索协议](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/era_main_search.md)、[算法说明](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/era_algorithm.md)、[SkillOpt 接口](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/skillopt_comparison.md)。
6. [论文实验总计划](experiment_fill_plan.md)、[baseline 文献与出版字段审计](experiment_literature_audit.md)、[真实记录模板](../data/experiment_templates/README.md)。

**覆盖关系：** 最新用户要求覆盖旧文档的“只做四域/其他域仅 panorama”和“每域必须 OOD”；本轮是全部 22 域、域内独立 held-out，不要求 OOD。其他任务边界、真实 H、许可和独立验收约束继续有效。新版数据审计优先于旧库存说明，例如 SurveyReview 评价的是综述论文，不是审稿意见质量；不能拿它补 AR5 的 H。方法实现必须冻结，发现论文与 runtime 不一致时另写 discrepancy，不在运行中偷偷改变算法或替作者改稿。

## 2. 数据规模、抽样单位与访问边界

### 2.1 每域采用同一规模目标

| 对象 | 每域目标 | 用途 / 访问 |
|---|---:|---|
| Train 候选输入池 | 1,000 source groups | 先运行冻结信号，待筛选部分的 H 对 miner 隐藏；不是要求给 1,000 组全补人评 |
| Proposal | 200 groups | 从上述池选出；可见输入、候选、H0/H1、已有人类 H2/H3；允许详细诊断 |
| Checking | 100 groups | 与 Train 池隔离；固定开发选择集，反馈权限由统一 adapter 控制 |
| Validation | 100 groups | 与前两者隔离；只作搜索结束后的冻结选择，不向 optimizer 反馈详细案例 |
| Test | 200 groups | 域内同标准、独立 source；所有程序和选择规则冻结后才作最终评测 |
| Smoke / annotation pilot | Proposal 的随机 anchor 内取 20 groups | 只作接口/标注可行性验证，不碰 Test，不额外制造一个泄漏 split |
| 完整 N-way 子集 | 上述 Test 中预先随机选 100 groups，N=4 | 必须有同输入 4 个完整候选及匹配的人类完整排序（允许并列） |

每域因此需要 **600 个入组且有标签的 source groups**；含未选 Train 池共需 **1,400 个独立 source groups**。22 域合计目标 **13,200 个入组 groups / 30,800 个含池 groups**，不是现有数量。完整 N-way 目标共 2,200 groups，包含在 Test 中，不另增加 source 数。

- 主配对实验每 group 先盲定一个 canonical pair。候选不足、渲染失败、缺标签均分别计数。保留额外 pairs，但只能作另报的 group-weighted 分析，不能把一个 source 的十对作品当十个独立样本。
- 同网页/文档/图像/论文/表格及其近重复、版本、裁剪、派生候选必须同组；AR 域按源论文和相关 context 聚类，翻译按源文档而非句子数膨胀样本量。跨域共享源也登记，macro CI 不默认跨域来源独立。
- 1,000 组不是“抓够 1,000 行”。先语义与 hash 去重再计数；小数据域按配套清单补**同一任务标准**的 inputs 与 candidates。无法补足时保留 blocked，不用 bootstrap 复制行填规模。
- 首先锁定 checking/validation/test，再做 Train mining。Test 从目标域自然候选分布随机抽取，不能只挑分歧大的 hard cases。所有方法使用相同 splits、候选、标签和输入视图。
- 固定 data seed `20260921`；优化 seed `[11,23,37,53,71]`。五个优化 seed 不改变数据分组，不等于五份独立 Test。

### 2.2 Mining 的两条数据路线

已有 H：保留标签的来源与原始键，但先隐藏待筛选池标签，冻结选择后才揭示；报告“使用的有标签 groups / pairs”，不把复用数写成新增标注成本。

没有 H：先选候选，再新增匹配的人类 H；单列人数、judgments、person-minutes 与费用。模型生成的诊断只能作标记清楚的辅助材料，不能填入 human 字段。

200 proposal 的默认组成是 **40 随机 anchor + 160 mining groups**。anchor 从 Train 池预先独立抽出；若用其标签校准信号，待筛选池不能包含 anchor。与随机采样对照共享这 40 组，另外随机取 160 组。规模曲线用 `[20,50,100,200]`，anchor 分别 `[4,10,20,40]`，预先冻结可复用的嵌套采样顺序。

不要把“跨维度取舍”和“同维 scorer 冲突”混为一类；多个同源 checkpoint 不按多份独立证据加票。必须输出 dimension × source 映射和采样理由。miner 从旧 labels 直接按错误选样是另一个 supervised 采样方法，不能命名 label-blind disagreement mining。

### 2.3 标签与污染门禁

- Proposal：H0 + 核心 H1 全覆盖目标；至少 50/200 groups 带可定位 H2（40 随机 anchor + 10 个按预定规则选的冲突案例）。Checking/Validation 至少 H0 与核心 H1；Test 收 H0 与预注册核心 H1。缺 H1/H2 的先记录为 H0-only pilot，不称完成原计划全部监督要求。
- 新标开发样本默认两名独立标注者，冲突交第三人；新标最终 Test 默认三名独立标注者。专家域需要学科匹配的人类专家；保留原始分歧、tie、abstain、insufficient，不能用模型裁决当第三人。
- 已有人工偏好可以依原协议复用，不为统一“三人”虚构额外 votes；报告原始人数/聚合方式。H1 的 pointwise 分数不直接等同 H0；必须区分 direct / derived / newly annotated。主 overall 人类偏好行优先 direct/new H0，derived 结果分开报告，不混成同一构念。
- 对新输出重新标注；旧作品的 label 不继承给修改后的作品。任意补标或新候选生成均先核对资源与许可，不擅自联系标注者或购买服务。
- 既有研究中看过的 Val/Test、历史反馈/反思文本及其近重复都进入 exposure ledger。**不能把旧 Val 改名 Test。** Design2Code 已暴露的 20-page Test、旧 IG1 Val、既有 SV4 比较只能按其实际历史用途处理。
- 预训练/奖励模型训练重叠另列风险，尤其 PickScore/ImageReward/HPS 与其数据、COMET 与 WMT。没有足够无污染 source 时，不声称完成干净 confirmatory test。
- Test 的 human tie/不可判不进入 strict-preference 分母，但保留计数及单独 tie 端点；不得看到模型输赢后换 pair、补样或排除。入组 200 不保证 strict-H0 有效数恰为 200。

## 3. 必跑 baseline：不要把 scorer 和 optimizer 混在一起

### 3.1 全 22 域的静态评分底座

| ID | 条件 | 固定定义 |
|---|---|---|
| S0 | Generic judge | 同 backbone、pointwise、单个 overall 0–100 分；只给任务/输入/作品，不提供专门 rubric 和外部工具 |
| S1 | **Fixed rubric judge（主表 fixed model judge）** | 每域预先冻结 rubric；各维 1–5 分、简短证据定位；等权平均后以 `25 × (mean − 1)` 映射到 0–100，不学习权重 |
| S2 | Input-specific rubric judge | 只用任务输入（不得看候选/H）生成每输入 4–8 条标准，缓存后同组共享；同 S1 等权计分。这是自定义强静态对照，不冒称复现某篇 query-specific 方法 |
| S3 | Native metrics / specialized judges | 配套清单的逐域指标，每个单独报；不能只运行一个 generic judge 代表领域 ecosystem |
| S4 | Fixed signal ensemble | 冻结非冗余的 S1/S3 scalar features；只用 Proposal 拟合经验分位数变换、统一高分方向，再等权合成；不根据 Test 选信号 |
| S5 | Learned signal fusion（主表） | 与 S4 完全相同 features，用 H0 训练 L2 pairwise logistic ranker；部署时仍独立输出每件作品的线性 score |
| S6 | Seed evaluator（主表） | 本域完整但未进化的 tool-using evaluation program；冻结 rubric、工具、routing、fusion、adapter 与依赖 |

S1 提示词统一骨架：`仅根据给定任务、输入与作品，按以下冻结标准逐项评价；每项返回 score(1–5)、evidence、uncertainty；1=严重不满足，3=基本满足但有明显缺陷，5=充分满足。不得推测生成器或隐藏偏好。` 每域的 2/4 分锚点和维度释义也写入 rubric 文件。采用 domain contract 预定的必需维度；缺必需证据返回 invalid/insufficient，不临时删除维度或让模型改权重。

S5 默认正则候选 `C=[0.01,0.1,1,10]`，只用 Checking 选择，平分取更强正则；只在 Proposal 拟合 scaler/缺失值填充（feature 中位数 + missing indicator）。pair 特征为两个 pointwise feature vectors 的差，交换增强不增加有效样本量。Test 上禁止重训、重标定或选择最佳单指标。

**观测公平性：** S0/S1/S2 无工具，S6 和全程序优化器有相同可用工具，这是系统对照，不是只变 optimizer 的消融。候选原始输入/图像/源文档必须一致；超长 deck/document 的固定视图或截断协议须记录，不能只给某个 baseline 少看材料。

每域 registry 标注 `search_tool / static_baseline / external_reserve`。已供进化调用的 metric 可作 static baseline，但不是独立验收证据；External Metric Reserve 的实现、分数与 traces 不得暴露给 optimizer。保留区不应靠复制同一 scorer 名字伪造独立性。

### 3.2 全 22 域的核心优化器

| ID / 主表行 | 必须保留的机制 | 适配与可用状态 |
|---|---|---|
| O1 SkillOpt | 官方 ReflACTTrainer、reject/history 与所选 slow/meta update；仅修改固定 fusion 文本 | 已有桥接。用 `prompt_surface: fusion`、`selection_role: train_internal`；不得用历史 program-edit fork 冒充官方算法 |
| O2 GEPA (program adaptation) | 官方 reflective/population/Pareto 搜索及所选原生 merge 设置；完整 evaluation program 的适配 | **尚需完成并验证项目桥接**；不能拿 history-only 内部控制替代 |
| O3 Meta-Harness | 官方 harness-code 搜索、可读的历史程序/分数/traces；完整程序适配 | **尚需完成并验证项目桥接**及相同模型 transport；不可偷换为每轮 incumbent 独立重启 |
| O4 IterEval | 当前冻结的方向状态、working program、diagnostics、checking-best 和方向内更新 | 已有运行入口；冻结 runtime flags，不能混用不同历史 ERA 模式 |

主表共 **S1/S5/S6/O1/O2/O3/O4 七行**。每个 O 条件每域 5 seeds，即 **22 × 4 × 5 = 440 次主搜索**；这是计划规模，不是已经获准无限付费。S0/S2/S3/S4 放完整附表。AFlow、ADAS、DGM、额外 judge 权重训练不是本轮主 baseline 必跑项，不能为了凑数量挤掉这四个优化器。

### 3.3 必需的同空间与机制对照

全域另跑三个内部控制 + 一个 text-only IterEval，各 5 seeds：共 **440 次附加搜索**；与主搜索合计 **880 次**。Full IterEval 与 SkillOpt 直接复用 O4/O1，不重复跑。

1. Active direction + best-parent：只改变继续方向时的 parent，拒绝后从 best 修订。
2. History-only + best-parent：同 parent policy、保留历史，不保持方向优先。
3. No-history + best-parent：再移除失败历史。
4. Text-only IterEval：与 O1 完全相同 fusion 字段、可见证据、工具与编辑约束。

Full−1 是 working-parent 效果；1−2 是相同 parent 下的方向优先效果；2−3 是历史效果。不要把 Full−2 写成单因素消融。编写 adapter tests 保证只改规定开关；当前没有对应可验证开关时先实现，不用不同 legacy mode 名字近似替代。

Mining 曲线/2×2 interaction、组件消融、H 粒度、C2/C3 是[总计划](experiment_fill_plan.md)中的独立任务，不包含在上述 880 次 baseline/机制搜索中。不能把 baseline 跑完说成整篇所有实验完成；本文件优先交付全 22 域的 C1 和公平 baseline。

## 4. 模型、预算与冻结设置

以下为新 run 默认值，不迁移旧 run。模型服务若不支持则报告，不静默 fallback。

| 设置 | 默认值 / 约束 |
|---|---|
| 通用生成模型 | `gpt-5.6-sol`，评分、反思/修改均固定此 model ID；记录服务返回的实际版本及 endpoint 别名，不写凭证 |
| 专用指标模型 | 可用其官方冻结 checkpoint（如 PickScore/COMET）；不得宣称与通用模型同 backbone |
| 评分重复 | 普通搜索测量 1 次；官方算法要求的内部多次观察保留并计费；最终评分每 artifact 独立 3 次，pointwise median 后成对比较 |
| 决策规则 | 正向分越大越好；不按 Test 调 tie threshold。严格 H0 下预测相等计为未正确排序；另报 tie 与 coverage |
| 单次输出 allowance | 简单 rubric/generic judge 4,096 tokens；optimizer/复杂完整 runtime 16,384 tokens。同任务同角色各方法一致，具体 role 映射写 manifest |
| 每搜索通用硬上限 | `budget.max_calls=20000`，`budget.max_completion_tokens=128000000`；任一先耗尽即停，不自动追加 |
| IterEval 本地日程 | 30 个 measured rounds；direction 最多 6 步、checkpoint interval 3；screen 32 / full checking 100；其他设置取冻结模板 |
| 并发 | 实现推荐的单实验 `workers=128` 仅是本地上限，不是允许所有域各开 128。调度器先限定同时 1 个重型 run；获资源许可后提高总并发 |
| 重试 | 仅冻结的传输错误重试，同样计费；不得因内容差/分数低重试至满意 |
| 最终选择 | 搜索后只比较 checking-best 与 seed；Validation 100 groups ×3 repeats，预定同一规则择优，平分保留 seed；其他 terminal 候选不得临时加入 |

当前实现 `max_completion_tokens` 计的是**请求 output allowance 的累计值**，不是实际生成 tokens；必须另记实际 input/output/cached/reasoning usage。20,000 calls 与 128M allowance 是资源天花板，不是预计花费，也不等于美元预算。预算表同时给出准确单价来源/日期或留金额 unavailable，不从 token 上限编美元。

每条轨迹记录总 calls、实际 tokens、GPU seconds、latency、失败、原始候选尝试和 measured rounds。搜索包括提案、诊断、工具内模型调用、筛查、完整测量、原生反思与重试。共享静态缓存需报告一次建设成本与每方法所用访问成本，不能只对 IterEval 免费。

30 IterEval rounds 不等于 30 SkillOpt/GEPA/Meta-Harness steps。外部方法按其原生步定义运行到冻结日程或通用预算上限；不同方法未用完预算也不填满虚拟成本。结论写“相同资源上限”并给 actual-cost 曲线；如果要声称等实际成本，使用预定成本 checkpoints 的共同覆盖区间，不插值出未测候选、不把提前停止当完成最大预算。

20 组 smoke 只用于确认接口、输出 allowance 与资源估算。在任何主实验开始前生成 `budget_projection`（22 域 × 方法的预计成本区间）并确认总授权。投影须分别包括资产生成/渲染、mining、人工标注、静态评分、搜索、Validation 与 Test；每搜索硬上限不替代最终评测阶段或全项目的总费用授权。需要调整上述上限时，统一更新协议版本后再开始全部比较，不见到某方法收益不足才扩预算。

### 4.1 当前实现必须显式记录的设置

以 [v2 示例](../../Auto-Evolve-Harness-for-Slide-Evaluation/configs/team_search_era_v2.example.json) 为源，逐项写入每域运行配置：`train_examples`、`case_guided_v3`、`era_search_v2`、`mechanism_transaction_v1`、`patch_revision_v1`、`mechanism_first_v1`、`tool_session_v1`、`edit_guidance_v1`、`evidence_direction_v2`、`coverage_checking_v1` 和 `exclude_unexecuted_failures_v1`。默认未测构建失败不耗 measured round，但仍耗 API 预算；连续失败恢复上限保留。只有 full checking 能提升 best，screen 不能终结方向。

这不是要求外部方法模仿 IterEval 的筛查策略：它们共享候选执行接口、数据权限和总预算，保留原生搜索决策。Validation/Test 不得变成其中任何方法的每步 selection data。

SkillOpt 默认 pin `79124b37e9a6371e13b753f8bcd7adb1e493ade1`，使用 clean upstream；本地候选路径 `/home/azureuser/muzhao/SkillOpt-upstream-79124b3`。默认 native recipe：`num_epochs=3, batch_size=100, minibatch_size=2, edit_budget=4, merge_batch_size=8, analyst_workers=8, use_slow_update=true, use_meta_skill=true, slow_update_samples=4`；各 seed 独立。不得用历史 slow/meta 关闭的结果充当这一 variant。GEPA/Meta-Harness 的 upstream commit/API/原生 schedule/adapter diff 在 smoke 前补齐；尚未 pin 就保持 pending。

## 5. 执行顺序与真实可用入口

### Phase A：只读盘点与冻结

- 读必读文档；记录各 repo commit **及 dirty patch/hash**。当前工作树含其他会话改动，不能 `reset`、清空或盲目提交。使用隔离的冻结运行快照，不把当前 HEAD 等同完整代码版本。
- 创建 22 个域的 contract/data/rubric/scorer/split manifest，列实际 source groups 和与目标差额。下载前核对许可；历史库存数量只作线索。
- 同一 domain 的所有主方法先就绪再开始该域正式比较；可跨域按资源排序准备，不因人评贵或 headroom 小撤销域。

### Phase B：接口与防泄漏 smoke

对每域的 20 个随机 Train groups 跑全部静态 scorer；验证完整输入、score 方向、解析失败和缺失记录。用 1–2 个 group 验证每优化器能提出、执行、选择/拒绝候选并恢复运行。smoke 结果不是正式效果，不带入其他 seed 的优化历史。

必须测试：更换隐藏 H/生成器名字不改变推理输入；pointwise score 不读取 opponent；无效/超时不变成 0 分“正确”；Test 读路径被 optimizer 拒绝；resume 不改配置、不重复计费；缓存键含 program/artifact/model/render/repeat hashes。

### Phase C：静态与主搜索

完成 label-blind mining 和 label 接入后，冻结 S0–S6。按 seed 交错运行 O1–O4，再跑内部控制；避免把不同 endpoint 时期完全绑定不同方法。每个 run 独立目录，不导入其他方法的进化记忆。

以下是**现有入口示意**，`/absolute/path/...` 必须替换成已冻结的私有配置；不是本轮已经创建好的 runnable config：

```bash
cd /home/azureuser/muzhao/Auto-Evolve-Harness-for-Slide-Evaluation
.venv/bin/python scripts/p2e.py check --config /absolute/path/itereval.json
.venv/bin/python scripts/p2e.py search --config /absolute/path/itereval.json
.venv/bin/python scripts/p2e.py search --config /absolute/path/itereval.json --resume
.venv/bin/python scripts/p2e.py confirm --config /absolute/path/itereval.json
.venv/bin/python scripts/p2e.py skillopt-check --config /absolute/path/skillopt.json
.venv/bin/python scripts/p2e.py skillopt-smoke --config /absolute/path/skillopt.json
.venv/bin/python scripts/p2e.py skillopt-search --config /absolute/path/skillopt.json
.venv/bin/python scripts/p2e.py skillopt-confirm --config /absolute/path/skillopt.json
```

**不得捏造 `gepa-run` / `meta-harness-run` CLI。** 先基于各官方 engine 实现统一 adapter，交付测试与完整 README/命令，再将其加入 runnable matrix。SkillOpt 的 `skillopt-run` 会在 development improved 时才自动 confirm；最终比较必须对所有 seed 的冻结输出（包括未改进、回退 seed）评测，不能依这个条件筛选成功 runs。

### Phase D：独立最终评测

当前 `frozen_comparison_v1` 的 train/val diagnostic 接口**不接受 Test/OOD**；不能给 Test 换标签绕过检查。必须另实现只加载冻结 evaluator 的 isolated final assessor，禁止修改程序或调用 optimizer。现有 `confirm` 只承担其声明的 confirmation，不替代独立 Test。

最终 assessor 对所有冻结输出运行 Test 的 3 次 pointwise scoring；同样对每个静态 baseline 测量。确定性指标只需计算一次并按明确缓存规则复用，不能声称获得三次独立观察。人类标签只交分析器。N=4 需兼容人类并列与 missing，不用当前只接受完整严格 ranking 的接口冒充已支持。失败不删样；保留完整 run、coverage 和原因。代码修复若影响已揭示 Test 的模型行为，该版本降为 exploratory；新 confirmatory 必须再锁独立 inputs/H。

### Phase E：统计与交付

- Strict-H0 agreement：以有可判 human strict preference 的全部 pairs 为分母；候选评分 invalid 或预测 tie 记未正确。另报 valid-only accuracy、pair coverage、human tie/abstain 比例。每 source 等权。
- N=4：按 median pointwise score 选择，模型平分用预定 artifact-hash 顺序；报告命中 human top set、normalized rank regret、完整有效组 coverage。人类并列采用共同最小名次，所选作品的 regret 为 `(human_rank − 1)/(N − 1)`。四个候选任何一个缺有效分数，该组在 failure-adjusted 指标中计 selection failure（top-set hit=0、regret=1），另报四个分数均有效时的 valid-only 结果；不得缩为 N=3。仅 pair labels 不可推导完整排名；pointwise ratings 派生的排序另列。
- 95% CI 用 10,000 次 source-group paired bootstrap，所有方法同一抽样；同时报告 5-seed 均值/SD。若给跨种子 CI，采用外层 seed 重采样、内层 source-group 重采样并保持方法配对，不能把 repeats/五个 seed 当独立 Test 扩样。
- 主摘要为 22 域等权 macro；四家族等权是另一 estimand，明确另报。未完成时只报 `completed / 22` 的 provisional 汇总和完整缺失名单，不称“22 域结果”。方法覆盖不一致时不各取自己的有利域比较。
- 200 个 Test groups 在独立 Bernoulli 近似、准确率 0.5 时单方法 95% 半宽约 7 个百分点；聚类/并列会降低有效样本数。此设计不保证检测 1–2 点增益；事后不得按 p 值扩样。
- 定义主对比、校正族后再看 Test。多 baseline 显著性使用 paired 检验并 Holm 校正；不靠“某 seed 显著”作结论。

## 6. 交付目录与完成标准

实际数据和运行放私有、版本化目录，建议 `/home/azureuser/muzhao/itereval_baselines_22d_20260921/`；本执行书不预创建空结果冒充完成。

```text
protocol.md / protocol_manifest.json / budget_projection.csv
domain_readiness.csv             # 固定 22 行，目标/实际/缺口/阻塞
run_matrix.csv                  # domain × method × seed，含未运行项
domains/TD-*/contract.json
domains/TD-*/data_manifest.json  # source/version/license/assets/H provenance
domains/TD-*/rubric.json
domains/TD-*/scorer_registry.json
domains/TD-*/splits/             # source-group keys + hashes；Test 权限隔离
domains/TD-*/configs/            # 每方法可执行配置，不含密钥
domains/TD-*/runs/               # 程序、日志、账单、traces、失败、resume 记录
analysis/                       # 固定分析脚本和结果表
reports/                        # 总报告、逐域报告、blocked 清单、命令手册
```

readiness 至少包含 `domain_id, contract_hash, data_doc, source_version, license, target_groups, available_groups, proposal_n, checking_n, validation_n, test_n, h0_route, h1_coverage, h2_coverage, n4_eligible, exposure_audit, adapter_status, scorer_status, blocker`。run matrix 至少包含 `domain, method, seed, protocol_hash, status, run_path, model_id, upstream_commit, actual_cost, terminal_program_hash, failure_reason`；status 区分 pending/blocked/running/completed/failed，不把 failed 标成未尝试。

沿用[真实记录模板](../data/experiment_templates/README.md)导出逐作品 scores、human judgments/rankings、costs、search events、summary estimates；必要时扩展 schema 并注明版本，不把空白模板或 ideal scenario 改造成“真实数据”。

论文回填映射：Table 1 = 七方法绝对最终 C1；Fig. 3 = **同一批结果**的逐域增益与部署成本，保留现有配色/饼图布局；Fig. 4 = 搜索轨迹与内部控制；附表 A2–A9 = 数据、H、权限、适配、成本及逐域结果；A10–A11 = 对照。C2/Table 2 与其他机制实验仍为独立后续任务，不能从 C1 数字推算。

**完成 baseline 任务需要：** 22 域全部列明；每个适用静态指标真实运行或有可核查阻塞；四个核心优化器与四个追加条件按冻结 seeds 运行；独立 Test 与必要 N-way 标签有效；完整成本、失败和 CI 可追溯。若缺人工 H、官方适配或资源授权，交付已完成工作及明确缺口，不能写“全部跑完”。所有效果方向由实测决定，理想图不是最低达标分数。
