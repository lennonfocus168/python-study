import logging;
import asyncio
from aiohttp import web

from www import orm
from www.handlers import index

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop)
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
