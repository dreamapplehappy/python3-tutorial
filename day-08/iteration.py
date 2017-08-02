# 迭代

## 迭代list
names = ['dream', 'apple', 'happy']

for name in names:
    print('Hello,', name)

# 迭代dict

classmates = {
    'dream': 18,
    'apple': 19,
    'happy': 20
}

# 迭代键
for key in classmates:
    print('key is:', key)

# 只迭代值
for value in classmates.values():
    print('value is:', value)

# 迭代键值对
for k,v in classmates.items():
    print('key is %s, and value is %s' % (k, v)) # 格式化的字符串

# 判断一些数据类型是否可以迭代

from collections import Iterable

print(isinstance('', Iterable)) # 字符串是可迭代的数据类型
print(isinstance([], Iterable)) # list是可迭代的数据类型
print(isinstance((1,), Iterable)) # tuple是可迭代的数据类型
print(isinstance({}, Iterable)) # dict是可迭代的数据类型

print(isinstance(123, Iterable)) # 整数不是可迭代的数据类型

# 使用enumerate函数将一个可以迭代的数据类型变成含有索引

fruits = ['apple', 'banana', 'orange']

fruits_with_index = list(enumerate(fruits, 0)) # [(0, 'apple'), (1, 'banana'), (2, 'orange')]
print(fruits_with_index)

fruits_with_index_1 = list(enumerate(fruits, 1)) # [(1, 'apple'), (2, 'banana'), (3, 'orange')]
print(fruits_with_index_1)

# for 后面的是一个tuple, 可以省略括号
for (index, value) in fruits_with_index_1:
    print(index, value)

for index, value in fruits_with_index_1:
    print(index, value)

for t in fruits_with_index_1:
    print(t) # t is a tuple
    print(isinstance(t, tuple)) # true

name = 'dreamapple'
name_letters = list(enumerate(name))

for char in name:
    print(char)

for index, letter in name_letters:
    print(index, letter)