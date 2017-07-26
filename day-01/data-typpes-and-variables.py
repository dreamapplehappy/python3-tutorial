# 整数
import math
from math import inf
a = 100
# 浮点数
b = 0.333
c = 1.3e12
d = 1.2e-4
# 字符串
e = 'hello'
f = "hello"
g = 'I\'m OK'
# 转义
h = '\\'
# 输出上面的变量
print(a, b, c, d, e, f, g, h)
# r'' 内的字符串默认不转义
print(r'\n\t\\\\\\\\')
# 使用'''...'''
print('''hello,
world\\
welcome''')
# 使用r'''...'''
print(r'''hello,
world\\
welcome''')
# 布尔值
i = True
j = False
print(i, j)
# 运算符
k = i and True
l = i or j
m = not i
print(k, l, m)
# 常量按照约定俗成全部使用大写
PI = 3.1415926
# 空值
n = None
print(n)
# 除法 / 结果是小数； // 结果是整数，向下取整
o1 = 10 / 3
o2 = 10 // 3
print(o1, o2)
# 求模
p = 10 % 3
print(p)
# 无限大
r = inf
print(r)

# 第二次练习
# 字符串
print('====== 第二次练习 ======')
print('a')
print('"a"')
print('\'a"')
print('\n')
print(r'\n')
print('''the first line
the second line\n
the third line''')
print(r'''the first line
the second line\n
the third line''')
# 布尔值 注意大小写
print(0 > 1)
print(2 > 1)
print(True, False)
# 布尔运算
print(0 and 1)
print(1 and 1)
print(0 or 1)
print(0 or 0)
print(not 0)
print(not 1)
# 空值
print(None)
# 除法运算
print(10 / 3)
print(9 / 3)
# 地板除
print(10 // 3)
print(9 // 3)
print(10 % 3)
print(9 % 3)
# 无限大的数
print(10e100)

print(float('NaN'))
print(math.isnan(0))
