import gzip
import http.cookiejar
import io
import urllib.parse
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

headers.append(('Cookie', 'FASAST=vr6pb7hmj0asehlitrk2dpsm26'))

print(headers)
data = {'uname': 'zeghaun', 'password': 'abc123', "submit": "Submit"}

post_url = "http://acm.fzu.edu.cn/login.php?act=1&dir=Lw=="
get_url = "http://http://acm.fzu.edu.cn/index.php"


def zip_to_encode_html(response, encoding='utf-8'):
    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=BytesIO(response.read()))
        content = gzip_f.read()
    else:
        content = response.read()
    return content.decode(encoding)


post_data = urllib.parse.urlencode(data)
cj = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = headers

response = opener.open(post_url, post_data.encode('utf-8'))
y = zip_to_encode_html(response)

print("post Member ", y.find("Member") > 0)
print("post zeghaun", y.find('zeghaun') > 0)

request = urllib.request.Request(get_url)
response = urllib.request.urlopen(request)
y = zip_to_encode_html(response)

print("post Member ", y.find("Member") > 0)
print("post zeghaun", y.find('zeghaun') > 0)
print(y)
