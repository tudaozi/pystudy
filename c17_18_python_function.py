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
    print(something + ' ' + something)


shuru('haoduo')  # 有参调用


# 有参数+条件函数
def i(num):
    if num % 2 == 0:
        print(str(num) + '是偶数')
    else:
        print(str(num) + '是奇数')


i(2)  # 调用


# 函数参数--多个参数
def the_sum(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)


the_sum(1, 2, 3)


# 位置参数

def the_name(name1, name2):
    print('my name is ' + name1)
    # return 'my name is' + name1
    print('my name is ' + name2)
    # return 'my name is' + name2


the_name('xiaoli', 'xiaozhang')


# 关键字参数
def gjzhs(name1, name2):
    print('我的名字是：' + name1)
    print('我的名字是：' + name2)


gjzhs(name1='xiaoli', name2='xiaoming')
gjzhs(name2='xiaoming', name1='xiaoli')


# 默认参数
def mrcs(mrcs_c1, mrcs_c2='我是默认参数2'):
    print('我是参数：' + mrcs_c1)
    print('我是参数：' + mrcs_c2)


mrcs('canshu1 ')


# 无数参数
def wscs(*arg):
    print(arg)


wscs(1, 2, 3, 4)


# 收集参数
def sjcs(*arg):
    for word in arg:
        print(word)


sjcs(1, 2, 3, 4, 5)

tuple1 = (1, 2, 3, 4, 5)
a, b, *arg = tuple1
print(a, b, *arg)


# 双新关键字参数
def sxcs(**arg1):
    '''
    :param arg1: 默认参数示例
    :return: 空
    '''
    print(arg1)


sxcs(a=1, b=2, c=3)
help(sxcs)
