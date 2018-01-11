import time, queue, sys
from multiprocessing.managers import BaseManager

class QueueManger(BaseManager):
    pass

QueueManger.register('get_task_queue')
QueueManger.register('get_result_queue')

m = QueueManger(address=('127.0.0.liaoxuefeng-tutorial', 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()


for i in range(10):
    try:
        t = task.get(timeout=1)
        r = t * t
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('Nothing...')
