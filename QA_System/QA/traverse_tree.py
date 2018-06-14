# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 23:14
# @Author  : QSHZH
# @Email   : qshzh@buaa.edu.cn
# @File    : create_tree.py
# @Software: PyCharm
"""
description:
    遍历树搜索信息
"""
from anytree import Node, RenderTree, DoubleStyle,PostOrderIter
import pickle
from bs4 import BeautifulSoup

fn = 'test.pkl'
with open(fn, 'rb') as f:
    summer = pickle.load(f)
#print(RenderTree(summer, style=DoubleStyle).by_attr())

# root3 = [node for node in PostOrderIter(summer, filter_=lambda n:n.name == '备案中心')]
# root2 = [node for node in PostOrderIter(root3[0], filter_=lambda n:n.name == '常见问题 ')]
# root4 = [node for node in PostOrderIter(root3[0], filter_=lambda n:n.name == '常见问题')]
# print(RenderTree(root2[0], style=DoubleStyle).by_attr())
# root2[0].children[0].parent = root4[0]
# root2[0].children[0].parent = root4[0]
# root2[0].children[0].parent = root4[0]
# root2[0].children[0].parent = root4[0]
# root2[0].parent = Node('wdwdwdwdwddwd')
# print(RenderTree(summer, style=DoubleStyle).by_attr())
# error = []
# original_path = r"../../data/znwdxtsjykf_cssj/support.huaweicloud.com"
#
# with open('../../data/map.txt', 'r') as f:
#     ii = 0
#     while ii < 6:
#         ii = ii + 1
#         str = []
#         filename = f.readline()
#         if ii!=6:
#             filename = filename[:-1]
#         htmlfile = open(original_path + '/' + filename, 'r', encoding='utf8')
#         soup = BeautifulSoup(htmlfile.read(), 'lxml')
#         titles = soup.select('#content > div.wrapper > div > div.record-main > div.crumbs > a')
#         for i in range(0,len(titles)):
#             str.append(titles[i].get_text().replace(' >', ''))
#         text = soup.select('#content > div.wrapper > div > div.record-main > div.crumbs > span')
#         for j in text:
#             str.append(j.get_text().replace(' >',''))
#         if len(str) == 0: #记录不符合规范的文件名
#             error.append(filename)
#             continue
#         roott = root2
#         for j in str:
#             print("%s" % j, end=' ')
#         print('')
#         for i in range(0, len(str)):
#             if len([node.name for node in
#                     PostOrderIter(roott, maxlevel=2, filter_=lambda n: n.name == str[i])]) == 0:
#                 tmp = Node(str[i], parent=roott)
#                 if i == len(str) - 1:
#                     tmp.src = filename
#                 roott = tmp
#             else:
#                 tmp = [node for node in PostOrderIter(roott, maxlevel=2, filter_=lambda n: n.name == str[i])][0]
#                 roott = tmp
# #print(RenderTree(root2, style=DoubleStyle).by_attr())
# for item in error:
#     print(item)
# print(len(error))

# fn = 'test.pkl'
# with open(fn, 'wb') as f: #树对象存入文件中
#     picklestring = pickle.dump(summer, f)
#tmp = [node for node in PreOrderIter(summer, filter_=lambda n:n.name == '智能装车服务')]
#print(tmp[0].src)
# max = -1
# index = 0
# for s in tmp:
#     print("%s"%s)
# for i in range(0,len(tmp)):
#     if len(tmp[i]) > max:
#         index = i
#         max = len(tmp[i])
# print(max, "%s"%tmp[index])