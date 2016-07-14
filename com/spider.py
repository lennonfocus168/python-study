# coding=utf-8
import os
import re
import urllib
import urllib.request
import urllib.request
from os.path import basename
from urllib.parse import urlsplit

# 知乎爬虫
import time

spider_url = r'https://www.zhihu.com/question/37709992'
# spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
collection_url = r'https://www.zhihu.com/collection/90762956'
# collection_url = r'https://www.zhihu.com/collection/101134785'  # 自己

PATH = r"E:\image\\"
URL_PRE = "https://www.zhihu.com"


# 给一个完整的html页面，下载照片
def download_photos(page_url, name):
    def_log(page_url)
    re_str = 'src="(http[s]?://.*?b.jpg)"'
    file_path = PATH + name
    request = urllib.request.Request(page_url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # 很多图片会重复，用set变成去重
    img_url_list = set(re.findall(re_str, content, re.M | re.I))

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    def_log(img_url_list)
    for img_url in img_url_list:
        try:
            img_data = urllib.request.urlopen(img_url).read()
            file_name = basename(urlsplit(img_url)[2])
            img_path = file_path + "\\" + file_name
            output = open(img_path, 'wb')
            output.write(img_data)
            log(file_path, img_path)
        except Exception as e:
            print("download_photos:", e)
        finally:
            output.close()


def get_page(col_url):
    result_url = []
    page = 1
    col_re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'
    while True:
        tep_url = col_url + "?page=" + str(page)
        page += 1
        request = urllib.request.Request(tep_url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        col_url_list = re.findall(col_re_str, content, re.M | re.I)
        if col_url_list is None or len(col_url_list) <= 0:
            break
        def_log(col_url_list)
        result_url = result_url + col_url_list

    return result_url


def log(file_path, text):
    log_path = file_path + "\log.txt"
    try:
        output = open(log_path, 'a', encoding='utf-8')
        output.write("\n\n")
        output.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "\n")
        output.write(str(text))
        print(text)
    except Exception as e:
        print("LOG Exception:", e)
    finally:
        output.close()


def def_log(text):
    log(PATH, text)


if __name__ == "__main__":
    # request_url = ""
    # # request_url = str(input("请输入集合：")).strip()
    # print(request_url)
    # if request_url is None or len(request_url) < len('https://www.zhihu.com/collection/'):
    #     print("集合有误，使用默认集合")
    #     request_url = collection_url
    #
    # col_list = get_page(request_url)
    #
    # for url, name in col_list:
    #     page_url = URL_PRE + url
    download_photos("https://www.zhihu.com/question/19855515", "test")
