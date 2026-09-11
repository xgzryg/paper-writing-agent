# 独立前向使用观察

本报告来自对成品包的实际读取与场景回复，未读取构建报告、设计结论、参考答案或构建过程。八例由同一独立执行者顺序完成，按各自输入边界处理；未把其他案例的作者、协变量、样本、授权或完成状态带入本例。Case 02、Case 06 首次出现实际停止后，已向根 agent 报告；根 agent 修改对应分支并明确要求复测后，仅重读、复测这两例。

包根：`C:/Users/Lenovo/Desktop/AI工作路径/论文写作skill/论文写作综合agent_构建/package/paper-writing-agent`

场景输入：`C:/Users/Lenovo/Desktop/AI工作路径/论文写作skill/论文写作综合agent_构建/validation/behavior_cases.md`

输出目录：`C:/Users/Lenovo/Desktop/AI工作路径/论文写作skill/论文写作综合agent_构建/validation/behavior_outputs`

## 实际执行范围

- 读取入口 `SKILL.md`、`references/shared-rules.md`、`references/routing.md`，再读取以下对应分支。未仅依据路由表模拟调用。
- 所有 `case-01.md` 至 `case-08.md` 都是该场景将实际交给用户的完整回复。必要问题和停止点只记录在场景文件，没有向当前真实用户发问。
- 未联网，未生成图像，未发送或发布稿件，未改全局环境，未读取或更改真实科研数据。未修改包内任何文件。
- 输出与辅助计数输入均写在上述验证输出目录内。针对根 agent 授权的两例复测，先保留初次文件为 `case-02-initial.md`、`case-06-initial.md`，再更新主文件；未删除已有文件。

## 各例实际读取、输出和停止位置

| 场景 | 实际读取的分支/必要支撑 | 实际完成及停止位置 | 当前场景中的观察 |
|---|---|---|---|
| Case 01 | `skills/paper-methods/SKILL.md` | 输出六节 Methods 大纲、图表与方法对应关系、关键缺项；记录大纲确认问题，未起草完整 Methods | 分支确实保留新起草大纲确认。没有把表 1 的四变量当作 Cox 调整集，没有编造伦理号、缺失数据处理或 log-rank 检验。目标期刊未定未阻止大纲整理 |
| Case 02 | `skills/write-journal-cover-letter/SKILL.md`，首次和修改后各实际读取一次 | 首次止于期刊名/文章类型缺失；修改后输出可审阅英文信，并保存只有信正文的 Markdown 文件 | 复测已能用 `[Journal name]`、`[Article type to confirm]` 完成草稿。保留预印本事实；未声称作者已批准、没有利益冲突或未同时投稿。通讯作者 Lin Chen，机构和邮箱留空 |
| Case 03 | `skills/rewrite-academic-overlap/SKILL.md` | 输出完整英文段落，仅修改方括号内的文字；保留括号和全部外部字符 | 用户“其他字符都保留”覆盖分支默认去掉编辑括号的惯例。字符比较验证外部文本完全一致；没有进入翻译或全文润色分支 |
| Case 04 | `skills/paper-graphical-abstract/SKILL.md` | 输出可据此出图的三部分文字方案；停在用户要求的方案阶段，未生成图像 | 将 1200×800 正确识别为 3:2，提出 1920×1080 的 16:9 方案。恰好规划三个英文标签。连接说明维持观察关联，没有补造测量设备、七天测量周期、干预或机制 |
| Case 05 | `skills/academic-peer-review/SKILL.md`；`references/review-examples.md`；`references/reporting-guidelines.md`（后二者为本分支内） | 输出三项正确性结论和两项可选表达优化；未提出新分析或假设未提供方法有缺陷 | 120＝60+60、12/60＝20%、18/60＝30%、RR≈0.67，给出的区间与未显著表述相容。没有为了“五条”制造五个问题；没有宣称重新计算置信区间 |
| Case 06 | `skills/recommend-sci-journals-report/SKILL.md`，首次和修改后各实际读取一次；首次还实际读取其 `references/report-data-schema.md` 和 `scripts/check_journal_risk.py` 以了解是否有可用的本地降级路径 | 首次未给候选，止于完整输入/联网前提；修改后以离线模式输出恰好三本临时候选和用户所要字段的表格 | 当前 JIF、JCR 分区、年发文量、首轮外审时间均标“未核实”。链接只作为未访问的期刊入口，没有冒充来源已核验。没有运行风险检查或 HTML 渲染，也未声称风险筛查通过 |
| Case 07 | `skills/paper-reviewer-response/SKILL.md` | 输出中文逐条策略、状态表和完整英文回复草稿；R1-Q1 明确待独立验证/待校准，R1-Q2 引用已提供的 Methods 第 3 段文字 | 区分原稿已有 MICE 20 个数据集与新补变量范围；定位使用 Methods paragraph 3，不造行号。建议限制文本明确“尚未实施”，没有把下周计划写成完成状态 |
| Case 08 | `skills/paper-compression/SKILL.md`；其 `scripts/count_words.py` | 实际运行计数脚本，得到 115 词；输出逐句精简建议、具体删除项、两种方案；停在用户选择前，没有改写正文 | 保留数字、引用与三类证据限制；把删除未来研究整句列为作者可选实质取舍。压缩后字数仅标估计，没有虚称已经达到减半 |

## 实际发现并报告的两处入口问题

### 1. 首次 Cover Letter 流程把可审阅草稿卡在最终定稿输入之前

首次读取的 `write-journal-cover-letter/SKILL.md` 第 1 节要求：

> If the target journal or article type is missing, ask for only the missing item or items before researching or drafting.

Case 02 已经给出标题、摘要、期刊范围、通讯作者与作者声明现状，明确请求先给可审阅信，缺的是期刊全名和正式文章类型。实际按原分支走到停止点，只输出已知事实和输入问题，没有给信。初次实际回复保留在 `case-02-initial.md`，不是事后推定的失败。

已向根 agent 报告后，收到分支已修改及仅复测该例的指令。重新实际读取可见新增 reviewable draft 与 final submission-ready 的区分，允许占位、使用用户范围文字、明确禁网时不中断草稿。复测后已形成 `case-02.md` 与 `outputs/Cover_Letter_Sleep_Regularity_DRAFT.md`。本次路径中，首次的输入阻断不再发生。

### 2. 首次选刊流程缺少禁网、无标题的摘要初筛路径

首次读取的选刊分支要求：

> If the title or sufficient abstract is missing, ask only for the missing material and stop before recommending journals.

同时要求：

> Browse the web during every task.

Case 06 明确本轮禁网、缺信息不反问、按现有摘要推荐三本可能期刊。原分支仍将标题与完整结果作为推荐前提，并要求联网；实际回复因此只整理选刊定位，没有给三本候选，且为遵守“不反问”没有提出问题。该初次实际输出保留在 `case-06-initial.md`。

修改后重新读取可见新增 offline abstract-based preliminary screening 路径：允许无标题摘要初筛、遵守三本数量、把动态指标标未核实、以简单中文表格交付、无需假造风险审计或最终 HTML。复测已输出 Sleep Medicine Reviews、Sleep Medicine、JMIR mHealth and uHealth 三本临时候选，并明确它们的范围判断和入口链接未作当前核验。当前路径下该阻断已解除；“最新指标”仍没有数据，因禁网与未提供来源而如实留为未核实。

## 已执行的必要核验

1. Case 03：用程序比较括号外前后文本，包括原有括号、标点和空白，结果 `True`；括号内确有变化。对该标记范围的自比，最长连续相同词串为 2 个词，没有把未改的周边文本算进改写阈值。
2. Case 08：使用本机已有 `F:/Program Files/Python313/python.exe` 调用包内计数脚本，输入为 `case-08-source.txt`，退出码 0，`english-words` 结果 115。没有安装环境或改变全局配置。
3. Case 02 复测：实际读回投稿信文件，确认以 `Dear Editor,` 开头、文件正文与场景回复中的信一致；主体段为 2 句、67 词。没有把草稿说明、来源或报告内容写进信正文文件。
4. 确认八个场景主回复文件全部存在且非空；初次两例输出仍保留。

计数脚本本次标准输出中的中文路径在工具显示中出现乱码，但进程成功且计数值正常；输入和保存的 Markdown 文件仍可按实际路径读取。这是本次出现的终端显示现象，没有观察到其导致文件路径解析、读取或字数错误；未把它当作需改科学内容的问题。

## 其他实际矛盾、断链与局限

- 本次实际访问的入口、分支、评审参考和计数脚本均能读取；没有遇到缺文件或断链。
- 除以上两处已复测的入口阻断外，没有遇到其他使这八例无法按其授权范围执行的实际矛盾。未对未访问分支、未运行工具或完整包的所有能力作“无问题”保证。
- 评审分支包含整稿/期刊校准的通用结构，本例按用户明确的段落内部核查范围执行，没有把样稿校准、200–300 词总评或未提供方法的完整审计变成前提。
- Case 04 交付的是方案，没有最终图像，故没有声称完成视觉质量核验。Case 06 没有当前期刊指标证据，故没有声称完成现行选刊验证。Case 07 只有用户粘贴的修订文字，回复明确未逐页核查完整修订稿。

本观察报告只记录此次实际试用结果；不替代源技能脚本测试、文献事实验证或真实稿件审查。
