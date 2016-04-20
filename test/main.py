import threading
import asyncio


# 在同一个线程里并行执行  异步IO
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    n = yield from hi(4, 'tttt')
    print('Hello again! (%s)' % n)


def hi(r, str="hello"):
    print('Hi! (%s)' % str)
    yield from asyncio.sleep(2)
    print('Hi! (%s) %s' % (r, str))
    return r * r


loop = asyncio.get_event_loop()
tasks = [hello(), hi(99)]
loop.run_until_complete(asyncio.wait(tasks))
print('end')
loop.close()
