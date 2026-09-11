# 八个原始 skill 的实际适配记录

执行日期：2026-09-11

本记录对应已经完成的代码/文本变化。来源审读见02号报告与skills_analysis.json；设计依据为07号综合创建提示词。源解包目录保持不变，所有修改发生在新包副本。

## 共同适配

25个有效运行源文件从8个原skill目录复制，排除.DS_Store、__MACOSX、__pycache__与.pyc；原始解包目录未改。八入口均加入../../references/shared-rules.md，Word与PDF路径映射至../paper-documents/SKILL.md、../paper-pdf/SKILL.md，路径按分支目录解析。原署名保留于来源metadata，不能成为新文稿/报告作者。

## academic-peer-review

保留7维度、样本提取、研究/综述分流、分阶段评价与两份references。删除‘Step1/2所有文件必须是样本’以及Step3重复上传硬门槛；依据用户标注/内容确定角色，区分期刊样本校准与一般审阅。删除major数量指标及按问题数机械判决，允许0主要问题；已有修改授权继续完成。文献身份与期刊当前信息须核实。author/channel/version移入metadata。

## reporting-guidelines参考表

加历史教学速查与实际设计/当前官方版本边界；删除PRISMA一律至少2库、所有综述应注册的绝对规则；MIAME不再泛称RNA-seq通用标准；临床AI按预测/诊断/试验方案/完成试验选规范；缺失与不足的严重性按实际影响判断。

## write-journal-cover-letter

保留三问证据brief、简短信件结构、期刊官网核验、匹配Markdown文件。直接替换默认无一稿多投/无COI/全作者批准条款：只写当前作者真实确认事实，缺事实可完成有据草稿，相关终稿声明待补。默认末位通讯作者改为用户指定或稿件明确通讯标记。删全面禁预印本/DOI规则，按真实信息与期刊要求披露。五段与Dear Editor保留为默认而非盖过官方要求；YAML同步删除旧假设。

## proofread-journal-manuscripts

保留全文重建、逐页视觉证据、锁定转录、1–2段窗口、三类问题、6列表与Word生成。改为默认逐节确认；用户已要求全文自动时连续执行。指出脚本只验证账本文字与字段一致性，不代替实际看图。外部documents/pdf改内置；取消宿主固定Python和系统缓存；字体--font可选，不指定则由文档/系统fallback，必须实际检查字形。原macOS配置改无固定路径的惰性历史占位，不再调用，并新增font-configuration.md。

## translate-academic-manuscript-zh-to-en

保留逐块直译→反思→意译、一次实质歧义术语确认、保护数值引用限定词、manifest恢复与clean/过程双交付。反思明确为可见误差诊断/修改理由，不记录隐藏思维链；Word依赖替换内置路径，YAML同步。

## generate-paper-highlights

保留标题/摘要/完整结果证据、候选排序去重、独立可读性和因果限制。无Results标题的综述可用完整证据综合章节。用户/期刊限额优先；一般草稿未给限额时85字符是明示工作默认；具体期刊终稿规则无法核实则只停相关合规终稿。按真实要求条数判断，不硬凑3条；更小有据集合标临时稿。脚本新增word-limit/no-limit分支与非空条目校验，保留字符与条数判定。

## polish-academic-manuscript

完整保留顺序小块、style sheet、编辑标准、科学边界、原格式拼接和终检，修改只涉及共享规则、内置Word/PDF路径与UI调用方式；未删有效润色功能或扩大成事实重写。

## recommend-sci-journals-report

去掉未提供recommend-sci-journals幽灵前置引用；保留当前期刊事实、JCR/官方排名/OA费用/不同审稿周期/HTML交付。实际候选数和分组服从用户，三组15本仅默认。历史名单明确为原课程包无官方URL的第三方记录，不把拷贝等同核真。renderer命令加入实际--risk-list参数，并同步schema。

## rewrite-academic-overlap

保留整段/明确标记双模式、标记外逐字符不变、科学与署名边界、13词自比较局限及长稿合并。添加共享规则与内置Word/PDF映射，UI不再假定全局另装分支。

## 四脚本：字符检查

check_highlights.py保留Python Unicode代码点长度；增加互斥--limit/--word-limit/--no-limit，词数明示为空白分词，不冒充所有期刊的词数定义；空条目不再因长度0通过。

## 四脚本：风险核查

check_journal_risk.py从实际名单‘统计截止’元数据读取年月，审计中保存完整解析risk_entries供直接比较，不新建hash。原候选SHA256保留；ISSN格式和共享ISSN重复候选检查防错误身份。核查结论注明历史边界，并只枚举实际名单类别。

## 四脚本：HTML渲染

render_journal_report.py要求--risk-list。根据当前候选和实际名单fresh build_audit，逐字段对比日期、完整风险记录、快照元数据、计数、匹配和既有候选指纹；任一不同则拒用旧审计。相同名单路径内容变化也会被发现。保留原HTML文本转义、URL检查、风格和结构检查；未新增hash/freeze/gate框架。

## 四脚本：Proof报告

build_proofreading_report.py用可选--font代替写死Arial Unicode MS，清除新DOCX的来源作者署名；增加coverage必须与section标题序列一致、included sections/segments非空要求。保留所有原excerpt/Current/uncertain/visual-note验证和横向六列表。

## 验证

27项脚本检查全部通过；8项入口frontmatter与共享/内置路径声明检查通过，7个YAML可解析且默认提示存在。执行脚本路径为包内修改版，原脚本未运行；测试无写pycache。验证资料为合成夹具，不是实际期刊建议或真实论文校对。

## 实际验证范围

Highlights：85/86字符边界、默认2条拒绝/显式2条允许、空条拒绝、单词边界/超限、无上限。选刊：原快照43条/2026-07、clear生成HTML、历史已知名单命中、候选变更拒旧audit、同路径名单新增命中拒旧audit、fresh新命中、过时audit日期、新月份正确读取。Proof：合法DOCX、非源excerpt、变造Current、不确定段、未锁定、coverage错序/标题差异、视觉类型无证据注释；另确认DOCX含原句/建议/中文理由且无固定作者/字体。

## 未声称事项

此任务没有联网核实历史风险名单和报告指南的当前状态，也没有为生成的Proof样例执行Word渲染。DOCX可生成且内部内容正确不等于视觉终检通过；包主流程可另行完成渲染。完整链接存在性/ZIP/隔离安装由主构建验证；本次只维护八分支及其适配记录。

## 已复制和修改的运行文件

| 分支 | 包内路径 | 状态 |
|---|---|---|
| academic-peer-review | skills/academic-peer-review/references/reporting-guidelines.md | 已适配 |
| academic-peer-review | skills/academic-peer-review/references/review-examples.md | 原样内置 |
| academic-peer-review | skills/academic-peer-review/SKILL.md | 已适配 |
| write-journal-cover-letter | skills/write-journal-cover-letter/agents/openai.yaml | 已适配 |
| write-journal-cover-letter | skills/write-journal-cover-letter/SKILL.md | 已适配 |
| proofread-journal-manuscripts | skills/proofread-journal-manuscripts/agents/openai.yaml | 已适配 |
| proofread-journal-manuscripts | skills/proofread-journal-manuscripts/references/font-configuration.md | 新增 |
| proofread-journal-manuscripts | skills/proofread-journal-manuscripts/references/macos-fontconfig.conf | 已适配 |
| proofread-journal-manuscripts | skills/proofread-journal-manuscripts/scripts/build_proofreading_report.py | 已适配 |
| proofread-journal-manuscripts | skills/proofread-journal-manuscripts/SKILL.md | 已适配 |
| translate-academic-manuscript-zh-to-en | skills/translate-academic-manuscript-zh-to-en/agents/openai.yaml | 已适配 |
| translate-academic-manuscript-zh-to-en | skills/translate-academic-manuscript-zh-to-en/SKILL.md | 已适配 |
| generate-paper-highlights | skills/generate-paper-highlights/agents/openai.yaml | 已适配 |
| generate-paper-highlights | skills/generate-paper-highlights/scripts/check_highlights.py | 已适配 |
| generate-paper-highlights | skills/generate-paper-highlights/SKILL.md | 已适配 |
| polish-academic-manuscript | skills/polish-academic-manuscript/agents/openai.yaml | 已适配 |
| polish-academic-manuscript | skills/polish-academic-manuscript/references/editorial-standard.md | 原样内置 |
| polish-academic-manuscript | skills/polish-academic-manuscript/SKILL.md | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/agents/openai.yaml | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/references/2026-journal-risk-lists-through-july.md | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/references/report-data-schema.md | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/scripts/check_journal_risk.py | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/scripts/render_journal_report.py | 已适配 |
| recommend-sci-journals-report | skills/recommend-sci-journals-report/SKILL.md | 已适配 |
| rewrite-academic-overlap | skills/rewrite-academic-overlap/agents/openai.yaml | 已适配 |
| rewrite-academic-overlap | skills/rewrite-academic-overlap/SKILL.md | 已适配 |

## 验证交付

- 项目相对目录 validation/source-skills/：合成输入JSON、历史名单副本、生成HTML/DOCX、失败审计、results.json、metadata_results.json、run_validation.py。
- results.json：27项，27通过，0失败；metadata_results.json：8入口、7UI。
- 期刊HTML和Proof DOCX均为标明用途的合成验证样例，不作为真实学术成果使用。
- 原包作者归属保留在源metadata与项目溯源报告中；不新增第三方许可声明。

## 前向试用后的定向修正

- Case02投稿信草稿：把精确期刊名/官方类型从所有起草的硬前置条件改为终稿核实条件。用户只要可审阅草稿时，依据已给标题、摘要和范围直接完成，用明确[Journal name]/[Article type to confirm]保留未知，不虚构；用户禁止提问时将缺项写成待核，文件名标DRAFT。官方信息不可取得只限制终稿合规声明，不阻断有据草稿。
- Case06离线摘要选刊：新增真实offline abstract-based preliminary screening分支。仅有摘要也可按用户数量给临时候选；明禁网时不联网，不因缺标题/完整Results反问。当前JIF/JCR/排名/发文量/费用/时效/索引状态全部明确未核实，不以历史风险筛查冒充现行核验。可交简单中文表/Markdown，不能给final HTML捏造clear审计。现行正式选刊仍保留授权联网核实流程。
- PDF P16简版与原Cover Letter skill模板：两种来源改为条件分支。用户指定PDF简版或只要信时，主要发现与期刊fit同段、最多2句，不展示三问brief；标准模式保留可用三问准备和独立fit，main-work也优先2句，brief是否展示服从任务。没有将‘三问先展示’与‘只交信’同时设为强制。
- 两分支UI默认提示同步更新；Cover Letter short_description缩至64字符以内。定向复核两份frontmatter与UI YAML可解析。四脚本未再变更，沿用实际27/27测试，不为纯提示词变化重跑无关脚本。
