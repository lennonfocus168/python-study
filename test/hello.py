# coding=utf-8
import urllib
import urllib.request
import urllib.request
import json

from urllib.parse import urlsplit

spider_url = r'https://www.btctrade.com/'
# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
headers = {'Content-Type': 'application/json', 'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1', 'Host': 'zhihu.com',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
           'DNT': '1'}

url = r'http://localhost:8080/v0.1/demo'
data = {"name": "zeg104935408632"}
print(str(data))
print(json.dumps(data))
request = urllib.request.Request(url, json.dumps(data).encode(encoding='utf-8'), headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)
