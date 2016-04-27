import asyncio
import inspect


@asyncio.coroutine
def hello(n):
    print('Hello nworld! (%s)' % n)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % n)


# 关于inspect.Parameter 的  kind 类型有5种：
# POSITIONAL_ONLY		只能是位置参数
# POSITIONAL_OR_KEYWORD	可以是位置参数也可以是关键字参数
# VAR_POSITIONAL			相当于是 *args
# KEYWORD_ONLY			关键字参数且提供了key，相当于是 *,key
# VAR_KEYWORD			相当于是 **kw

def get_required_kw_args(fn):
    args = []
    print(inspect.signature(fn).parameters)
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        print("key:name=%s  param=%s %s %s" % (name, param, param.kind, param.default))

        args.append(name)
    return tuple(args)


module_name = 'test.haha.tttt'
n = module_name.rfind('.')

if n == (-1):
    mod = __import__(module_name, globals(), locals())
else:
    # name = module_name[n+1:]
    # mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    # 上面两行是廖大大的源代码，但是把传入参数module_name的值改为'handlers.py'的话走这里是报错的，所以改成了下面这样
    mod = __import__(module_name[:n], globals(), locals())


# print(mod)
# print(dir(mod))

