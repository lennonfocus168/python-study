import urllib
import urllib.request

import time

data = {}
data['word'] = '1'
data['ie'] = 'OIE'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

time.sleep(1)

data = urllib.request.urlopen(full_url).read()

print(type(data))
print(type(data.decode('UTF-8')))

f = open(r'E:/1.html', 'wb')

f.write(data)

f.close()
