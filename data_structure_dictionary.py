#!/usr/bin/env python
# encoding: utf-8
'''
@author: Tudaozi
@contact: tudaozi@126.com
@project: pystudy
@file: data_structure_dictionary.py
@time: 2019-02-07 15:26
@desc:
'''

# 字典
'''
字典没有顺序，不能通过切片来取元素，
它是通过互不相同的key来访问元素
字典是可变的，可以随意增加、修改或者删除其中的键值对。
'''

# 字典的创建
'''
使用{}将键值对（key：value）创建字典
使用dict()将其他类型的双值子序列数据转换为字典
字典是无序的
'''

# 创建字典--创建字典dic
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)

# 将双值序列数据转换为字典--将双值序列的列表dict转换为字典
dic = ['ab', 'cd', 'ef']

print(dict(dic))  ##无法使用，在python解释器中可以正常运算

# 字典取值--获取字典dic中a的值
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic['a'])
print(dic['b'])

# 字典的修改
'''
字典数据添加
字典数据的修改
字典合并：update()
字典数据的删除 del、clear()
'''

# 字典数据添加--采用赋值的形式，对字典进行增加数据--字典dic增加key为d，values为4
dic = {'a': 1, 'b': 2, 'c': 3}
dic['d'] = 4
print(dic)

# 修改字典数据--采用赋值的形式，对字典key和values进行修改--字典dic中key为c的值修改为5
dic = {'a': 1, 'b': 2, 'c': 3}
dic['c'] = 5
print(dic)

# 合并字典--合并字典dic2到字典dic1
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'d': 1, 'e': 2, 'f': 3}
dic1.update(dic2)
print(dic1)

# 删除字典中的指定key数据
dic1 = {'a': 1, 'b': 2, 'c': 3}
del dic1['a']
print(dic1)

# 清空字典中的数据
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic1.clear()
print(dic1)

# 字典数据的获取
'''
通过 in 判断一个key是否存在
通过[key]获取元素，dict.get()
使用key()、values()和item()
'''

# 判断某个key是否在字典中--判断key：c是否在dic字典中
dic = {'a': 1, 'b': 2, 'c': 3}
t = 'c' in dic
print(t)

f = 'd' in dic
print(f)

# 判断某个key是否在字典中,值是多少--判断key：c是否在dic字典中值是多少
dic = {'a': 1, 'b': 2, 'c': 3}
dic2 = dic.get('a')
print(dic2)

dic3 = dic.get('b')
print(dic3)

dic4 = dic.get('c')
print(dic4)

# 打印字典中的所有key
dic = {'a': 1, 'b': 2, 'c': 3}
dic2 = dic.keys()
print(dic2)

# 打印字典中所有values
dic = {'a': 1, 'b': 2, 'c': 3}
dic2 = dic.values()
print(dic2)

# 打印字典中所有key values
dic = {'a': 1, 'b': 2, 'c': 3}
dic2 = dic.items()
print(dic2)

# 本节课作业
'''
创建一个包含 类似于 1 代表 one ，2  代表 two 等等的
数字和其对应的英文字母的字典。
在字典最后添加 100 和 1000对应的英文字母
获取 5  和  6 对应的英文，获取字典中所有的数字
'''

# 创建字典dic键值one：1
dic = {'one': 1., 'two': 2, 'three': 3, 'four': 4, 'Fives': 5, 'six': 6, 'Seven': 7, 'Eight': 8}
dic['hundred'] = 100
dic['one thousand'] = 1000
print(dic)
dic2 = dic.get('5')
print(dic2)
dic3 = dic.values()
print(dic3)
