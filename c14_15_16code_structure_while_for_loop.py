#!/usr/bin/env python
# encoding: utf-8
'''
@author: Tudaozi
@contact: tudaozi@126.com
@project: pystudy
@file: c14_15_16code_structure_while_for_loop.py
@time: 2019-02-09 15:33
@desc:
'''

# 循环与迭代
# while循环
'''
while  x：
            ….
 break和continue
 因此，pet是未被定义的“变量",因此无法判断逻辑的正确性。因此while 后面跟的语句，一定是逻辑可判断True或者False的才能执行。
'''

# 满足条件循环执行--while后面的条件满足时，继续执行下面的语句，不满足则停止
count = 10
while count > 0:
    print(count)
    count -= 1
    if count < 5:
        break

# 将输入的字符转换成大写，当输入q时退出程序
while True:
    stuff = input("string to upper, please input a string[q to quit]")
    if stuff == 'q':
        break
    print(stuff.upper())

# 将输入的字符转换成大写，当输入q时退出程序,当输入的数是偶数时，计算它的平方
while True:
    num = input("string to upper, please input a string[q to quit]")
    if num == 'q':
        break  # 满足条件直接退出循环，不在执行下面的语句，反之继续执行西面的语句。
    num = int(num)
    if num % 2 == 0:
        continue  # 满足条件重新循环，不在执行下面的语句，反之继续执行西面的语句。
    print(num * num)

# for循环
'''
for循环是最频繁使用的迭代器
我们前面讲过的列表、字符串、元祖、集合等都是可以迭代的。
'''

list1 = ['xiaoli', 'xiaowang', 'xiaoming']
for name in list1:
    print(name)
