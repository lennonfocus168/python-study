import asyncio
import logging
import aiomysql
import pymysql


@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info("create database connection pool...")
    global __pool
    __pool = yield from aiomysql.create_pool(host=kw.get('host', 'localhost'),
                                             port=kw.get('port', 3306),
                                             user=kw['zeghaun'],
                                             password=kw['password'],
                                             db=kw['test'],
                                             charset=kw.get('charset', 'utf8'),
                                             autocommit=kw.get('autocommit', True),
                                             maxsize=kw.get('maxsize', 10),
                                             minsize=kw.get('minsize', 1),
                                             loop=loop
                                             )


@asyncio.coroutine
def test():
    global __pool
    with __pool.get() as conn:
        cur = yield from conn.cursor()

        cur.execute('create table user1 (id varchar(20) primary key, name varchar(20))')
        cur.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])


print(__name__)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [create_pool(loop)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.wait([test()]))
    loop.close()
