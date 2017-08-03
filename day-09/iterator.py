# 判断一个对象是否是可以迭代的 Iterable

from collections import Iterable

print(isinstance([], Iterable)) # True
print(isinstance((1,), Iterable)) # True
print(isinstance('', Iterable)) # True
print(isinstance({}, Iterable)) # True
print(isinstance(123, Iterable)) # False

# 判断一个对象是否是迭代器 Iterator
print('--- divider ---')

from collections import Iterator

print(isinstance((x for x in range(1)), Iterator)) # True
print(isinstance([], Iterator)) # False

print('--- divider ---')

# 将一个Iterable转变为Iterator
print(isinstance(iter([]), Iterator)) # True

iterator1 = iter([1, 2, 3])
print(iterator1)
for n in iterator1:
    print(n)