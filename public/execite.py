# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2019/12/31 11:01
import os
import unittest

import time
from BeautifulReport import BeautifulReport
from selenium import webdriver

from process.baseProc import baseProc

current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class execite(unittest.TestCase):
    """ 测试代码生成与loader 测试数据"""

    def setUp(self):
        # print("开始测试")
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")

    def tearDown(self):
        # print("结束测试")
        self.driver.close()

    def test_is_none(self):
        """
        test None object
        :return:
        """
        self.save_some_img('错误截图')
        self.assertEqual("1", "2")

    def save_some_img(self, img_name):
        screenpath = r'D:\code\SafetyappEducate\save_img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(screenpath), current_time + img_name))
        png = "../save_img" + "/" + current_time + img_name + ".png"
        print("<img src='" + png + "' width=1000 height=500 />")



