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
collection_url = r'https://www.zhihu.com/collection/62864589'
# collection_url = r'https://www.zhihu.com/collection/101134785'  # 自己
URL_PRE = "https://www.zhihu.com"

re_str = 'src="(http[s]?://.*?jpg)"'
col_re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'

col_list = []
page = 1
while True:
    col_url = collection_url + "?page=" + str(page)
    page += 1
    request = urllib.request.Request(col_url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    searchObj = re.findall(col_re_str, content, re.M | re.I)
    if searchObj is None or len(searchObj) <= 0:
        break

    col_list = col_list + searchObj

print(col_list)
print(len(col_list))
