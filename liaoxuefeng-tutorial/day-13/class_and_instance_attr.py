class Animal(object):

    is_alive = True

    def __init__(self, name, age):
        self.__name = name
        self.age = age


animal1 = Animal('Duo', 10)

print(animal1.is_alive)  # True
print(Animal.is_alive)  # True

Animal.is_alive = False
print(Animal.is_alive)  # False

print(animal1.age)  # 10
