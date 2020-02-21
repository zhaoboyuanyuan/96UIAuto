# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/18 10:24


# 2、Pass平台--组织架构--测试帐号托管
# 3、《企业基本信息》填写
# 4、切回管理员，测试帐号赋值测试企业，（编辑测试帐号）--用户扩展信息

#优化点：1、主表太长，与附表一起编辑时，附表页面会卡住不动，单独添加附表时则不会；
#       2、主表一起编辑时，点击添加——周边环境信息，周边信息定位不到，单独添加附表时则不会；
import random
import time

import pykeyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.initializationModel import initializationModel
from process.baseProc import baseProc
from process.commonProc import commonProc
from public import data
from public import excel
from util.webdr import webdr

com=commonProc()
wd=webdr()
im=initializationModel()

class initializationProc(baseProc):

    def switch(self, driver, num):
        if num == 0:
            self.intoCenter(driver)
        elif num == 1: # 测试账号托管
            self.account(driver)
        elif num == 2:
            self.changeTest(driver)
        elif num == 3:
            self.enterForm(driver)
        elif num == 4:
            if com.findItem(driver,self.name1)==False:
                com.messageAndScreen(driver,'创建企业表失败')
        elif num == 5:
            self.addendum(driver)
        elif num == 6:
            if com.findItem(driver,self.name2)==False:
                com.messageAndScreen(driver,'创建附表失败')



    def account(self,driver):
        self.tabNewpage(driver,'https://www.51safety.com.cn/paas/index')
        wd.clickByXpath(driver,excel.xpathCon('organization'))
        com.waitAmoment()
        if com.findItem(driver,'控制台')==False:
            com.messageShow('未进入控制台!')
        if com.findItem(driver,'删除托管')==False:
            wd.clickByXpath(driver,excel.xpathCon('btn-user1'))
            wd.clickByXpath(driver,excel.xpathCon('topButton'))
            wd.clickByXpath(driver,excel.xpathCon('testId'))
            wd.clickByXpath(driver,excel.xpathCon('defineButton'))
            com.waitAmoment()
            if com.getTextByXpath(driver,excel.xpathCon('btn-user1'))!='删除托管':
                com.messageShow('更改测试账号托管失败！')
        self.back(driver)


    #进入应用中心
    def intoCenter(self,driver):
        wd.clickByXpath(driver, excel.xpathCon('workbench'))
        com.waitAmoment()
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        driver.close()

    # 在打开到新的页面
    def tabNewpage(self, driver, url):
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.get(url)
        com.waitAmoment()

    #退回到工作台
    def back(self,driver):
        wd.clickByXpath(driver,'//*[@id="x-header-app"]/div[1]/a')

    #切换为测试账号
    def changeTest(self,driver):
        com.tapWeb(driver)
        wd.clickByXpath(driver,'//*[@id="x-header-app"]/div[2]/div/ul/li[8]/div')
        wd.aboveByXpath(driver,'//*[@id="x-header-app"]/div[2]/div/ul/li[8]/ul/li[1]/span')
        com.waitAndClickByXpath(driver,'//*[@id="role-list"]/li[2]')
        com.waitAmoment()

    def scrollToBm(self,driver):
        # com.tapWeb(driver)
        # js = "var q=document.documentElement.scrollTop=10000"
        # js = "var q=document.body.scrollTop=10000"
        js="window.scrollTo(0, document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(3)

    def dropDownBox(self,driver,xpath,text):
        wd.clickByXpath(driver,xpath)
        time.sleep(1)
        wd.clickByXpath(driver, '//span[contains(text(),"'+text+'")]')

    #滑动到指定xpath元素那
    def dragXpath(self,driver,xpath):
        target = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].scrollIntoView();", target)

    #移除js属性，对input输入值
    def excejs(self,driver,xpath,text):
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"  # 1.原生js，移除属性
        driver.execute_script(js)
        wd.enterByXpath(driver,xpath,text)


    #点击添加进入表格
    def intoappInformation(self,driver):
        driver.get('https://www.51safety.com.cn/space-taicangxintaijiujin1/app/!/information/QiYeXinXi5')
        com.waitAmoment()
        wd.clickByXpath(driver, '//*[@id="J_body"]/section/main/div/div/div[2]/div/div[1]/div/span[1]')
        com.waitAmoment()

    #点击上传
    def upload(self,driver):
        wd.clickByXpath(driver,'//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[4]/div[2]/div[1]/div[2]/div/div/div/button')
        k1 = pykeyboard.PyKeyboard()
        k1.type_string(r'D:\code\upload_file.txt')
        time.sleep(2)
        k1.tap_key(k1.enter_key)
        k1.tap_key(k1.enter_key)
        time.sleep(2)

    #获取四位随机数
    def getFourRandomNum(self):
        seeds = "1234567890"
        # 定义一个空列表，每次循环，将拿到的值，加入列表
        random_num = []
        # choice函数：每次从seeds拿一个值，加入列表
        for i in range(4):
            random_num.append(random.choice(seeds))
        return "".join(random_num)

    # 核准日期
    def approvalDe(self, driver):
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
        driver.execute_script(js)
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[11]/div[2]/div/div/div/input',
                        '2020-02-05')

    # 营业期限至
    def occupationDe(self, driver):
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
        driver.execute_script(js)
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[11]/div[4]/div/div/div/input',
                        '2020-02-20')

    #键盘模拟输入,下键+确定
    def keyBoard(self):
        k1=pykeyboard.PyKeyboard()
        k1.tap_key(k1.down_key)
        k1.tap_key(k1.enter_key)
        time.sleep(2)


    # 点击更多，编辑进入测试编辑页
    def moreEdit(self,driver):
        wd.aboveByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/section/main/div/div/div[2]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/div[3]')
        # wd.aboveByXpath(driver,
        #                 '//*[@id="J_body"]/section/main/div/section/main/div/div/div[2]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/div[3]')
        time.sleep(1)
        wd.clickByXpath(driver, '/html/body/ul/li[2]/div')



        # 填写表格
    def enterForm(self, driver):
        self.name1='无忧研发测试组' + self.getFourRandomNum()
        self.intoappInformation(driver)
        # 企业名称
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/input',
                        self.name1)
        # 企业代码
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[4]/div/div/div/input',
                        self.getFourRandomNum())
        # 法定代表人
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div/div/input',
                        '爱因斯坦')
        # 点击选择日期，成立日期
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div/div/input')
        wd.clickByXpath(driver, '/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[3]/td[4]/div')
        # 企业性质
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/input',
                         '国有企业')
        # 企业规模
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[4]/div/div/div/div/input',
                         '大型')
        # 员工总数(人)
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div/div/input',
                        100)
        # 主要负责人
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div[4]/div/div/div/input',
                        '爱因斯坦')
        # 监管行业大类
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/div/div/div/input',
                         '危险化学品')

        # 监管行业小类
        # self.dropDownBox(driver,'//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div[4]/div/div/div/div/input','危险化学品存储')
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div[4]/div/div/div/div/input')
        self.keyBoard()

        # 国民经济行业大类
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]/div[2]/div/div/div/div/input',
                         '农、林、牧、渔业')

        # 国民经济行业小类
        # self.dropDownBox(driver,'//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]/div[4]/div/div/div/div/input','农业')
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]/div[4]/div/div/div/div/input')
        com.waitAmoment()
        self.keyBoard()

        # 所在区域
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[7]/div[2]/div/div/div/div/input',
                         '江苏省')
        # 详细地址
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[9]/div[2]/div/div/div/input',
                        '南京市')
        # 登记机关
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[10]/div[2]/div/div/div/input',
                        '南京市')
        # 登记状态
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[10]/div[4]/div/div/div/div/input',
                         '存续')
        # com.waitAmoment()

        # 核准日期
        self.approvalDe(driver)

        # 营业期限至
        self.occupationDe(driver)
        # 企业联系人
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[12]/div[2]/div/div/div/input',
                        '爱因斯坦')
        # 联系电话
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[12]/div[4]/div/div/div/input',
                        '15951644332')
        # 注册资金(万元)
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[13]/div[2]/div/div/div/input',
                        100)
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[13]/div[3]/div/div/div/div/input',
                         '人民币')

        # 经营范围
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[14]/div[2]/div/div/div/input',
                        '南京市')

        # 滑动之后填表
        self.scrollThen(driver)

        #点击确定
        com.waitAndClickByXpath(driver,'//*[@id="J_body"]/section/footer/div/button[2]')
        time.sleep(10)




    #滑动之后的填表
    def scrollThen(self,driver):

        # 滑动到安全管理机构设置情况
        self.dragXpath(driver,
                       '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/input')
        com.waitAmoment()

        # 安全管理机构设置情况
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/input',
                         '已设置')
        # 安全管理机构
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[4]/div/div/div/input',
                        '南京市')

        # 安标创建情况
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[7]/div[2]/div/div/div/div/input',
                         '已创建')

        self.dropDownBox(driver,
                         '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[7]/div[4]/div/div/div/div/input',
                         '一级')
        # 安标建立时间
        self.excejs(driver,
                    '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[8]/div[2]/div/div/div/input',
                    '2020-02-20')
        com.clickOnText(driver, '安标建立时间')

        # 是否存在重点监管危化品
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[2]/div/div/div/div/input')
        self.keyBoard()

        # 是否存在重点监管危险工艺
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[4]/div/div/div/div/input')
        self.keyBoard()

        # 是否存在危化品重大危险源
        wd.clickByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/div[6]/div/div/div/div/input')
        self.keyBoard()

        # 主要生产工艺简介
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]/div/div/div/textarea',
                        '爱因斯坦')

        # 重大危险源描述
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div[3]/div[2]/div/div/div/textarea',
                        '爱因斯坦')

        #上传文件
        self.upload(driver)


    #填写附表
    def addendum(self,driver):
        self.name2=self.getFourRandomNum()
        self.moreEdit(driver)

        # 点击添加——周边环境信息
        wd.aboveByXpath(driver, '//*[@id="J_body"]/section/main/div[1]/div[1]/div[2]/div')
        com.waitAndClickByXpath(driver, '/html/body/ul[2]/li')
        com.waitAmoment()

        com.tapWeb(driver)

        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/input',
                        '100')

        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div/input',
                        '100')
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div/div/div/input',
                         '东')
        self.dropDownBox(driver,
                         '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[4]/div/div/div/div/input',
                         '军事禁区、军事管理区')
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div/input',
                        self.name2)
        wd.clickByXpath(driver, '//*[@id="J_body"]/div[2]/div[5]/button[3]')
        com.waitAmoment()

        # 滑动到安全管理机构设置情况
        self.dragXpath(driver,
                       '//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div/div/input')
        com.waitAmoment()


    def te(self,driver):
        self.intoCenter(driver)
        self.changeTest(driver)
        driver.get('https://www.51safety.com.cn/space-taicangxintaijiujin1/app/!/information/QiYeXinXi5')
        com.waitAmoment()

        self.moreEdit(driver)
        # 点击添加——周边环境信息
        wd.aboveByXpath(driver,'//*[@id="J_body"]/section/main/div[1]/div[1]/div[2]/div')
        time.sleep(2)
        com.waitAndClickByXpath(driver, '/html/body/ul[2]/li')
        com.waitAmoment()

        com.tapWeb(driver)
        wd.enterByXpath(driver,
                        '//*[@id="J_body"]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/input',
                        '100')


        time.sleep(10)


    #Pass平台--组织架构--测试帐号托管
    def accountHost(self,driver):
        self.basePr(driver,[0,1])


    def fillForm(self,driver):
        # self.te(driver)
        self.basePr(driver,[0,2,3,4,5,6])






