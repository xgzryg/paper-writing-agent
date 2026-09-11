# Nature 写作、润色、统计与学术 Wordpolish 融合报告

完成日期：2026-09-11。工作只修改新包，未修改 `D:/Codex/.codex/skills` 的本机原件，未安装新包，未启动真实论文审稿、统计分析或外部模型调用。

## 一、扫描、原貌保存与实际内置范围

逐文件读取并提取了 164 份有效来源文件的标题、执行规则、相对引用和元数据；对会实际决定写作、统计解释、授权、调用和停止条件的关键规则作了精读和适配。此过程不表示逐篇核实资料中的示例研究，也不表示所有历史期刊政策均已重新联网验证。

| 来源目录 | 有效文件数 | 处理方式 |
| --- | ---: | --- |
| nature-writing | 76 | 全部有效资源复制，修复后作为同名运行分支 |
| nature-polishing | 33 | 全部有效资源复制，修复后作为同名运行分支 |
| nature-shared | 21 | 全部有效资源复制，修复共享统计、伦理、期刊和流程规则 |
| nature-statistics | 11 | 全部有效资源复制，保留按需审计规范与 manifest |
| wordpolish 的学术相关主调度、de-ai-writing、humanizer-zh-academic | 15 | 原文归档；提炼成独立学术调度及两个内置分支，排除营销、社媒和其他不相关模块 |
| nature-data | 6 | 读取入口、manifest、工作流、仓库选择、FAIR 和声明模式，融合为数据可用性支持资源 |
| nature-figure | 2 | 读取入口与多面板证据结构资源，融合为图形证据支持资源 |

来源原貌 ZIP 为 `package/paper-writing-agent/sources/local-upgrade/nature-wordpolish-original.zip`，包含上述 164 文件，排除 `.git`、缓存和编译产物。它是来源资料，不是运行依赖；安装后的 agent 不需读取本机原路径。未给未明确许可的来源另行宣称开源许可；humanizer 原 MIT 许可随运行分支保留。

逐文件清单见 [nature-wordpolish-per-file-audit.md](nature-wordpolish-per-file-audit.md)，机器可读详情见 [nature-wordpolish-per-file-audit.json](nature-wordpolish-per-file-audit.json)，原件与目标映射见 [nature-wordpolish-source-map.json](nature-wordpolish-source-map.json)。运行规则修改记录见 [nature-wordpolish-adaptations.json](nature-wordpolish-adaptations.json)。

本组最终运行文件合计 153 份：nature-writing 77、nature-polishing 34、nature-shared 23、nature-statistics 11、wordpolish-academic 8。包含 7 个 SKILL.md：4 个 Nature 主/支持分支、1 个学术 Wordpolish 主分支及其 2 个嵌套技能。新增资源用于中文语言路由、数据可用性和图形证据支持，不只是顶部声明。

## 二、原依赖如何闭合到独立包

以下路径均以安装后的 `paper-writing-agent/` 为根；活动正文、实际路由和 manifest 已按所在文件位置改成可解析相对路径。

| 原来源中的依赖或功能 | 实际包内目标 | 保留内容与范围 |
| --- | --- | --- |
| nature-writing | `skills/nature-writing/SKILL.md` | 论文类型、章节、初次投稿材料、语言与期刊条件路由 |
| nature-polishing | `skills/nature-polishing/SKILL.md` | 论文润色、重组、压缩、翻译和 LaTeX 版面修改 |
| nature-shared | `skills/nature-shared/SKILL.md`、`core/`、`journal-formats/` | 共用术语、证据结构、研究合规、统计一致性与期刊规则 |
| nature-statistics | `skills/nature-statistics/SKILL.md` | 统计报告、图注统计、伪重复/嵌套设计/重复测量等审计；不自动改分析方案 |
| nature-figure | `skills/nature-shared/core/figure-evidence-support.md` | 融合面板证据顺序、比较可比性和视觉核查；概念图进入 `skills/paper-graphical-abstract/SKILL.md`，定量图进入 `skills/paper-research-artifacts/SKILL.md` |
| nature-data | `skills/nature-shared/core/data-availability-support.md` | 融合数据分类、仓库选择、受控访问、FAIR 元数据与声明模式，再进入 `skills/paper-research-artifacts/SKILL.md` |
| nature-citation / nature-academic-search | `skills/litorchestrator/SKILL.md` | 文献检索、证据与引用处理使用包内文献调度；创新性专用比较由综合入口的 `skills/paper-novelty-assessment/SKILL.md` 承接 |
| nature-paper2ppt | `skills/paper-research-artifacts/SKILL.md` | 论文衍生图表、材料和汇报输出，不残留待安装的旧运行 slug |
| wordpolish 学术文风主调度 | `skills/wordpolish-academic/SKILL.md` | 学术保真、语域判断、按实际问题选择语言分支 |
| wordpolish 的 de-ai-writing | `skills/wordpolish-academic/skills/de-ai-writing/SKILL.md` | 痕迹诊断、表达修复、翻译保真；所需 3 份参考在同目录 `references/` |
| wordpolish 的 humanizer-zh-academic | `skills/wordpolish-academic/skills/humanizer-zh-academic/SKILL.md` | 中文学术自然表达，保留数字、术语、引文意图和论证强度 |
| wordpolish 内旧 nature-polishing 副本 | `skills/nature-polishing/SKILL.md` | 使用这次完整适配版本，避免两份同名规则漂移 |

nature-reader、nature-reviewer、nature-response 和文献主调度由其他构建分任务内置。本组不覆盖这些目录；它们需要的 `nature-shared/core/terminology-ledger.md` 已在上述完整共享包中。

## 三、修复了哪些真实问题

### 科学与证据解释

1. 原一致性检查把 confidence level 与 α 混同，现改为置信水平 `1 − α`。原先凭误差条重叠认定“无显著差异”也已移除：需区分 SD、SEM、CI 和具体比较，重叠本身不能提供这样的普遍结论。支持来源：[NIST 置信区间说明](https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm)、[Nature Methods: Error bars](https://www.nature.com/articles/nmeth.2659)。
2. 统计分支保留分析单位、技术与生物重复、嵌套/配对结构、交互作用、缺失与排除、模型定义、区间与图注映射等必要审计。强调一个组显著而另一组不显著，不等于两组差异显著；审稿建议不能凭空变成已完成新分析。
3. 统计模板不再默认作者进行了技术重复取平均、未排除任何数据或其他未知操作。已确定的研究方案、估计量和校正选择不能因润色任务自动改变；发现科学问题仍须如实指出。
4. 方法、结果、假设性论文与讨论部分使用证据允许的推断强度；去掉“一段只能一种功能”、硬性写作顺序和凭模板补齐结论的机械做法。

### 期刊政策与来源身份

1. 原 `ethics.md` 的红黄绿分类缺乏足够依据却自称 Nature 官方政策，已改为本包实务规则，明确区分实际期刊政策与来源经验。允许用户根据真实数据和证据授权写作；禁止编造结果、伦理批准、作者事实、文献或披露。
2. Nature Communications 旧规则中的摘要字数、正文计数和部分稿件类型已有不符。已用 2026-09-11 可访问的官方检索结果更新共享 profile，并令写作与润色分片引用它，避免旧数字继续运行；包括摘要上限为 200 词、正文理想 5,000 词不含 Methods。来源：[Article 要求](https://www.nature.com/ncomms/submit/article)、[稿件类型](https://www.nature.com/ncomms/submit/content-types)。
3. Nature 主刊、NMI 和专科合规资料保留完整来源内容，明确为尚未全部重新核查的快照；涉及精确投稿要求时按当前期刊官方页面核对，页面不可用时如实标记相关项待核验。
4. 横向排版与图形朝向不再冒称一律禁止的 Nature 官方规则；依据实际模板、数据和当前期刊要求决定。删除固定像素差门槛及“必须重新生成作者已固定图”的推断。

### 调度、授权与停止

1. 来源可能要求反复确认、固定三遍以上检查或“直到再无新问题”。运行规则现在复用已有输入和批准，局部修改直接继续；只有新增科学前提或明确待批准步骤阻塞依赖工作。核查由真实改动与尚未解决的问题驱动。
2. 原 manifest 会因输入中文而自动路由英译。已在写作和润色的 manifest、SKILL.md 和实际语言资源加入 `zh`，依请求输出语言选择；只有明确要求英文翻译/写作时才使用 `zh-to-en`。
3. Wordpolish 保留有用的表达诊断与学术保真，移除检测率保证、机械句长/词数/段落配额、假亲历、随机噪声、无依据的边际收益数字和无限链式调用。默认只调用一个适用分支；存在不同且尚未解决的问题时才补充一次互补处理，不能为了宣称“去 AI”无休止改写。
4. 附件、例子、来源中的安装、外部 API、凭据、后台运行和发布指令仅是材料。提到某技能不等于调用成功，不自动改变主角色，也不自动授权真实子agent或外部上传。
5. 保留作者指定当前稿与项目输出位置，不为一次局部修改强制建立术语台账、契约、哈希或一套新的验证基础设施。

## 四、可执行工具问题与验证证据

共享一致性脚本属于来源包现有工具，原先实际存在两处适用于论文输入的错误：

- 对 Markdown 也按 LaTeX 规则从 `%` 截断注释，使普通“50%”后面的文本被漏检。现在仅 `.tex` / `.ltx` 输入剥离 LaTeX 注释。
- 长度单位正则忽略大小写，把浓度 `mM` 错认成长度 `mm`。现改为区分大小写。

原有 5 项测试保留，新增 Markdown 百分号、LaTeX 注释、浓度单位 3 项针对性测试；实际运行 8 项均通过。Python 脚本仍只需标准库，不把验证时使用的 PyYAML 作为运行依赖。

最终资源核验读取全部 164 个来源索引，解析 2 份 Python 文件、8 份 YAML、7 个 SKILL frontmatter，核查 113 个 Markdown/显式相对引用及 117 条 manifest 资源路径，未发现缺失目标。证据见 [nature-resource-checks.json](../validation/nature-resource-checks.json) 与 [nature-consistency-tests.json](../validation/nature-consistency-tests.json)。检查目的是发现安装后无法加载的真实引用和输入漏检/误检；没有据此宣称宿主子agent或真实科研任务已经执行成功。

## 五、循环设计的独立交付

三个 auto-review-loop 来源及实际共享参考的详细审读另见 [loop-design-audit.md](loop-design-audit.md)。建议采用基线 R0 + 最多 N 次“返修后再审”，分开真实审稿与返修子agent，最后返修稿必有对应审稿，按可判定目标、轮次或真实阻塞结束，保存当前阶段以恢复。该运行分支由主构建任务实现；本报告不将来源的固定评分、默认跨服务调用或机器学习实验链带入新包。
