# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart  # python2.4及之前版本该模块不是这样调用的，而是email.MIMEMultipart.MIMEMultipart(),下同
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



def send_email(msg, file_name):
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = file_name  # 邮件标题，这里我把标题设成了你所发的附件名
    msgText = MIMEText('%s' % msg, 'html', 'utf-8')  # 你所发的文字信息将以html形式呈现
    msgRoot.attach(msgText)
    att = MIMEText(open('%s' % file_name, 'rb').read(), 'base64', 'utf-8')  # 添加附件
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
    msgRoot.attach(att)
    i = 1;

    print("test %d" % i)
    smtp.sendmail(sender, receiver, msgRoot.as_string())  # 发送邮件


if __name__ == "__main__":
    MSG = "awfegafeafawefwafe"  # 要发送的文字
    FILE = "F:\\1.txt"  # 要发送的文件
    send_email(MSG, FILE)
