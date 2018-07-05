#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'dreamapple'

# 布尔型
is_a_man = True
print(is_a_man)

# 数值类型
# 可以使用 type() 函数来检测任何值或变量的类型
print(type(1))
print(type(1.0))
# 可使用 isinstance() 函数判断某个值或变量是否为给定某个类型
print(isinstance(1, int))
print(type(int))
# 可以通过调用 int() 将 float 强制转换为 int
# int() 将进行取整，而不是四舍五入
print(int(2.34))
print(int(2.64))
# int() 函数朝着 0 的方法进行取整。它是个真正的取整（截断）函数，而不是 floor［地板］函数
print(int(-2.34))
print(int(-2.64))
# 通过调用float() 函数，可以显示地将 int 强制转换为 float
print(float(2))
# 浮点数精确到小数点后 15 位
print(1.123456789012345666666)
# 整数可以任意大
print(100000000000000000000000000000000003)


# 常见数值运算 TODO


