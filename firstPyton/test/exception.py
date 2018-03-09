#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError, Argument:
    print "Error: 没有找到文件或读取文件失败, 没有文件写权限", Argument
else:
    print "内容写入文件成功"
    fh.close()
finally:
    print "Error: 我总是要执行的"

try:
    1 / 0
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print "0不能被除"
else:
    '''保护不抛出异常的代码'''
    print "没有异常"
finally:
    print "最后总是要执行我"