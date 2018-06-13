# coding:utf-8
import jieba
import jieba.analyse

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
        txt_key = [word for word in list(txt_key) if word not in stoplist]  # 去停用词
        print(txt_key)
    else:
        print('error')

if __name__ == '__main__':
    txt = input("Enter your text:")
    extract(txt)
