import types


# 使用type进行类别的判断
print(type(1))  # <class 'int'>
print(type('str'))  # <class 'str'>
print(type(True))   # <class 'bool'>
print(type(lambda x: x))  # <class 'function'>
print(type(None))  # <class 'NoneType'>
print(type(abs))  # <class 'builtin_function_or_method'>


class Animal(object):
    def __init__(self, name):
        self.__name = name

    def __len__(self):
        return 1


animal1 = Animal('DuoDuo')


def func():
    pass


print(type(animal1))  # <class '__main__.Animal'>
print(type(func))  # <class 'function'>

print(type(func) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type(x for x in range(10)) ==  types.GeneratorType)  # True

# 使用isinstance判断一个对象是否是一个类的实例
print(isinstance(animal1, object))  # True
print(isinstance(animal1, Animal))  # True

# 还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))  # True


# 使用dir获取一个对象的所有属性和方法
print(dir(animal1))  # 太多了，暂时不列举出来
print(len([]))  # 0
print(len(animal1))  # 1，这个方法需要我们在对象的内部进行实现

# 使用getattr， setattr， hasattr方法
print(getattr(animal1, 'name', 404))  # 404
print(setattr(animal1, 'age', 10))  # None
print(hasattr(animal1, 'age'))  # True


