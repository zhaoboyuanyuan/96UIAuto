# coding=utf-8

import unittest
from time import sleep

from selenium import webdriver

from process.commonProc import commonProc
from public import data
from util.webdr import webdr

wd = webdr()
com = commonProc()


class openWeb():
    def writeSetUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = data.urlFirst
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.login()



    def writeTearDown(self):
        self.driver.quit()
        # assertEqual([], self.verificationErrors)
        print('测试流程完成')

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
        com.waitAmoment()



    def login(self):
        a=0
        while 1:
            self.driver.find_element_by_id('login').click()
            self.driver.find_element_by_id('userName').clear()
            self.driver.find_element_by_id('userName').send_keys(data.userName)
            self.driver.find_element_by_id('password').clear()
            self.driver.find_element_by_id('password').send_keys(data.password)
            self.driver.find_element_by_id('loginBtn').click()
            if com.findToast(self.driver, '登录成功') == True:
                break
            elif a==5:
                com.messageShow("登录5次失败，退出")
            else:
                com.waitAmoment()
                self.driver.find_element_by_xpath('//*[@id="paas-app"]/div/header/nav/ul[2]/li[1]/a/span').click()
                self.driver.find_element_by_xpath('//*[@id="paas-app"]/div/header/nav/ul[2]/li[1]/div/a[1]').click()
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
                a=a+1

        com.waitAmoment()


# o = openWeb()
# o.writeSetUp()
# o.writeTearDown()
