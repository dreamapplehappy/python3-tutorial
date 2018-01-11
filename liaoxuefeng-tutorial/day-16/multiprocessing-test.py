import os

print('Process(%d) start...' % (os.getpid()))
pid = os.fork()

if pid == 0:
    print('I(%d) was created by %d' % (os.getpid(), os.getppid()))
    print('Second process(%d) start...' % (os.getpid()))
    child_pid = os.fork()
    if child_pid == 0:
        print('second: I(%d) was created by %d' % (os.getpid(), os.getppid()))
    else:
        print('second: I(%d) create a child process(%d)' % (os.getpid(), child_pid))
else:
    print('I(%d) create a child process(%d)' % (os.getpid(), pid))