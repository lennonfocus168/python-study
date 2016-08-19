import re
import socket
import urllib.request

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),

           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'bosszhipin.ui.cn'), ('Origin', 'http://bosszhipin.ui.cn'),
           ('Referer', 'http://bosszhipin.ui.cn/s.html?act=ruw&type=hot')]

timeout = 20
socket.setdefaulttimeout(timeout)

url = "http://www.baidu.com/s?ie=UTF-8&wd=ip"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

re_str = '<span class="c-gap-right">本机IP:&nbsp;(.*?)</span>(.*)'

print(re.findall(re_str, content, re.M | re.I))
