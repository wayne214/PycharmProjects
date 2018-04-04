#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('google'):
    google_flag = '是'
else:
    google_flag = '否'

if form.getvalue('runoob'):
    runoob_flag = '是'
else:
    runoob_flag = '否'

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2>菜鸟教程选择了：%s</h2>" % runoob_flag
print "<h2>Google选择了：%s</h2>" % google_flag
print "</body>"
print "</html>"
