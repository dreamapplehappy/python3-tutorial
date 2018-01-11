class Animal(object):

    def __init__(self):
        pass

    def run(self):
        print('this animal is running!')


class Dog(Animal):

    def run(self):
        print('this dog is running')


class Cat(Animal):

    def run(self):
        print('this cat is running')



animal1 = Animal()
dog1 = Dog()
cat1 = Cat()

animal1.run()
dog1.run()
cat1.run()

# 多态的好处
def run(animal):
    animal.run()

run(animal1)
run(dog1)
run(cat1)

# 使用方法isinstance判断一个对象是不是一个类的实例
print(isinstance(animal1, Animal))
print(isinstance(dog1, Dog))
print(isinstance(cat1, Cat))