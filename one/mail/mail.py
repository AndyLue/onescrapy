# coding=utf-8
'''
Created on 2014年9月5日

@author: 绝尘
'''
from scrapy.mail import MailSender

mailer = MailSender()

def send_mail(message, title):
    print "Sending mail..........."
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    gmailUser = '123'
    gmailPassword = '123'
    recipient = '123@123'
  
    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = title
    msg.attach(MIMEText(message))
  
    mailServer = smtplib.SMTP('123', 12)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print "Mail sent"
    
if __name__ == '__main__':
#     mailer.send(to=["sunxiang@jiuqi.com.cn"], subject="Scrapy Test by Sun Xiang", body="Test")
    send_mail("123", "Mail Test001")
