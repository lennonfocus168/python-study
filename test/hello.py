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

spider_url = r'https://www.zhihu.com/question/32674678'
spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
file_path = r"E:\image\\"

headers = [('User-Agent',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Referer', spider_url),
           ('Host', 'www.zhihu.com')]


def get_html(pageurl, encoding='utf-8'):
    # 获取目标网站任意一个页面的html代码
    request = urllib.request.Request(pageurl)
    response = urllib.request.urlopen(request)
    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=BytesIO(response.read()))
        result = gzip_f.read()
    else:
        result = response.read()
    return result.decode(encoding)


content = get_html(spider_url)
with open(r"E:\1.html", "w", encoding='utf-8') as fw:
    try:
        fw.write(content)
    except Exception as e:
        print(e)
    finally:
        fw.close()

re_str = 'img .*?src="(http://.*?.jpg)"'
searchObj = re.findall(re_str, content, re.M | re.I)

if not os.path.exists(file_path):
    os.makedirs(file_path)

for img_url in searchObj:
    try:
        img_data = urllib.request.urlopen(img_url).read()
        file_name = basename(urlsplit(img_url)[2])
        output = open(file_path + file_name, 'wb')
        print(file_path + file_name)
        output.write(img_data)
        output.close()
    except Exception as e:
        print(e)
