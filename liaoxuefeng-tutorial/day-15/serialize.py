import json
import pickle

dream = dict(name='dreamapple', age=24, gender='man')
print(json.dumps(dream))
dream_str = json.dumps(dream)
dream1 = json.loads(dream_str)
print(dream1)

dream2 = dict(name='dreamapple', age=24, gender='man')
dream2_str = pickle.dumps(dream2)
print(dream2_str)

# with open('./test', 'ab') as f:
#     pickle.dump(dream2, f)

# with open('./test', 'a') as f:
#     json.dump(dream, f)

with open('./test', 'r') as f:
    print(json.load(f))


# 序列化一个对象
class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

s1 = Student('dreamapple', 24, 'man')

def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'gender': stu.gender
    }

s1_str = json.dumps(s1, default=student2dict)
print(s1_str)
s2_str = json.dumps(s1, default=lambda obj: obj.__dict__)
print(s2_str)

def str2class(obj):
    return Student(obj['name'], obj['age'], obj['gender'])

stu1 = json.loads(s2_str, object_hook=str2class)
print(stu1)