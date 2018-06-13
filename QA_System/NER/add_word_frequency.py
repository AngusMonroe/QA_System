# coding:utf-8
__author__ = 'XJX'
__date__ = '2018.06.13'

"""
description:
    在用户词典中添加词频字段，默认100
"""

input_file = open(r'../../data/user_dict_pre.txt', 'r', encoding='utf8')  # 打开文件
txt = input_file.readlines()   # 读取文件

output_file = open(r'../../data/user_dict.txt', 'w', encoding='utf8')   # 打开文件，其实这里，是创建文件。因为user_dict.txt是不存在的
for line in txt:  # for循环
    if not line:     # 如果不存在该行，就跳出循环
        break
    line = line.strip("\n")
    new_line = line + ' 100' + '\n'
    output_file.write(new_line)  # write方法，写入到指定文件中
input_file.close()  # 关闭文件
output_file.close()  # 关闭文件
print("done")
