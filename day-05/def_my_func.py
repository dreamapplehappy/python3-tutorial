# 定义一个求绝对值的函数
def dr_abs(x):
    # 进行参数的类型检查
    if not isinstance(x, (int, float)):
        raise TypeError('您传递的参数类型不对！')
    if x > 0:
        return x
    else:
        return -x

# 定义一个空函数
def dr_empty():
    pass


# 使用系统的函数库
import math

def move(x, y, step, angle):
    ns = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return ns, ny