# coding=utf-8
import os
import re
import urllib
import urllib.request
import urllib.request
from os.path import basename
from urllib.parse import urlsplit

# 知乎爬虫

spider_url = r'https://www.zhihu.com/question/37709992'
# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
collection_url = r'https://www.zhihu.com/collection/62864589'
# collection_url = r'https://www.zhihu.com/collection/101134785'  # 自己

PATH = r"E:\image\\"
URL_PRE = "https://www.zhihu.com"


def downloan_photos(page_url, name):
    re_str = 'src="(http[s]?://.*?jpg)"'
    file_path = PATH + name + "\\"
    request = urllib.request.Request(page_url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    img_url_list = re.findall(re_str, content, re.M | re.I)

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    print(img_url_list)
    for img_url in img_url_list:
        try:
            img_data = urllib.request.urlopen(img_url).read()
            file_name = basename(urlsplit(img_url)[2])
            output = open(file_path + file_name, 'wb')
            print(file_path + file_name)
            output.write(img_data)
            output.close()
        except Exception as e:
            print(e)


def get_page(col_url):
    result_url = []
    page = 1
    col_re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'
    while True:
        col_url = collection_url + "?page=" + str(page)
        page += 1
        request = urllib.request.Request(col_url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        col_url_list = re.findall(col_re_str, content, re.M | re.I)
        if col_url_list is None or len(col_url_list) <= 0:
            break
        result_url = result_url + col_url_list

    print(result_url)
    return result_url


if __name__ == "__main__":
    col_list = get_page(collection_url)

    for url, name in col_list:
        page_url = URL_PRE + url
        downloan_photos(page_url, name)
