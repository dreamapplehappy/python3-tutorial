class Animal(object):
    pass


class RunnableMixIn(object):
    def run(self):
        print('I can run!')


class FlyableMixIn(object):
    def fly(self):
        print('I can fly!')

class Dog(Animal, RunnableMixIn):
    pass

dog = Dog()
print(dir(dog))
dog.run()
