# 递归函数
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))

## 使用尾递归
## @尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def tail_factorial(n, result):
    if n == 1:
       return result # 这里是关键的一步
    return tail_factorial(n-1, n*result)

print(tail_factorial(10, 1))
print(factorial(10))