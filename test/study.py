import json

import time

data = {"name": "zeg104935408632"}

str = "%a, %d %b %Y %H:%M:%S GMT"
print(time.strftime(str, time.localtime(time.time())))
print(time.strftime(str, time.localtime(time.time() - 365 * 24 * 60 * 60)))
print(time.strftime(str, time.gmtime(time.time())))

'Fri, 22 Jul 2016 08:31:29 GMT'
