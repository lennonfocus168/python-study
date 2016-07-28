import gzip
import io
import urllib.request

url = "http://www.ip138.com/"


def zip_to_encode_html(request, encoding='utf-8'):
    response = urllib.request.urlopen(request)

    if response.info().get('Content-Encoding') == 'gzip':
        gzip_f = gzip.GzipFile(fileobj=io.BytesIO(response.read()))
        content = gzip_f.read()
    else:
        content = response.read()
    return content.decode(encoding)


request = urllib.request.Request(url)
content = zip_to_encode_html(request, "gb2312")

re_str = 'src="(http[s]?://.*?)"'
print(content)

with open(r"E:\1.html", "w", encoding='utF-8') as output:
    output.write(content)