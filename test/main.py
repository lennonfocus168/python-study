from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 附件需要使用MIMEMultipart
msg = MIMEMultipart('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# 正文部分
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('F:\\1.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEText('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    # mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    # mime.add_header('Content-ID', '<0>')
    # mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.login(from_addr, password)

server.sendmail(from_addr, [to_addr], msg.as_string())

server.quit()
