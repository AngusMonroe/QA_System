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
from anytree import Node, RenderTree, DoubleStyle,PreOrderIter
import pickle
fn = 'test.pkl'
with open(fn, 'rb') as f:
    summer = pickle.load(f)
print(RenderTree(summer, style=DoubleStyle).by_attr())
tmp = [node.name for node in PreOrderIter(summer, filter_=lambda n:n.is_leaf is True)]
max = -1
index = 0
for s in tmp:
    print("%s"%s)
for i in range(0,len(tmp)):
    if len(tmp[i]) > max:
        index = i
        max = len(tmp[i])
print(max, "%s"%tmp[index])