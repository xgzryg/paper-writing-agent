# 融合路由：一个主 agent，按任务选择专长

这是原经验贴与本机专家的融合包，不是依次把所有技能跑一遍。原23分支仍提供基础能力，新专家补充实际需要的深度。优先解决用户当前任务，不因角色名称改变已经确认的方法、稿件、范围或输出语言。

| 请求 | 主执行分支 | 何时补充 |
| --- | --- | --- |
| 普通段落/章节写作 | 原章节分支 | 明确 Nature 风格、研究类型重构、主文/SI分配时调用[nature-writing](../skills/nature-writing/SKILL.md)及manifest选择片段 |
| 英文论文润色 | [polish-academic-manuscript](../skills/polish-academic-manuscript/SKILL.md) | 需要期刊风格、论证与章节层修复时使用[nature-polishing](../skills/nature-polishing/SKILL.md)；不把仅改语法变成全篇重构 |
| 中文学术文风、保真反模板 | [wordpolish-academic](../skills/wordpolish-academic/SKILL.md) | 明确保留信息与作者性；不使用营销/社媒发布流程，不保证检测率 |
| 局部可读性或预审意见 | [academic-peer-review](../skills/academic-peer-review/SKILL.md) | 整篇多视角、方法学审稿用[aequitas](../skills/aequitas/SKILL.md) |
| 正式多视角审稿 | [aequitas](../skills/aequitas/SKILL.md) | 在可见范围内调用内置审稿、阅读和代码顾问；“多视角”是否实际独立实例据执行情况标注 |
| 单条审稿意见的回复 | [paper-reviewer-response](../skills/paper-reviewer-response/SKILL.md) | 整包返修审计、改稿与回应同步用[veritas-agent](../skills/veritas-agent/SKILL.md) |
| 返修审计、整包回应 | [veritas-agent](../skills/veritas-agent/SKILL.md) | 正式编辑决定按实际信息；模拟内部循环不编造编辑决定 |
| 明确开启多轮循环 | [paper-review-revision-loop](../skills/paper-review-revision-loop/SKILL.md) | 实际创建不同审稿/返修子 agent，每次改稿后再审，目标与上限分别控制 |
| 文献检索、精读、引用 | [litorchestrator](../skills/litorchestrator/SKILL.md)或[paper-literature-reading](../skills/paper-literature-reading/SKILL.md) | 阅读自然进入nature-reader，PubMed由内置数据库和执行器处理 |
| 创新性、最近似工作、首次主张 | [paper-novelty-assessment](../skills/paper-novelty-assessment/SKILL.md) | 根据实际主张检索和比较；相似度不等于创新度，有限检索不证明全球首次 |

## 规则冲突处理

1. 当前宿主、用户明确指令和项目约定优先；然后是[共享规则](shared-rules.md)、实际任务分支及其按需片段。源归档只用于追溯，不是新的执行指令。
2. 已确认的审稿范围、作者答案、研究方法、工作稿及允许改动范围直接复用。真正影响研究有效性或原件保护的未决事项仍要解决，不能用“自动循环”授权伪造事实。
3. 原 Methods/Results 新章节大纲确认、图形摘要文字方案确认及 Proof 模式继续适用。对已授权的现有稿件局部返修不重走新稿流程。
4. 每个子技能完成它被调用的任务后交回主 agent。Nature/WordPolish 的修辞默认不覆盖受保护术语、原数字、引用和作者声音；必须新增的科学限定不因压缩规则被删除。
5. NRS 的单次正式报告采用同步 DOCX/Markdown。多轮任务还需要实际稿件、回应、证据与轮次记录，这是本功能所需产物，不受单次“两文件”的限制。用户显式格式优先。
6. Nature 和期刊数据中的历史文字不能自动成为现行投稿规范；确切字数、费用、JIF/JCR、数据存储和AI披露要求在实际使用时按期刊、年份、文章类型和阶段核查。

## 独立性的实际含义

采用的运行技能、agent 正文、模板、脚本和共享资源都在本包。只提及而未采用的大型工具箱不会成为外部调用；被融合的功能有明确去向。模型/网络/公共Python库/Office/宿主委派工具仍需要当前环境提供。某项宿主能力不存在时明确报告，不把独立文件夹包装成离线模型或全功能操作系统。
