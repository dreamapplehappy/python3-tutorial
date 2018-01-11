print(abs(-10))

print(abs) # <built-in function abs>

# 修改变量abs的指向

import builtins
builtins.abs = 10

# TypeError: 'int' object is not callable
# abs(10)

# 定义一个高阶函数
def sum(a, b, func):
    return func(a) + func(b)

# 这里重新定义abs函数 暂时没有异常捕获
def abs(x):
    if isinstance(x, (float, int)):
        if x > 0:
            return x
        else:
            return -x

print(sum(1, 2, abs)) # 3