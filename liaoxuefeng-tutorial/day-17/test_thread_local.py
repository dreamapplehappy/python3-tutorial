import threading

local_student = threading.local()

def process_stu():
    stu = local_student.stu
    print('thread(%s) is running, stu name is %s' % (threading.current_thread().name, stu))

def test_thread(name):
    local_student.stu = name
    process_stu()


t1 = threading.Thread(target=test_thread, args=('happy',), name='T1')
t2 = threading.Thread(target=test_thread, args=('hello',), name='T2')

t1.start()
t2.start()

t1.join()
t2.join()