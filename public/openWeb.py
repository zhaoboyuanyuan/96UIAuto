# coding=utf-8

import unittest
from time import sleep

from selenium import webdriver

from process.commonProc import commonProc
from public import data
from util.webdr import webdr

wd=webdr()
com = commonProc()
class openWeb():

    def writeSetUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = data.urlFirst
        self.verificationErrors =[]
        self.accept_next_alert = True
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.testLogin()

    def writeTearDown(self):
        self.driver.quit()
        # assertEqual([], self.verificationErrors)
        print('启动浏览器成功！')

    def getDr(self):
        return self.driver

    def testLogin(self):
        # wd.clickById(self.driver,'login')
        self.driver.find_element_by_id('login').click()
        self.driver.find_element_by_id('userName').clear()
        self.driver.find_element_by_id('userName').send_keys(data.userName)
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(data.password)
        self.driver.find_element_by_id('loginBtn').click()
        # self.driver.implicitly_wait(30)
        if com.findToast(self.driver, '登录成功') == False:
            com.messageAndScreen(self.driver,"登录失败!")
        sleep(2)



# o=openWeb()
# o.writeSetUp()
# o.writeTearDown()

