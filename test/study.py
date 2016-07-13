import re

from os.path import basename, dirname

content = '<div class="zm-item" data-za-module="AnswerItem"><h2 class="zm-item-title"><a target="_blank" href="/question/20399991">女生的美腿是怎样炼成的？成长期要注意什么？</a></h2>'

re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'
searchObj = re.findall(re_str, content, re.M | re.I)
print(searchObj)

print('-' * 100)
URL_PRE = "https://www.zhihu.com"

lis = [('/questio1531/1531/5/531', '胸大是遗传吗？'),
       ('/question/20399991', '女生的美腿是怎样炼成的？成长期要注意什么？'), ('/question/36225746', '在家装里，最划算的投入是什么？')]


col_list = [('/question/36225746', '在家装里，最划算的投入是什么？'), ('/question/21178783', '麻烦介绍一下行程规划（旅行规划）类的网站或者APP软件？')]

for page, name in col_list:
    print(page, name)


