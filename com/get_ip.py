import re
import urllib.request

url = "http://www.baidu.com/s?ie=UTF-8&wd=ip"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

re_str = '<span class="c-gap-right">本机IP:&nbsp;(.*?)</span>'
print(re.findall(re_str, content, re.M | re.I))
