# Preference-Guided Evaluator Evolution 论文草稿

**Learning to Evaluate Structured Artifacts from Human Preferences**

本仓库用于撰写“人类偏好驱动的评估器进化”项目的论文。项目研究不同评价标准下的可执行评估器学习，幻灯片、网页和其他结构化产物是候选应用，不将研究范围限定为 slide generation。源码仓库 [Auto-Evolve-Harness-for-Slide-Evaluation](https://github.com/Moore-Tian/Auto-Evolve-Harness-for-Slide-Evaluation) 保留历史名称，不代表当前研究范围。

当前采用官方 **ICLR 2027** 模板，保留匿名审稿模式。它是方法与实验设计骨架，不是已完成实验的投稿版本；模板自带的 “Under review” 页眉不代表已经投稿。

项目定位与方法名分开使用：**Preference-Guided Evaluator Evolution** 描述整个研究项目；**ERA**（Evidence-Guided Revision of Agentic Evaluators）是其中的评估器修订方法。论文题目围绕研究问题组织，目前为工作标题。这里没有重命名已有代码仓库或本地目录。

## 阅读与修改

- `paper.pdf`：已编译的预览。
- `main.tex`：主入口，Overleaf 选择此文件。
- `sections/`：摘要、引言、相关工作、问题定义、方法、实验设计、结果、讨论、结论及附录。
- `figures/`：主图入口与两张可编辑的 TikZ 细节图，分别说明研究整体、评估器结构和数据边界。
- `output/imagegen/overview-final.png`：GPT Image 2 生成的 3840×2160 主图；其中的作品缩略图是概念示意，不是真实实验案例。
- `references.bib`：参考文献；核对来源见 `.paper/reference_sources.json`。
- `.paper/`：写作范围、主张—证据索引、图文对应和待补事项，不参与 PDF 编译。

正文按论文论证组织，不收录调试流水账、探索历程或历史中间方案。研究工程中的可选分支没有自动升级为论文贡献。

## 编译

需要 TeX Live 或同等环境，包含 `pdflatex`、`bibtex`、TikZ、`algorithm`、`algpseudocode`、`booktabs`、`tabularx` 和 `natbib`；检查脚本使用 Python 3 标准库。

```bash
make
make check
```

构建中间文件位于 `build/`；最终预览为 `paper.pdf`。`make clean` 仅删除构建目录，不删除已生成的预览。Overleaf 使用 pdfLaTeX，上传本仓库的 TeX、BibTeX、样式、`figures/` 与 `output/imagegen/` 即可。编译不需要 Azure 登录或模型 API。

主图使用指定的 GPT Image 2，经 Azure OpenAI 兼容接口生成与编辑；原始提示及箭头修订提示保存在 `.paper/prompts/`，生成说明见 `.paper/image_generation.md`。两张精确结构图保留 TikZ 源码。所有插图均为方法与协议示意，没有虚构性能曲线或观测数值。

## 继续写作前需要补齐

1. 确认最终题目、作者顺序、机构和匿名发布方案。
2. 冻结实验域、数据版本、原始输入分组、人工标注协议、模型版本和预算。
3. 运行经授权的对照实验，再填入 `sections/results.tex`；所有 `—` 均表示尚未测量，不是零值。
4. 补充真实的区间估计、成本、消融、选择与改进实验，以及经过许可的案例。
5. 完成人工审读、伦理/数据许可确认和 AI 使用声明。当前不宣称作者已经完成这些核验。

方法约定：单作品独立评分；每个作品至少三次完整评分后取中位数，再比较人类严格偏好；提案 Train 与封闭开发 Train 分离；Val 只在候选冻结后使用；Test/OOD 不参与修订。具体结果和实验记录不在此公开仓库中。

此仓库公开可见，`.paper/` 含项目来源，不属于匿名投稿材料。正式提交时须单独检查 PDF、补充材料、代码链接及元数据的匿名性。不要提交凭据、私有运行路径、真实样本标识、日志或未经授权的结果。

## 模板来源

`iclr2027_conference.sty` 与 `iclr2027_conference.bst` 原样取自
[ICLR/Master-Template](https://github.com/ICLR/Master-Template/tree/46ed6f4c6cef5b175dde23639e77d44c3463b230/iclr2027)，提交
`46ed6f4c6cef5b175dde23639e77d44c3463b230`。未修改字体、页边距或版芯参数。
初投稿正文上限为 9 页；参考文献、附录及规定的声明不计入。提交前应再次核对当年的官方政策。
