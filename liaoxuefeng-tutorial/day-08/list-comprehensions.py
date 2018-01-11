# 列表生成器

l1 = list(range(1, 11))
print(l1) # [liaoxuefeng-tutorial, official-tutorial, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = [n for n in range(1, 9)]
print(l2) # [liaoxuefeng-tutorial, official-tutorial, 3, 4, 5, 6, 7, 8]

l3 = [n * n for n in range(1, 5)]
print(l3) # [liaoxuefeng-tutorial, 4, 9, 16]

## 可以添加判断
l4 = [n * n for n in range(1, 11) if n % 2]
print(l4) # [liaoxuefeng-tutorial, 9, 25, 49, 81]

## 两重循环
l5 = [n * m for n in range(1, 4) for m in range(6, 9)]
print(l5) # [6, 7, 8, 12, 14, 16, 18, 21, 24]

## 可以使用多个变量
l6 = [('key is %s, and value is %s' % (k, v)) for k,v in enumerate(range(3, 5))]
print(l6)

l7 = ['A', 'B', 12, 'C']
l8 = [s.lower() for s in l7 if isinstance(s, str)]
print(l8) # ['a', 'b', 'c']

# 第二次练习
print('######第二次练习######')

print(list(range(1, 11)))
## for 循环
print([n * n for n in range(1, 11)])
## for 循环以及判断
print([n * n for n in range(1, 11) if n % 2])
## 循环字符串 左边for语句先进行循环
print([x + y for x in 'XYZ' for y in 'ABC'])
## 列出当前目录的文件
import os
print([d for d in os.listdir('../')])
## 可以循环多个变量
print(['%s->%s; %s->%s' % (a, b, c, d) for a, b in enumerate('XYZ') for c, d in enumerate('ABC')])