## 生成器，先练习作业

### 第一次的思路，感觉不是很好
def yang_hui_trangle():
    n, l = 1, []
    while n:
        if n == 1:
            l = [1]
            yield [1]
        elif n == 2:
            l = [1, 1]
            yield [1, 1]
        else:
            pre_list_len, index = len(l), 1
            new_list = [1 for n in range(0, pre_list_len + 1)]
            while index < pre_list_len:
                new_list[index] = l[index - 1] + l[index]
                index = index + 1
            l = new_list
            yield l
        n = n + 1

g = yang_hui_trangle()

times = 0
for n in g:
    if times < 10:
        print(n)
        times = times + 1
    else:
        break


# TODO liaoxuefeng-tutorial.为什么python没有i++ official-tutorial.更好的杨辉三角解决方案

# 学习generator

g = ( n * n for n in range(10))
print(g)
# print(next(g))
for n in g:
    print(n)


a = 1
b = 2

a, b = b, a+b
print(a, b)

# 定义一个generator
def odd():
    print('the first step')
    yield 1
    print('the second step')
    yield 3
    print('the third step')
    yield 5

g1 = odd()
print(next(g1))
print('------')
print(next(g1))
print('------')
print(next(g1))
print('------')
# StopIteration
# print(next(g1))

# fibonacci

def fibonacci(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield a
        a, b = b, a+b
        n = n + 1
    return 'done'

g2 = fibonacci(10)

for n in g2:
    print(n)

g3 = fibonacci(6)

print('------')

while True:
    try:
        print(next(g3))
    except StopIteration as e:
        print(e.value)
        break # 这里要使用break终止程序的运行

# 一些其他的解决办法

# 通过前后补零来实现
def yang_hui_trangle7():
    p = [1]
    while True:
        yield p
        p.insert(0,0)
        p.append(0)
        p = [p[i] + p[i+1] for i in range(len(p) - 1)]

# 很巧妙 借助两个数组前后补零
def yang_hui_trangle8():
    p = [1]
    while True:
        yield p
        a = p[:]
        b = p[:]
        a.insert(0,0)
        b.append(0)
        p = [a[i] + b[i] for i in range(len(a))]

# 这个方法很巧妙 末尾补零
def yang_hui_trangle9():
    p = [1]
    while True:
        yield p
        p.append(0)
        p =  [p[i-1] + p[i] for i in range(len(p))]

# 这个方法和yang_hui_trangle8 异曲同工
def yang_hui_trangle10():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

print(list(range(2)))
l1 = list(range(2))
print(l1.insert(0, 0), l1)
