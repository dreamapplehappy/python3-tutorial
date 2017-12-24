# map函数

l = list(range(10))

def f(x):
    return x * x

print(map(f, l)) # <map object at 0x10373c7f0>

print(list(map(f, l))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(str, l))) # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce
from functools import reduce

print(sum(l)) # 45

def add(a, b):
    return a + b

print(reduce(add, l)) # 45

l1 = [1, 3, 5, 7, 9]

def fn(a, b):
    return a * 10 + b

print(reduce(fn, l1)) # 13579

# 将字符串转变为整数

def str2int(string):
    str2int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def compute(a, b):
        return a * 10 + b
    def char2int(s):
        return str2int_dict[s]

    return reduce(compute, map(char2int, string))

print(str2int('12345')) # 12345

# test.md 1
def normalize(name):
    return name.capitalize() # 使用字符串的capitalize方法
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# test2
def prod(L):
    def multi(a, b):
        return a * b
    return reduce(multi, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# test3 这个函数写的有点长可以优化的
def str2float(string):
    str2int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    '.': -1}

    def char2digital(s):
        return str2int_dict[s]
    def compute_int_part(x, y):
        return x * 10 + y
    def compute_decimal_part(x, y):
        return (x * 10 + y)

    digital_list = list(map(char2digital, string))

    if -1 in digital_list:
        negative_index = digital_list.index(-1)
        int_part_list = digital_list[:negative_index]
        decimal_part_list = digital_list[negative_index + 1:]
        decimal_part_list_len = len(decimal_part_list)
        if len(int_part_list) > 0:
            int_part = reduce(compute_int_part, int_part_list)
            decimal_part = reduce(compute_decimal_part, decimal_part_list)
            return int_part + decimal_part / pow(10, decimal_part_list_len)
        else:
            decimal_part = reduce(compute_decimal_part, decimal_part_list)
            return decimal_part / pow(10, decimal_part_list_len)

    else:
        int_part_list = digital_list[:]
        return reduce(compute_int_part, int_part_list)





print(str2float('123.456'))
print(str2float('123.1'))
print(str2float('123'))
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

# 1.lambda 2 nonlocal

# lambda是一个表达式
print(lambda x, y: x + y) # <function <lambda> at 0x104bfdf28>
add_x_y = lambda x, y : x + y
print(add_x_y(1, 2)) # 3

def str2float2(string):
    str2int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    '.': -1}
    l = list(map(lambda s: str2int_dict[s], string))

    has_point = False
    step = 1

    def compute(f, point):
        if point == -1:
            nonlocal has_point
            has_point = True
            return f

        if has_point:
            nonlocal step
            step = step * 10
            return f + point / step
        else:
            return f * 10 + point

    x = reduce(compute, l, 0.0)

    return x

print(str2float2('123.456'))
print(str2float2('.456'))
print(str2float2('0.456'))

