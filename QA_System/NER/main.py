# coding:utf-8
import logging
import json
from gensim.models import word2vec
from input_dispose import *
from answer_location import *
import webbrowser

__author__ = 'XJX'
__date__ = '2018.06.14'

"""
description:
    主函数，程序入口
"""


def main(txt):
    logging.basicConfig(filename="../search.log", format='%(asctime)s:%(levelname)s: %(message)s',
                            level=logging.INFO, filemode='a')
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    model = word2vec.Word2Vec.load("../ml.model")

    keywords = extract(txt)

    if keywords:
        print(keywords[0][0])
        node = find_match(keywords)
        src = node.src
        aim_path = '../../data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src
        logger.info("The aim file is: " + aim_path)
        if not src == '':
            ans = find_answer(node.name, keywords, aim_path)
            web = webbrowser.get('chrome')
            web.open_new('file://' + '/Users/xujiaxing/Documents/GitHub/QA_System/data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src)
            print(ans)
        else:
            ans = ''
        res = [aim_path, ans]
        return res
    else:
        print('error')
        return

if __name__ == '__main__':
    txt = input("Enter your text:")
    res = main(txt)
    print(res)
