#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/15 16:00
import unittest
from store.user import register
class RegisterUnit(unittest.TestCase):
    #初始化注册对象
    @classmethod
    def setUpClass(cls):
        cls.register= register.RegisterControl()
    #对注册请求进行单元测试
    def test_Register(self):
      self.response=  self.register.register_Success()
      print(self.response)
      #断言-判断结果是否相等
      self.assertEqual('1',self.register.getCode())





