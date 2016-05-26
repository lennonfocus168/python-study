# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------------
# Name:        模块2
# Purpose:
#
# Author:      lenovo
#
# Created:     06/09/2013
# Copyright:   (c) lenovo 2013
# Licence:     <your licence>
# -------------------------------------------------------------------------------
# coding=utf-8
import re
import urllib
import urllib.request
import urllib.request
import http.cookiejar
import re

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA=='),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', ' 1'),
           ('Pragma', 'no-cache')]


# ('Accept-Encoding', 'gzip,deflate')

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
        _d = _response.read()
        _d = _d.decode(bianma)
        return _d

    def getpagehtml(self, pageurl, bianma):
        '''''获取目标网站任意一个页面的html代码'''
        req2 = urllib.request.Request(pageurl)
        _response2 = urllib.request.urlopen(req2)
        _d2 = _response2.read()
        _d22 = _d2.decode(bianma)
        return _d2


if __name__ == "__main__":
    x = xiaobai()
    # 参递一个post参数
    x.post_data = urllib.parse.urlencode(
        {'uname': 'zeghaun', 'password': 'huan31415', "submit": "Submit"}).encode(
        encoding='UTF8')
    # print('x.post_data:',urllib.parse.parse_qs(x.post_data))
    acm_url = "http://acm.fzu.edu.cn/login.php?act=3&dir=L2F3YXJkLnBocA=="
    y = x.login(acm_url, "utf-8")  # 登陆
    # 获取一个页面的html并输出
    # print (x.getpagehtml("http://www.lvye.org/userinfo.php?uid=404071","utf-8"))
    print(y)
    f = open(r'E:/1.html', 'wb')

    f.write(bytes(y.encode('utf-8')))

    f.close()
