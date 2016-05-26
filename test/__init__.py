headers = {
    "Host": "acm.fzu.edu.cn",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Origin": "http//acm.fzu.edu.cn",
    "Upgrade-Insecure-Requests": " 1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Referer": "http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA==",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
}

list_headers = []
for (k, v) in headers.items():
    list_headers.append((k, v))

print(list_headers)


headers=[('Content-Type', 'application/x-www-form-urlencoded'), ('Connection', 'keep-alive'), ('DNT', '1'), ('Cache-Control', 'no-cache'), ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36'), ('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6'), ('Referer', 'http//acm.fzu.edu.cn/login.php?dir=L2luZGV4LnBocA=='), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), ('Host', 'acm.fzu.edu.cn'), ('Origin', 'http//acm.fzu.edu.cn'), ('Upgrade-Insecure-Requests', ' 1'), ('Pragma', 'no-cache'), ('Accept-Encoding', 'gzip, deflate')]
