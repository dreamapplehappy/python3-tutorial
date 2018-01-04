from multiprocessing import Process, Queue
import os, time, random

def write_q(q):
    for v in ['A', 'B', 'C', 'D']:
        q.put(v)
        print('%c has been put in queue' % v)
        time.sleep(random.random())

def read_q(q):
    while True:
        v = q.get(True)
        print('%c has been read' % v)

if __name__=='__main__':
    q = Queue()
    qw = Process(target=write_q, args=(q,))
    qr = Process(target=read_q, args=(q,))

    qw.start()
    qr.start()

    qw.join()
    qr.terminate()