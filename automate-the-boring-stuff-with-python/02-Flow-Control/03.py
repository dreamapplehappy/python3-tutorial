import random
import sys

for i in range(1, 10):
    print(random.randint(1, 10))

while True:
    response = input('请输入 exit 来终止程序\n')
    if response == 'exit':
        sys.exit()
