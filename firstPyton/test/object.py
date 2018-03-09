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


class Child(Employee):
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print "调用子类方法"

    # def displayCount(self):     # 重写父类方法
    #     print "方法重写-调用子类的方法"


c = Child()
c.childMethod()
c.displayCount()

print 'hhh', issubclass(Child, Employee)  # 判断一个是是否是另一个类的子类或者子孙类
print 'll', isinstance(c, Employee)  # 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true
