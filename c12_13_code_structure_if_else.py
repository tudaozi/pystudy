#!/usr/bin/env python
# encoding: utf-8
'''
@author: Tudaozi
@contact: tudaozi@126.com
@project: pystudy
@file: code_structure_if_else.py
@time: 2019-02-08 18:39
@desc:
'''

# Python代码结构
'''
Python使用缩进区分代码块
#既可以单独一行，也可在同一行
一行写不完，可以用 \ 放在行尾
'''

'''
使用If,elif,else进行判断
if else这样的语句是自顶往下执行的
'''

# if-else
height = 190
if height > 180:
    print('height')
else:
    print('no height')

# if-elif-else
height = 170
if height > 180:
    print('height')
elif height < 170:
    print('no height')
elif 170 < height < 175:
    print('no height')
else:
    print('no no no height')

# 常见的比较判断操作符
'''
==     相等              ！=    不等于
<        小于             <=     小于等于
>        大于             >=     大于等于
in       属于（被包含）
通过返回的布尔值（True或False）来判断
'''

# 判断两个元素是否相等，如果相等输出True，如果不相等输出False
a = 1
b = 1
if a == b:
    print('True')
else:
    print('False')

# 判断a是否等于b，如果相等输出True，如果不相等输出False
a = 1
b = 1
if a != b:
    print('True')
else:
    print('False')

# 判断a是否小于b，如果小于输出True，如果不小于输出False
a = 1
b = 2
if a < b:
    print('True')
else:
    print('False')

# 判断a元素是否在b列表中，如果是输出True，如果不是输出False
a = 1
b = [1, 2, 3]
if a in b:
    print('True')
else:
    print('False')

# 布尔操作符
'''
and
or
not
'''

# 关于True和False
'''
以下情况属于False：
None
0     和   0.0
‘’、 []  、()、{}、set()
'''

print(bool())
print(bool([]))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(()))
print(bool({}))
print(bool(set()))
