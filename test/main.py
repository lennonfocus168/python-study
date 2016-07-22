# coding=utf-8
import re

# spider_url = r'https://www.zhihu.com/question/37006507'

spider_url = r'http://bbs.fengniao.com/forum/8982080.html'
collection_url = r'https://www.zhihu.com/collection/62864589'
# collection_url = r'https://www.zhihu.com/collection/101134785'  # 自己
URL_PRE = "https://www.zhihu.com"

re_str = 'src="(http[s]?://.*?)"'
col_re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'

col_list = []
page = 1
read = open("E:\\1.html", "r", encoding='utf-8')
content = read.read()
url_list = set(re.findall(re_str, content, re.M | re.I))

print(url_list)
print(len(url_list))

end_set = {}

for i in range(10):
    print(i)

