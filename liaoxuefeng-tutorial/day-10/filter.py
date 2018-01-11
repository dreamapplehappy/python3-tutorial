# 使用函数filter

## [1, 3, 5]
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6])))

## ['A', 'dream']
print(list(filter(lambda s: s and s.strip(), ['A', '', 'dream'])))

## 打印一定范围的素数

def primes():
    # 构造初始序列
    def init_list():
        n = 1
        while True:
            n = n + 2
            yield n

    def _not_divisible(n):
        return lambda x: x % n != 0
    def not_divisible(n):
        def divisible(x):
            return x % n != 0
        return divisible

    yield 2
    l = init_list()
    while True:
        prime = next(l)
        yield prime
        # 这里不直接使用 lambda x: x % prime != 0
        # 因为要绑定prime
        l = filter(_not_divisible(prime), l)

my_primes = primes()

for p in my_primes:
    if p < 100:
        print(p)
    else:
        break


print(lambda x: x % n == 0)

from functools import reduce

def is_palindrome(n):
    l = []
    init_n = n
    while n > 9:
        k = n % 10
        l.append(k)
        n = n // 10
    l.append(n)

    reversed_n = reduce(lambda x, y: x * 10 + y, l)

    if init_n == reversed_n:
        return True
    else:
        return False

print(is_palindrome(808))

output = filter(is_palindrome, range(1, 1000))
print(list(output))

# 使用切片来做一个

def _is_palindrome(num):
    s = str(num)
    if s[::] == s[::-1]:
        return True
    else:
        return False

# 改进一下，选择使用三目运算符
def _is_palindrome2(num):
    s = str(num)
    return True if s[::] == s[::-1] else False

output = filter(_is_palindrome2, range(1, 1000))
print(list(output))