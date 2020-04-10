import random
import unittest
from time import sleep

import re
from selenium import webdriver

from public import data


# class MyTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = data.urlFirst
#         self.verificationErrors = []
#         self.accept_next_alert = True
#         self.driver.get(self.base_url)
#         self.driver.maximize_window()
#
#
#     def test_something(self):
#         try:
#             self.assertEqual(True, False)
#         except AssertionError as e:
#             self.verificationErrors.append(str(e))
#
#     def test_something1(self):
#         try:
#             self.assertEqual(True, True)
#         except AssertionError as e:
#             self.verificationErrors.append(str(e))
#
#     def tearDown(self):
#         self.driver.quit()
#         print(self.verificationErrors)
#         print('启动浏览器成功！')
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()


# str='[<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="2b3f8946-1b88-47ca-ad6d-908ca7167913", element="85e6a4e8-fac7-41b7-bd59-9f02496bb9c8")>,<selenium.webdriver.firefox.webelement.FirefoxWebElement (session="2b3f8946-1b88-47ca-ad6d-908ca7167913", element="e56bee9a-a164-4877-8bff-c8ef9b171f7c")>, <selenium.webdriver.firefox.webelement.FirefoxWebElement (session="2b3f8946-1b88-47ca-ad6d-908ca7167913", element="42e88271-2b8e-475d-9cdd-c113f5309f25")>]'
# a=str.split('>,')
# b=re.match('^<+.*+>,$',str)
# print(b)
# print(a)
# print(len(a))







