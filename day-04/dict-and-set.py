# dict
score = {'dream': 100, 'apple': 99}
print(score['dream'])

# 向字典中添加数据
score['happy'] = 98
print(score)

# 检查一个key是否在字典中
print('dream' in score) # 使用in操作符
print('Dream' in score)

print(score.get('dream'))
print(score.get('Dream')) # None
print(score.get('Dream', -1)) # 不存在就返回给定的值

# 删除一条数据
# 使用pop删除数据 返回的结果就是删除的key相应的value值
print(score.pop('apple'))
print(score)

# set
s = {1, 2, 3} # 使用set字面量
print(s)
s.add(3) # 加入相同的元素不会起作用
print(s)
s.add(4)
print(s)
print(s.remove(4)) # 删除一个元素 返回值是None
print(s)

# 求集合的交集与并集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2) # 交集
print(s1 | s2) # 并集

s.add((1, 2, 3)) # 可以添加元组
print(s)
# s.add((1, [2, 3])) # 不可以添加tuple里面包含list就不是不可变的对象了
print(s)