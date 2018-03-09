#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
print "Python 是一个非常棒的语言， 不是吗？"

# str = raw_input("请输入：");
# print "你输入的内容是：", str

# str = input("请输入：");
# print "你输入的内容是：", str

# 打开一个文件
# fo = open("foo.txt", "wb")
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace
# write()方法
# write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# write()方法不会在字符串的结尾添加换行符('\n')：
# fo.write( "www.runoob.com!\nVery good site!\n");

# 关闭打开的文件
# fo.close();

# 读取文件
# fo = open("foo.txt", "r+");
# str = fo.read(10);
# print "读取的字符串是：", str
# # 查找当前位置
# position = fo.tell();
# print "当前文件位置：", position
#
# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 1);
# str = fo.read();
# print "重新读取字符串：", str
# # 关闭文件
# fo.close();

# 重命名文件foo.txt到foo1.txt
# os.rename("foo.txt", "foo1.txt")

# 创建目录-mkdir()
# os.mkdir("newdir")
# 改变当前目录
# os.chdir("/home/newdir")
# 显示当前工作目录
# str = os.getcwd();
# print str


# 删除目录
os.rmdir("home/newdir")