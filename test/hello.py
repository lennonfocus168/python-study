# coding=utf-8
import gzip
import http.cookiejar
import urllib
import urllib.request
import urllib.request
from io import StringIO

from setuptools.compat import BytesIO

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA=='),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', ' 1'),
           ('Cookie', 'FASAST=7vbtpgjviv872vsg60me6n8086')]

print(headers)


class xiaobai:
    post_data = b""  # 登陆提交的参数

    def __init__(self):
        '''''初始化类，并建立cookies值'''
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        opener.addheaders = headers
        urllib.request.install_opener(opener)

    def login(self, loginurl, bianma):
        '''''模拟登陆'''
        req = urllib.request.Request(loginurl, self.post_data)
        _response = urllib.request.urlopen(req)

        if _response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(_response.read())
            gzip_f = gzip.GzipFile(fileobj=buf)
            content = gzip_f.read()
        else:
            content = _response.read()
        _d = content
        _d = _d.decode(bianma)

        return _d

    def getpagehtml(self, pageurl, bianma):
        '''''获取目标网站任意一个页面的html代码'''
        req2 = urllib.request.Request(pageurl)
        _response2 = urllib.request.urlopen(req2)
        if _response2.info().get('Content-Encoding') == 'gzip':
            gzip_f = gzip.GzipFile(fileobj=BytesIO(_response2.read()))
            content = gzip_f.read()
        else:
            content = _response2.read()
        return content.decode(bianma)


if __name__ == "__main__":
    x = xiaobai()
    # 参递一个post参数
    x.post_data = urllib.parse.urlencode(
        {'uname': 'zeghaun', 'password': 'abc123', "submit": "Submit"}).encode(
        encoding='UTF-8')
    # print('x.post_data:',urllib.parse.parse_qs(x.post_data))
    post_url = "http://acm.fzu.edu.cn/login.php?act=1&dir=Lw=="
    get_url = "http://acm.fzu.edu.cn/"

    y = x.login(post_url, "utf-8")  # 登陆
    print("post Member ", y.find("Member") > 0)
    print("post zeghaun", y.find('zeghaun') > 0)

    y = x.getpagehtml(get_url, "utf-8")
    print("get Member ", y.find("Member") > 0)
    print("get zeghaun", y.find('zeghaun') > 0)
