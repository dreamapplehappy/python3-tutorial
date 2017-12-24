# ## 第二次学习 ## #
# 定义函数的时候注意函数的参数的位置，必选参数，可选参数，可变参数，命名关键字参数，关键字参数

# 注意默认参数
def test1(list1=[]):
    list1.append('test.md')
    return list1


print(test1())
print(test1())
print(test1())
print(test1([1, 2, 3]))


# 参数的传递
def func1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


func1(1, 2, 3, 4, name='dreamapple', age=23)  # a= 1 b= 2 c= 3 args= (4,) kw= {'age': 23, 'name': 'dreamapple'}


def func2(a, b=0, *args, name, age, **kw):
    print('a =', a, 'b =', b, 'args =', args, 'name =', name, 'age =', age, 'kw =', kw)

func2(1, 2, 3, 4, 5, name='dreamapple', age=23, city='Hangzhou')

# ## 第一次学习 ## #

# 位置参数
def power(num):
    result = num * num
    return result
print(power(6))

# @计算任意n次方,使用默认参数n=2
def power1(num, n=2):
    result = 1
    while n > 0:
        result *= num
        n = n - 1
    return result
print(power1(6, 3))
print(power1(6))

# @一个注册的函数
def enroll(name, gender, age=7, city='Hangzhou'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('dream', 'male')

# 默认的参数可以不按照顺序来进行传参
enroll('dream', 'male', city='Wuhan')

# 参数为list
def add_end(L=[]):
    L.append('something')
    print(L)
    return L

add_end([1, 2, 3])
add_end([1, 2, 3])
# 使用默认参数
add_end()
add_end()

### 默认参数必须指向不变对象！
def advanced_add_end(L=None):
    if L is None:
       L = []
    L.append('something')
    print(L)
    return L

advanced_add_end()
advanced_add_end()

### 可变参数部分
def many_arguments(nums):
    sum = 0
    for num in nums:
        sum += num
    print(sum)
    return sum

many_arguments([1, 2, 3, 4, 5])

### @使用*
def advanced_many_args(*nums):
    print(nums) # 内部接受的参数是一个tuple
    sum = 0
    for num in nums:
        sum += num
    print(sum)
    return sum

arr1 = [2, 4, 5, 6]
advanced_many_args(1, 2, 3, 4)
# 可以在数组的前面加上一个星号
advanced_many_args(*arr1)
print(*arr1) #展开参数列表

# 关键字参数
def kw_func(name, age, **kw):
    print('name:', name)
    print('age:', age)
    print('kw:', kw)

kw_func('dream', 19, gender='male', score=100)

# 字典参数的分解
extra = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(extra)
kw_func('happy', 20, **extra) # 在这里把extra转换为键值对形式的参数

# 命名关键字参数
### 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *, city, job):
    print(name, age, city, job)


person('a', 10, city=2, job=3) # 命名关键字参数需要指定名字
# person('a', 10, city=2, job=3, demo=5) 命名关键字参数只可以传递命名的参数

def advanced_person(name, age, *nums, city='Hangzhou', job):
    print(name, age, nums, city, job)

advanced_person('dream', 20, 1, 2, 3, city='Hangzhou', job='coder')
advanced_person('dream', 20, 1, 2, 3, job='coder') # 命名关键字参数也可以使用默认参数

###### 最终版本的一个函数参数
# @1 必选参数
# @2 默认参数
# @3 可变参数
# @4 命名关键字参数
# @5 关键字参数

def final_func(name, age=20, *nums, city, job, **extra):
    print(name, age, nums, city, job, extra)

final_func('dream', 23, 3, 4, city='Hangzhou', job='codeer', color='red')
final_func('dream', 2, 3, 4, city='Hangzhou', job='codeer', color='red')

###### 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

###### 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。