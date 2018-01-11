# 调用函数
print(abs(-100)) # 求一个数的绝对值使用abs()

# max函数返回给出的参数中最大的一个参数
print(max(1, 2, 3, -4))

# 使用数据类型转换
# int()
print(int('123')) # 123
# float()
print(float('123.56')) # 123.56
# str()
print(str(123)) # '123'
# bool()
print(bool(0)) # False
print(bool(1)) # True

# hex()
print(hex(123456)) # 0x1e240

# 第二次学习
print(abs(-7))
print(int(2.3))
print(int(0))
print(float(2))
print(max(2, 4, 7))
print(hex(234))
# print(hex(234, 345)) 参数的数量不对

import math
from def_my_func import dr_abs
from def_my_func import dr_empty
from def_my_func import move
print(dr_abs(2))
# print(dr_abs('official-tutorial')) 这里会报错 传递参数的类型不对
print(dr_empty()) # None
print(move(1, 2, 3, math.pi / 4)) # 返回的值的类型是一个 tuple