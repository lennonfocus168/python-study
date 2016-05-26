import urllib

from aiohttp.hdrs import CONTENT_LENGTH

acm_url = "http://acm.fzu.edu.cn/login.php?act=1&dir=L2F3YXJkLnBocA=="
data = {"uname": "zeghaun",
        "password": "abc123",
        "submit": "Submit"}

post_data = urllib.parse.urlencode(data)
headers = {
    "Host": "acm.fzu.edu.cn",
    "Connection": "keep-alive",
    "Content-Length": CONTENT_LENGTH,
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
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cookie": " _gscu_1331749010=63020751tpm7ze17; _gscbrs_1331749010=1; FASAST=7v5ckg6291kb3mau85bn3cg3v5; __utmt=1; __utma=174014643.300573640.1464166421.1464166421.1464166421.1; __utmb=174014643.31.10.1464166421; __utmc=174014643; __utmz=174014643.1464166421.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)"
}

t = urllib.request.request(acm_url, post_data, headers=headers)
