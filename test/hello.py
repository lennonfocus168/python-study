# coding=utf-8
import gzip
import http.cookiejar
import os
import urllib
import urllib.request
import urllib.request

import re

from os.path import basename
from urllib.parse import urlsplit

from setuptools.compat import BytesIO

spider_url = r'https://www.btctrade.com/'
# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'

url = r'http://localhost:8080/test/3223/323'
data = {"name": "zeg104935408632"}
post = urllib.parse.urlencode(data)
post = post.encode('utf-8')

request = urllib.request.Request(url, post)
print(str(request.data))
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)
