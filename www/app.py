import asyncio
import logging;
import pathlib

import aiohttp_jinja2
import jinja2
from aiohttp import web

from www import orm
from www.handlers import show_all_users

logging.basicConfig(level=logging.INFO)
TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'


# 在正式处理之前打印日志
@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info('Requst : %s, %s' % (request.method, request.path))
        return (yield from handler(request))

    return logger


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop)
    app = web.Application(loop=loop)
    print(TEMPLATES_ROOT)
    # app.router.add_route('GET', '/', index)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(r'E:\Pycharm-workspace\study3\www\templates'))
    app.router.add_route('GET', '/', show_all_users)
    # app.router.add_route('GET', '/', api_get_users)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
