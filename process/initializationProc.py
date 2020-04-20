# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/18 10:24

# 2、Pass平台--组织架构--测试帐号托管
# 3、《企业基本信息》填写
# 4、切回管理员，测试帐号赋值测试企业，（编辑测试帐号）--用户扩展信息

#优化点：1、主表太长，与附表一起编辑时，附表页面会卡住不动，单独添加附表时则不会；
#
import random
import time

import pykeyboard
from pymouse import PyMouse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.initializationModel import initializationModel
from process.baseProc import baseProc
from process.commonProc import commonProc
from process.initialBaseProc import initialBaseProc
# from public import data
from public import excel
from util.webdr import webdr

com=commonProc()
wd=webdr()
im=initializationModel()
ex=excel
inba=initialBaseProc()
url=ex.dataCon('murl')


class initializationProc(baseProc):

    def switch(self, driver, num):
        if num == 0:
            self.intoCenter(driver)
        elif num == 1: # 测试账号托管
            self.account(driver)
        elif num == 2:
            com.changeTest(driver)
        elif num == 3:
            self.enterForm(driver,im.pname)
        elif num == 4:
            if com.findItem(driver,im.pname)==False:
                com.messageAndScreen(driver,im.message)
        elif num == 5:
            self.addendum(driver,im.sname)
        elif num == 6:
            if com.findItem(driver,im.sname)==False:
                com.messageAndScreen(driver,im.message)
        elif num ==7:
            self.process(driver)
        elif num==8: #点击添加表格
            self.intoappInformation(driver)
        elif num==9: #点击企业名称
            self.clickEle(driver)
        elif num==10: #校验字符
            if com.findItem(driver,im.itext)==False:
                com.messageAndScreen(driver,im.message)
        elif num==11:
            self.clickMath(driver)
        elif num==12:
            self.distanceNotNull(driver)
        elif num==13:
            self.distanceMath(driver)
        elif num==14: #进入企业基本信息表
            # driver.get('https://www.51safety.com.cn/space-taicangxintaijiujin1/app/!/information/QiYeXinXi5')
            driver.get('https://www.51safety.com.cn/space-'+url+'/app/!/information/QiYeXinXi5')
            time.sleep(5)
        elif num==15:
            inba.changeMaster(driver)
        elif num==16:
            inba.intoOrg(driver)
        elif num==17:
            inba.teInfo(driver)
        elif num == 18:
            self.foreData(driver)
        elif num == 19:
            self.operat(driver,im.pname)
        elif num == 20:
            self.intoappIn(driver)
        elif num == 21: #电话填入为空时，点击
            self.clicknum(driver)
        elif num == 22: #电话填入为数字222时，点击
            self.clicknumMatch(driver)


    #测试帐号托管
    def account(self,driver):
        # self.tabNewpage(driver,'https://www.51safety.com.cn/paas/index')
        # wd.clickByXpath(driver,ex.xpathCon('organization'))
        self.tabNewpage(driver,'https://www.51safety.com.cn/enterprise/orgManage')
        com.waitAmoment()
        if com.findItem(driver,'控制台')==False:
            com.messageShow('未进入控制台!')
        if com.findItem(driver,'删除托管')==False:
            wd.clickByXpath(driver,ex.xpathCon('btn-user1'))
            wd.clickByXpath(driver,ex.xpathCon('topButton'))
            wd.clickByXpath(driver,ex.xpathCon('testId'))
            wd.clickByXpath(driver,ex.xpathCon('defineButton'))
            com.waitAmoment()
            if com.getTextByXpath(driver,ex.xpathCon('btn-user1'))!='删除托管':
                com.messageShow('更改测试账号托管失败！')
        self.back(driver)


    #进入应用中心
    def intoCenter(self,driver):
        wd.clickByXpath(driver, ex.xpathCon('workbench'))
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
        wd.clickByXpath(driver,excel.xpathCon('back'))


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
        # driver.get('https://www.51safety.com.cn/space-taicangxintaijiujin1/app/!/information/QiYeXinXi5')
        driver.get('https://www.51safety.com.cn/space-'+url+'/app/!/information/QiYeXinXi5')
        time.sleep(5)
        com.forclick(driver, ex.xpathCon('addButton'))
        com.waitAmoment()

    #点击添加进入表格
    def intoappIn(self,driver):
        # driver.get('https://www.51safety.com.cn/space-taicangxintaijiujin1/app/!/information/QiYeXinXi5')
        driver.get('https://www.51safety.com.cn/space-'+url+'/app/!/information/QiYeXinXi5')
        time.sleep(5)
        self.delete(driver)
        com.forclick(driver, ex.xpathCon('addButton'))
        com.waitAmoment()

    #点击上传
    def upload(self,driver):
        wd.clickByXpath(driver,ex.xpathCon('upload'))
        k1 = pykeyboard.PyKeyboard()
        k1.tap_key(k1.shift_key)
        time.sleep(2)
        k1.type_string(r'D:\code\upload_file.txt')
        time.sleep(2)
        k1.tap_key(k1.space_key)
        time.sleep(2)
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
                        ex.xpathCon('approvalDate'),
                        '2020-02-05')

    # 营业期限至
    def occupationDe(self, driver):
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly')"
        driver.execute_script(js)
        wd.enterByXpath(driver,
                        ex.xpathCon('businessDate'),
                        '2020-02-20')

    #键盘模拟输入,下键+确定
    def keyBoard(self):
        k1=pykeyboard.PyKeyboard()
        k1.tap_key(k1.down_key)
        time.sleep(1)
        k1.tap_key(k1.enter_key)
        time.sleep(1)

    # 点击更多，编辑进入测试编辑页
    def moreEdit(self,driver):
        wd.aboveByXpath(driver,
                        ex.xpathCon('more'))
        # wd.aboveByXpath(driver,
        #                 '//*[@id="J_body"]/section/main/div/section/main/div/div/div[2]/div/div/div[1]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/div[3]')
        time.sleep(1)
        wd.clickByXpath(driver, ex.xpathCon('edit'))

    #鼠标强制点击添加-周围环境按钮
    def focusClick(self):
        m = PyMouse()
        x, y = m.screen_size()
        # print(x,y)
        # m.click(x - 100, y - 550, 1, 1)
        m.click(x - 100, y - 850, 1, 1)
        com.waitAmoment()


        # 填写表格
    def enterForm(self, driver,pname):
        # 企业名称
        wd.enterByXpath(driver,
                        ex.xpathCon('epname'),
                        pname)

        # 企业代码
        wd.enterByXpath(driver,
                        ex.xpathCon('epcode'),
                        self.getFourRandomNum())
        # 法定代表人
        wd.enterByXpath(driver,
                        ex.xpathCon('represen'),
                        '爱因斯坦')
        # 点击选择日期，成立日期
        wd.clickByXpath(driver,
                        ex.xpathCon('estaDate'))
        wd.clickByXpath(driver, ex.xpathCon('chooseDate'))
        # 企业性质
        self.dropDownBox(driver,
                         ex.xpathCon('quality'),
                         '国有企业')
        # 企业规模
        self.dropDownBox(driver,
                         ex.xpathCon('scope'),
                         '大型')
        # 员工总数(人)
        wd.enterByXpath(driver,
                        ex.xpathCon('empnum'),
                        100)
        # 主要负责人
        wd.enterByXpath(driver,
                        ex.xpathCon('personCharge'),
                        '爱因斯坦')
        # 监管行业大类
        self.dropDownBox(driver,
                         ex.xpathCon('largeClass'),
                         '危险化学品')

        # 监管行业小类
        # self.dropDownBox(driver,'//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[5]/div[4]/div/div/div/div/input','危险化学品存储')
        wd.clickByXpath(driver,
                        ex.xpathCon('subclass'))
        self.keyBoard()

        # 国民经济行业大类
        self.dropDownBox(driver,
                         ex.xpathCon('majorNational'),
                         '农、林、牧、渔业')

        # 国民经济行业小类
        # self.dropDownBox(driver,'//*[@id="J_body"]/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[6]/div[4]/div/div/div/div/input','农业')
        wd.clickByXpath(driver,
                        ex.xpathCon('nationalEconomy'))
        com.waitAmoment()
        self.keyBoard()

        # 所在区域
        self.dropDownBox(driver,
                         ex.xpathCon('location'),
                         '江苏省')
        # 详细地址
        wd.enterByXpath(driver,
                        ex.xpathCon('detailedAddress'),
                        '南京市')
        # 登记机关
        wd.enterByXpath(driver,
                        ex.xpathCon('registrationAu'),
                        '南京市')
        # 登记状态
        self.dropDownBox(driver,
                         ex.xpathCon('registrationSt'),
                         '存续')

        # 核准日期
        self.approvalDe(driver)

        # 营业期限至
        self.occupationDe(driver)
        # 企业联系人
        wd.enterByXpath(driver,
                        ex.xpathCon('contacts'),
                        '爱因斯坦')
        # 联系电话
        wd.enterByXpath(driver,
                        ex.xpathCon('telephone'),
                        '15951644332')
        # 注册资金(万元)
        wd.enterByXpath(driver,
                        ex.xpathCon('registeredCap'),
                        100)
        self.dropDownBox(driver,
                         ex.xpathCon('currency'),
                         '人民币')

        # 经营范围
        wd.enterByXpath(driver,
                        ex.xpathCon('bussScope'),
                        '南京市')

        # 滑动之后填表
        self.scrollThen(driver)

        # 点击确定
        com.waitAndClickByXpath(driver,ex.xpathCon('sureButton'))
        time.sleep(10)



    #滑动之后的填表
    def scrollThen(self,driver):

        # 滑动到安全管理机构设置情况
        self.dragXpath(driver,
                       ex.xpathCon('setup'))
        com.waitAmoment()

        # 安全管理机构设置情况
        self.dropDownBox(driver,
                         ex.xpathCon('setup'),
                         '已设置')
        # 安全管理机构
        wd.enterByXpath(driver,
                        ex.xpathCon('management'),
                        '南京市')

        # 安标创建情况
        self.dropDownBox(driver,
                         ex.xpathCon('safetyCreation'),
                         '已创建')

        self.dropDownBox(driver,
                         ex.xpathCon('oneLevel'),
                         '一级')
        # 安标建立时间
        self.excejs(driver,
                    ex.xpathCon('establishment'),
                    '2020-02-20')
        com.clickOnText(driver, '安标建立时间')

        # 是否存在重点监管危化品
        wd.clickByXpath(driver,
                        ex.xpathCon('dangerousChe'))
        self.keyBoard()

        # 是否存在重点监管危险工艺
        wd.clickByXpath(driver,
                        ex.xpathCon('dangerousPro'))
        self.keyBoard()

        # 是否存在危化品重大危险源
        wd.clickByXpath(driver,
                        ex.xpathCon('majorDanger'))
        self.keyBoard()

        # 主要生产工艺简介
        wd.enterByXpath(driver,
                        ex.xpathCon('briefIntroduction'),
                        '爱因斯坦')

        # 重大危险源描述
        wd.enterByXpath(driver,
                        ex.xpathCon('hazardSources'),
                        '爱因斯坦')

        #上传文件
        self.upload(driver)
        com.waitAmoment()

    #填写附表
    def addendum(self,driver,sname):

        # self.moreEdit(driver)
        # # 点击添加——周边环境信息
        # wd.aboveByXpath(driver, '//*[@id="J_body"]/section/main/div[1]/div[1]/div[2]/div')
        # com.waitAndClickByXpath(driver, '/html/body/ul[2]/li')
        # com.waitAmoment()
        com.tapWeb(driver)
        #距离
        wd.enterByXpath(driver,
                        ex.xpathCon('distance'),
                        '100')

        #该区域人数
        wd.enterByXpath(driver,
                        ex.xpathCon('numberPeople'),
                        '100')
        #方位
        self.dropDownBox(driver,
                         ex.xpathCon('position'),
                         '东')
        #类型
        self.dropDownBox(driver,
                         ex.xpathCon('type'),
                         '军事禁区、军事管理区')
        #周边环境名称
        wd.enterByXpath(driver,
                        ex.xpathCon('surrounding'),
                        sname)
        wd.clickByXpath(driver, ex.xpathCon('save'))
        com.waitAmoment()

        # 滑动到安全管理机构设置情况
        self.dragXpath(driver,
                      ex.xpathCon('setup'))
        com.waitAmoment()

    def process(self,driver):
        # 点击最新的一条
        wd.clickByXpath(driver,
                        ex.xpathCon('newCase'))
        com.waitAmoment()
        # 点击编辑
        wd.clickByXpath(driver, ex.xpathCon('editOne'))
        com.waitAmoment()
        # 添加-周围信息
        wd.aboveByXpath(driver, ex.xpathCon('addOne'))
        time.sleep(2)
        # self.focusClick()
        wd.clickByXpath(driver, '/html/body/ul/li')

    #填入为空时，点击
    def clickEle(self,driver):
        wd.clickByXpath(driver,ex.xpathCon('epname'))
        com.clickOnText(driver,'企业名称')

    #电话填入为空时，点击
    def clicknum(self,driver):
        wd.clickByXpath(driver,ex.xpathCon('lianxinum'))
        com.clickOnText(driver,'联系电话')

    #电话填入为数字222时，点击
    def clicknumMatch(self,driver):
        wd.enterByXpath(driver,ex.xpathCon('lianxinum'),'222')
        com.clickOnText(driver,'联系电话')

    #员工总数(人)填入文字
    def clickMath(self,driver):
        wd.enterByXpath(driver,ex.xpathCon('empnum'),'中国')
        com.clickOnText(driver,'员工总数(人)')

    #距离不能为空
    def distanceNotNull(self,driver):
        wd.clickByXpath(driver,ex.xpathCon('distance'))
        com.clickOnText(driver,'距离（m）')

    #距离不能为文字
    def distanceMath(self,driver):
        wd.enterByXpath(driver,ex.xpathCon('distance'),'中国')
        com.clickOnText(driver,'距离（m）')

    #更改名称为测试企业
    def foreData(self,driver):
        # 点击最新的一条
        wd.clickByXpath(driver,
                        ex.xpathCon('newCase'))
        com.waitAmoment()
        # 点击编辑
        wd.clickByXpath(driver, ex.xpathCon('editOne'))
        com.waitAmoment()
        wd.enterByXpath(driver,
                        ex.xpathCon('epname'),'测试企业')
        # 点击确定
        com.waitAndClickByXpath(driver, ex.xpathCon('sureButton'))
        com.waitSuMom(driver)

    #删除信息
    def delete(self,driver):
        try:
            #点击第一项
            wd.clickByXpath(driver,
                            '/html/body/div[1]/div/section/main/div/section/main/div/div/div[2]/div/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
            time.sleep(2)
            com.clickOnText(driver,'删除')
            wd.clickByXpath(driver,ex.xpathCon('sureButton1'))
            com.waitAmoment()
        except:
            pass

    def operat(self,driver,pname):
        driver.get('https://www.51safety.com.cn/space-'+url+'/app/!/information/QiYeXinXi5')
        time.sleep(5)
        self.delete(driver)
        com.forclick(driver, ex.xpathCon('addButton'))
        com.waitAmoment()
        self.enterForm(driver, pname)


    # def te(self,driver):
    #     self.intoCenter(driver)
    #
    #     self.changeTest(driver)
    #     driver.get('https://www.51safety.com.cn/space-taixingjinyanhuaxuea/app/!/information/QiYeXinXi5')
    #     time.sleep(5)
    #     # 点击最新的一条
    #     wd.clickByXpath(driver,
    #                     ex.xpathCon('newCase'))
    #     com.waitAmoment()
    #     # 点击编辑
    #     wd.clickByXpath(driver, ex.xpathCon('editOne'))
    #     com.waitAmoment()
    #     # 添加-周围信息
    #     wd.aboveByXpath(driver, ex.xpathCon('addOne'))
    #     time.sleep(2)
    #     # wd.clickByXpath(driver,'/html/body/ul/li')
    #     css = 'u1 li[title="周边环境信息"]'
    #     wd.clickByCss(driver, css)
    #     time.sleep(10)


    #Pass平台--组织架构--测试帐号托管
    def accountHost(self,driver):
        self.basePr(driver,[0,1])

    #填写主表
    def fillForm(self,driver):
        im.pname='测试企业' + str(self.getFourRandomNum())
        im.message='创建企业表失败'
        self.basePr(driver,[0,2,20,3,4])

    #增加附表
    def collateralForm(self,driver):
        im.pname='测试企业'
        im.sname=self.getFourRandomNum()
        im.message='创建附表失败'
        self.basePr(driver,[0,2,19,7,5,6])

    #主表校验不能为空
    def checkEmpty(self,driver):
        im.itext='此处不能为空'
        im.message='未弹出提示此处不能为空'
        self.basePr(driver,[0,2,8,9,10])

    #主表校验员工人数为数字
    def checkNotMath(self,driver):
        im.itext='此处为数字'
        im.message='未弹出提示此处为数字'
        self.basePr(driver,[0,2,8,11,10])

    #周围环境表格校验不能为空
    def checkCollEmpty(self,driver):
        im.itext = '此处不能为空'
        im.message = '未弹出提示此处不能为空'
        self.basePr(driver,[0,2,14,7,12,10])

    #周围环境表格校验为数字
    def checkCollMath(self,driver):
        im.itext = '此处为数字'
        im.message = '未弹出提示此处为数字'
        self.basePr(driver,[0,2,14,7,13,10])

    #切回管理员，测试帐号赋值测试企业，（编辑测试帐号）--用户扩展信息
    def editTestAccount(self,driver):
        im.itext = '应用保存成功'
        im.message = '未弹出提示应用保存成功'
        self.basePr(driver,[0,15,16,17,10])

    # 主表校验联系电话不能为空
    def checknumEmpty(self, driver):
        im.itext = '此处不能为空'
        im.message = '未弹出提示此处不能为空'
        self.basePr(driver, [0, 2, 8, 21, 10])

    # 主表校验联系电话格式不正确
    def checknumFormat(self, driver):
        im.itext = '电话号码格式不正确'
        im.message = '未弹出提示电话号码格式不正确'
        self.basePr(driver, [0, 2, 8, 22, 10])






