# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/3/11 17:04
import os
import unittest

import time
from BeautifulReport import BeautifulReport

from public.execite import execite

if __name__ == '__main__':
    # test_suite = unittest.defaultTestLoader.discover('../process', pattern='test*.py')
    test_suite = unittest.TestSuite()
    test_suite.addTest(execite('test_is_none'))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    path='D:\\测试报告'
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)

    BeautifulReport(test_suite).report(filename='测试报告_'+current_time, description='测试deafult报告',
                                       log_path=path)