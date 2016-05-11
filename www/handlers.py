from aiohttp import web
from aiohttp.web_reqrep import StreamResponse

from www.coroweb import get
from www.models import User


@get('/')
def index(request):
    print("index")
    users = yield from User.findAll()
    t = {'__template__': 'test.html', 'users': users[0]}
    print(t)
    return t
