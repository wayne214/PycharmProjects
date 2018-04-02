#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 面向对象


class Employee:
    '所有员工的基类'
    __secretCount = 1   # 私有变量
    empCount = 0        # 公开变量

    def __init__(self, name, salary):   # 构造函数
        self.name = name        # self 代表类的实例，而非类
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.__secretCount

    def displayEmployee(self):
        print "Name: ", self.name, "，Age: ", self.age, "，Salary: ", self.salary

    # def __del__(self):  # 在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
    #     class_name = self.__class__.__name__
    #     print class_name, "销毁"

"创建Employee类的实例"
e = Employee('wayne', 14000)
e.age = 27  # 添加一个'age'属性
e.age = 28  # 修改'age'属性
# del e.age   # 删除'age'属性
e.displayCount()    # 访问类的属性
e.displayEmployee()
setattr(e, 'age', 21)  # 设置属性的值
# delattr(e, 'age')  # 删除属性
print '判断是否存在属性age', hasattr(e, 'age')
print '获取属性age的值', getattr(e, 'age')
# print e.__secretCount      # Python不允许实例化的类访问私有数据
# print '设置属性age的值', setattr(e, 'age', 21)
print e._Employee__secretCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

# del e

# 类的继承


class Child(Employee):
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法"

    def displayCount(self):
        print "子类重写父类的方法的"

    # def displayCount(self):     # 重写父类方法
    #     print "方法重写-调用子类的方法"


c = Child()
c.childMethod()
c.displayCount()  # 调用父类的方法

print 'hhh', issubclass(Child, Employee)  # 判断一个是是否是另一个类的子类或者子孙类
print 'll', isinstance(c, Employee)  # 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true

# 类的属性和方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
#
# 类的方法
# 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
#
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用


class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print "count1", self.__secretCount

    def count2(self):
        print "count2", self.__secretCount


counter = JustCounter()
# counter.count()
# counter.count()

print counter.publicCount
# print "self.secretCount", counter.count2()
# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性
print counter._JustCounter__secretCount

try:
    counter.count2()
except IOError:
    print "不能调用非公有属性！"
else:
    print "OK!"  # 现在呢，证明是滴


# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。