import time, threading

def loop():
    print('Thread %s is running...' % (threading.current_thread().name))
    n = 0
    while n<5:
        n += 1
        print('Thread %s is running >>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s is end' % (threading.current_thread().name))

print('Thread %s is running...' % (threading.current_thread().name))
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s is end' % (threading.current_thread().name))

# test official-tutorial

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        # 上锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))

t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
# 循环的次数足够多 balance就会产生错误
print(balance)
