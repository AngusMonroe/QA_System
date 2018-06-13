#coding=utf8
__author__ = 'QSHZH'
__date__ = '2018.06.07'

"""
description:
    构建数据结构树
"""
from bs4 import BeautifulSoup
import os
import fnmatch
import re
import sys
from anytree import Node, RenderTree, DoubleStyle,PostOrderIter
import pickle as pickle
import imp
imp.reload(sys)
sys.setdefaultencoding('utf8')

original_path = r"./data"
map_text = r"./data/map.txt"      #储存关键词映射
dirs = os.listdir( original_path )#所有文件列表
#print(type(dirs))
print((len(dirs)))
#filename = dirs[0]
root=Node('root')
root1=Node("开发者中心")
root2=Node('帮助中心')
error=[]
ii=0
for filename in dirs:
    if fnmatch.fnmatch(filename, 'developer.*'): #处理以developer开头的文件

        htmlfile = open(original_path+'/'+filename, 'r')
        soup = BeautifulSoup(htmlfile.read(), 'lxml')
        titles = soup.select('#content > div.wrapper > div.crumbs > a')
        str = []  #将层次结构存入str数组，然后进行判断

        for i in range(0, len(titles)):
            str.append(titles[i].get_text())
        text = soup.select('#content > div.wrapper > div.crumbs > span')

        for j in text:
            str.append(j.get_text())
        #print( str )

        if len(str) == 0:
            Node(soup.title.text, parent=root1, src=filename)
        else:
            for i in range(1, len(str)):
                if i == len(str)-1 or len([node.name for node in PostOrderIter(root1, filter_=lambda n: n.name == str[i])]) == 0:
                    if i == 1:
                        if i == len(str)-1:
                            Node(str[i], parent=root1, src=filename)
                        else:
                            Node(str[i], parent=root1)
                    else:
                        if i == len(str) - 1:
                            Node(str[i], parent=[node for node in
                                                PostOrderIter(root1, filter_=lambda n: n.name == str[i - 1])][0], src=filename)
                        else:
                            Node(str[i], parent=[node for node in
                                                 PostOrderIter(root1, filter_=lambda n: n.name == str[i - 1])][0])
    elif fnmatch.fnmatch(filename, 'support.*'):#处理以以support开头文件，
        htmlfile = open(original_path + '/' + filename, 'r')
        soup = BeautifulSoup(htmlfile.read(), 'lxml')
        titles = soup.select('#content > div.help-cen > div > div.help-main > div.crumbs > a')
        str = []  # 将层次结构存入str数组，然后进行判断

        for i in range(0, len(titles)):
            str.append(titles[i].get_text())
        text = soup.select('#content > div.help-cen > div > div.help-main > div.crumbs > span')

        for j in text:
            str.append(j.get_text())

        if len(str) == 0: #记录不符合规范的文件名
            error.append(filename)
            continue
        print(ii) #统计处理进程
        ii = ii+1
        if len(str) == 0:
            continue
        else:
            roott = root2
            if str[1] == '产品新特性':
                #h1 = soup.select('#content > div.help-cen > div > div.help-main > div.helpContent > div > div > div > h1 > span')
                str.append(soup.title.text)

            for j in str:
                print("%s " % (j), end=' ')
            print('')

            for i in range(1, len(str)):
                if len([node.name for node in
                        PostOrderIter(roott, maxlevel=2, filter_=lambda n: n.name == str[i])]) == 0:

                    tmp = Node(str[i], parent=roott)

                    if i == len(str)-1:
                        tmp.src = filename
                    roott = tmp
                else:
                    tmp = [node for node in PostOrderIter(roott, maxlevel=2, filter_=lambda n: n.name == str[i])][0]
                    roott = tmp
        # if len(str) == 0 or str[0] != '帮助中心':
        #     continue
        #     #Node(soup.title.text, parent=root2, src=filename)
        # else:
        #     for i in range(1, len(str)):
        #         if i == len(str)-1 or len([node.name for node in PostOrderIter(root2, filter_=lambda n: n.name == str[i])]) == 0:
        #             if i == 1:
        #                 if i == len(str)-1:
        #                     Node(str[i], parent=root2, src=filename)
        #                 else:
        #                     Node(str[i], parent=root2)
        #             else:
        #                 if i == len(str) - 1:
        #                     Node(str[i], parent=[node for node in
        #                                         PostOrderIter(root2, filter_=lambda n: n.name == str[i - 1])][0], src=filename)
        #                 else:
        #                     Node(str[i], parent=[node for node in
        #                                          PostOrderIter(root2, filter_=lambda n: n.name == str[i - 1])][0])
for item in error:
    print(item)
print(len(error))
root1.parent = root
root2.parent = root
print((RenderTree(root, style=DoubleStyle).by_attr()))
fn = 'test.pkl'
with open(fn, 'w') as f:
    picklestring = pickle.dump(root, f)
#print([node for node in PostOrderIter(root1,filter_=lambda n:n.name=='DevOps解决方案')][0].src)
