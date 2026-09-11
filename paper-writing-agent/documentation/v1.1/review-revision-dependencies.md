# 审稿与返修 agent 的依赖审读、融合与验证

本轮从本机实际安装的 `D:/Codex/.codex/skills/aequitas`、`veritas-agent` 出发，读取其 SKILL、agent 正文、可见范围规则、元数据与模板，追踪可执行调用到 NRS、Nature Reviewer/Response、Calder、学术代码审查及返修工具。完整源文件清单另见同目录 `review-revision-dependencies.json`。未修改本机安装内容。

## 1. 实际依赖拓扑与采用决定

| 起点 | 原调用/依赖 | 实际状态 | 包内处理 |
| --- | --- | --- | --- |
| Aequitas | agents/aequitas.md + reviewer-visible-scope.md | 角色正文与可见范围均存在 | 内置，融合便携优先级与本轮循环授权；原规则另归档 |
| Aequitas | nature-review-studio.review | 技能文本存在，旧工程与 renderer 不存在 | 内置12维/20实列策略/8基础状态；新写真实渲染器，不假装旧工程可用 |
| Aequitas | nature-reader | 条件解析依赖 | 由文献分支内置；亦可调用已有 paper-pdf / paper-documents |
| Aequitas | litorchestrator | 条件文献顾问 | 由文献分支递归内置；创新性、引文缺口、近似论文对比共用该入口 |
| Aequitas | calder / calder-code-reviewer | calder为历史调用名，实际安装名为calder-code-reviewer | 内置实际角色与code-review-academic，仅代码进入可见范围时读取 |
| Aequitas | nature-reviewer | 本机更完整的审稿独立性、证据与严重性规则 | 主动融合补充；保留20个源文件及资源 |
| Veritas | reviewer_response_blank_template.docx | 当前相对目录下存在 | 原文件完整内置，按副本使用；不依赖旧WorkBuddy路径 |
| Veritas | nature-review-studio.respond | 同上，原管线缺失 | 保留内部策略支持，正式作者面走真实模板/Nature Response |
| Veritas | nature-response | 37文件、1个实际执行脚本和3个LaTeX模板 | 完整内置；原脚本7项行为测试通过 |
| Veritas | rebuttal-writing | 单文件MIT标注技能，有内嵌示例代码 | 原件保留，安全功能融合；实际提供评论解析/计数/骨架脚本，语气/模板复用Nature Response |
| Veritas | peer-review | 3文件方法学与规范检查库 | 内置全部，移除默认AI示意图与不存在的scientific-slides脚本依赖 |
| Veritas | reproducibility-checklist | 单文件 | 内置，追加适用性，不把检查表强制变成重分析 |
| Veritas | nature-writing / nature-polishing | 内容重写、语言修改时条件使用 | 由其他构建分支内置，共用相对路径 |
| Veritas | docx/pdf/pptx/图表工具 | 原目录有广泛工具名，并非必须串联 | 复用包内paper-documents、paper-pdf、paper-research-artifacts，避免机器本地依赖 |
| Calder | code-review-academic | 单文件，完整13步骤与七类报告覆盖 | 内置，去掉“至少指出一个风险”的问题配额 |
| code-review-academic | 6个ReproFlow技能及5个引用参考 | 6个技能目录共11文件，均存在 | 完整内置为 references/reproflow 下审计资料；保留相互参考，不把建模/训练自动纳入审稿 |

本分支共采用10个运行技能目录，并完整保存6个ReproFlow规范来源目录。源目录总计101个有效文件，来源快照位于包内 `sources/local-installed/`；ReproFlow活动资料中将入口改为 `audit-source.md`，不作为独立技能路由注册。头像、模板、原测试等原始资源一并复制；未复制 `.nrs_root`、缓存或环境机密文件。

### 推荐工具箱不是实际全量运行闭包

Aequitas §6 声称“222 skill按需调用”，实际上混列了明确技能名、通配符、旧别名及多个与论文审稿不直接相关的领域工具。逐项候选名称和本机存在情况在JSON的 `original_toolbox_catalog` 中记录。

这里不能将一个 `bio-atac-seq-*` 通配符误当成已定义且已执行的依赖，也不能只复制Aequitas而保留向外调用数百技能的隐形依赖。按用户明确允许的功能融合，本包移除该大目录作为可执行路由，把实际审稿所需方法检查归并到peer-review、nature-reviewer、代码审计、可复现性及文献分支。图表重制、文档、写作依赖指向已有内置能力。

药物筛选、数据库全量分析、UKB字段再提取、全组学分析、临床决策系统等仅推荐生态能力不作为论文审稿运行依赖采用，也未声称全部内置其分析引擎。后续若用户明确要实施新的分析，按当前研究计划、真实输入和已有内置执行能力判断，不凭旧工具箱自动开算。

## 2. 本机NRS工程缺失与真实补足

两份本机 `.nrs_root` 均指向 `K:/UKB文章/AI选刊/nature-review-studio`，该目录不存在。检查了其父目录，并在当前工作区、Codex workspace、WorkBuddy中搜索 `render_review_docx*.py` 等指定文件，没有找到原渲染器。安装技能自身只含SKILL、README和6个references。未发现随技能提供的cases.jsonl、case graph、top-k索引或更新管线。

原source-basis混有“50个样本已内置”“全1287已完成”“全1287尚不在范围”三种版本说明，不能作为现状证据。原response-axes标题声称21项，但表格实际20项；本包按20项保留，不编造第21项。

新增工具均位于 `skills/nature-review-studio/scripts/`：

- `render_review_docx.py`：从可核查JSON形成内容同步的DOCX/MD，支持review/respond；检查意见ID、定位、解决标准、Minor非阻塞、汇总对应ID及8列任务行。DONE/VERIFIED_DONE要求实际文件中的摘录匹配。保留公共PMID/DOI等证据标识。不覆盖已有输出。
- `ingest_prf.py`：提取用户明确提供的PDF/DOCX/TXT/MD，保留页/块/表定位，输出 `source_extracted_not_distilled` 状态。供agent逐条阅读和形成任务内经验草稿。它不是旧NRS知识图谱，也不自动匿名化、训练模型、更新全局记忆或发布。

render脚本只检查结构与摘录存在，不判断科学合理性、未读全文或实验真实性；内容审查仍由审稿角色完成。完成态摘录存在也不能单独证明它足以关闭意见。

## 3. 重要规则冲突与修正

| 原问题 | 融合后规则 |
| --- | --- |
| 原Aequitas把NRS硬约束置于用户之上 | 宿主/用户当前请求与共享规则优先，文件格式默认不反向阻断用户 |
| Aequitas禁止自动交给Veritas | 单次审稿保持单次；明确开启循环后主调度可直接交接，已获得授权不再重问 |
| Aequitas强制重叠率<35%，有一处把单审稿人发现从最终文件删除 | 独立报告完成后才比较；自然重复保留，重要单人发现保留，不为制造多样性改审稿内容 |
| 多视角混同独立多agent | 普通任务可标明虚拟多视角；要求独立时用真实隔离上下文；循环实际启动审稿与返修子agent，单子任务不递归扩为3人 |
| Nature Response默认真实决定必问 | 正式返修沿用真实决定，模拟循环明确simulation，不虚构决定也不等待不存在的编辑信 |
| 缺审稿意见自动模拟后当正式回应 | 只有明确模拟/循环任务可模拟；正式意见缺失不得编造 |
| 原NRS一律删除DOI、NCT、accession甚至不常见缩写 | 保留公开证据定位符，只按实际匿名化/隐私要求处理身份 |
| 原模板固定5审稿人/不得删改章节 | 实际模板只有2名示例审稿人、7评论块和11张表，原模板也明确可复制评论、删除可选块；按真实人数/评论适配 |
| 句库、待办和使用清单都必须送编辑 | 五字段完整逻辑保留，作者内部句库/清单移至内部，正式稿无虚假“已全部完成” |
| 原rebuttal示例默认已补统计、固定日期、全部修好、按语气推荐申诉 | 仅归档为历史示例；采用真实完成证据、实际截止日和独立申诉任务，不运行该启发式决策器 |
| 原peer-review每报告默认生成AI示意图 | 仅实际需要且任务授权时调用包内图表能力 |
| 原幻灯片指向不存在的scientific-slides脚本且禁止文本读取 | 复用包内PDF渲染工具，真实查看图像；文本可辅助，不能替代视觉检查 |
| 一些统计经验写成硬阈值或建议observed power | 提醒按设计解释；改为报告精度，不以事后观察功效替代证据；不为清单自动改分析方案 |
| 原Calder“至少指出最高风险” | 无问题时明确通过，不造发现；审稿不自动修改代码/训练 |

## 4. 复制许可与外部运行条件

- Aequitas、Veritas、Calder的元数据为从用户已有LobsterAI/WorkBuddy迁移，目录未见单独LICENSE；Nature系列目录也未见限制性复制许可文件。保留原来源和原元数据，在本次用户明确要求的个人整合包中复制，不宣称获得新的公开再分发权。
- rebuttal-writing frontmatter明确标注MIT、awesome-rosetta-skills contributors；保留其原始声明与示例。`re>=3.11`、`pathlib>=3.11`是原迁移元数据对标准库的误表述，不作为安装依赖。
- 没有复制其他工具的受限许可证实现。Word/PDF/PPT能力复用已有自建paper-documents/paper-pdf/paper-research-artifacts；Python公共库、Office/TeX和宿主子agent/联网工具仍为条件运行环境。
- 不打包用户研究数据，不复制旧NRS项目、原始1287篇PRF文件或任何API凭据。不在本机全局安装或改写agent。

## 5. 实际验证

本轮新增工具13个实际CLI情境全部通过：review同步导出；重复输出拒绝且旧文件不变；重复ID拒绝；Minor阻塞拒绝；未知汇总ID拒绝；缺证据的VERIFIED_DONE拒绝；真实摘录对应的完成回复成功；虚假摘录拒绝；TODO_ANALYSIS可明确未完成导出；评论分割保留0.82/0.92小数并准确解析3条评论；Word提取；2页PDF提取；提取输出覆盖拒绝。

Nature Response原有LaTeX一致性脚本7项行为测试通过，包括真实引用匹配、引用不符、评论/回复数不符、净稿标改稿漂移、静态include展开、显式引用替换、删除标记处理。测试临时目录显式设在本项目validation下。

证据：`upgrade-v1.1/validation/review-revision/results.json` 与 `nature-response-unittest.txt`。DOCX已读回核对内容及公共PMID保留；未进行页面渲染，因此没有声称Word版面已验证。脚本行为测试不等于真实科学审稿性能评估，主循环情境验证由总构建任务另行完成。

## 6. 文件衔接

运行入口全部使用包内相对路径。原文件快照仅用于追踪，不作为活动调用资源。标准SKILL frontmatter只保留name/description；历史其他字段和本机安装来源在归档中留存。当前包活动代码/引用不存在对旧NRS_ROOT或WorkBuddy运行目录的需求。

最终本分支10个SKILL的YAML元数据及所有复制/新增Python源码已实际解析通过。再次检查活动SKILL、agent、references和manifest，未保留nature-ref-verifier、scientific-writing、statistical-analysis、旧文献工具箱或WorkBuddy的未内置调用；共享nature-shared路径和转交nature-response路径已改为可解析的包内相对路径。代码审计中出现的用户项目脚本名和硬编码路径反例是待审代码示例，不是包内运行依赖。

构建脚本：`upgrade-v1.1/scripts/build_review_revision.py`。该脚本按本轮新版本目录执行一次以保留旧包，拒绝重建已有来源目录；后续局部修订应在当前新版本工作稿继续，不用旧脚本覆盖人工确认成品。
