# age = 18
# name = 'Tom'
# weight = 65.5
#
# print('今年我的年龄是%03d岁' % age) # %03d
# print('我的名字是%s' % name)
# print('我的体重是%.3f公斤' % weight)# %.3f
# print('我叫%s,今年%d岁。' % (name , age))# 输出多个
# print('我叫%s,今年%s岁。' % (name , age)) # %s可以输出整型，浮点型


"""
字符串常用操作

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)


























# str = '01234567'
# print(str[2:5:1])   #234
# print(str[2:5:2])   #24
# print(str[2:5])     #234
# print(str[:5])      #01234
# print(str[2:])      #234567
# print(str[:])       #01234567
#
# #负数测试
# print(str[::-1])    #76543210 如果步长为负数，表示倒叙选取
# print(str[-4:-1])   #456 表示从-4到-1位置输出，即倒数第四个到倒数第1个
#
# print(str[-4:-1:-1])#不能选取出数据：从-4开始到-1结束，选取方向为从左到右，但步长为-1，代表从右向左选取
# #如果选取方向（下标开始到结束的方向）和 步长的方向冲突，则无法选取数据。

# age = 18
# name = 'Tom'
# weight = 65.5
#
# print('今年我的年龄是%03d岁' % age) # %03d
# print('我的名字是%s' % name)
# print('我的体重是%.3f公斤' % weight)# %.3f
# print('我叫%s,今年%d岁。\n' % (name , age))# 输出多个
# print('我叫%s,今年%s岁。' % (name , age)) # %s可以输出整型，浮点型
#
# print(f'我的名字是{name},今年{age}岁了') # 结果：我的名字是Tom,今年18岁了

# print(7**2);

# str = 'hello'
# list = ['world']
# t = ('world',)
# print(str * 5) # 'hellohellohellohellohello'
# print(list * 5) # ['world','world','world','world','world']
# print(t * 5) # ('world','world','world','world','world')
#
#
# print('h' in str) # True

str = 'hello'
list = ['world']
t = ('world',)
s = {1,2,3}
dict = {'name':'Tom','age':20}

# print(len(str))
# print(len(dict))

# print(max(str))

