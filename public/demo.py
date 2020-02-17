# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/1/8 17:13
import unittest

from ddt import ddt, data, unpack

from public import excel



@ddt
class demo(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
        # self.assertEqual(actual, expected)

    # def test_dict(self, value1, value2):
    # @data({'value1': 1, 'value2': 2}, {'value1': 3, 'value2': 4})
    # @unpack


    # @data([1,2,3],[4,5,6],[7,8,9])
    # @unpack
    # def testAs01(self,a,b,expected):
    #     print(a,b,expected)
        # actual = int(a) - int(b)
        # expected = int(expected)
    #     print(value1, value2)
    #     # self.assertEqual(value2, value1 + 1)

    #
    #指定的用例testcase，用同一个脚本运行
    @data(excel.case(1),excel.case(2))
    @unpack
    def testAs01(self,inform,expected):
        print(inform,expected)


    #sheet2模块下新增的，自动同一个脚本运行
    @data(*excel.newSheet01())
    @unpack
    def testAs01(self,url, username, password):
        print(url,username,password)




if __name__ == '__main__':
    unittest.main()