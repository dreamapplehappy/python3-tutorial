
i = 0
while i < 5:
    i += 1
    # i = 4 终止循环
    if i == 4:
        break
    # i= 2 跳过本次循环
    if i == 2:
        continue
    print(i)

for j in range(3):
    print(j)

for k in range(10, 13):
    print(k)

for l in range(0, 10, 3):
    print(l)