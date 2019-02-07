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

# 从第二位到倒数第二位，步长3
print(a[1:-2:3])

# 从第二位到倒数第二位，步长1
print(a[1:-2:1])

# 列表的修改(一)
'''
逆序列
列表可以包含列表，双重索引
通过偏移量直接修改list
合并列表extend() 或者 +
'''

# 倒序排列
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen', 'baoan', 'luohu', 'nanshan', 'longhua']
print(a[::-1])

# 修改列表a中第一位
a[0] = 'huangtian'
print(a)

# 列表中包含另外一个列表b
a[1] = ['hangcheng', 'xixiang', 'xinan', 'fuyong', 'shajin', 'shiyan']
print(a)

# 获取二级列表中的元素--获取列表a中第二位元素中的第三个元素
print(a[1][2])

# 同时修改列表中的多个元素--同时修改列表a中的第一二位元素值
a[:1] = [1000, 2000]
print(a)

# 将两个列表进行合并生成新的列表（不改变原来列表的元素）--合并列表a和列表b生成列表c
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen']
b = ['hangcheng', 'xixiang', 'xinan', 'fuyong', 'shajin', 'shiyan']
c = a + b
print(a)
print(b)
print(c)

# 将两个列表进行合并为一个列表--将列表b合并到列表a
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen']
b = ['hangcheng', 'xixiang', 'xinan', 'fuyong', 'shajin', 'shiyan']
a.extend(b)
print(a)
print(b)

# 将两个列表进行合并为一个列表--将列表a合并到列表b
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen']
b = ['hangcheng', 'xixiang', 'xinan', 'fuyong', 'shajin', 'shiyan']
b.extend(a)
print(a)
print(b)

# 列表的修改（二）
'''
使用append()添加元素到尾部
使用pop()删除指定位置的元素
'''
# 列表尾部添加元素--列表a尾部添加元素4和5
a = [1, 2, 3]
a.append(4)
a.append(5)
print(a)

# 删除列表指定位置的元素--删除列表a中第三个元素
a = [1, 2, 3, 4, 5]
a.pop(2)
print(a)

# 删除列表元素最后一个元素--删除列表a的最后一个元素
a = [1, 2, 3, 4, 5]
a.pop()
print(a)

# 列表的修改（三）
'''
del 删除指定位置的元素
remove() 删除某个元素
insert() 插入某个元素
'''

# 删除列表指定位置的元素--删除列表a中第三个元素
a = [1, 2, 3, 4, 5]
del a[2]
print(a)

# 删除列表中的某个元素--删除列表a中的元素3
a = [1, 2, 3, 4, 5]
a.remove(3)
print(a)

# 在列表指定位置插入元素
a = [1, 2, 3, 4, 5]
a.insert(0, 10)
print(a)

# 列表元素的判断(一)
'''
使用 in 判断一个元素是否在list中
使用.sort()排序
使用len()获取列表的长度
'''

# 判断某元素是否在列表中--元素3是否在列表a中
a = [1, 2, 3, 4, 5]
b = 3 in a
c = 6 in a
print(b)
print(c)

# 对列表中的元素进行排序--对列表a中的元素进行排序
a = [3, 5, 7, 1, 2, 6]
a.sort()
print(a)

# 获取列表的长度--获取列表a的长度
a = [1, 2, 3, 4, 5]
b = len(a)
print(b)

# 列表元素的判断（二）
'''
使用 index 判断一个元素的位置
使用count()查询元素出现的次数
'''

# 判断某一元素在列表中的位置--判断3在列表a中的位置
a = [1, 2, 3, 4, 5]
b = a.index(3)
print(b)

# 查询元素在列表中出现的次数--元素3在列表a中出现的次数
a = [1, 2, 3, 4, 5]
b = a.count(3)
print(b)

a = [3, 2, 3, 4, 3]
b = a.count(3)
print(b)

# 作业
#创建列表a
a = ['beiing', 'shanghai', 'guangzhou', 'shenzhen']
#在列表a尾部添加dongguan、huizhou这两个元素
a.append('dongguan')
a.append('huizhou')
print(a)

#删除列表a中huizhou这个元素
a.remove('huizhou')
print(a)
