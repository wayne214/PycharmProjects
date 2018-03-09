# encoding=utf-8 中文编码
# 注释
'''
这是多行注释，使用单引号
'''
"""
这是多行注释，使用双引号
"""
# print '你好，世界'
# # 下面的程序执行后就会等待用户输入，按回车建就会退出
# # raw_input("\n\nPress the enter key to exit.")
# # Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
# import sys; x = 'hello'; sys.stdout.write(x + '\n')
# # 变量赋值
# counter = 100 # 整型
# mile = 100.0 # 浮点型
# name = 'json' # 字符串
# print counter, mile, name
# # 多个变量赋值
# a = b = c = 1
# a, b, c = 1, 2, 'jack'
# print a, b, c
# # 字符串 string
# str = 'Hello World!'
# print str
# print str[0]
# print str[2:5]
# print str[2:]
# print str * 2
# print str + "TEST"
# # 列表 list 使用 【】 标识
# list = ['wayne', 869, 2.32, 'john', 70.3]
# tinylist = [123, 'john']
# list[1] = 555
#
# print list # 完整列表
# print list[0] # 列表的第一个元素
# print list[1:3] # 输出下标一到三的元素，包含下标一元素，但是不包含下标三元素
# print list[1:]
# print list + tinylist
# print list * 2
# # 遍历list数组
# the_count = [1,2,3,4,5]
# for number in the_count:
#     print "This is count %d" % number
#
# # 元组tuple, 使用()标识, 内部使用逗号隔开， 但是元祖不能二次赋值，相当于只读列表
# tuple = ('runbo', 786, 22.3, 'json', 70.2)
# tinytuple = (123, 'world')
# print "tuple is  %d" % tuple[1]
# print tuple[1:2]
# print tuple[3:]
# print tuple * 3
# print tuple + tinytuple
# # 字典dictionary ，使用{}标识，有索引(key)和对应的值(value)组成
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
#
# print dict['one']  # 输出键为'one' 的值
# print dict[2]  # 输出键为 2 的值
# print tinydict  # 输出完整的字典
# print tinydict.keys()  # 输出所有键
# print tinydict.values()  # 输出所有值


# ---------运算符------
# a = 21
# b = 10
# c = 0
#
# c = a / b
# print "1 - c 的值为：", c
#
# a = 2
# b = 3
# c = a ** b
# print "2 - c 的值为：", c
#
# # 修改变量 a、b、c
# a = 2
# b = 3
# c = a*b
# print "3 - c 的值为：", c
#
# a = 10
# b = 5.0
# c = a // b
# print "4 - c 的值为：", c
#
# a = 4444
# b = 4444
# print (a is b)
#
# c = 5555; d = 5555
# print (c is d)
# ---------运算符-----------

# ------条件语句-------
# flag = False
# name = 'luren'
# if name == 'python':
#     flag = True
#     print 'welcome boss'
# else:
#     print name
#
# # elif 用法
# num = 2
# if num == 3:
#     print 'boss'
# elif num == 2:
#     print 'user'
# elif num == 1:
#     print 'worker'
# elif num < 0:
#     print 'error'
# else:
#     print 'roadman'
#
# # 简单语组
# var = 100
# if var == 100:
#     print '变量 var 的值为100'
#
# # 一个简单的条件循环语句实现汉诺塔问题
#
#
# def my_print(args):
#     print args
#
#
# def move(n, a, b, c):
#     my_print((a, '-->', c)) if n == 1 else (move(n-1, a, c, b) or move(1,a,b,c) or move(n-1,b,a,c))
# move(3, 'a', 'b', 'c')

# ------条件语句-------

# ------循环语句-------
# While循环语句
# 猜大小游戏
# import random
#
# s = int(random.uniform(1, 10))
# # print(s)
# m = int(input('输入整数：'))
# while m != s:
#     if m > s:
#         print '大了'
#         m = int(input('输入整数：'))
#     if m < s:
#         print '小了'
#         m = int(input('输入整数：'))
#     if m == s:
#         print 'OK'
#         break
# 九九乘法表
# i = 1
# while i:
#     j = 1
#     while j:
#         print j, "*", i, " = ", i * j, '  ',
#         if i == j:
#             break
#
#         j += 1
#         if j >= 10:
#             break
#
#     print "\n"
#     i += 1
#     if i >= 10:
#         break

# for 循环语句
# for letter in 'Python':
#     print '当前字母：', letter
#
# fruits = ['banana', 'apple',  'mango']
# for fruit in fruits:        # 第二个实例
#    print '当前水果 :', fruit
#
# sequence = [12, 34, 34, 23, 45, 76, 89]
# for i, j in enumerate(sequence):
#     print i, j
#
#
# width = int(raw_input('输入对角线长度： '))
# for row in range(width + 1):
#     for col in range(width + 1):
#         if ((abs(row - width / 2) + abs(col - width / 2)) == width / 2):
#             print "*",
#         else:
#             print " ",
#     print " "

# --------日期和时间------
# import time
#
# # 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
#
#
# import calendar
#
#
# cal = calendar.month(2017, 10)
# print cal
# --------日期和时间------

# --------函数------
#定义函数
# def printme( str ):
#     "打印传入的字符串"
#     print str
#     return
#
# #调用缓释
# printme('我爱你中国')
#
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2
#     print "函数内 : ", total
#     return total;
#
#
# # 调用sum函数
# total = sum(10, 20);
#
# # python使用lambda 来创建匿名函数
# # lambda只是一个表达式，函数体比def简单很多。
# # lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# # lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# # 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#
# summ = lambda arg1, arg2: arg1 + arg2;
#
# # 调用 函数
# print "相加后的值为：", summ(10, 20)
# --------函数---------------------

# --------模块-----------------


# --------模块------------
# 如果要给函数内的全局变量赋值，必须使用 global 语句。
# Money = 2000
#
#
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
#
#
# print Money
# AddMoney()
# print Money