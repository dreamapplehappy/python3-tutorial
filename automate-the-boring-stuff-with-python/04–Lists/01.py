users = ['dream', 'apple', 'happy']

print(users)
print(users[0])
print(users[1])
print(users[2])

# 负数下标
print(users[-1])
print(users[-2])
print(users[-3])

# 列表的切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:2])
print(numbers[:2])
print(numbers[1:])
print(numbers[:])

# 使用负数
print(numbers[-10:-1])
print(numbers[:-1])
print(numbers[-10:])

# 获取列表的长度
print(len(numbers))

numbers[0] = -1
print(numbers)

# 列表的连接和复制
testnumbers = [1, 3, 5, 7, 9]
print(numbers + testnumbers)
print(numbers * 2)

del numbers[0]
print(numbers)

# 列表的循环
for num in numbers:
    print('current number is: ' + str(num))

for i in range(len(numbers)):
    print('current number index is :' + str(i))

print(5 in numbers)
print(-5 in numbers)
print(-5 not in numbers)
print(5 not in numbers)

year, month, day = [2018, 12, 22]
print(year, month, day, sep='-')

test1 = 2
test1 += 2
print(test1)
test1 -= 1
print(test1)
test1 %= 2
print(test1)
test1 *= 10
print(test1)
test1 /= 3
print(test1)

