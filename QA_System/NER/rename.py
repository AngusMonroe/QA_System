# coding:utf-8
__author__ = 'XJX'
__date__ = '2018.05.23'

"""
description:
    将一个目录下所HTML文件重命名为其大标题
"""

import os
import re
import fnmatch


def rename1(path):
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        if not fnmatch.fnmatch(files, '*.html'):
            continue
        print(path + files)
        f = open(path + files, 'r+')
        txt = f.read()
        # print(txt)
        try:
            linkre = re.findall("<span class='text'>\S+</span>", txt)  # 匹配目标标题
            if linkre:
                print(linkre)
                word = linkre[0]
                word = word.replace('<span class=\'text\'>', '')
                word = word.replace('</span>', '')
                print(word)
                while os.path.exists(path + word + ".html"):
                    word = word + "1"
                os.rename(path + files, path + word + ".html")  # 重命名

        except Exception:
            print('error')
            continue


def rename2(path):
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        if not fnmatch.fnmatch(files, 'support*'):
            continue
        print(path + files)
        f = open(path + files, 'r+')
        txt = f.read()
        print(txt)
        try:
            linkre = re.findall("<span class='text'>\S+</span>", txt)  # 匹配目标标题
            # if linkre:
            #     print(linkre)
            #     word = linkre[0]
            #     word = word.replace('<span class=\'text\'>', '')
            #     word = word.replace('</span>', '')
            #     print(word)
            #     while os.path.exists(path + word + ".html"):
            #         word = word + "1"
            os.rename(path + files, path + "support1.html")  # 重命名

        except Exception:
            print('error')
            continue
        break


if __name__ == '__main__':
    # rename1(path="../../data/znwdxtsjykf_cssj/data/")
    rename2(path="../../data/znwdxtsjykf_cssj/data/")
    print("done")
