import json
import re
import urllib.request

url = "https://api.douban.com/v2/book/1220565"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

print(json.loads(content))
