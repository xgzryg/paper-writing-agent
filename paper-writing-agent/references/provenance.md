# 来源与改编说明

本包依据用户提供的 8 个 skill ZIP、18 篇专题提示词 PDF、1 份 Codex 科研指南整合。19 份 PDF 共 117 页；8 包包含 33 个有效源文件、1 个嵌套ZIP和10个系统/编译缓存条目。

原作者“迪娜学姐”的署名与材料归属保留。`sources/original/` 保存用户提供原件，`sources/pdf-text/` 保存带页码的提取文本；文本存在字形/版式损失时以PDF原页为准。全部源码学习清单在 `documentation/01_全文件扫描清单.md`，内容审读见 02–05 号报告，整合决定见 06，构建提示词见 07。

原8技能的有效资源内置于 `skills/`，必要适配见 [source-skill-adaptations.md](source-skill-adaptations.md)。其他11个写作功能和4个支撑技能由本次根据经验独立整合实现。新Word/PDF技能及工具未复制本机第三方文档技能。构建阶段使用的Research-Assistant和skill-creator不是成品运行依赖。

源材料中的旧提示词、推广、示例姓名、模型偏好、版权声明和历史快照仍是来源材料，不自动取得执行优先级。源包内系统缓存不进入实际技能目录；原ZIP作为来源保留其原貌。没有把来源改标为开源，也不声称个人整合赋予额外公开传播或商业再授权。

独立性指一个文件夹包含全部agent/skill资源；Python库、模型、联网/Office/宿主服务见 [dependencies.md](dependencies.md)。没有依赖其他本地agent/skill目录或创建盘符映射。

## v1.1 本机来源融合

本轮按用户要求内置 Aequitas、Veritas 及其实际审稿/返修/文献依赖，补充 Nature 写作、润色、共享统计指导和中文学术文风融合。详细来源目录、逐文件清点、选择与适配见 `documentation/v1.1/`。开发目录保留逐文件来源副本；最终安装ZIP将这些副本收入 `sources/local-installed.zip`、`sources/local-literature.zip`，原来的相对目录结构保存在归档内；Nature/Wordpolish原貌在 `sources/local-upgrade/nature-wordpolish-original.zip`。它们用于追溯，不是当前执行入口，旧SKILL入口不散装进安装目录。

新双子agent循环与PubMed证据工具依据本轮创建提示词实现。Aequitas和文献agent的数百项推荐生态未被当成全量执行依赖；需要的审稿、写作、阅读和导出能力已映射到包内实际文件。缺失的旧NRS工程和1287案例库未被虚构为已复制；本包提供现有聚合经验和实际可运行的新报告工具。

原作者、许可和历史数据年份保留；个人整合不授予新的公开再分发或商业使用权。本机角色安装和v1.0.0压缩包保持不变。
