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



# 列表的创建形式
'''
使用[]或者list()
使用list()将其他类型的数据转换为列表
'''

# 1
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen']
print(a)

# 2
a = list('abcdefg')
print(a)



# 列表的切片操作
'''
格式：
    使用[start : end : step]分片
    开始：结束：步长
    
    [start : ] , [ : end] , [start : end]
    认识负偏移量、步长
'''

a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen', 'baoan', 'luohu', 'nanshan', 'longhua']

# 打印第二位
print(a[1])

# 打印倒数第二位
print(a[-2])

# 打印第四位到末尾
print(a[3:])

# 从0位打印到倒数第四位
print(a[: -4])

# 倒序排列
print(a[::-1])

#从第二位到倒数第二位，步长3
print(a[1:-2:3])

#从第二位到倒数第二位，步长1
print(a[1:-2:1])



#列表的修改
'''
逆序列
列表可以包含列表，双重索引
通过偏移量直接修改list
合并列表extend() 或者 +
'''

