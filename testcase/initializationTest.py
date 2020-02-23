# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/18 10:35
import unittest

from process.commonProc import commonProc
from process.initializationProc import initializationProc
from public.openWeb import openWeb


o = openWeb()
com = commonProc()
init=initializationProc()


class initializationTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()

    def tearDown(self):
        o.writeTearDown()

    # 1.Pass平台--组织架构--测试帐号托管
    def testAccountHost(self):
        init.accountHost(self.driver)

    # 2.填写主表
    def testFillForm(self):
        init.fillForm(self.driver)

    # 3.增加附表
    def testCollateralForm(self):
        init.collateralForm(self.driver)

    # 4.主表校验不能为空
    def testCheckEmpty(self):
        init.checkEmpty(self.driver)

    # 5.主表校验员工人数不能为数字
    def testCheckNotMath(self):
        init.checkNotMath(self.driver)

    # 6.周围环境表格校验不能为空
    def testCheckCollEmpty(self):
        init.checkCollEmpty(self.driver)

    # 7.周围环境表格校验为数字
    def testCheckCollMath(self):
        init.checkCollMath(self.driver)



if __name__ == '__main__':
    unittest.main()
