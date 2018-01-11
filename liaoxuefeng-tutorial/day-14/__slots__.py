class Student(object):
    __slots__ = ('name', 'age', 'score', 'set_name')
    pass

s1 = Student()
s1.name = 'dreamapple'
print(s1.name)

def set_name(self, name):
    self.name = name

from types import MethodType
s1.set_name = MethodType(set_name, s1)
print(s1.set_name('happy'))
print(s1.name)

#s1.city = 'Hangzhou'  # AttributeError: 'Student' object has no attribute 'city'


class HighSchoolStudent(Student):
    pass

hs1 = HighSchoolStudent()
hs1.city = 'Hangzhou'
print(hs1.city)  # Hangzhou