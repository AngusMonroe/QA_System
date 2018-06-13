#coding=utf8
__author__ = 'QSHZH'
__date__ = '2018.06.07'

"""
description:
    遍历树搜索信息
"""
from anytree import Node, RenderTree, DoubleStyle,PreOrderIter
import pickle as pickle
import sys
import imp
imp.reload(sys)
sys.setdefaultencoding('utf8')
fn = 'test.pkl'
with open(fn, 'r') as f:
    summer = pickle.load(f)
print((RenderTree(summer, style=DoubleStyle).by_attr()))
print(([node for node in PreOrderIter(summer,filter_=lambda n:n.name=='如何预测攻击者下一步攻击手段？')][0].src))