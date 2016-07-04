import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import sys


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#qq邮箱好像不行 要用163
from_addr = ''  # 发件人地址
to_addr = ''  # 收件人地址
smtp_server = 'smtp.163.com'  # 邮件服务器
password = ''  # 密码

# 附件需要使用MIMEMultipart
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 zeghaun <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('好好学习，sendToKindle', 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

try:
    path = sys.argv[1]  # 获取路径参数
    if path is None or not isinstance(path, str) or not os.path.exists(path):
        print("路径或者文件有误,最好路径与文件名没有空格、特殊字符等")
        exit(1)
except IndexError:
    raise Exception("想传输的文件直接用该程序打开,即文件直接鼠标左击拉动到exe上")

print("路径：" + path)
filename = path.split("\\")[-1]
print("文件名字：" + filename)
with open(path, 'rb') as fp:
    mime = MIMEBase('kindle', 'mobi', filename=filename)
    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(fp.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

try:
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.starttls()  #建立安全连接，上面的端口也要改，未成功
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
except Exception as e:
    print("无法建立连接，可能是网络等异常", e)
finally:
    server.quit()

