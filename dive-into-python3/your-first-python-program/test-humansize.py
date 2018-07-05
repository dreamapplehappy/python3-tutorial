#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'dreamapple'

from humansize import approximate_size

# 测试传递参数的顺序
print(approximate_size(100000, True))
print(approximate_size(size=100000, a_kilobyte_is_1024_bytes=False))
print(approximate_size(a_kilobyte_is_1024_bytes=True, size=1000000))

print(approximate_size.__doc__)

# 使用 try...except 块来处理异常
try:
    not_define_var
except NameError:
    not_define_var = 1

print(not_define_var)