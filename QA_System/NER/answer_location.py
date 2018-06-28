# coding:utf-8
import jieba
import jieba.analyse
from gensim.models import word2vec
import os
import re
from bs4 import BeautifulSoup
from input_dispose import *

__author__ = 'XJX'
__date__ = '2018.06.14'

"""
description:
    从文件中找到匹配度最高的句子
"""

logger = logging.getLogger(__name__)

model = word2vec.Word2Vec.load("../../data/ml.model")
jieba.load_userdict("../../data/user_dict.txt")
stoplist = {}.fromkeys([line.strip() for line in open("../../data/stopwords.txt")])


def find_answer(name, keywords, path):
    logger.info("Start to find sentence.")
    f = open(path, 'r+', encoding='utf8')
    lines = f.read()
    soup = BeautifulSoup(lines)
    for s in soup('script'):
        s.extract()
    for s in soup('style'):
        s.extract()
    lines = soup.__str__()
    reg2 = re.compile('<[^>]*>')
    lines = reg2.sub('', lines)
    reg3 = re.compile('-->')
    lines = reg3.sub('', lines)
    reg4 = re.compile('&(\S)?gt')
    lines = reg4.sub('', lines)
    reg5 = re.compile('New!')
    lines = reg5.sub('', lines)
    reg6 = re.compile('  ')
    lines = reg6.sub('', lines)
    ans = lines.split("\n")
    content = []
    for sentence in ans:
        if not sentence == '':
            content.append(sentence)
        if sentence == '法律声明':
            break
    # print(content)

    num = 0
    sentence_num = 0
    aim_sentence = content[0]
    flag = 0
    for sentence in reversed(content):
        sentence_num += 1
        if sentence_num % 100 == 0:
            logger.info("Find {0:d} sentence.".format(sentence_num))
        if sentence == name:  # 排除与节点名相同的句子
            flag = 1
            continue

        # if flag == 1:
        #     aim_sentence = sentence
        #     break

        match_key = jieba.analyse.extract_tags(sentence, topK=10, withWeight=True)  # 从输入中提取关键词
        match_key = [word for word in match_key if word not in stoplist]  # 去停用词

        if calculate_sentence_vector(keywords, match_key) > num:
            num = calculate_sentence_vector(keywords, match_key)
            aim_sentence = sentence
    logger.info("Sentence has already been found.")
    return aim_sentence

if __name__ == '__main__':
    logging.basicConfig(filename="../../data/search.log", format='%(asctime)s:%(levelname)s: %(message)s',
                        level=logging.INFO, filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    txt = input("Enter your text:")
    keywords = extract(txt)

    node = find_answer(keywords, '../../data/znwdxtsjykf_cssj/support.huaweicloud.com/support.huaweicloud.com_api-ais_zh-cn_scl_api.html')
    ans = node.src
    print(ans)
