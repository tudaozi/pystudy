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
我们前面讲过的列表、字符串、元组、集合等都是可以迭代的。
对字典的迭代：
        默认返回的是字典的key
        可以单独对values和items迭代
'''

# 将列表中的所有元素打印出来
list1 = ['xiaoli', 'xiaowang', 'xiaoming']
for name in list1:
    print(name)

# 将字符串中的所有字母打印出来
for letter in 'beijing':  # for a in b,a是b中的下一级元素或b的拆分
    print(letter.upper())

# 将字典中的所有key、values打印出来
dict1 = {'a': 1, 'b': 2, 'c': 3}
for key, values in dict1.items():
    print(key, values)

# 将字典中的所有key打印出来
dict1 = {'a': 1, 'b': 2, 'c': 3}
for key in dict1:
    print(key)

# 将字典中的所有values打印出来
dict1 = {'a': 1, 'b': 2, 'c': 3}
for values in dict1.values():
    print(values)

# 将元组中的所有元素打印出来
tuple1 = (1, 2, 3,)
for name in tuple1:
    print(name)

# 将集合中的所有元素打印出来
set1 = {'a', 'b', 'c'}
for name in set1:
    print(name)

# zip()函数并行迭代器
'''
将多个相同类型序列进行对应组合并压缩
每循环一次，释放一组组合
多个序列中最少的序列用完后停止释放组合
zip()同时对多个序列迭代
'''

# zip()迭代器功能展示
list1 = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
list2 = ['huabei', 'huadong', 'huanan', 'huanan']
list3 = ['zhongguo', 'zhongguo', 'zhongguo']
print(zip(list1, list2, list3))
list4 = list(zip(list1, list2, list3))
print(list4)

# 使用for对zip()迭代器进行遍历
list1 = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
list2 = ['huabei', 'huadong', 'huanan', 'huanan']
list3 = ['zhongguo', 'zhongguo', 'zhongguo']
for chenshi, weizhi, guojia in zip(list1, list2, list3):
    print(chenshi, weizhi, guojia)

# range()生成自然数序列
'''
格式：
    range(star,end,step)
'''

# 打印range的实际参数
print(list(range(10)))

# range默认从0开始，如果没有填写开始项，默认是range(0,10)
for i in range(10):
    print(i * i)

# range指定从某值开始到某某值，步长是某某某
for i in range(2, 10, 2):
    print(i * i)

# 推导式
'''
列表推导式：
  [x for x in range(100)  if x%2==0]
  字典推导式
'''

# 使用常规方法将0-10之间的所有数的平方变成列表
square = []
for i in range(10):
    square.append(i * i)
print(square)

# 使用推导式将0-10之间的所有数的平方变成列表
[i * i for i in range(10)]

# 元组--不能使用推导式,使用括号
list1 = list(i * i for i in range(10))
print(list1)

# 集合
set1 = set()
for i in range(10):
    set1.add(i * i)
print(set1)

{i * i for i in range(10)}

{word for word in ['xiaom', 'xiaop', 'xiaoq', 'yaom'] if word.startswith('yao')}

# 字典
{word: type(word) for word in range(10)}

{word: len(word) for word in ['xiaom', 'xiaop', 'xiaoq', 'yaom'] if word.startswith('xiao')}
