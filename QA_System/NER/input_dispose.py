# coding:utf-8
import jieba
import jieba.analyse
from gensim.models import word2vec
from anytree import Node, RenderTree, DoubleStyle,PreOrderIter
import pickle as pickle

__author__ = 'XJX'
__date__ = '2018.06.13'

"""
description:
    将输入的自然语言进行处理，提取出10个关键词
    输入最长为50个字符，超出则不予处理
"""


def extract(txt):
    print(txt)

    if(len(txt) <= 50):
        jieba.load_userdict("../../data/user_dict.txt")
        stoplist = {}.fromkeys([line.strip() for line in open("../../data/stopwords.txt")])
        txt_key = jieba.analyse.extract_tags(txt, topK=10, withWeight=True)  # 从输入中提取关键词
        txt_key = [word for word in txt_key if word not in stoplist]  # 去停用词
        return txt_key
    else:
        print('error')
        return


def find_match(keywords):
    fn = '../QA/test.pkl'
    with open(fn, 'rb') as f:
        summer = pickle.load(f)
        list = [node for node in PreOrderIter(summer, filter_=lambda n: n.name != '')]
        print(len(list))
        aim_node = list[0]
        num = 0
        for node in list:
            jieba.load_userdict("../../data/user_dict.txt")
            stoplist = {}.fromkeys([line.strip() for line in open("../../data/stopwords.txt")])
            match_key = jieba.analyse.extract_tags(node.name, topK=10, withWeight=True)  # 从输入中提取关键词
            match_key = [word for word in match_key if word not in stoplist]  # 去停用词
            if calculate_sentence_vector(keywords, match_key) > num:
                num = calculate_sentence_vector(keywords, match_key)
                aim_node = node

    return aim_node.src


def calculate_sentence_vector(keywords, match_key):
    model = word2vec.Word2Vec.load("../../data/ml.model")
    table = [[0 for i in range(len(keywords))] for j in range(len(match_key))]  # 构建二维数组
    for d1 in range(len(keywords)):
        for d2 in range(len(match_key)):
            try:
                table[d1][d2] = model.similarity(keywords[d1][0], match_key[d2][0])
            except KeyError:
                table[d1][d2] = 0

    res = 0
    for j in range(min(len(keywords), len(match_key))):
        num = 0
        x = 0
        y = 0
        for d1 in range(len(keywords)):
            for d2 in range(len(match_key)):
                if table[d1][d2] > num:  # 更新最大值并将其所在行和所在列置为0
                    num = table[d1][d2]
                    x = d1
                    y = d2
        for i in range(len(keywords[d1])):
            table[d1][i] = 0
        for i in range(len(match_key[d2])):
            table[i][d2] = 0
        res += num * keywords[x][1] * match_key[y][1]
    return res

if __name__ == '__main__':
    txt = input("Enter your text:")
    keywords = extract(txt)
    print(keywords[0][0])

    if keywords:
        src = find_match(keywords)
        print('../../data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src)
    else:
        print('error')

    # model = word2vec.Word2Vec.load("../../data/ml.model")
    # try:
    #     y1 = model.similarity(u"智能", u"智能")
    # except KeyError:
    #     y1 = 0
    # print(u"【智能】和【装车】的相似度为：" + str(y1))
