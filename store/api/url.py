#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/15 15:20
class URL(object):
    #测试的接口地址
    base_test_url = "http://120.27.23.105"
    #生产环境的接口
    base_online_url = "https://www.zhaoapi.cn"

    # 注册
    register = "/user/reg"
    # 登录
    login = "/user/login"
    # 获取用户信息
    userinfo = "/user/getUserInfo"