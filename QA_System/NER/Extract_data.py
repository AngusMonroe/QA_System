# coding:utf-8
__author__ = 'XJX'
__date__ = '2018.05.17'

"""
description:
    利用正则表达式提取关键词
"""

import os
import re
import codecs
import sys
import importlib
import msgpack


def Extract(aimpath):
    in_text = aimpath#原合同文本
    out_text = r"../data/keyword.txt"#储存所提取的关键词
    data_text = r"../data/data.txt"#储存替换后的合同文本
    map_text = r"../data/map.txt"  # 储存关键词映射

    f1 = open(in_text,'r+')
    f2 = open(out_text,'w',encoding='utf8')
    f3 = open(data_text, 'w', encoding='utf8')
    f4 = open(map_text, 'w', encoding='utf8')

    num = 1

    for line in f1.readlines():
        try:
            linkre1 = re.findall("_+(\d+)_+年_+(\d+)_+月_+(\d+)_+日", line)#处理日期格式
            for key in linkre1:
                date = key[0] + '年' + key[1] + '月' + key[2] + '日'
                #print(date)
                date_tran = re.sub('_+(\S*)_+日', '__' + date + '__', line)#将'_x_年_x_月_x_日'替换为'_x年x月x日_'格式
                #print(date_tran)
                #print(line)
                line = line.replace(line, date_tran)
                #print(line)

            linkre2 = re.findall("_+([^_]*)_+",line)
            if linkre2:
                print(linkre2)
                for keyword in linkre2:
                    print(keyword)
                    if keyword:
                        f2.write(keyword+'\n')

                        flag = re.findall("_+([^_]*)_+",line)#匹配'_x_'字段
                        while flag:
                            print(flag)
                            keyword_tran = re.sub('_+([^_]*)_+', '##' + str(num) + '##', line, count=1)#将匹配到的字段转化为'##num##'格式
                            f4.write('##' + str(num) + '## ' + flag[0] +'\n')
                            #print(keyword_tran)
                            #print(line)
                            num += 1
                            line = line.replace(line, keyword_tran)
                            flag = re.findall("_+([^_]*)_+", line)

            f3.write(line)
            #line = f1.readline()
        except Exception:
            print('error')
            #print(line)
            #line = f1.readline()
            continue

    f1.close()
    f2.close()
    f3.close()
    f4.close()
