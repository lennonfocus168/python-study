import threading
import asyncio


@asyncio.coroutine
def hello(n):
    print('Hello nworld! (%s)' % n)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % n)


loop = asyncio.get_event_loop()
tasks = [hello(1), hello(2)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
