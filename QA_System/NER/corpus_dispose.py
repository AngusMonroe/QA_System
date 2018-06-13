# coding:utf-8
import fnmatch
import os
import re
from bs4 import BeautifulSoup

__author__ = 'XJX'
__date__ = '2018.06.13'

"""
description:
    将html数据集处理为txt语料，去除html标签以及非法字符
"""

path = '../../data/data/'
out_file = open('../../data/corpus.txt', 'a', encoding='utf8')
filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
print(filelist)
for files in filelist:  # 遍历所有文件
    if not fnmatch.fnmatch(files, '*.html'):
        continue
    print(path + files)
    f = open(path + files, 'r+', encoding='utf8')
    txt = f.read()
    soup = BeautifulSoup(txt)
    for s in soup('script'):
        s.extract()
    for s in soup('style'):
        s.extract()
    txt = soup.__str__()
    reg2 = re.compile('<[^>]*>')
    txt = reg2.sub('', txt)
    reg3 = re.compile('-->')
    txt = reg3.sub('', txt)
    reg4 = re.compile('&(\S)?gt')
    txt = reg4.sub('', txt)
    reg5 = re.compile('New!')
    txt = reg5.sub('', txt)
    ans = txt.split("\n")
    print(ans)
    for word in ans:
        if not word == '':
            out_file.write(word)
            out_file.write('\n')
        if word == '法律声明':
            break
    f.close()

out_file.close()
print("done")
