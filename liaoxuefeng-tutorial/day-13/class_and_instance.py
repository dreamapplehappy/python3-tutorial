class Student(object):
    # 初始化类的实例
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 获取分数等级
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'C'


dreamapple = Student('dreamapple', 90)
print(dreamapple)
print(dreamapple.get_grade())

dreamapple.age = 24
print(dreamapple.age)
