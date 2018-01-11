class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        self.__score = score

    def show_info(self):
        print('this student\'s name is %s and his(her) score is %d.' % (self.__name, self.__score))

s1 = Student('dream', 99)
s1.show_info()
print(s1.get_name())
s1.set_name('dreamapple')
print(s1.get_name())