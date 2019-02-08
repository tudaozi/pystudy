#!/usr/bin/env python
# encoding: utf-8
'''
@author: Tudaozi
@contact: tudaozi@126.com
@project: pystudy
@file: data_structure_tuple.py
@time: 2019-02-08 16:46
@desc:
'''

# 元组
'''
元组与列表类似，也是由任意类型元素组成的序列。
元组是不可变的
'''

'''
使用()创建元组，注意，逗号的使用
元组主要使用逗号来识别
 () 空元组和一个元素的元组
使用元组多个变量直接赋值
'''

# 创建一个多个元素的元组
tuple1 = (1, 2, 3,)
print(tuple1)

# 创建一个单元素的元组
tuple2 = (1,)
print(tuple2)

# 创建一个空元素的元组
tuple3 = ()
print(tuple3)

# 将元组中的元素赋值给对应个数的变量
tuple1 = (1, 2, 3,)
a, b, c = tuple1
print(a)
print(b)
print(c)

'''
使用元组交换多个变量的值
tuple函数创建元组
'''

# 使用元组的形式交换（复制）变量的值
a = 1
b = 2
a, b = b, a
print(a)
print(b)

# 将列表转换成元组
list1 = [1, 2, 3]
print(tuple(list1))
# 将字典转换成元组
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(tuple(dict1))

# 集合
'''
集合就是舍弃了值，只剩下key的字典
使用{}来创建集合
使用set()来创建集合
'''

# 创建集合--使用花括号{}创建集合
set1 = {'a', 'b', 'c'}
print(set1)

# 创建集合--使用set()创建集合()里面是列表
set2 = set(['d', 'e', 'f'])
print(set2)

# 创建空集合
set3 = set([])
print(set())  # 无效

'''
集合是无序的
集合的元素是唯一的
可以使用 in 判断是否存在
'''

# 集合中的元素是唯一的
set3 = {'a', 'b', 'c', 'a'}
print(set3)

# 判断元素是否在集合中
set4 = {'a', 'b', 'c'}
set5 = 'a' in set4
print(set5)

set6 = 'd' in set4
print(set6)

'''
集合的运算
交集、并集、差集
'''
# 交集
set7 = {'a', 'b', 'c'}
set8 = {'a', 'c', 'd'}
print(set7 & set8)

# 并集
set7 = {'a', 'b', 'c'}
set8 = {'a', 'c', 'd'}
print(set7 | set8)

# 差集
set7 = {'a', 'b', 'c'}
set8 = {'a', 'c', 'd'}
print(set7 - set8)
print(set8 - set7)
