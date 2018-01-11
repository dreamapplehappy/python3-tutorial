def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-100))

# 使用pass
def my_pass(x):
    pass # TODO

print(my_pass(1))

# 处理错误类型
def my_new_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError('不是正确的参数类型')
    else:
        if x >= 0:
            return x
        else:
            return -x

print(my_new_abs(1))

# 函数的返回结果是一个tuple
def fetch_result():
    return 1, 2, (3, 4, 5), [6, 7] # 函数的这种返回结果很有用

a, b, c, d = fetch_result()
print(a, b, c, d)