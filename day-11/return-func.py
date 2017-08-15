# 返回函数

def calc_sum(*arg):
    sum = 0
    for num in arg:
        sum += num
    return sum

print(calc_sum(1, 2, 3)) # 6

def lazy_sum(*arg):
    def sum():
        lsum = 0
        for num in arg:
            lsum += num
        return lsum
    return sum

print(lazy_sum(1,2,3))
print(lazy_sum(1,2,3)())

def count():
    l = []
    for n in range(1,4):
        def f():
            return n * n
        l.append(f)
    return l

f1, f2, f3 = count()
print(f1, f2, f3)
print(f1(), f2(), f3())

print(range(4)) # range(0, 4)
print(range(1,4)) # range(1, 4)


# 使用闭包

def closure_count():
    l = []
    for n in range(4):
        def compute(k):
            def c():
                return k * k
            return c
        l.append(compute(n))
    return l

c0, c1, c2, c3 = closure_count()

print(c0, c1, c2, c3)
print(c0(), c1(), c2(), c3())

print('--- divider ---')
def closure_count2():
    l = []
    for n in range(4):
        # 添加默认参数
        l.append(lambda x = n: x * x)
    return l

a0, a1, a2, a3 = closure_count2()
print(closure_count2())
print(a0, a1, a2, a3)
print(a0(), a1(), a2(), a3())

