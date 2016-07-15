import re

content = '<div class="zm-item" data-za-module="AnswerItem"><h2 class="zm-item-title"><a target="_blank" href="/question/20399991">女生的美腿是怎样炼成的？成长期要注意什么？</a></h2>'

re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'
searchObj = re.findall(re_str, content, re.M | re.I)
print(searchObj)

print('cdscsdcc'.find('Q'))
