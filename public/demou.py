import unittest
from time import sleep

from selenium import webdriver

from public import data


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = data.urlFirst
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url)
        self.driver.maximize_window()


    def test_something(self):
        try:
            self.assertEqual(True, False)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_something1(self):
        try:
            self.assertEqual(True, True)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        print(self.verificationErrors)
        print('启动浏览器成功！')




if __name__ == '__main__':
    unittest.main()
