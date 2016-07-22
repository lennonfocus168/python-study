# coding=utf-8
import urllib
import urllib.request
import urllib.request
import json

from urllib.parse import urlsplit

import time

spider_url = r'https://www.btctrade.com/'
# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
str = "%a, %d %b %Y %H:%M:%S GMT"
Date = time.strftime(str, time.gmtime(time.time()))
expires = time.strftime(str, time.gmtime(time.time() - 365 * 24 * 60 * 60))

headers = {"Cache-Control": "no-store",
           "Connection": "keep-alive",
           "Content-Encoding": "gzip",
           "Content-Length": "12667",
           "Content-Security-Policy": "default-src *; img-src * data:; frame-src 'self' *.zhihu.com getpocket.com note.youdao.com; script-src 'self' *.zhihu.com *.google-analytics.com zhstatic.zhihu.com res.wx.qq.com 'unsafe-eval'; style-src 'self' *.zhihu.com 'unsafe-inline'",
           "Content-Type": "application/json",
           "Date": Date,
           "Pragma": "no-cache",
           "Server": "Qnginx/1.1.1",
           "Set-Cookie": "_xsrf=; Domain=zhihu.com; expires=" + expires + "; Path=/",
           "Vary": "Accept-Encoding",
           "X-Frame-Options": "DENY",
           "X-NWS-LOG-UUID": "7a8162f6-e654-4b3d-affc-1bf31c6172d7",
           "X-Req-ID": "2C4353585791D89E",
           "X-Za-Response-Id": "0d052e41d5734e6fb712286b6412613a"}

print(json.dumps(headers))

url = r'https://www.zhihu.com/node/QuestionAnswerListV2'
data = {"method": "next", "param": {"url_token": 20702054, "pagesize": 10, "offset": 20}}

request = urllib.request.Request(url, json.dumps(data).encode(encoding='utf-8'), method='POST')
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)
