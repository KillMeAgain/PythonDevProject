#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header
class Mail(object):
    def __init__(self, account,subject, content):
        self.smtpserver = 'smtp.qq.com'
        self.sender     = 'youjingqiang@foxmail.com'
        self.user       = '297403080@qq.com'
        self.password   = 'inhvuqqjgiiabicf'
        self.account = account
        self.subject = subject
        self.content = content
    # 发送邮件
    def send(self):
        self.msg = MIMEText(self.content, 'plain', 'utf-8')
        self.msg['Subject'] = Header(self.subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect(self.smtpserver)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.user, self.password)
        smtp.sendmail(self.user, self.account, self.msg.as_string())
        smtp.quit()
        self.write()
    # 写文件存储
    def write(self):
        f = open('mails.log','a')
        f.writelines("-------------------------------------------------------------\n")
        f.writelines("Time: %s \n" % datetime.now())
        f.write('Content-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\n')
        f.write("Subject: %s\n" % self.subject)
        f.write("Content: %s\n" % self.content)
        f.writelines("-------------------------------------------------------------\n")
        f.close()
