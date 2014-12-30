#!/usr/bin/env python3    
#coding: utf-8    

import smtplib    
from email.mime.text import MIMEText    

receiver = 'guoylyy@163.com'    
sender = '327272993@qq.com'    
subject = 'python email test'    
smtpserver = 'smtp.qq.com'    
username = '327272993'    
password = '9011238cy'    

msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')    

msg['Subject'] = subject    

smtp = smtplib.SMTP()    
smtp.connect('smtp.qq.com','25')    
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()  
