# coding=utf-8

# Python编程语言零基础入门到爬虫实战
# Python编程语言零基础入门

# 1、Python的安装
# ..............

# 2、Python的运行

'''
1、使用交互式解释器‘python命令行’
2、使用Python文件‘.py结尾的文件’
'''

print(100)
print('Mac输出')

# 3、基本数据类型（一）

'''
布尔型：（True和False）
整型：如30
浮点型：如24.86
字符串：如‘nihao’

Python变量
对象类型是不可变
所以变量就是为方便引用一个值（对象）,给它取得名字。
变量用 = 赋值
变量名智能包含大小写、数字、下划线

'''
a = 3 // 2
print(a)

# 8、基本数据结构-列表
'''
创建一个包含beijing、shanghai、tianjin、chongqing、qingdao的列表
在列表最后添加jinan和wuhan
删除列表中的chongqing
对列表排序
'''

a = ['beijing', 'shanghai', 'tianjing', 'chongqing', 'qingdao']
print(a)

a=list('abcdefg')
print(a)
#a[:-2:3]   3就是步长比
a=list('abcdefg')
a[0]