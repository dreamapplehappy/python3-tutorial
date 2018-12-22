# 列表的增删改查
num = [1, 3, 5, 7, 9]

# 列表增加一个元素
num.append(10)
print(num)
num.insert(0, 0)
print(num)

# 删除一个元素
del num[1]
print(num)
num.remove(7)
print(num)

# 修改一个元素
num[0] = -1
print(num)

# 查找一个元素
print(num.index(9))

# 列表排序
num.insert(0, 8)
print(num)
num.sort()
print(num)

characters = ['a', 'b', 'C', 'A', 'c', 'B']
characters.sort()
print(characters)
characters.sort(reverse=True)
print(characters)
characters.sort(key=str.lower)
print(characters)

print('Hello ' + \
      'World!')