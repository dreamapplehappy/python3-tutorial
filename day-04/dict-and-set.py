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

# 第二次学习
# dict
classmates = {
    'zhangsan': '张三',
    'lisi': '李四',
    'wangwu': '王五',
}
# 查找
print(classmates['zhangsan'])
# 替换
classmates['zhangsan'] = '三张'
print(classmates)
# 删除某个key
classmates.pop('zhangsan')
print(classmates)
# 哪一个键是否存在
print('zhangsan' in classmates)
print(classmates.get('zhangsan'))
print(classmates.get('zhangsan', -1))
# 添加键值
classmates['ligoudan'] = '李狗蛋'
print(classmates)

# set
arr = {1, 2, 3} # 不重合的元素
print(arr)
arr.add(3) # 重合的元素
print(arr)
arr.add(4)
print(arr)

arr1 = {3, 4, 5}
print(arr1 & arr) # 求两个集合的交集
print(arr1 | arr) # 求两个集合的并集

# arr1.add([1, 2, 3]) 不可以添加list元素，因为list元素是可变的
arr1.remove(5) # 删除一个元素
print(arr1)
arr1.add((1, 2, 3))
print(arr1)
# arr1.add((1, 2, [1, 2])) # 元组里面包含可变的list所以也是不可以的