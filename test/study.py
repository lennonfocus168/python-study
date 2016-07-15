import re

content = ''


def scopetest():
    global var
    var = 6
    print('test', var)  #


var = 5
print(var)
scopetest()
print(var)
