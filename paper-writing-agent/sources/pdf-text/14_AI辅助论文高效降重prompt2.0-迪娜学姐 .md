# 14_AI辅助论文高效降重prompt2.0-迪娜学姐 .pdf

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

论文高效降重提示词 2.0 
By 迪娜学姐 Dyna ©版权所有 
 
一、降重提示语： 
场景 1：针对整段重复的降重，比如 Methods 部分整段重复： 
I would like you to act as an expert in the [field of biology] and a scientific editor to 
assist in reviewing my manuscript for potential plagiarism, as it is intended for 
submission to [Nature]. The manuscript will be scrutinized for instances of 13 
consecutive identical words, which would be deemed as duplication. It’s essential to 
employ strategies such as rearranging subjects, verbs, and objects, utilizing 
synonyms, and modifying word count to ensure the originality of the text, while 
maintaining the integrity of the meaning, structure, and clarity of the manuscript. 
Please proceed with modifying the subsequent paragraph, ensuring the preservation 
of clear, concise, and logical expression throughout the text. 
 
（说明：输入整段内容，标黄部分改成你自己的领域和目标期刊，等Claude 回复后，再输
入整段需要降重的文字。 ） 
 
场景 2：针对零星句子，降重不彻底，一句话中只改了几个动词，在查重时还是被高亮
出来。类似下面框红的句子： 

## PDF page 3

 
 
用下面的提示语，AI 工具用 Claude sonnet 4.5： 
 
I would like you to act as an expert in the [Alzheimer's Disease] and a scientific editor to assist 
in reviewing my manuscript for potential plagiarism, as it is intended for submission to 
[Nature]. The manuscript will be scrutinized for instances of 13 consecutive identical words, 
which would be deemed as duplication. It’s essential to employ strategies such as rearranging 
subjects, verbs, and objects, utilizing synonyms, and modifying word count to ensure the 
originality of the text, while maintaining the integrity of the meaning, structure, and clarity of 
the manuscr ipt. Please proceed with modifying the subsequent paragraph, ensuring the 
preservation of clear, concise, and logical expression throughout the text. Please notice that 
only content in [ ] need to be rewrited. Do you understand? 
 
对话示范： 


## PDF page 4

 
 
把需要降重改写的句子用[ ]框起来，在第二轮对话中整段提供给 AI。 
 
 
这样既能针对需要降重的句子有效改写，又能和上下文衔接顺畅。避免改完段落不通顺。 


## PDF page 5

 
如果还有其他部分需要降重，继续这样操作。 
 
 
模型选择：Claude sonnet 4.5 