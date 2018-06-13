# coding:utf-8
import sys

import jieba
import jieba.analyse
import re
from gensim.models import word2vec
import logging

__author__ = 'XJX'
__date__ = '2018.06.13'


def train(file):

    # 主程序
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(file)  # 加载语料
    model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型，默认window=5

    print(model)
    # 计算两个词的相似度/相关程度
    # try:
    #     y1 = model.similarity(u"高血压", u"头痛")
    # except KeyError:
    #     y1 = 0
    # print(u"【高血压】和【头痛】的相似度为：" + str(y1))
    # print("-----\n")
    #
    # # 计算某个词的相关词列表
    # y2 = model.most_similar(u"高血压", topn=20)  # 20个最相关的
    # print(u"和【高血压】最相关的词有：\n")
    # for item in y2:
    #     print(item[0], item[1])
    # print("-----\n")

    # 保存模型，以便重用
    model.save(u"../../data/ml.model")
    # 对应的加载方式
    # model_2 =word2vec.Word2Vec.load("text8.model")

    # 以一种c语言可以解析的形式存储词向量
    # model.save_word2vec_format(u"书评.model.bin", binary=True)
    # 对应的加载方式
    # model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)


def segmentation():
    wiki_file = open('../../data/wiki.txt', 'r', encoding='utf8')
    in_file = open('../../data/corpus.txt', 'r', encoding='utf8')
    out_file = open('../../data/train_data.txt', 'a', encoding='utf8')
    jieba.load_userdict("../../data/user_dict.txt")
    stoplist = {}.fromkeys([line.strip() for line in open("../../data/stopwords.txt")])
    txt1 = in_file.readlines()
    for line in txt1:
        reg = re.compile('  ')
        line = reg.sub('', line)
        seg_list = jieba.cut(line, cut_all=False)  # 分词
        seg_list = [word for word in list(seg_list) if word not in stoplist]  # 去停用词

        for word in seg_list:
            if not word == '':
                out_file.write(word + ' ')
    in_file.close()
    txt2 = wiki_file.readlines()
    for line in txt2:
        reg = re.compile('  ')
        line = reg.sub('', line)
        seg_list = jieba.cut(line, cut_all=False)  # 分词
        seg_list = [word for word in list(seg_list) if word not in stoplist]  # 去停用词

        for word in seg_list:
            if not word == '':
                out_file.write(word + ' ')
        out_file.write('\n')
    wiki_file.close()
    out_file.close()

if __name__ == '__main__':
    # segmentation()
    train('../../data/train_data.txt')
