import re

content = '<img src="https://p98ec73a_b.jpg"> <img src="http://p98ec73a_b.jpg"'

re_str = 'img .*?src="(http[s]?://.*?)"'
searchObj = re.findall(re_str, content, re.M | re.I)

print(searchObj)
