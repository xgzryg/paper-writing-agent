# 7_Discussion撰写提示词2.0-迪娜学姐.pdf

## PDF page 1

《迪娜学姐 AI 辅助学术写作系列课程》版权与保密声明 
 
本课程内容，是“迪娜学姐”公众号创始人基于其多年的 SCI 期刊编辑经验，深度融合 AI 技术与学
术写作方法，精心打磨的原创知识成果。 
 
为了保护原创者，维护所有付费学员的共同利益，营造一个健康、有序的学习环境，特此声明如下： 
 
一、 版权归属 
本课程（包含但不限于所有视频、音频、课件 PPT、文字稿件、案例分析、数据集、独家提示词设计  及
所有随附资料）的全部知识产权（包括但不限于著作权、商标权等）均归“迪娜学姐”及其创始人（以下
简称“版权方”）所有，受《中华人民共和国著作权法》及相关法律法规的严格保护。 
 
二、 授权范围 
您购买课程后所获得的，是“仅限您个人学习使用”的、不可转让的”授权许可。 
 
三、 严禁行为 
未经版权方书面明示许可，任何个人或组织（包括但不限于所有付费学员）不得进行以下任何形式的侵权
行为： 
1. 复制与录制： 对课程内容进行任何形式的录屏、录音、截图、拍照、抄袭。 
2. 传播与分享： 将课程资料（全部或部分）通过任何渠道分享、传播、转借或转赠给任何第三方。  
3. 商业使用： 以任何形式对课程内容进行二次销售、转卖，或用于任何其他商业目的（如开设雷
同课程、进行付费咨询等） 。 
 
四、 侵权后果 
版权方已启用课程保护系统。 
对于任何形式的传播、分享或转卖行为，系统后台均有记录。一旦发现，无论情节轻重，版权方将立即采
取包括但不限于以下措施，且无需承担任何责任： 
1. 立即终止侵权方所有课程的观看权限及一切后续服务（包括更新） ，且不予退款。 
2. 公示侵权方的学员标识及侵权事实。 
3. 依法追究侵权方的法律责任，包括但不限于要求赔偿版权方的全部经济损失、维权成本等。 

## PDF page 2

论文讨论 Discussion 撰写提示词 2.0 
By 迪娜学姐 ©版权所有 
 
和写前言的思路一样，分三步完成。 
1 先定框架； 
2 利用 deep research完成文献调研（这一步 AI 不能一步到位，需要自己再补充一些文献支
撑，或者综合几个 AI 的结果，才能更详实。娜姐的建议： 
OpenAI deep research 写的初稿结构最符合 Discussion 结构要求，但是文献支撑太少。可
以用它的文献调研做初稿，自己进一步补充文献，或者把 Gemini/Claude 的相关段落中的
论据补充进来。放在对应段落即可，第三步 Claude 会帮你理顺和衔接句子。） 
3 把第二步的初稿交给 Claude，让它根据提示词指示，按要求撰写 Discussion 部分。 
 
 
1 Discussion 讨论部分框架拟定提示词 
 
你是一位[免疫学]领域的资深教授，发表过 100 篇 top 期刊论文，有丰富的学术论文撰写经
验。以下是我即将投稿到 Frontiers in Immunology 期刊的论文标题、摘要、前言和结果部
分，然后帮我拟定 Discussion 部分的框架。 
 
请你先仔细阅读我给出的资料，然后给我三种本论文 Discussion 部分的框架方案，并说明
理由。 
 
# Inputs 
<Title> 
{{你的论文标题 IFNλ1 is a STING-dependent mediator of DNA damage and induces immune 
activation in lung cancer}} 
</Title> 
 
<Abstract> 
{{你的论文摘要 Introduction: The importance of the cGAS-STING pathway and type I….}} 
</Abstract> 
 
<Introduction> 
One of the hallmarks of activating the innate immune system is the production of interferons 
(IFNs) and inflammatory cytokines. The role of IFNs in cancer and how they support anti -
tumor responses can be dated back to 1969, where it for the first time was shown to eradicate 
tumors in mice (1). Sixteen years later, type I IFN alpha was approved as the first type of 
immunotherapy to treat cancer though the mechanism of action was not clear. The diverse 
biological effects and high degree of toxicity did, however, rapidly limit the use of type I IFNs 

## PDF page 3

in clinical practice……. 
</Introduction> 
 
<Results> 
3.1. IFNλ is a broad marker of STING activation in NSCLC  
As STING protein expression is a prerequisite for pathway activity ( Figure 1A ), we conducted 
an initial screening of STING expression in 11 different NSCLC cell lines. This revealed that 
approximately half of the cell lines did not express STING while th e cell lines HCC827, 
H358, …… 
</Results> 
 
# output format 
<example> 
1 cGAS-STING 通路在抗肿瘤免疫中的核心地位（200 字）  
文献检索关键词：cGAS-STING pathway, tumor immunity, DNA damage response, innate 
immunity cancer; 
内容：阐述 cGAS-STING 作为胞质 DNA 感知通路的基本机制，其在肿瘤免疫监视中的关键
作用。 
2 I 型与 III 型干扰素的差异化功能（250 字） 
文献检索关键词： type I interferon, type III interferon, IFN -lambda, epithelial immunity, 
antiviral response； 
内容：对比 I 型和 III 型 IFN 的表达模式、受体分布和生物学功能，强调 III 型 IFN 的组织特
异性。 
...... 
</example> 
 
# Requirements 
1 详略得当，整个框架的目的是通过与以往文献结论的全面深入的对比讨论，突出我的研
究的重要性； 
2 Discussion 部分总计 1500 字，请务必仔细思考，详略得当，然后列出每一部分合理的字
数规划； 
3 列出每个主题的文献综述检索关键词，以便我能在 web of science、pubmed 等数据库中
精准找到相关文献，与本文结果进行比较和讨论。 
 
请一步一步思考。 
 
说明： 
1 模型：Claude opus 4.1 thinking  
 （如果是 Claude 官网使用，打开对话框下方的 extended thinking；如果是其他平台 poe，
选择 thinking 模式；如果是 openrouters，对话框打开 reasoning）； 
2 标黄部分换成你自己的内容即可。 
 
 
 

## PDF page 4

2 文献综述调研提示词 
 
请按照如下框架，帮我进行系统、深入、批判性的学术论文文献综述。该文献综述将用于
指导我撰写我论文的 Discussion 部分，投稿到 Frontiers in Immunology。 
 
**内容要求** 
- 优先引用近五年发表在 top 学术期刊的文献。 
- 按照我给出的框架逐段展开，不要偏离。 
- 字数目标：2000 字左右。 
 
**写作风格** 
- 深入、客观、正式的学术风格 
 
# Inputs 
<Title> 
{{你的论文标题 IFNλ1 is a STING-dependent mediator of DNA damage and induces immune 
activation in lung cancer}} 
</Title> 
 
<Abstract> 
{{你的论文摘要 Introduction: The importance of the cGAS -STING pathway and type I 
interferon (IFN) in anti-tumor immunity has been widely studied. However, there is limited …}} 
</Abstract> 
 
<Introduction> 
你的前言部分内容。请注意，如果是用 OpenAI deep research，可以把前言和结果部分加
上，它在写文献综述时，会更好的理解你的内容，并引用结果部分结论；如果是 Gemini 和
Claude 的 deep research，把你的原文的 Introduction 和 Results 部分删去，太多内容对于这
两个深度研究工具是一种干扰，只需要框架指引就行了。 
One of the hallmarks of activating the innate immune system is the production of interferons 
(IFNs) and inflammatory cytokines. The role of IFNs in cancer and how they support anti-…… 
</Introduction> 
 
<Results> 
你的结果部分 3.1. IFNλ is a broad marker of STING activation in NSCLC As STING protein 
expression is a prerequisite for pathway activity ( Figure 1A ), we conducted an initial 
screening …… 
</Results> 
 
<framework> 
(上一步 AI 帮你生成的框架。删去字数约束。 
1. IFNλ 作为 STING 通路新型标志物的生物学意义 
文献检索关键词： STING biomarker, IFN-lambda cancer, type III interferon tumor immunity, 

## PDF page 5

epithelial cancer interferon, STING pathway markers NSCLC  
内容： 深入讨论为何 IFNλ 比 IFNβ 在上皮源性肿瘤中更适合作为 STING 激活标志物，对比
文献中其他 STING 标志物(CXCL10, CCL5 等)的局限性，强调本研究发现的普适性。 
…… 
5. 研究局限性与未来方向 
内容： 承认体外实验局限性，提出体内验证、TME 研究、临床样本验证等未来方向。 
</framework> 
 
# Requirements  
- 严格区分本研究结论和你查找的外部文献结论，不要混淆。 
- Query type determination: This is a depth-first query (Claude research 加这句，其他两
个可不加) 
 
 
说明： 
1 这一步用各大模型的 deep research 完成，Claude，Gemini，OpenAI 都可以。可以同时
使用，综合成一份更完整的综述。正如前面娜姐的建议： 
OpenAI deep research 写的初稿结构最符合 Discussion 结构要求，但是文献支撑太少。可
以用它的文献调研做初稿，自己进一步补充文献，或者把 Gemini/Claude 的相关段落中的
论据补充进来。放在对应段落即可，第三步 Claude 会帮你理顺和衔接句子。 
2 字数部分，可以是你的讨论部分字数的 2-3 倍，以便综述更全面。 
3 标黄部分换成你自己的内容。 

## PDF page 6

3 讨论 Discussion 全文撰写提示词 
 
# Role 
I am an expert in Immunology with a profound academic background in Immunology and I'm 
familiar with the professional concepts and terminology in this field. I also have extensive 
experience in writing academic papers, particularly for the 'Frontiers in Immunology' journal. 
 
## Attention 
Based on the background info (title, abstract, introduction, results，framework of discussion， 
and draft of literature review), create a strong Discussion for my article which will be submitted 
to the journal ' Frontiers in Immunology', emphasizing the significance and contributions of 
the research. 
 
## Goals 
Compose an Introduction that meets the quality standards of 'Frontiers in Immunology' based 
on the draft literature review and framework of the Discussion section. 
 
## Background 
<Title>  
{{你的论文标题 IFNλ1 is a STING-dependent mediator of DNA damage and induces immune 
activation in lung cancer}}  
</Title>  
 
<Abstract>  
{{你的论文摘要 Abstract Introduction: The importance of the cGAS-STING pathway and type 
I interferon (IFN) in anti -tumor immunity has been widely studied. However, there is 
limited ……}}  
</Abstract> 
 
<Introduction> 
你的论文前言 One of the hallmarks of activating the innate immune system is the production 
of interferons (IFNs) and inflammatory cytokines. The role of IFNs in cancer and how they …… 
</Introduction> 
 
<Results> 
你的论文结果部分 
3.1. IFNλ is a broad marker of STING activation in NSCLC As STING protein expression is a 
prerequisite for pathway activity ( Figure 1A ), we conducted an initial screening of STING 
expression in 11 different NSCLC cell lines. This revealed that approximately half of the cell …… 
</Results> 
 
<framework>  
第一步的框架，6 是额外加的 Conclusion 部分 

## PDF page 7

1. IFNλ 作为 STING 通路新型效应分子的发现意义（350 字） 
2. IFNLR1 下调作为肿瘤免疫逃逸新机制（300 字） 
3. 化疗诱导内源性 IFNλ 的治疗学意义（300 字） 
4. CRISPRa-IFNLR1 作为增敏策略的转化潜力（350 字） 
5. 研究局限性与未来方向（100 字） 
6. 结论：重申本研究结论和意义 （100 字） 
</framework> 
 
<Draft literature review> 
第二步的文献综述，加上自己补充 论据，参考文献的初级版本，字数可以是讨论部分实际
字数的 2-3 倍。参考文献最好整理成（作者，年）形式，便于识别核对，AI 会保留： 
1. IFNλ作为 STING 通路新型标志物的生物学意义 
经典观点认为，STING 通路激活后主要产生 I 型干扰素（如 IFNβ）及炎性趋化因子
（CCL5、CXCL10 等）以启动抗肿瘤免疫(Biskup,2020; Lohinai 2022)。然而，近年研究显示
在上皮源性肿瘤中，III 型干扰素（IFNλ）的上调更为显著。IFNλ受体（IFNLR1）的表达高
度限于上皮细胞及少数免疫细胞 ( Karlowitz 2022)，使其信号主要局限于上皮组织，从而在
上皮源性癌症（如 NSCLC）中具有特殊意义。本研究发现在多种 NSCLC 细胞系中，通过
HT-DNA 或化疗药物激活 STING 后，IFNλ1/2 的转录和分泌普遍升高，而 IFNβ仅在极少数
细胞系中可检测到。这与 Rahim 等的发现一致：在肿瘤细胞-免疫细胞共培养体系中，肿
瘤细胞自身的 STING 活化可强烈诱导 III 型 IFN，而经典炎性标志物 CXCL10 等的表达则不
依赖于癌细胞 STING (Cetinbas 2024)。换言之，即便免疫细胞 STING 完整，只有肿瘤细胞
携带 STING 时才能产生大量 IFNλ (Cetinbas 2024)，而 CXCL10 的产生对肿瘤细胞 STING 缺
失并不敏感。研究表明，IFNLR1 在表皮细胞及特定免疫细胞亚群中呈现组织特异性表达
(Woo 2015; Manivasagam 2021; Lasfar 2011).综上所述，IFNλ作为 STING 通路活化标志
物，在上皮源性癌症中具有独特优势，可能比 IFNβ和其他细胞因子更可靠地指示肿瘤细胞
自身的 STING 信号激活。 
2. 肿瘤细胞 IFNLR1 下调的免疫逃逸机制 
本研究发现 NSCLC 细胞系相较于正常上皮细胞显著下调了 IFNLR1 表达，肿瘤组织中的恶
性上皮细胞 IFNLR1 水平也低于邻近正常组织。IFNLR1 下调意味着肿瘤细胞即使分泌 IFN
λ，也无法通过自身受体形成自分泌或旁分泌信号。这一机制类似于肿瘤抑制其他抗肿瘤
信。 。 。 。 。 。 
</Draft literature review> 
 
## Skills 
• Understanding and Applying Core Academic Writing Skills: Arrange the Discussion section 
in a structured order, including a clear summary of research findings, an analysis of the 
significance of the results, identification of research limitations, and proposing future research 
directions. Strong ending to emphasize the importance of research findings and how to 
effectively present these points in the discussion section.  
• Adapting to Specific Journal Style and Requirements: Conduct in -depth research on the 
specific style and format requirements of my target journal, including but not limited to 

## PDF page 8

citation standards, data presentation methods, and paper structure.  
• In-Depth Analysis and Literature Comparison: Use logically structured paragraphs, with each 
paragraph focusing on a single point or analytical perspective. Provide detailed analysis of 
each research result and compare it with existing literature to demonstrate how your research 
interacts with the existing knowledge framework.  
• Comprehensive Discussion of Research Results: Elaborate on research results in the 
Discussion section, including, but not limited to, comparisons with known literature, 
theoretical models, research methods, sample characteristics, and multi-dimensional analysis.  
• Critically Assessing Research Limitations and Future Directions: Clearly point out the 
limitations of the study, such as sample size, research design, choice of analytical methods, 
and suggest future research recommendations based on these shortcomings.  
• Structured and Logical Paragraph Organization: Ensure logical and interconnected 
paragraphs with a clear structure that adheres to the Discussion section's format.  
• Validating Research Hypotheses and Addressing Research Questions: Analyze whether the 
research hypotheses are validated, if research questions are answered, and the contribution 
and impact of the study on the relevant field of knowledge.  
• Accurate and Concise Expression: Strive for accuracy and conciseness in expression; 
important points should be supported with evidence, avoiding overemphasizing the 
significance of the research.  
• Summarize and Emphasize the Significance of the Research: Summarize the entire paper in 
the final paragraph, emphasizing the significance and innovation of the research, aligning 
with the introduction section to ensure internal logical coherence.  
• Paragraph Transitions: Use transitional vocabulary to connect different  
paragraphs' viewpoints, ensuring logical continuity and rhythm throughout the paper.  
• Tone and Format: Maintain a formal and academic tone, adhering to the formatting 
requirements of the target journal.  
• Precision and Conciseness: Use precise and concise language, avoiding vague expressions 
and unnecessary details.  
• Internal Paragraph Coherence: Employ clear topic sentences, supportive sentences, 
transitional devices, and maintain consistent focus within paragraphs.  
• Inter-Paragraph Coherence: Organize paragraphs logically, establish effective connections 
between them, maintain thematic continuity, and use concluding sentences that segue into 
the next paragraph.  
• Organization and Structure: Ensure that the discussion is well -organized and logically 
structured. Use clear and concise language, and ensure that arguments flow logically from 
one point to the next. Use subheadings to guide the reader through the discus sion and 
highlight the main points of your argument.  
• Tone and Style: Maintain a formal and objective tone throughout the discussion. Avoid using 
overly complex language or jargon that may confuse the reader. Be respectful of other 
researchers' work, even when critiquing it or presenting alternative viewpoints.  
• Logical Linking: Ensure that your arguments and points are logically linked. Each paragraph 
should have a clear main point, and all points within the paragraph should support that main 
point. Use transition words and phrases to guide the reader through your argument and show 
the relationships between different points. 

## PDF page 9

 
## Example 
<Title>  
{{作为例文让 AI 模仿写作风格的文章标题、摘要和讨论部分 SLAMF7 (CD319) enhances 
cytotoxic T-cell differentiation and sensitizes CD8(+) T cells to immune checkpoint blockade}}  
</Title>  
 
<Abstract> 
Tumors frequently evade immune destruction by impairing cytotoxic CD8
+
 T-cell responses, 
highlighting the need for strategies that restore T -cell functionality. Here, we identify 
SLAMF7 …… 
</Abstract> 
 
<Discussion>  
{{Our study demonstrates that SLAMF7 co-stimulation enhances activation, proliferation, and 
cytotoxic differentiation of human CD8
+
 T cells (  Figure 4 ), including those from tumor -
draining lymph nodes of HNSCC patients. Furthermore, sequential SLAMF7 engagement …… 
}}  
</Discussion>  
 
## Constraints 
- Adhere strictly to the provided framework. 
- Limit writing to the Discussion section only. 
- Preserve in-text citations from the literature review materials exactly as they appear (e.g., 
“(Zhang, 2025)” or numbered “[1,2]”). 
- Use the ## Example section only to learn structure and style for an academic Discussion; 
do not mix its case content with the scientific focus in my ## Background section. 
- Write the Discussion based on the literature-review draft and this study’s results only; do 
not introduce additional content. 
- Use a mix of long and short sentences; ensure smooth transitions between sentences 
and paragraphs, clear logic, and an academic style. 
- Maintain a neutral, objective tone; avoid hyperbole (e.g., “striking,” “for the first time”). 
 
Please think step by step. 
 
1 模型：Claude opus 4.1 thinking； 
2 标黄部分换成自己的内容，只替换{{ }}里面的内容； 
3 ## Example 部分给一篇你想要模仿的例文，让 AI 更好的学习文风。 