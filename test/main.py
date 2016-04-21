import asyncio

import time
import uuid


@asyncio.coroutine
def hello(n):
    print('Hello nworld! (%s)' % n)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % n)


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


print(time.time())
print(next_id())
print(next_id())
