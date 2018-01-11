
# 使用functools.partial创建偏函数
print(int('123')) # 123
print(int('123', base=8)) # 83

# 固定函数的部分参数
def int_base_2(x, base=2):
    return int(x, base)

print(int_base_2('1010110')) # 86

# 使用functools
import functools

int_base_2_v2 = functools.partial(int, base=2)

print(int_base_2_v2('1010110')) # 86

max_10 = functools.partial(max, 10)
print(max_10(2, 3, 4)) # 10