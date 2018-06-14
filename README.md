# QA_System

### 需求
- 前台
	
	Android APP实现QA对话界面，该界面可以基于用户提问，自动连接后台、并从知识库寻找答案，并呈现给用户，前台问题可以是由主题、关键词、短语构成。
	
- 后台

	搭建本地/web服务器，实现前后端通讯
	
- 知识库

	NER、seq2seq
	
### Directory Introduction
- `QA_System` directory contains Android client, NER, QA and sever code.
- `Paper` directory contains important papers related to the project, mainly involving QA system and deep learning
- `data` directory contains the training data of this project.

### Usage

run `QA_System/NER/main.py`

### Requirement

- python3.6
- Android（SDK？）
- django（？）
- urllib, urllib2, json, word2vec, jieba

### QA
|标准问题ID（可选）|标准问题（必填）|主题（可选）|答案（必填）|答案链接（必填）|扩展问题（可选，一行一条，最多100条）|
|----------|--------|------|------|--------|---------------------|
|mls060001|什么是机器学习？|MLS|机器学习(Machine Learning, ML)是一门多领域交叉学科，涉及概率论、统计学、逼近论、凸分析、算法复杂度理论等多门学科。专门研究计算机怎样模拟或实现人类的学习行为，以获取新的知识或技能，重新组织已有的知识结构使之不断改善自身的性能。|文件名：问答对提取的文件名 http://support.huaweicloud.com/usermanual-mls/zh-cn_topic_user_guide.html|机器学习的概念？|