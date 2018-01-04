from multiprocessing import Process
import os

def task(name):
    print('Child process is running, pid is %d, name is %s' % (os.getpid(), name))

if __name__=='__main__':
    print('Parent process is running...')
    p = Process(target=task, args=('task',))
    p.start()
    p.join()
    print('Child process is over')