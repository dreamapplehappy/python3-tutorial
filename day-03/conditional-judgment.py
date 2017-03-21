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