# coding=utf-8
import json
import time


# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
import urllib.request

str = "%a, %d %b %Y %H:%M:%S GMT"
Date = time.strftime(str, time.gmtime(time.time()))
expires = time.strftime(str, time.gmtime(time.time() - 365 * 24 * 60 * 60))

headers = {"Accept": "*/*",
           "Accept-Encoding": "gzip, deflate, br",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Origin": "https://www.zhihu.com",
           "Referer": "https://www.zhihu.com/question/20702054",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
           "X-Requested-With": "XMLHttpRequest",
           "X-Xsrftoken": "ee6d3fc7636e5a3ada84c59bb56fd704"}

print(json.dumps(headers))

url = r'https://www.zhihu.com/node/QuestionAnswerListV2'
data = {"method": "next", "param": {"url_token": 20702054, "pagesize": 10, "offset": 20}}

request = urllib.request.Request(url, json.dumps(data).encode(encoding='utf-8'), headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)
