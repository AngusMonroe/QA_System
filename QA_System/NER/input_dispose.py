# coding:utf-8
import jieba
import jieba.analyse
from gensim.models import word2vec
from anytree import Node, RenderTree, DoubleStyle, PreOrderIter
import pickle as pickle
import logging

__author__ = 'XJX'
__date__ = '2018.06.13'

"""
description:
    将输入的自然语言进行处理，提取出10个关键词
    输入最长为50个字符，超出则不予处理
"""

logger = logging.getLogger(__name__)

model = word2vec.Word2Vec.load("../ml.model")
jieba.load_userdict("../user_dict.txt")
stoplist = {}.fromkeys([line.strip() for line in open("../stopwords.txt")])


def extract(txt):
    print(txt)

    if(len(txt) <= 50):
        jieba.load_userdict("../user_dict.txt")
        stoplist = {}.fromkeys([line.strip() for line in open("../stopwords.txt")])
        txt_key = jieba.analyse.extract_tags(txt, topK=10, withWeight=True)  # 从输入中提取关键词
        txt_key = [word for word in txt_key if word not in stoplist]  # 去停用词
        logger.info("Input has {0:d} keywords.".format(len(txt_key)))
        logger.info(txt_key)
        return txt_key
    else:
        return


def find_match(keywords):
    logger.info("Start to find file.")
    fn = '../QA/test.pkl'
    with open(fn, 'rb') as f:
        summer = pickle.load(f)
        list = [node for node in PreOrderIter(summer, filter_=lambda n: n.name != '')]
        print(len(list))
        aim_node = list[0]
        num = 0
        node_num = 0
        for node in list:
            node_num += 1
            if node_num % 100 == 0:
                logger.info("Find {0:d} nodes.".format(node_num))
            try:
                if node.src == '':
                    continue
                match_key = jieba.analyse.extract_tags(node.name, topK=10, withWeight=True)  # 从输入中提取关键词
                match_key = [word for word in match_key if word not in stoplist]  # 去停用词
                if calculate_sentence_vector(keywords, match_key) > num:
                    num = calculate_sentence_vector(keywords, match_key)
                    aim_node = node
            except Exception as e:
                continue
    logger.info("File has already been found.")
    logger.info("The title of the aim file is: " + aim_node.name)
    try:
        return aim_node
    except Exception as e:
        return ''


def calculate_sentence_vector(keywords, match_key):
    table = [[0 for i in range(len(match_key))] for j in range(len(keywords))]  # 构建二维数组
    logger.debug("The table is {0:d} * {1:d}".format(len(table), len(table[0])))
    for d1 in range(len(keywords)):
        for d2 in range(len(match_key)):
            logger.debug("d1:{0:d} d2:{1:d}".format(d1, d2))
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
        logger.debug("x:{0:d} y:{1:d}".format(x, y))
        for i in range(len(keywords)):
            table[i][y] = 0
        for i in range(len(match_key)):
            table[x][i] = 0
        res += num * keywords[x][1] * match_key[y][1]
    return res

if __name__ == '__main__':
    logging.basicConfig(filename="../search.log", format='%(asctime)s:%(levelname)s: %(message)s',
                        level=logging.INFO, filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    txt = input("Enter your text:")
    keywords = extract(txt)

    if keywords:
        print(keywords[0][0])
        src = find_match(keywords).src
        print('../../data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src)
    else:
        print('error')

    # model = word2vec.Word2Vec.load("../ml.model")
    # try:
    #     y1 = model.similarity(u"智能", u"智能")
    # except KeyError:
    #     y1 = 0
    # print(u"【智能】和【装车】的相似度为：" + str(y1))
