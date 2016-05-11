import aiohttp_jinja2
from flask import logging

from www.coroweb import get
from www.models import User


# 获取页数，主要是做一些容错处理
def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


@get('/')
def index(request):
    print("index")
    users = yield from User.findAll()
    t = {'__template__': 'test.html', 'users': users[0]}
    print(t)
    return t


# 显示所有的用户
@aiohttp_jinja2.template('test.html')
def show_all_users(self):
    print("fwfewafw")
    users = yield from User.findAll()
    # return (404, 'not found')
    print(users)
    return {
        '__template__': 'test.html',
        'users': users
    }
