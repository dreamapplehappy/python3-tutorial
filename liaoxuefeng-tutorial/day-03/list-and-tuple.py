# list数据类型
# 类比JavaScript中的数组，实现增删改查功能
car = []
print(car) # 长度为0的list

car.append(1) # list增加元素
car.append(2)
print(car)

seat = ['red', 'blue']
car.append(seat)
car.append(3)
car.append(4)

ele1 = car.pop() # 删除最后一个元素
print(ele1)

car.append(4)
car.pop(3) # 删除指定位置的元素
print(car)

car.insert(0, 'start')
print(car)
print(len(car))

car[1] = 9
print(car) # 改变具体位置的值
print(car[3][1]) # 取出list中list的值 list可以当做多维数组使用

# 使用 tuple
tu = (1, 2, 3)
print(tu)
print(tu[0])
tu1 = (1) # 这相当于定义了 tu1 = liaoxuefeng-tutorial 而不是一个tuple
print(tu1)
tu2 = (1,) # 规定一个元素的tuple需要添加一个逗号
print(tu2) # 输出单个元素tuple也会加上一个逗号

# 第二次学习
classmates = ['张三', '李四', '王五'] # 这是list数据类型
# 末未添加
classmates.append('李狗蛋')
print(classmates)
# 尾部删除
classmates.pop()
print(classmates)
# 删除指定位置的元素
classmates.pop(0)
print(classmates)
# 在指定位置添加元素
classmates.insert(0, '张三')
print(classmates)
# 修改指定位置的元素
classmates[0] = '李狗蛋'
print(classmates)
# 打印指定位置的元素
print(classmates[-1])
print(classmates[0])

# 元组
atom = (1, 2, 3)
print(atom)

# 无法修改元素
# 一个元素的元组
atom1 = (1, )
print(atom1)
# 计算长度
print(len(classmates))

