# coding=utf-8
import os
import re
import urllib
import urllib.request
import urllib.request
from os.path import basename
from urllib.parse import urlsplit

# spider_url = r'https://www.zhihu.com/question/37006507'
spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
file_path = r"E:\image\\"

request = urllib.request.Request(spider_url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

re_str = 'img .*?src="(http[s]?://.*?)"'
searchObj = re.findall(re_str, content, re.M | re.I)

if not os.path.exists(file_path):
    os.makedirs(file_path)

print(searchObj)
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
