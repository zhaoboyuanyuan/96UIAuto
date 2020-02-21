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

    def testAccountHost(self):
        init.accountHost(self.driver)


    def testFillForm(self):
        init.fillForm(self.driver)



if __name__ == '__main__':
    unittest.main()
