# P2E 论文草稿

**P2E: Evolving Evaluation Systems for Open-Ended Generation**

本仓库撰写 Preference-Guided Evaluator Evolution（P2E）项目的论文。研究范围是开放式生成的评估系统，涵盖结构化视觉产物、图像与 3D、文本生成和自动科研，不限定为 slide generation。ERA（Evidence-Guided Revision of Agentic Evaluators）仅指其中的评估器修订方法。

本轮按源码项目的 `docs/plans/p2e_v2_plan.md` 重组了完整论证：评价生态 → 语义空间与分歧挖掘 → H0–H3 → 证据表 Z → ERA → 独立下游验证。当前采用原版 ICLR 2027 模板，匿名审稿模式；是方法与研究设计草稿，尚无实证结果，模板的 “Under review” 页眉不表示已经投稿。源码仓库 [Auto-Evolve-Harness-for-Slide-Evaluation](https://github.com/Moore-Tian/Auto-Evolve-Harness-for-Slide-Evaluation) 保留历史名称，未重命名代码仓库或本地目录。

## 阅读

- [paper.pdf](paper.pdf)：编译预览，正文 9 页。
- [main.tex](main.tex)：主入口，Overleaf 选择此文件。
- [sections/](sections/)：正文和附录，新增独立的偏好挖掘章节。
- [figures/](figures/)：8 张可编辑图，5 张正文图、3 张附录图。
- [完整覆盖映射](.paper/plan_coverage.md)：计划条目与正文、图表、证据边界的对应。
- [主张索引](.paper/claims.yml)、[图表索引](.paper/figures.yml)：后续写作与图文一致性校验的结构化记忆。
- [references.bib](references.bib)：33 条引文，核对来源见 [reference_sources.json](.paper/reference_sources.json)。

8 张图分别解释完整 P2E 框架、信号—维度矩阵、六组件评估器、方向假设与修订、C1/C2/C3 对照、跨域标注示例、数据与保留指标边界、语义融合。10 张表覆盖主结果模板、完整 22 领域、标注来源、就绪条件、消融、训练对照及报告要求。22 个领域是研究全景，不是已经完成的 22 项实验。

C1 检验固定候选池上的对齐与选择；C2 从共享的新生成输出出发比较 critic；C3 设计冻结 reward 下的 LoRA + GRPO 对照。C3 仅为研究设计，本次没有启动参数训练。结果表中的横线均表示未测量，不是零值。

## 编译和检查

需要 TeX Live 或同等环境，含 pdfLaTeX、BibTeX、TikZ、algorithm/algpseudocode、booktabs/tabularx/longtable、multirow、placeins 和 natbib。日常离线检查仅用 Python 3 标准库。

```bash
make
make check
```

构建中间文件位于 `build/`，最终文件为 `paper.pdf`。编译不需要 Azure 登录或模型 API。Overleaf 上传 TeX、BibTeX、模板、`figures/`、`output/imagegen/` 即可。`.paper/*.yml` 使用 JSON 兼容的 YAML，便于标准库检查，仍可由 YAML 工具读取。

`make check` 检查引用、标签、9 页限制、溢出、图像哈希与分辨率，以及 22 领域、主张证据状态、图注和图表索引及正文引用。结构检查不代替学术审读或实证验证。

## 插图与证据

GPT Image 2 已通过指定的 Azure Foundry 接口生成四类领域的插图素材，最终资产为 [domain-panorama-final.png](output/imagegen/domain-panorama-final.png)，3840×1280。精确流程、数学、图内文字和其余图全部保留 TikZ 源码。生成提示与说明见 [image_generation.md](.paper/image_generation.md)。

所有现有图均为概念图或明确标记的合成示例，不是实验观察。性能曲线、效率曲线、真实案例和数值结果必须等获准的数据与冻结分析准备好后再加入。写作不收录调试流水账、探索历程或历史中间方法。

## 后续作者工作

冻结实际实验域、数据、标注协议、模型、对照和预算；提供经授权的结果与新生成输出的盲化判断；完成作者信息、许可、伦理和 AI 使用声明。不得用 H0 推导出并不存在的 H1/H2，不能把模型解释写成人类理由。

本公开仓库含可识别的项目来源，不是匿名补充材料。投稿前需独立检查 PDF、代码链接、补充材料与元数据的匿名性。不得提交凭据、私有运行路径、真实样本标识、日志、生成评估器或未经授权的结果。

## 模板来源

`iclr2027_conference.sty` 与 `iclr2027_conference.bst` 原样取自
[ICLR/Master-Template](https://github.com/ICLR/Master-Template/tree/46ed6f4c6cef5b175dde23639e77d44c3463b230/iclr2027)，提交 `46ed6f4c6cef5b175dde23639e77d44c3463b230`。
未修改字体、页边距或版芯。初投稿正文上限为 9 页，参考文献、附录及规定声明不计入；提交前再次核对当年官方政策。
