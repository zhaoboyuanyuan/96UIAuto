# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/24 15:22

# 4、切回管理员，测试帐号赋值测试企业，（编辑测试帐号）--用户扩展信息
from time import sleep

import pykeyboard
from pymouse import PyMouse
from selenium.webdriver import ActionChains

from process.commonProc import commonProc
from public import excel
from util.webdr import webdr

wd=webdr()
com=commonProc()
ex=excel
class initialBaseProc(object):

    #切回管理员账户
    def changeMaster(self,driver):
        com.tapWeb(driver)
        wd.clickByXpath(driver, ex.xpathCon('setInf'))
        wd.aboveByXpath(driver, ex.xpathCon('accountChange'))

        com.waitAndClickByXpath(driver, ex.xpathCon('masterAc'))
        com.waitAmoment()

    def quitAcc(self,driver):
        com.tapWeb(driver)
        wd.clickByXpath(driver, '//*[@id="x-header-app"]/div[2]/div/ul/li[6]/div')
        wd.clickByXpath(driver,'//*[@id="li-sub"]')
        wd.clickByXpath(driver,'/html/body/div[2]/div/div[3]/button[2]')

        com.waitAmoment()


    #进入组织架构，控制台,点编辑，点修改信息
    def intoOrg(self,driver):
        driver.get('https://www.51safety.com.cn/enterprise/orgManage')
        com.waitAmoment()
        if com.findItem(driver, '控制台') == False:
            com.messageShow('未进入控制台!')
        else:
            wd.clickByXpath(driver,ex.xpathCon('editTwo'))
            com.tapWeb(driver)
            wd.clickByXpath(driver,ex.xpathCon('modifyInfo'))
            com.waitAmoment()
            if com.findItem(driver, '测试扩展信息') == False:
                com.messageShow('未进入测试扩展信息页面!')

    #填写测试扩展信息
    def teInfo(self,driver):
        #用户类型
        com.dropDownBox(driver,ex.xpathCon('customerType'),'企业用户')
        com.waitAmoment()
        #单位名称
        com.dropDownBox(driver,ex.xpathCon('unitName'),'测试企业')
        #所属部门
        wd.enterByXpath(driver,ex.xpathCon('departments'),'产品部')
        #所属岗位
        wd.enterByXpath(driver,ex.xpathCon('station'),'测试组')
        #证件类型
        com.dropDownBox(driver,ex.xpathCon('idType'),'居民身份证')
        #证件号
        wd.enterByXpath(driver,ex.xpathCon('idNumber'),'110')
        #员工工号
        wd.enterByXpath(driver, ex.xpathCon('staffNumber'), '110')
        #是否为特种作业人员
        wd.clickByXpath(driver,ex.xpathCon('specialOperator'))
        com.keyBoard()
        #户籍所在地
        wd.enterByXpath(driver,ex.xpathCon('domicileLocation'),'南京市')
        #毕业院校
        wd.enterByXpath(driver, ex.xpathCon('school'), '南京大学')
        #在线学习系统角色
        com.dropDownBox(driver,ex.xpathCon('onlineLearn'),'学员')
        #点击确定按钮
        wd.clickByXpath(driver,'//*[@id="J_body"]/div[2]/div[3]/section/footer/div/button[2]')
        sleep(5)

    #
    # #所属岗位为空
    # def notNull(self,driver):
    #     wd.clearByXpath(driver, ex.xpathCon('station'))
    #     wd.clickByXpath(driver, '//*[@id="J_body"]/div[2]/div[3]/section/footer/div/button[2]')
    #     com.waitAmoment()







