import re

from os.path import basename, dirname

import time

content = '<div class="zm-item" data-za-module="AnswerItem"><h2 class="zm-item-title"><a target="_blank" href="/question/20399991">女生的美腿是怎样炼成的？成长期要注意什么？</a></h2>'

re_str = '<a target="_blank" href="(.*?)">(.*?)</a>'
searchObj = re.findall(re_str, content, re.M | re.I)
print(searchObj)


def log(file_path, text):
    log_path = file_path + "\log.txt"
    try:
        output = open(log_path, 'a')
        output.write("\n\n")
        output.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "\n")
        output.write(text)
    except Exception as e:
        print(e)
    finally:
        output.close()


s = set()
s.add("fawefw")
s.add("ewfwe")
print(s)
