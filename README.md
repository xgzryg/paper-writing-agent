# Paper Writing Agent

An academic writing agent for literature research, manuscript drafting, polishing, peer review, revision, and submission preparation. Automatically routes tasks to bundled skills and supports configurable review–revision loops with separate subagents, plus PubMed-based novelty assessment.

一个覆盖文献研究、论文写作、学术润色、审稿、返修与投稿准备的综合科研写作助手。根据任务自动调用内置技能，支持由独立子 agent 执行的审稿—返修循环，可配置轮数与完成目标，并结合 PubMed 近似文献检索评估研究创新性。

## 下载与安装 / Download and Install

**当前版本 / Current version: v1.1.1**

- [下载独立安装包 / Download the standalone ZIP](https://github.com/xgzryg/paper-writing-agent/raw/refs/heads/main/downloads/paper-writing-agent-v1.1.1.zip)
- [下载 HTML 用户使用说明书 / Download the HTML user guide](https://github.com/xgzryg/paper-writing-agent/raw/refs/heads/main/论文写作综合agent_用户使用说明书.html)
- [查看安装说明 / Installation instructions](paper-writing-agent/INSTALL.md)

解压独立安装包，将整个 `paper-writing-agent` 文件夹放入宿主的 skills 目录。保留文件夹内的层级，按宿主方式刷新技能或开启新任务，然后输入 `$paper-writing-agent` 并说明任务。包内包含 47 个直接功能分支和 2 个嵌套辅助技能，无需另行安装这些 agent 或 skill。

Extract the standalone ZIP and place the complete `paper-writing-agent` folder in your host's skills directory. Keep its internal structure, refresh skill discovery or start a new task as required by your host, then invoke `$paper-writing-agent` with your task. The package bundles 47 direct branches and 2 nested supporting skills.

若使用 GitHub 的 **Code → Download ZIP**，请进入仓库压缩包，再找到其中的 `paper-writing-agent` 文件夹；仓库根目录本身不是 skill 的安装目录。

When using GitHub's **Code → Download ZIP**, locate the `paper-writing-agent` folder inside the downloaded repository. That folder is the installable skill.

## 主要功能

1. **选题与研究设计**  
   梳理研究主题、寻找可验证的问题，结合已有数据和资源提出选题，规划研究方案、统计思路及论文图表。

2. **文献检索与精读**  
   检索 PubMed 等可用数据库，核验引用，获取可访问全文，逐图逐表解读论文，整理证据表和综述框架。

3. **创新性评估**  
   查找近似文献，逐篇比较研究问题、对象、方法与发现，判断本研究实际增加了什么，并帮助准确表述贡献。

4. **论文写作与语言处理**  
   撰写前言、方法、结果、图注、讨论、标题、摘要、结论和 Highlights；支持中译英、学术润色、期刊风格调整、篇幅压缩和指定片段改写。

5. **多视角审稿与质量核查**  
   从研究设计、统计报告、创新性、图表、引用和论证强度等方面找出实质问题；提供代码时，也可按指定范围检查实现与可复现性。

6. **返修与逐条回复**  
   根据审稿意见修改实际工作稿，同步核对正文、图表与回复信，逐条说明修改内容、证据和位置，区分已完成工作与待补事项。

7. **自动审稿—返修循环**  
   开启后，由不同的真实子 agent 分别审稿和返修。你可以设置最大轮数、完成目标、是否加入创新性评估、是否逐轮确认；每次返修后再审，达到目标或轮数上限后结束。

8. **投稿准备与成果交付**  
   支持选刊、期刊信息核查、Cover Letter、返修文件包、Proof 校样检查，以及 Word、PDF、HTML、表格、图形摘要和汇报材料制作。

## 用户使用说明 / User Guide

[下载 HTML 用户使用说明书](https://github.com/xgzryg/paper-writing-agent/raw/refs/heads/main/论文写作综合agent_用户使用说明书.html)，保存后用浏览器打开。说明书包含安装方法、全部功能、调用示例、自动写作流程和审稿—返修循环设置，支持离线阅读、功能搜索与指令复制。

Download the [HTML user guide](https://github.com/xgzryg/paper-writing-agent/raw/refs/heads/main/论文写作综合agent_用户使用说明书.html) and open it in a browser. It covers installation, available functions, task prompts, writing workflows, and review–revision loops. The guide is currently in Chinese and works offline.

## 调用示例 / Example

```text
请使用 $paper-writing-agent，开启审稿—返修循环，最多3轮，
并加入PubMed创新性评估。审稿和返修使用不同的真实子agent，
保留既定统计结果，只修改工作副本。
目标是解决范围内重大问题，使创新主张与证据一致，并完成最终稿再审。
```

实际执行需要宿主提供相应模型、文件工具、网络和真实子 agent 能力。最多 3 轮指最多 3 次返修及其再审，加上基线审稿，最多共 4 次审稿。

Execution requires the relevant model host, file tools, network access, and real subagent support. A limit of 3 rounds means up to 3 revisions, each followed by another review, plus the initial review: at most 4 reviews in total.

## 运行条件 / Runtime Requirements

本包是可移植的 agent 与 skill 指令、脚本及资源集合。模型服务、Python 与公共库、联网检索、文档渲染和真实子 agent 工具由宿主提供，按任务需要使用。公共 Python 库见 [requirements.txt](paper-writing-agent/requirements.txt)。

期刊指标查询支持用户提供有权使用的历史数据文件，或由宿主联网核验。公开包不附带商业期刊指标数据库；结果必须注明数据年份和实际查证范围。

This portable bundle contains agent and skill instructions, scripts, and supporting resources. Your host supplies model access, Python and relevant libraries, network access, document rendering, and real subagent tools as needed. Journal metrics can be checked against a user-supplied dataset or verified online; commercial journal-metrics datasets are not bundled.

保留各组件自带的许可证与署名；这些组件仍适用各自的许可条件。

Bundled components retain their respective license notices and attribution.
