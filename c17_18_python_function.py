#!/usr/bin/env python
# encoding: utf-8
'''
@author: Tudaozi
@contact: tudaozi@126.com
@project: pystudy
@file: c17_18_python_function.py
@time: 2019-02-10 22:26
@desc:
'''

# Python函数

# 函数的定义
'''
函数：接收输入  返回结果
函数的定义：
     def donothing():
         函数内部代码
'''


# 创建一个简单的函数--print()是执行语句会直接打印结果--return * 是将结果返回给调用者
# 无参函数
def justprint():
    print('Hi')
    return False


word = justprint()  # 无参调用
print(word)

if justprint():
    print(print)
else:
    print('No')


# 有参函数
def shuru(something):
    return something + ' ' + something


diaoyong = shuru('haoduo')  # 有参调用
print(diaoyong)


# 有参数+条件函数
def i(num):
    if num % 2 == 0:
        return str(num) + '是偶数'
    else:
        return str(num) + '是奇数'


panduan = i(2)  # 调用
print(panduan)


# 函数参数--多个参数
def the_sum(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


sum_end = the_sum(1, 2, 3)
print(sum_end)
