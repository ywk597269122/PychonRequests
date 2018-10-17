#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/15 16:18
import os
import smtplib
# 导入设置系统编码
import sys
import time
import unittest
from email.header import Header
from email.mime.text import MIMEText

import HTMLTestRunner

from store.unit import registerunit

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#发送邮件
def send_mail(new_report):
    f = open(new_report, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('八维接口自动化测试报告', 'utf-8')
    # 这里使用 简单邮件协议
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('1553685468@qq.com', 'wsnesoroewnzhfde')  # 不是你的邮箱登录密码，而是你登录成功之后设置授权码
    smtp.sendmail('1553685468@qq.com', '1553685468@qq.com', msg.as_string())
    smtp.quit()
    print ('邮件已发出！注意查收。')


#======查找测试目录，找到最新生成的测试报告======

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print (file_new)
    return file_new



#定义主方法
if __name__=='__main__':
    #添加单元测试到测试套件中
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(registerunit.RegisterUnit))
    #直接添加单元测试到测试套件中
    #suit= unittest.makeSuite(registerunit.RegisterUnit,"test")
    path = os.getcwd()  # 此脚本的父级目录
    report_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    report_name = path + '\\report\\' + report_time + '-report.html'  # 报告保存路径及名称
    #写入
    with open(report_name, 'wb') as fp:
       # 生成报告未HTML格式，
       runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'电商注册接口测试报告', description=u'用例执行情况')
       runner.run(suit)  # 开始执行生成测试报告
    #此方法是获取测试报告的所在目录路径
    new_report = new_report(path + '\\report\\')
    #此方法根据测试报告所在目录路径发送邮件
    send_mail(new_report)