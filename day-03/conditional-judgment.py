# 条件判断
a = 24
if a > 20:
    print('yeah, welcome!')
elif a > 30:
    print('hello, welcome')
else:
    print('nice, welcome')

age = input('输入您的年龄：')
age = int(age) # 将字符串转换整数
if age > 17:
    print('00前')
elif age > 27:
    print('90前')
else:
    print('00后')


# 第二次学习条件判断
if None:
    print('None')
else:
    print('Else if')

# 使用elif:
x = input('请输入一个数字：')
num = int(x)
if num >= 8:
    print('num >= 8')
elif num >= 3:
    print('num >= 3')
else:
    print('num?')