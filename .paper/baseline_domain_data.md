# IterEval 全 22 域：数据文档与基础评分清单

2026-09-21；配合[baseline 执行书](baseline_execution.md)使用。所有域均是必做任务，不是四个主域加十八个可选域。下表是候选接入路线与待实现 scorer 清单，**不是数据/权重已下载、指标已跑通的声明**。

每域目标一律为 **200 proposal / 100 checking / 100 validation / 200 Test source groups**；Train 候选池目标 1,000 groups（proposal 包含其中），Test 的 N=4 完整排名子集目标 100 groups。按源输入而非 rows/pairs/pages 计数；小来源不足时补同标准输入和新候选/人评，不能靠多 pair 扩增独立组数。所有数量与数据访问规则见执行书 §2。

## 1. 执行 agent 应该读哪些数据文档

| 文档 | 用法 |
|---|---|
| [主计划 §2.4](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_plan.md#24-研究覆盖的-domain-全景) | 域的定义与 22 个稳定 TD-ID；不是按文件格式任意合并 |
| [新版领域与数据审计](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md) | **优先读**：每域 rubric、scorer、数据/H 表、适用边界、一级来源链接；下文每行直接链接到对应域 |
| [逐 TD 数据收集](../../auto_eval_harness/docs/plans/p2e_v2_td_data_collection.md) | 2026-09-04 的库存及恢复任务；查同 input 的候选和标签键 |
| [数据源审计](../../auto_eval_harness/docs/plans/p2e_v2_data_source_audit.md) | 下载入口、release/schema、许可及 per-TD 动作 |
| [下载记录](../../auto_eval_harness/docs/plans/p2e_hard_domain_download.md) | 已下载/部分下载目录与文件，不能由文档状态替代当前 hash 核验 |
| [近期 source evidence](../../auto_eval_harness/docs/plans/p2e_v2_recent_source_evidence.md) | 补充一级来源证据与历史核查 |
| [标注协议](../../auto_eval_harness/docs/plans/metric_informed_human_preference_protocol.md) | H0/H1/H2、随机参照和盲标；与新版审计中的 H 定义一起使用 |

旧文档的 Main/Alternate/Pilot/Boundary 是历史研究角色，**不再是删减本轮执行域的依据**。旧 OOD 方案不强制执行。数据语义有矛盾时以新版审计为准，再核官方 data card；不得仅凭旧表格把 SurveyReview、MQM 或某个 reward score 记为直接 H0。

## 2. Structured visual artifacts：6 域

所有视觉 judge 使用同一固定分辨率/缩放/页数协议；保留原始文本与必要输入。浏览器/PPTX/parser 在隔离环境处理不可信代码与文件，不给网络凭证或任意外网权限。

| 域 / 对应数据文档 | 数据入口、已有 H 与补齐动作 | S1 fixed rubric 维度 | S3 必跑基础指标/工具与边界 |
|---|---|---|---|
| **TD-SV1 brief→单页幻灯片** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv1) | BAMS 历史库存 250 briefs、3,038 candidate metadata（3,037 可渲染；800 曾抽样），先复核全量键；pointwise/SlideAudit 缺陷不是 direct H0。600 入组至少需再补 350 个独立 briefs，Train 池另补至目标；新标同 brief 多候选 H0/H1 | brief 内容覆盖、事实忠实、信息层级、可读性、布局/视觉一致性 | PPTX/渲染文本与几何检查（overflow、overlap）；OCR 文本覆盖；字号/contrast diagnostics；固定 VLM 内容/视觉 judge。几何合法不能直接当整体美观 |
| **TD-SV2 screenshot→网页重建** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv2) | Design2Code 484 pages；人工比较子集 100 pages/700 pairs；HARD 80 inputs 要去重后计。已暴露 20-page Test 只诊断。补足独立 screenshots/HTML，冻结 viewport/render，新增匹配 H0/H1；[接入说明](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/design2code_era.md) | 内容、位置/结构、颜色/样式、视觉细节、可读性与参考一致 | 官方 Design2Code Block-Match/Text/Position/Color scores；SSIM、CLIP 或 DINO screenshot similarity；render validity。功能符合 specification 不是本域主评价目标 |
| **TD-SV3 table+goal→可视化** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv3) | ChartQA/LIDA 数据只作 inputs；Chart-to-Experience 只小 anchor。固定 table+analysis goal+chart/spec 合同，补 600 同输入候选组 H0/H1；同一表换图不能跨 split | 数据正确、encoding 恰当、目标相关、可读性、洞察表达 | 可执行字段/聚合/轴/checker；render validity；固定 chart QA/VLM readability。SciVisAgentBench/VIS-Shepherd 作为代码/协议入口，适配后才计已运行；不能将图表 QA 直接当生成图整体 H0 |
| **TD-SV4 specification→网页** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv4) | WebDev Arena 10,501 battles；旧审计约 6,844 规范化请求、10,480 code-complete rows，须重新按请求/历史聚类。已有社区 H0；补核心 H1/interaction H2。WebGen/Cookie/LiveEval 补 input/checklist，不当新增人类标签；原始 Arena 数据有禁止再分发约束 | 需求满足、实际功能、可用性、视觉质量、稳健性 | WebGen 外观评分；Cookie 固定 functionality/aesthetics；冻结浏览器 interaction/checklist pass；axe-core accessibility。静态图上的“功能分”与真实执行分分别标记，LiveEval source/DOM 检查不是完整功能验收 |
| **TD-SV5 source→整套 slides** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv5) | PresentBench 官方 238 tasks；旧本地 104 instructions/104 prompts/103 stats，不代表完整 source。先恢复材料与许可，再补同标准来源、生成多 decks 并新标 H；不能拿单页数凑 600 | source 忠实、内容覆盖、跨页组织、视觉一致、可读性/可编辑性 | PresentBench checklist；SlidesGen Content/Aesthetics/Editability 适配；source claim coverage、跨页重复/矛盾、PPTX 结构与几何工具。references/checklists 不是 human H0 |
| **TD-SV6 topic→整套 slides** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-sv6) | Slides-Align 187 topic groups/1,326 ranking rows/9 products；先核 human provenance、产品名称到资产的键和许可。若合格仍需至少补 413 个 topic groups 至入组目标；不合格排名降为非独立 score 并重标 | topic 相关、内容正确、叙事组织、视觉一致、可读性 | 固定 deck-level topic/factuality/organization judge；跨页一致与版面工具。没有 source bundle 就不造“来源覆盖率”；SV5 不是 SV6 的同域数据 |

## 3. Image generation and understanding：6 域

CLIP/DINO 的 checkpoint、预处理、resize/crop、文本截断和聚合必须写 registry。相似度只代表相应信号；不得因为一个 learned metric 不可用而让 VLM 模拟它的分数。

| 域 / 对应数据文档 | 数据入口、已有 H 与补齐动作 | S1 fixed rubric 维度 | S3 必跑基础指标/工具与边界 |
|---|---|---|---|
| **TD-IG1 image→详细 caption** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig1) | CapArena manual：6,523 battles、3,627 image refs；bundle 5,100 images 不等于全部有 H0。LongCap-Arena 是逐维评价；DOCCI-Critique 是局部 factuality。恢复匹配键、按图像/近重复分组并排除历史 exposure；CapArena-Auto 不当人工 H | 事实准确、显著内容覆盖、细节、关系正确、简洁/组织 | 官方 CLIPScore；有适用人工 reference 才跑 RefCLIPScore/CIDEr/SPICE；固定原子 claim factuality 与 coverage judge。原 CLIPScore ViT-B/32 会截断长 caption，必须记录比例，不能声称全文测量 |
| **TD-IG2 text→image** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig2) | Pick-a-Pic/HPS/ImageReward/GenAI-Bench，按相同 prompt 分组、恢复实际图像与偏好；测试先查 reward training 重叠。[pilot 说明](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/text_to_image_pilot.md) 仅提供接入线索 | 提示词符合、组合/空间关系、视觉质量、细节、整体偏好相关美感 | CLIP similarity、PickScore、ImageReward、HPSv2；TIFA/DSG 分开计 QA 成本；GenEval 只在其可识别结构化 prompts 上跑，不编任意 prompt 的 GenEval 分 |
| **TD-IG3 source+instruction→编辑图** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig3) | EditReward-Compass 历史 2,251 rows（1,869 preference/382 tie），逐条核 winner 是整体还是某维；GenAI editing/GEditBench 等补输入。固定单 source 编辑，按 source image 聚类；缺 overall 就新标，不把 instruction-only 胜负当 H0 | 指令满足、非编辑内容保留、编辑区域质量、整体一致/自然 | EditReward 官方适配；GIE 指令 QA；有可信非编辑 mask 才用 masked DINO/LPIPS preservation。全图相似可能惩罚正确修改，必须与指令分开 |
| **TD-IG4 LR→超分** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig4) | RefSR-18K：历史 8,461 四候选组/rank labels，图片部分下载；恢复真实 LR/HR/outputs/rater 键，按原始图归组。PIPAL 只作相邻校准 | 结构忠实、细节/纹理、伪影、自然感、与 LR 一致 | PSNR/SSIM/LPIPS **仅有匹配真 HR 时**；RefReward-SR 若可用且污染审计通过；固定 LR+output VLM rubric。双线性上采样不是 HR 真值 |
| **TD-IG5 text→3D** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig5) | MATE-3D 多维 MOS/H1，T3Bench prompts；先核资产、许可与同 prompt 候选，再补整体 H0。维度均分不能伪装直接 overall 偏好 | 文本符合、几何/结构、纹理/材质、多视角一致、完整性 | T3Bench 多视角 quality/alignment；冻结 Blender 8 views（同 camera/light/background）；mesh validity；HyperScore checkpoint 可用后补。渲染设置是共同输入协议，不让每方法挑有利视角 |
| **TD-IG6 image→3D** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ig6) | 3D Arena 有资产线索，论文 vote 总数不是已拿到 payload；先找公开 vote–source–asset keys，拿不到就按 image-to-3D 合同新标。与 IG5 分开 | source 身份/形状、可见视角符合、几何合理、纹理、多视角一致 | 对齐 camera 后 source-view DINO/CLIP similarity；冻结 8-view VLM consistency；mesh diagnostics。不能拿文本 prompt alignment 代替输入图忠实度 |

## 4. Text generation：5 域

先冻结语言、任务标准、长度预算与输入可见性。参考文本只能在部署确实可得且各方法一致的 track 中使用；reference-based 辅助指标另报，不能悄悄成为无参考 evaluator 的额外工具。

| 域 / 对应数据文档 | 数据入口、已有 H 与补齐动作 | S1 fixed rubric 维度 | S3 必跑基础指标/工具与边界 |
|---|---|---|---|
| **TD-TG1 source→摘要** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-tg1) | `openai/summarize_from_feedback` direct H0；本轮先固定 TL;DR source-only 合同，不混 CNN/DM。SummEval 100 articles×16 summaries 提供 H1，不是 1,600 独立 source。新模型摘要需要新 H | 忠实、核心覆盖、相关、连贯、简洁 | 有匹配 reference 的 track：ROUGE-1/2/Lsum、BERTScore F1；source factuality：SummaCConv 或 AlignScore；固定事实/coverage judge。ROUGE 不衡量所有整体取舍 |
| **TD-TG2 RAG→长回答** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-tg2) | LFQA-E 1,618 questions/7,323 expert pairs 是候选；必须恢复 evidence bundle 且满足冻结 RAG contract，否则只相邻 LFQA。ExpertQA/ALCE 提供 inputs/corpus；RAGTruth 局部 H2 非 overall。需要时固定 retrieval snapshot 新生成/标 H | 回答正确、问题覆盖、证据支持、引用精确/完整、清晰 | ALCE citation precision/recall；claim–evidence NLI；问题覆盖/正确性 rubric。无 citation 条件不能伪造有 citation endpoint；各方法 retrieval 访问一致 |
| **TD-TG3 翻译** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-tg3) | WMT MQM/CD-ESA；默认先 en→de，同 source document 归组。MQM 是错误/质量标注；派生 pair 标 derived，不与 direct overall 混合。主 H0 不足时新标整体翻译质量；不能因 strong metric headroom 小就取消本域 | 准确、流畅、术语、遗漏/增译、文体 | SacreBLEU sentence BLEU + chrF（签名完整）；COMET 官方冻结 reference-based checkpoint；MQM-style fixed judge。只有句子数达标而文档不足时不算满足 group 目标 |
| **TD-TG4 指令约束回答** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-tg4) | IF-RewardBench 候选/graph 逐 edge 核 human provenance；IFEval 程序标签只作 checks。补同约束 prompts 的多候选 H0/H1；保留 control/boundary 角色但照样运行 | 明确约束满足、内容正确、有用、相关、表达 | IFEval strict/loose checks（仅支持的约束）；自定义 constraint checker 单列适配测试；固定 usefulness rubric。不能将完美格式通过率当整体 human alignment |
| **TD-TG5 开放对话回答** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-tg5) | 默认审计 HelpSteer2 的直接 preference 分支；不足时选单一兼容 HH-RLHF helpfulness setting 并在运行前冻结。不能混原五属性打分、另采 H0、harmlessness 与对话偏好；同 history 归组 | 有用、正确、上下文一致、相关、表达、安全 | 固定多维 dialogue judge；history contradiction/consistency checker；兼容 setting 的公开 reward checkpoint 另报并审计污染。BLEU/response 长度不是主要质量基线 |

## 5. Automated research：5 域

均需匹配学科的专家。论文/证据 bundle、版本与 publication cutoff 必须冻结；最终人类偏好不能由作者自评、被优化 judge、录用标签或未来引用代理替代。

| 域 / 对应数据文档 | 数据入口、已有 H 与补齐动作 | S1 fixed rubric 维度 | S3 必跑基础指标/工具与边界 |
|---|---|---|---|
| **TD-AR1 研究创意** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ar1) | Ideation Arena：6,441 expert records，D0 overall、D1–D4 维度；本地 literal query strings 去重约 1,848 不等于官方 2,191 contexts，需恢复真实 keys。**闭合文献 context，不额外 online retrieval**。数据按 CC BY-NC 4.0；ScholarIdeas/RQ-Bench 不自动补整体 pairs | novelty、feasibility、significance、specificity | 固定四维均分与 holistic overall 分别运行；closed-context claim/source support checker；不能把未来影响/Proof-of-Time proxy 当独立 expert H |
| **TD-AR2 ML/NLP 消融计划** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ar2) | AbGen-Eval 100 contexts×18 candidates 的 importance/faithfulness/soundness H1；无 overall H0。至少补 500 新 contexts 至入组目标并补专家 H0；AAAR/AblationBench 只在相同输入标准下供 context，不混临床/湿实验 | importance、faithfulness、soundness、控制/归因、可执行性 | AbGen-Eval 三维 fixed judge；intervention–control–outcome schema check；指标/样本/混杂诊断。原三维分不任意加权伪造 H0 |
| **TD-AR3 table→洞察报告** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ar3) | DataGovBench/BLADE/InsightEval 的 data+goal/reference；不是整体报告偏好库。先固定纯文本报告合同，生成同表同目标候选，补 600 source groups 专家 H0/H1 | 计算正确、证据充分、洞察价值、问题相关、解释/不确定性 | Python/SQL 重算数值 claims；字段与单位核验；固定 insight coverage/utility rubric。相关≠因果，代码成功≠有价值发现 |
| **TD-AR4 related work** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ar4) | RWGBench/SciRM/GREP 提供 inputs、retrieval/协议；GREP expert judgment payload 未确认公开。冻结 source bundle 和 cutoff，生成多 sections 新标专家 H0/H1；RWGBench 100-paper test 与 40,108 source papers 不是同一规模口径 | 覆盖、论点–引用支持、相对定位、综合/组织、书目信息正确 | citation existence；**作者/标题/年份/出版处（venue）逐字段核验**；claim–paper entailment；RWGBench coverage/organization。metadata 核验不同于 claim 支持；不能让 LLM 猜 venue |
| **TD-AR5 peer-review critique** · [专属文档](../../Auto-Evolve-Harness-for-Slide-Evaluation/docs/plans/p2e_v2_domain_knowledge_audit.md#td-ar5) | AAAR/PaperAudit/FLAWS 的论文与 controlled errors 供 inputs/H2；PRISM/PeeriScope 供协议。新生成同论文多 reviews 并专家比较 review 本身。**SurveyReview 评价 survey paper，不是 review quality，不能填本域 H0/H1** | 批评正确/有据、重要性、覆盖、可操作建议、公平/清晰 | 论文 evidence locator、controlled-error precision/recall（仅金标错误 subset）；固定 critique quality judge。paper acceptance 不是 review 质量；检出错误也不自动提供完整 review 排序 |

## 6. 可以先定位的本地数据，不把旧库存当完成证明

以下路径只用于 inventory。不要先打开其中历史 Test 的偏好来决定入组；先读 metadata、group keys、schema 与 exposure ledger。目录缺失时沿对应下载文档查找，不猜数据文件名。

| 路径 | 已知用途 / 限制 |
|---|---|
| `/home/azureuser/muzhao/auto_eval_harness/external_data/p2e_v2_main_domains_20260904/` | 旧四域原始源入口；不是 22 域全集，也不是冻结新 splits |
| 上述目录 `sv4/webdev-arena-preference-10k.json` | 10,501 rows；按完整请求归组并恢复网页 assets；禁止再分发原始 payload |
| 上述目录 `ar1/ideation-arena.json` | 6,441 rows；先查 context/candidate/维度键、重复判断、闭合文献输入和非商业许可 |
| 上述目录 `ar1/rq_bench.parquet` / `ar1/scholarideas.parquet` | 分别 input/rubric 相关记录；不是可直接拼接的 Ideation Arena H0 |
| 上述目录 `tg1/summarize_comparisons_train.parquet` | 历史 schema 92,858 rows /14,767 `info.id`；仍需 source 去重与污染检查 |
| 上述目录 `tg1/summarize_comparisons_validation.parquet` | 历史 86,086 rows，含 post/article 混合；不能直接整包作为当前 TL;DR Test |
| 上述目录 `tg1/summeval.parquet` | 100 source rows、每行多系统输出数组，不是足够的 600-source 主数据 |
| `/home/azureuser/muzhao/td-ig1/evidence/data/h0_cohort_report.json` | 旧 IG1 cohort 统计和 exposure 线索；旧 Val 不因重命名就成为未见 Test |
| `/home/azureuser/muzhao/sv4_era_skillopt_matched_20260921/` | 历史比较，仅作环境/资产线索。1 seed/8 updates、不同编辑面与 SkillOpt variant，不可直接充本次 5-seed 同预算结果 |

其他域的本地 asset 路径由执行 agent 从[下载记录](../../auto_eval_harness/docs/plans/p2e_hard_domain_download.md)和[数据源审计](../../auto_eval_harness/docs/plans/p2e_v2_data_source_audit.md)提取，写进自己的 `data_manifest.json`；本清单不把尚未核对的路径写成 ready。

## 7. 运行前的指标与来源核验

每个 S3 至少冻结：官方论文/实现链接、软件 commit、checkpoint hash、许可、输入合同、reference 可得性、文本/图像截断、原生 score 范围与正负方向、missing policy、GPU/模型调用成本、污染检查、search/reserve 角色。下列常见原生实现可优先读，更多领域入口在每域专属文档的 ecosystem 表中：

- [Design2Code](https://github.com/NoviScl/Design2Code)：官方截图指标，不移用为 specification 功能判定。
- [CLIPScore](https://github.com/jmhessel/clipscore)：ViT-B/32、前缀与长 caption 截断；默认原生设置，不悄悄换 pooling。
- [PickScore](https://github.com/yuvalkirstain/PickScore)、[ImageReward](https://github.com/THUDM/ImageReward)、[HPSv2](https://github.com/tgxs002/HPSv2)：各自训练集、checkpoint、输入与许可证分别核验。
- [ROUGE 实现](https://github.com/google-research/google-research/tree/master/rouge)、[BERTScore](https://github.com/Tiiiger/bert_score)、[SummaC](https://github.com/tingofurro/summac)：ROUGE-Lsum 的句分隔；BERTScore 固定 model/layer/baseline；SummaC 不由第三方包名猜变体。
- [SacreBLEU](https://github.com/mjpost/sacrebleu)、[COMET](https://github.com/Unbabel/COMET)：完整版本签名、语言对、reference 条件与训练污染。
- [CapArena](https://github.com/njucckevin/CapArena)、[summary 人工数据卡](https://huggingface.co/datasets/openai/summarize_from_feedback)、[Ideation Arena 数据卡](https://huggingface.co/datasets/yolo1213811/research-ideation-arena-dataset)：manual/auto 分开、同域 input 合同和最新 license 为准。

对有多个实现可选的指标，预先选一个并冻结，不在 Test 上挑版本。本轮默认 SummaC 为官方 SummaCConv（`models=["vitc"], bins="percentile", granularity="sentence", nli_labels="e", start_file="default", agg="mean"`）；其余需要下载的 checkpoint 先在 registry 写精确 revision 再进入 smoke。不可访问则记录 blocked，不让 agent 自造数值。

若写入论文的 references，检查**正式出版处**而非从 arXiv 年份推会议；已有字段审计见[文献审计](experiment_literature_audit.md)。例如 SummaC 正式记录是 [TACL 2022](https://aclanthology.org/2022.tacl-1.10/)，不能沿用旧 README 的年份。只确认 arXiv 的工作不补猜测 venue。

最后逐域回答四个问题：600 个独立有标签 groups 从哪里来？H0/H1/H2 对应的是哪一件作品？S1 和至少两种非冗余 evidence source 是否真能跑？独立 Test 与 N=4 标签是否满足合同？答案不完整就保留明确任务/阻塞；**22 域全做是执行范围，不是放松证据门槛。**
