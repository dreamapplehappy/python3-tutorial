#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'dreamapple'

import fractions
import math

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


# 常见数值运算
print('\n')
print(11 / 2) # / 运算得到的是浮点数
print(11 // 2) # 如果 // 左右的数值都是整数，那么结果也是整数
print(11 // 6) # // 运算结果是向下取整
print(-11 // 6)
print(11.0 // 2) # // 运算符并非总是返回整数结果，如果分子或者分母是 float，它的返回值将会是 float 类型
print(3 ** 4)
print(3.1 ** 2)
print(10 % 3)
print(10.0 % 3)

# 分数
x = fractions.Fraction(1, 3)
print(x)
print(type(x))
x = 2 * x
print(x)
y = fractions.Fraction(3, 2)
print(x * y)

# 三角函数
print('\n')
print(math.pi)
print(math.sin(math.pi / 2))
print(math.tan(math.pi / 4))

# 布尔类型
print('\n')
def is_it_true(anything):
    if anything:
        print('{0} is true'.format(anything))
    else:
        print('{0} is false'.format(anything))

is_it_true(1)
is_it_true(-1)
is_it_true(0)
is_it_true(0.1)
is_it_true(0.0)
is_it_true(fractions.Fraction(1, 2))
is_it_true(fractions.Fraction(0, 2))

# 列表
print('\n')
a_list = [1, 'a', True, fractions.Fraction(1, 3), [1, 2, 3]]
print(a_list)
print(a_list[3])
print(a_list[-2])
print(len(a_list))
# 列表切片
print(a_list[0:3])
print(a_list[:3])
print(a_list[1:5])
print(a_list[1:])
print(a_list[1:-1])
print(a_list[1:-2])
print(a_list[-2:1]) # []
# 向列表中新增项
print('------')
b_list = [1]
b_list += [True]
print(b_list)
b_list.append('hello')
print(b_list)
b_list.extend([3, 4, 5])
print(b_list)
b_list.insert(1, fractions.Fraction(1, 3))
print(b_list)
print('------')
c_list = [1, 2, 3]
print(c_list)
c_list.extend([4, 5, 6])
print(c_list)
c_list.append([4, 5, 6])
print(c_list)
# 在列表中检索值
print('------')
print(2 in c_list)
print(c_list.count(2))
print(c_list.index(2))
# print(c_list.index(2, 3, 5)) # ValueError: 2 is not in list















