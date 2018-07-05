def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s' % n)
        r = '200 OK'

def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] is producing %s' % n)
        r = c.send(n)
        print('[Producer] consumer return %s' % r)
    c.close()

c = consumer()
producer(c)

