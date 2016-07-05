# coding=utf-8
import gzip
import http.cookiejar
import urllib
import urllib.request
import urllib.request
from setuptools.compat import BytesIO

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA=='),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', '1')]


def get_html(pageurl, encoding='utf-8'):
    # 获取目标网站任意一个页面的html代码
    request = urllib.request.Request(pageurl)
    response = urllib.request.urlopen(request)
    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=BytesIO(response.read()))
        content = gzip_f.read()
    else:
        content = response.read()
    return content.decode(encoding)


spider_url = r'https://www.zhihu.com/question/22761172'
spider_url = r'http://bbs.fengniao.com/forum/8978324.html'
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = headers
html = urllib.request.install_opener(opener)

content = get_html(spider_url)
with open(r"E:\1.html", "w", encoding='utf-8') as fw:
    try:
        fw.write(content)
    except Exception as e:
        print(e)
    finally:
        fw.close()

print(content)
