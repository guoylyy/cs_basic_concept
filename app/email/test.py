#!/usr/bin/python

import smtplib

sender = 'yiliang@foxmail.com'
receivers = ['327272993@qq.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print "Successfully sent email"
except Exception, e:
    raise e
    print "Error: unable to send email"
