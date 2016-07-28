import gzip
import io
import urllib.request

import re

url = "http://www.baidu.com/s?ie=UTF-8&wd=ip"

def zip_to_encode_html(request, encoding='utf-8'):
    response = urllib.request.urlopen(request)

    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=io.BytesIO(response.read()))
        content = gzip_f.read()
    else:
        content = response.read()
    return content.decode(encoding)


request = urllib.request.Request(url)
content = zip_to_encode_html(request)

re_str = '<span class="c-gap-right">本机IP:&nbsp;(.*?)</span>'
print(re.findall(re_str, content, re.M | re.I))

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)
