import time, queue, random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManger(BaseManager):
    pass

QueueManger.register('get_task_queue', callable=lambda: task_queue)
QueueManger.register('get_result_queue', callable=lambda: result_queue)

manger = QueueManger(address=('', 5000), authkey=b'abc')

manger.start()

task = manger.get_task_queue()
result = manger.get_result_queue()

for i in range(10):
    print('%d ...' % i)
    task.put(i)

for i in range(10):
    r = result.get(timeout=10)
    print('%s ...' % r)