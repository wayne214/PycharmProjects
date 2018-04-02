#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 正则表达式
import re

# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print (re.match('www', 'www.baidu.com').span())  # 在起始位置匹配
print (re.match('com', 'www.baidu.com'))  # 不在起始位置匹配

line = "Cats are smater than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group()", matchObj.group()
    print "matchObj.group(1)", matchObj.group(1)
    print "matchObj.group(2)", matchObj.group(2)
else:
    print "No match!!"

# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
print (re.search('www', 'www.baidu.com').span())  # 在起始位置匹配
print (re.search('com', 'www.baidu.com').span())  # 不在起始位置匹配

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print "searchObj.group()", searchObj.group()
    print "searchObj.group(1)", searchObj.group(1)
    print "searchObj.group(2)", searchObj.group(2)
else:
    print "No match!"

# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# 检索和替换
# Python 的 re 模块提供了re.sub用于替换字符串中的匹配项。
phone = '2004-959-559 # 这是一个国外的电话号码'
# 删除字符串中的 python 注释
num = re.sub(r'#.*$', "", phone)
print "电话号码：", num
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print (re.sub('(?P<value>\d+)', double, s))

# re.compile 函数
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
#
# 语法格式为：

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print m
m = pattern.match('one12twothree34four', 2, 10)  # 从e的位置开始匹配，没有匹配
print m
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配, 返回一个match对象
print m

print m.group()
print m.start()
print m.end()
print m.span()

pattern2 = re.compile(r'([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m1 = pattern2.match('Hello World Wide Web')
print m1
print m1.group(0)
print m1.groups()

# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#
# 注意： match 和 search 是匹配一次 findall 匹配所有。

p = re.compile(r'\d+')
result1 = p.findall('www122 google 456')
result2 = p.findall('www88tt122google456', 0, 10)

print (result1)
print (result2)

# re.finditer
# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = re.finditer(r'\d+', '12a32bc34j56')
for match in it:
    print (match.group())

# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
split1 = re.split('\W+', 'runoob, runoob, runoob.')
print split1