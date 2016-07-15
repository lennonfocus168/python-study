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

PATH = "E:\\image\\"
URL_PRE = "https://www.zhihu.com"


# 给一个完整的html页面，下载照片
def download_photos(page_url, name):
    re_str = 'src="(http[s]?://.*?)"'
    file_path = PATH + name
    try:
        request = urllib.request.Request(page_url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
    except Exception as e:
        print("Exception:request ", e)
        return

    # 很多图片会重复，用set变成去重
    url_list = set(re.findall(re_str, content, re.M | re.I))
    # 以_b.jpg结尾的才是干货
    img_url_list = set()
    for i in url_list:
        if str(i).endswith('_b.jpg'):
            img_url_list.add(i)

    # file_path有可能会变,name是特别的字符时候，无法穿件目录，用数字来
    file_path = create_dirs(file_path, page_url)
    def_log(page_url + "    site:" + str(len(img_url_list)))

    for img_url in img_url_list:
        try:
            img_data = urllib.request.urlopen(img_url).read()
            base_name = basename(urlsplit(img_url)[2])
            img_path = file_path + "\\" + base_name
            output = open(img_path, 'wb')
            output.write(img_data)
        except Exception as e:
            print("download_photos:", e)
        finally:
            output.close()
            log(file_path, img_path)


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


def create_dirs(file_path, l_url):
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    except Exception as e:
        def_log("Exception: create_dirs--" + str(e))
        file_path = PATH + basename(l_url)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    finally:
        return file_path


def create_dir():
    create_dirs(PATH, "1000")


if __name__ == "__main__":
    # 输入想要爬虫的url
    request_url = ""
    request_url = str(input("请输入集合或者某个问题：")).strip()
    print(request_url)
    request_url=spider_url
    # 新建目录 E:\image
    create_dir()
    if request_url is None or len(request_url) < len('https://www.zhihu.com/collection/'):
        print("url有误，使用默认集合:" + collection_url)
        request_url = collection_url

    if request_url.find('collection') > 0:
        # 集合爬虫
        col_list = get_page(request_url)

        for url, name in col_list:
            page_url = URL_PRE + url
            download_photos(page_url, name)
    else:
        # 单个问题爬虫
        download_photos(request_url, basename(request_url))

    def_log(request_url + " 爬虫完成请请前往 " + PATH + " 查看 ")
    time.sleep(100)
