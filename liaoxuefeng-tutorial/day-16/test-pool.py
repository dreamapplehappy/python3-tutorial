from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('process %s is running, it\'s pid is %d' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('process %d cost %0.2f' % (os.getpid(), (end - start)))

if __name__=='__main__':
    print('Parent process is start...')
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('All subprocesses are created.')
    p.close()
    p.join()
    print('All subprocesses are done')
