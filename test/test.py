
import gzip
import http.cookiejar
import urllib.parse
import urllib.request

from setuptools.compat import BytesIO

headers = [('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', '1'),
           ('Cookie',
            'FASAST=vr6pb7hmj0asehlitrk2dpsm26;; __utmt=1; __utma=174014643.1328877597.1464769617.1464769617.1464769617.1;' +
            ' __utmb=174014643.3.10.1464769617; __utmc=174014643; __utmz=174014643.1464769617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)')]


referer = ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=Lw==')
headers.append(referer)
data = {'uname': 'zeghaun', 'password': 'abc123', "submit": "Submit"}

post_url = "http://acm.fzu.edu.cn/login.php?act=1&dir=Lw=="
get_url = "http://acm.fzu.edu.cn/index.php"


def zip_to_encode_html(response, encoding='utf-8'):
    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=BytesIO(response.read()))
        content = gzip_f.read()
    else:
        content = response.read()
    return content.decode(encoding)


def getCookie(response):
    cook = response.info().get('Set-Cookie')
    cook = None
    if cook:
        return cook
    else:
        return "FASAST=vr6pb7hmj0asehlitrk2dpsm26"  # chrome中抠来的


post_data = urllib.parse.urlencode(data).encode('ascii')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = headers
# urllib.request.install_opener(opener)

# re = opener.open(get_url)
# cookie = getCookie(re)
# opener.addheaders.append(("Cookie", "FASAST=" + cookie))
print(opener.addheaders)

connection = opener.open(post_url, post_data)
html = zip_to_encode_html(connection)
print("post Member ", html.find("Member") > 0)
print("post zeghaun", html.find('zeghaun') > 0)

opener.addheaders.remove(referer)
opener.addheaders.append(('Referer', 'http//acm.fzu.edu.cn/login.php?act=1&dir=Lw=='))  # 覆盖Referer
print(opener.addheaders)


# connection = opener.open(get_url)
# html = zip_to_encode_html(connection)
# print("post Member ", html.find("Member") > 0)
# print("post zeghaun", html.find('zeghaun') > 0)

