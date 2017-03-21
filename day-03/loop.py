# 循环
# for...in循环
for name in ['张三', '李四', '王五']:
    print(name)

# 使用for循环计算1+2+3+...+100
# 使用range()产生一个整数列表
sum = 0
for num in list(range(101)):
    sum += num
print(sum)

# 使用while循环
sum = 0
n = 100
while n > 0:
    sum += n
    n -= 2
print(sum)

# break:退出循环 continue:退出本次循环
sum = 0
n = 100
while n > 0:
    if n < 50:
        break
    n -= 2
    sum += n
print(sum)

sum = 0
n = 100
while n > 0:
    if n % 2 == 1: # 小心这里如果是 n % 2 == 0 的话就是死循环了
        continue
    n -= 2
    sum += n
print(sum)