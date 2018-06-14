# coding:utf-8
import logging
import json
from gensim.models import word2vec
from input_dispose import *
from answer_location import *

__author__ = 'XJX'
__date__ = '2018.06.14'

"""
description:
    主函数，程序入口
"""


def main():
    logging.basicConfig(filename="../../data/search.log", format='%(asctime)s:%(levelname)s: %(message)s',
                            level=logging.INFO, filemode='a')
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    model = word2vec.Word2Vec.load("../../data/ml.model")

    txt = input("Enter your text:")
    keywords = extract(txt)

    if keywords:
        print(keywords[0][0])
        src = find_match(keywords)
        aim_path = '../../data/znwdxtsjykf_cssj/support.huaweicloud.com/' + src
        logger.info("The aim file is: " + aim_path)
        ans = find_answer(keywords, aim_path)
        # print(ans)
        res = [aim_path, ans]
        return json.dumps(res)
    else:
        print('error')
        return

if __name__ == '__main__':
    res = main()
    print(res)