# 本机文献能力、真实依赖与内置适配审读

审读日期：2026-09-11。任务：为论文写作综合 agent 的审稿、返修和创新性查新内置本机能力，消除本机其他 skill 文件夹的运行依赖。

本报告区分“逐文件清点”“入口及关键资源审读”“完整脚本功能审读”“实际运行验证”。清点并留存59个来源文件，不声称59个文件全部逐行精读；大型下载器与40MB期刊数据分别采用关键执行路径审读及查询验证。没有修改本机原技能，没有读取、打印或复制用户凭据、浏览器 profile、`.env` 或 `config.local.toml`。逐文件路径、大小和归档位置见同目录 `literature-dependencies.json`。

## 1. 根技能与范围

| 来源技能/agent | 有效文件数 | 来源大小 | 审读重点 | 活动包处理 |
| --- | ---: | ---: | --- | --- |
| litorchestrator | 6 | 2,206,130 B | SKILL、完整agent角色正文、plugin元数据与附件结构 | 内置6文件；重写角色及入口的本机路径和调度依赖 |
| literature-workflow-orchestrator | 2 | 31,568 B | 完整SKILL及旧agent设置的重复/依赖关系 | 保留原档案，活动流程重写为实际包内路由 |
| pubmed-database | 4 | 45,640 B | 完整入口、API、检索语法与常用查询参考 | 内置；追加独立执行器说明，修正API key与全文搜索错误 |
| academic-literature-search | 1 | 16,587 B | 完整入口、MCP路由、arXiv与引用代码 | 内置；MCP变为条件调用、格式服从用户、失效引用不静默删除 |
| nature-reader | 20 | 67,980 B | 入口、manifest、static核心/5来源分支、输出规范、锚定、图表、公式脚本CLI及自测 | 整目录内置；PDF/HTML依赖改为包内分支 |
| ref-downloader | 8 | 297,598 B | 完整SKILL、runbook关键流程、配置schema、导入/路径/浏览器及清理执行路径 | 整目录内置；保留条件运行和真实环境边界 |
| journal-if-lookup | 6 | 40,351,899 B | 完整入口、query接口/路径、build_index来源路径，实际历史索引查询 | 连原XLSX/JSON内置；历史来源和使用边界明确 |
| pubmed-search | 1 | 3,912 B | 完整入口 | 功能融合进pubmed-database；原文件存档，不重复激活 |
| pubmed-database-2 | 10 | 65,661 B | 完整入口、8份API参考、pubmed_api.py主要完整函数与CLI | 知识融合，失效脚本链存档，不作为运行入口 |
| uv | 1 | 1,989 B | 完整入口 | 原依赖被移除；仅来源审计留存，不自动安装 |

新增 `paper-novelty-assessment` 分支及比较模板，新增独立标准库脚本 `scripts/pubmed_evidence.py`。本组实际提供7个既有技能入口+1个新入口。`nature-shared` 由另一协作者统一内置，避免复制同一依赖后漂移。

## 2. 真实依赖关系及闭包处理

原 `litorchestrator` 明确读取 `literature-workflow-orchestrator`，并调度 PubMed、全文下载、nature-reader和journal-if-lookup。原文还硬编码WorkBuddy/LobsterAI目录、桌面工作目录、指定模型和固定收费档位，这些均不是研究功能，活动版已删除，原件留存。

原文献流程列了40余种数据库、科研分析、导出和设计生态名字，包含“可以安装”的扩展建议以及若干不存在的专用工具路径。不能把这类清单全部当必要依赖。活动版将已经采用的检索、元数据、筛选、阅读、写作与导出步骤明确映射到包内：

```text
litorchestrator
└─ literature-workflow-orchestrator
   ├─ pubmed-database → scripts/pubmed_evidence.py（stdlib）
   ├─ academic-literature-search → 可用宿主官方检索 / 包内PubMed
   ├─ paper-novelty-assessment → 上述检索 + 按需nature-reader
   ├─ nature-reader → nature-shared/core/terminology-ledger.md
   │                  → paper-pdf / paper-research-artifacts
   ├─ ref-downloader → 本目录5个Python脚本与config.example.toml
   │                  → 条件Python库、浏览器及用户合法访问
   ├─ journal-if-lookup → 本目录query.py、build_index.py、原始XLSX/JSON
   └─ 已有paper-literature-reading / paper-documents /
      paper-pdf / paper-research-artifacts / paper-reviewer-response
```

没有复制本机完整科研生态来满足未使用的推荐菜单。未采用的推荐项从活动调度声明移除；其需要的写作或导出能力由本包既有分支覆盖。Nature共享层README的“由谁使用”也不是反向调用这些技能的授权。

## 3. PubMed实现发现与修正

原 `pubmed-search` 固定设置第三方邮箱，依赖BioPython，摘要在300字符处截断。活动版移除固定身份与截断，保留简易检索用途。

原 `pubmed-database-2` 的PEP723元数据依赖 `science-skills-common`，路径为 `../../science_skills_common`，导入 `science_skills.science_skills_common.http_client`；该需要的本地库不在技能目录，也未在候选路径找到。它还要求uv及home `.env`，因此原样复制不能声称独立。脚本只返回搜索PMID列表，丢失总命中数和query translation；title用findtext会丢内嵌XML后半内容；DOI未回退PubmedData/ArticleIdList；近邻只保留第一个linkset，不能用于可追溯的多种子创新性比较。

API参考还出现若干需要纠正的断言：移除字段限制不等于搜索PubMed全文；PMC链接存在不保证BioC OA全文可用；某个论文年龄不能保证已建立所有数据库链接；接口失败不等于论文不存在或全文不开放；引用匹配文档示例有字段数量/位置不一致。上述知识采用事实保留和边界修正方式融合，不复用错误运行链。

新脚本使用标准库urllib/XML/JSON，提供：

- ESearch保存实际query、query translation、总命中、取回窗口、PMID及截断状态。
- EFetch批量提取完整结构化摘要、内嵌XML正文、PMID/DOI/PMCID、作者、期刊、日期、发表类型及更正/撤稿关联。
- ELink `neighbor_score`逐种子取回并保存归属、排除种子自身、保留真实相似分与截断标记。
- `ok/no_hits/no_links/partial/error`不同状态；失败不会归为无相关文献。缺失摘要或记录不据此断言论文不存在。
- 至少0.4秒请求间隔、30秒单次超时、有限重试；无API key也工作。仅使用可选NCBI_API_KEY和专用途NCBI_EMAIL，不打印或复制凭据。
- 所有输出显式指定在任务目录，拒绝安装目录和已有文件路径，不自动装包或写home `.env`。

旧版其他通用E-utilities知识仍在pubmed-database API参考中按任务可用；本次自动化脚本明确只实现search/fetch/related，不声称原10函数原封不动全部已经运行验证。

## 4. 检索与创新性规则

本次创新性分支包含：拆解作者真实贡献、宽窄检索、同义词/旧词与MeSH、近期和先行文献、已验证种子近邻、逐篇比较相同点与具体增量、摘要/全文阅读级别、检索失败与截断、结果对审稿及返修的传递。

不按相似分计算创新性分数；不因为没有发现相同标题就宣称首次；不把换数据/人群/模型自动视为突破；不默认只看近三年、高IF或免费全文；不把PubMed检索说成全学科穷尽。相近文献更少时如实返回，不强凑数量或批评。实验未完成不得为解决创新性意见而编造完成状态。循环只在主张改变或已有检索存在实质缺口时补检索，不每轮机械重复。

原academic-literature-search强制使用特定MCP、固定GB/T 7714和全刊名，活动版改为先检查宿主、无MCP时走内置脚本、按用户/目标期刊格式。保留源代码引用管理能力，但无效引用标记变成显式错误，不能偷偷删除；跨DOI/PMID/题名去重必须核对，不声称简单首选键函数处理所有混合情况。PubMed对bioRxiv/medRxiv覆盖不完整已声明。

## 5. 文件、环境和权利边界

- 文献agent、PubMed参考、引用代码多数未附独立许可证；仅在用户要求下复制其本机已有材料，不附加新的开源或公众再分发许可。
- 原pubmed_api.py带Google Apache-2.0头，原文件头随来源档案保留；其代码未成为新stdlib执行器的导入依赖。
- `journal-if-lookup`原索引标注JCR 2025/Clarivate；将原数据作为用户已有材料的个人离线副本内置，不声称取得公开再分发权，不将2025源标注成2026实时指标。当前回读必须区分记录jcr_year、源字段和当前年份。该查询不用于评判单篇研究创新性。
- `nature-reader`的PDF、浏览器预览外部skill依赖分别由已内置paper-pdf、paper-research-artifacts替代。共享术语文件随nature-shared内置。公式源码、page/block锚点、图表裁剪与缺失说明规则保留。
- `ref-downloader`只携带脚本、模板与runbook；没有个人配置或cookie。Playwright/PyMuPDF、浏览器、机构SSO、可选CloakBrowser是实际运行依赖，不是技能文件缺失。不能自动装库、强杀Edge、读写个人profile或复制凭据；任务目录通过显式output/profile/tmp设置。源脚本中的有限清理和报告覆盖只允许在本次新建下载目录，不能对用户原件目录执行。没有在此次构建中启动浏览器下载。
- PubMed摘要可能受原作者/出版方版权约束。执行说明保留NCBI免责声明与版权入口，联网测试只验证公共API，不上传稿件。

## 6. 实际验证

证据：`upgrade-v1.1/validation/literature/validation-summary.json`，离线用例见 `scripts/test_pubmed_evidence.py`。

1. 新PubMed脚本14项离线测试通过：内嵌标题和结构化摘要、DOI/日期/更正字段、摘要缺失、真实零命中、query translation、截断、语法错误、网络错误、部分取回、多种子映射相关解析、无近邻、PMID校验及禁止写安装目录。
2. 实际联网查询 `CRISPR[Title/Abstract]`取回3篇完整摘要及DOI，记录总命中64,815且标记结果截断。检索时间2026-09-11，数字只作运行证据，不作科研判断。
3. 从真实返回结果选PMID 25315507为种子，接口返回740条近邻（已排除种子自身），选择并取回3篇摘要，PMID 25728500、24651067、25827103，保留各自NCBI相似分和seed归属。
4. 首次联网测试发现search忘记显式JSON解析模式；其错误被正确记录为error并保留总数null。修复参数并补入离线断言后，以上真实检索及近邻通过。初始失败结果保留供追溯。
5. nature-reader原公式验证器内置自测通过；临时目录显式位于本项目validation目录。该测试不等于真实论文视觉验收。
6. journal-if-lookup使用包内副本实际查询Nature成功；结果仅为内置历史数据，不称实时JCR核验。
7. ref-downloader wrapper `--help`正常运行，无本机其他skill导入；尚未执行真实机构登录、浏览器PDF下载或逐出版社全链验证。

包内路径最终检查和整包安装验证由主构建统一执行。上游不存在的README/CONTRIBUTING等跨仓库链接已从活动runbook改为非运行参考，示例输出assets路径仍是示例，不是安装时必须存在的资源。
