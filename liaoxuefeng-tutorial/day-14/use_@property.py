class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            print('请输入一个整数')
        elif score < 0 or score > 100:
            print('请输入正确的分数')
        else:
            self._score = score

s1 = Student()
# s1.score = '100'
# print(s1.score)  # AttributeError: 'Student' object has no attribute '_score'

s1.score = 99
print(s1.score)  # 99
