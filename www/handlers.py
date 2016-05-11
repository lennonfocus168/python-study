from www.coroweb import get
from www.models import User


@get('/')
def index(request):
    print("index")
    users = yield from User.findAll()
    print(str(users))
    return {'__template__': 'test.html',
            'users': users}
