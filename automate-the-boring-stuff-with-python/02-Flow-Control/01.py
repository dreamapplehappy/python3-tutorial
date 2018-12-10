# 布尔类型
print(True)
print(False)

# 比较运算符
print(1 == 3)
print(1 >= 3)
print(1 <= 3)
print(1 > 3)
print(1 < 3)
print(1 != 3)

# 布尔操作符
print(1 > 3 and 1 < 3)
print(1 > 3 or 1 < 3)
print(not 1 > 3)

# 运算的顺序
print(1 + 2 == 3 and not 1 > 3 or 2 + 4 <= 6)

# 控制流
name = 'dreamapple'
age = 25
if name == 'dreamapple':
    print('hello, dreamapple')
    if age > 18:
        print('wow')
    else:
        print('study')
else:
    print('sorry, you are not dreamapple')

# 使用elif的位置很重要
if age > 25:
    print('age > 25')
elif age > 10:
    print('age > 10')
else:
    print('age < 10')

#