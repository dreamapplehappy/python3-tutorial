# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# """ a test module """
#
# __author__ = 'dreamapple'
#
# import fractions
# import math
#
# # 布尔型
# is_a_man = True
# print(is_a_man)
#
# # 数值类型
# # 可以使用 type() 函数来检测任何值或变量的类型
# print(type(1))
# print(type(1.0))
# # 可使用 isinstance() 函数判断某个值或变量是否为给定某个类型
# print(isinstance(1, int))
# print(type(int))
# # 可以通过调用 int() 将 float 强制转换为 int
# # int() 将进行取整，而不是四舍五入
# print(int(2.34))
# print(int(2.64))
# # int() 函数朝着 0 的方法进行取整。它是个真正的取整（截断）函数，而不是 floor［地板］函数
# print(int(-2.34))
# print(int(-2.64))
# # 通过调用float() 函数，可以显示地将 int 强制转换为 float
# print(float(2))
# # 浮点数精确到小数点后 15 位
# print(1.123456789012345666666)
# # 整数可以任意大
# print(100000000000000000000000000000000003)
#
#
# # 常见数值运算
# print('\n')
# print(11 / 2) # / 运算得到的是浮点数
# print(11 // 2) # 如果 // 左右的数值都是整数，那么结果也是整数
# print(11 // 6) # // 运算结果是向下取整
# print(-11 // 6)
# print(11.0 // 2) # // 运算符并非总是返回整数结果，如果分子或者分母是 float，它的返回值将会是 float 类型
# print(3 ** 4)
# print(3.1 ** 2)
# print(10 % 3)
# print(10.0 % 3)
#
# # 分数
# x = fractions.Fraction(1, 3)
# print(x)
# print(type(x))
# x = 2 * x
# print(x)
# y = fractions.Fraction(3, 2)
# print(x * y)
#
# # 三角函数
# print('\n')
# print(math.pi)
# print(math.sin(math.pi / 2))
# print(math.tan(math.pi / 4))
#
# # 布尔类型
# print('\n')
def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")
#
# is_it_true(1)
# is_it_true(-1)
# is_it_true(0)
# is_it_true(0.1)
# is_it_true(0.0)
# is_it_true(fractions.Fraction(1, 2))
# is_it_true(fractions.Fraction(0, 2))
#
# # 列表
# print('\n')
# a_list = [1, 'a', True, fractions.Fraction(1, 3), [1, 2, 3]]
# print(a_list)
# print(a_list[3])
# print(a_list[-2])
# print(len(a_list))
# # 列表切片
# print(a_list[0:3])
# print(a_list[:3])
# print(a_list[1:5])
# print(a_list[1:])
# print(a_list[1:-1])
# print(a_list[1:-2])
# print(a_list[-2:1]) # []
# # 向列表中新增项
# print('------')
# b_list = [1]
# b_list += [True]
# print(b_list)
# b_list.append('hello')
# print(b_list)
# b_list.extend([3, 4, 5])
# print(b_list)
# b_list.insert(1, fractions.Fraction(1, 3))
# print(b_list)
# print('------')
# c_list = [1, 2, 3]
# print(c_list)
# c_list.extend([4, 5, 6])
# print(c_list)
# c_list.append([4, 5, 6])
# print(c_list)
# # 在列表中检索值
# print('------')
# print(2 in c_list)
# print(c_list.count(2))
# print(c_list.index(2))
# # print(c_list.index(2, 3, 5)) # ValueError: 2 is not in list
#
# # 从列表中删除元素
# print('------')
# d_list = [1, 3, 5, 7, 9]
# print(d_list)
# # 使用 del 语句从列表中删除某个特定元素
# del d_list[0]
# print(d_list)
# del d_list[:2]
# print(d_list)
# d_list.append(9)
# print(d_list)
# # 通过 remove() 方法从列表中删除某个元素。remove() 方法接受一个 value 参数，并删除列表中该值的第一次出现
# d_list.remove(9)
# print(d_list)
# d_list.remove(9)
# print(d_list)
# print('------')
# e_list = [1, 2, 3, 4, 5, 6]
# print(e_list)
# print(e_list.pop())
# print(e_list)
# print(e_list.pop(0))
# print(e_list)
# # 布尔上下文环境中的列表
# # 在布尔类型上下文环境中，空列表为假值
# # 任何至少包含一个上元素的列表为真值
# # 任何至少包含一个上元素的列表为真值。元素的值无关紧要
# f_list = []
# is_it_true(f_list)
# f_list.append(False)
# is_it_true(f_list)
#
# # 元组
# # 元组的定义方式和列表相同，除了整个元素的集合都用圆括号，而不是方括号闭合
# a_tuple = (1, 2, 3, 4, 5)
# print(a_tuple)
# print(a_tuple[0])
# print(a_tuple[-1])
# print(a_tuple[:-1])
# # 元组和列表的主要区别是元组不能进行修改
# print(2 in a_tuple)
# print(a_tuple.index(2))
# # 元组可转换成列表，反之亦然。内建的 tuple() 函数接受一个列表参数，并返回一个包含同样元素的元组，而 list() 函数接受一个元组参数并返回一个列表
# print(tuple([1, 2, 3]))

# 布尔上下文环境中的元组
is_it_true(())
is_it_true(('a', 'b'))
is_it_true((False,))
is_it_true((False))

print(type((False,)))
print(type((False)))

# 同时赋多个值
v = ('a', 1, True)
(v1, v2, v3) = v
# TODO print函数是否可以一次打印多个值
print(v1, v2, v3)

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)

# 集合
a_set = {1}
print(a_set)
print(type(a_set))
# TODO list中含有True转换为set值缺少
# http://pythontutor.com/visualize.html#code=a_list%20%3D%20%5B1,%202,%20True%5D%0Aprint%28set%28a_list%29%29%0A%0Ab_list%20%3D%20%5BTrue,%201,%202%5D%0Aprint%28set%28b_list%29%29&cumulative=false&curInstr=4&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# a_list = [1, 'hello', True]
a_list = [1, True]
# a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
print(a_set)

a_set = set()
print(a_set)
print(type(a_set))
print(len(a_set))

not_sure = {}
print(type(not_sure))

# 修改集合
a_set = {1, 2, 3}
a_set.add(5)
print(a_set)

a_set.update({2, 3, 7, 8})
print(a_set)
a_set.update({9, 10}, {10, 11, 12})
print(a_set)

# 从集合中删除元素
a_set.discard(2)
print(a_set)
a_set.discard(2)
print(a_set)

a_set.remove(3)
print(a_set)
# remove() 方法也接受一个单值作为参数，也从集合中将其删除。如果该值不在集合中，remove() 方法引发一个 KeyError 例外
# a_set.remove(3)
# print(a_set)

print(a_set.pop())
print(a_set.pop())

a_set.clear()
print(a_set)
# a_set.pop()

# 常见集合操作
a_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b_set = {6, 7, 8, 9, 10, 11, 12, 13, 14}
print(3 in a_set)
print(3 in b_set)

print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set.symmetric_difference(b_set))
print(a_set.difference(b_set))
print(b_set.difference(a_set))

a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
print(a_set.issubset(b_set))
print(b_set.issuperset(a_set))

# 布尔上下文环境中的集合
is_it_true(set())
is_it_true({False})


# 字典

a_dict = {'name': 'dreamapple', 'age': 25}
print(a_dict)
print(a_dict['name'])
a_dict['name'] = 'happy'
print(a_dict['name'])
a_dict['job'] = 'Front end Engineer'
print(a_dict)
a_dict[1] = 'first'
print(a_dict)

print(len(a_dict))
print(1 in a_dict)

is_it_true({})
is_it_true({'a': 1})

# None
print(type(None))
print(None == False)

is_it_true(None)
is_it_true(not None)