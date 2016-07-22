headers = {('Content-Type', 'application/json'), ('Connection', 'keep-alive'), ('DNT', '1'),
           ('Cache-Control', 'no-cache'), ('User-Agent',
                                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'),
           ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'),
           ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding', 'gzip, deflate'),
           ('Host', 'zhihu.com'), ('Upgrade-Insecure-Requests', '1')}

head = {}
print(type(head))
for key, value in headers:
    head[key] = value
    pass

print(head)
