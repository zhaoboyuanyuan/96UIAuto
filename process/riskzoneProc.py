# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/28 10:37
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from model.riskzoneModel import riskzoneModel
from process.baseProc import baseProc
from process.commonProc import commonProc
from process.riskzoneBaseProc import riskzoneBaseProc
# from public import data
from public import excel
from util.webdr import webdr

'''
    二、企业风险分区
    1、评估单元划分
    2、区域固有风险评估（校验值），L值，S值，区域固有风险的验证。
    3、控制风险评估（默认加个等待时间）
     LS   LEC   MES配置计算风险等级
     蒙德法，道化学法，订制脚本计算风险等级，查看页面没有报错。
         事故后果模拟，订制脚本计算事故后果模拟。
    需要验证1、表单里面的风险值；2、管控措施清单的风险值；3、风险点清单的风险值；风险点固有等级风险值。
    4、企业四色图打点，包括单元打点，风险点打点，查看打点信息等
    5、事故后果模拟打点，验证图形画出来。
'''


com=commonProc()
wd=webdr()
rz=riskzoneModel()
ex=excel
rb=riskzoneBaseProc()
class riskzoneProc(baseProc):

    def switch(self, driver, num):
        if num == 0: #进入风险区域划分页面
            self.intopage(driver,1)
        elif num == 1: #点击添加
            self.add(driver)
        elif num == 2: #填写评估单元表格
            self.evaluation(driver,rz.text)
        elif num == 3: #新建风险点清单
            self.riskPoints(driver)
        elif num==4:
            com.forclick(driver,"//*[contains(text(),'确定')]")
            com.waitElemByXpath(driver,ex.xpathCon('allButton')) #等待所有按钮显示
        elif num==5:
            if not com.findItem(driver,rz.text):
                com.messageAndScreen(driver,rz.message)
        elif num==6:  #进入区域固有风险评估
            self.intopage(driver,2)
        elif num==7:  #点击添加
            self.add1(driver)
        elif num==8: #填写区域固有风险评估
            self.enterInherent(driver,rz.text)
        elif num==9: #检查LSR值
            self.checkLSR(driver,rz.message)
        elif num==10: #进入区域控制风险评估
            self.intopage(driver,3)
        elif num==11: # 区域控制风险评估点击添加
            self.add2(driver)
        elif num==12: #填写区域控制风险评估
            self.enterConRi(driver)
        elif num==13:
            # rb.taixing(driver)   # 泰兴版本的LEC、LS、MES
            self.enterLES(driver)  #填写LES
            self.enterLS(driver)   #填写LS
            self.enterMES(driver)  #填写MES
        elif num==14:  #校验计算风险等级
            self.checkLECLCMES(driver)
        elif num==15:
            self.delete(driver)
        elif num==16: #填写蒙德法表格
            rb.enterMen(driver)
        elif num==17: #点击安全初期评价按钮
            rb.clickInitialEvaluation(driver)
        elif num==18: #点击安全补偿评价
            rb.clickCompensationEvaluation(driver)
        elif num==19: #点击提交按钮
            rb.submit(driver)
        elif num==20: #填写道化学
            rb.enterdow(driver)
        elif num==21: #道化学点击安全初期评价按钮
            rb.clickinitialEva(driver)
        elif num==22: #道化学点击安全补偿评价
            rb.clickcompenEva(driver)
        elif num==23: #时间比较
            self.complieTime(driver,rz.text,rz.message)
        elif num==24: #之后的操作
            self.thenMende(driver,rz.text,rz.message)
        elif num==25: #添加事故模拟,进入重大事故后果模拟评价页面
            rb.intoShiGu(driver)
        elif num==26: #计算值
            rb.calculate(driver)
        elif num==27: # 检查计算值
            rb.checkPoint(driver,rz.message)
        elif num==28: # 模拟
            rb.moni(driver,rz.message)
        elif num==29: # 点击提交
            rb.clickSub(driver)
        elif num==30: # 事故模拟之后的操作
            self.thenMende1(driver,rz.text,rz.message)
        elif num==31: # 进入企业风险四色图
            self.intopage(driver,4)
        elif num==32: #预处理
            rb.earliest(driver)
        elif num==33: #添加
            rb.build(driver)
        elif num==34: #新建成功
            self.newBuild(driver,rz.message)
        elif num == 35: #画不规则
            rb.drawIr(driver)
        elif num == 36: #画方形
            rb.drawSquare(driver)
        elif num == 37: #画椭圆形
            rb.drawCircle(driver)
        elif num == 38: #打点
            rb.drawPoint(driver)
        elif num == 39: #绑定区域
            rb.bindTu(driver)
        elif num == 40: #检查绑定
            rb.checkbind(driver,1)
        elif num == 41: #检查绑定
            rb.checkbind(driver,2)
        elif num == 42: #查看
            rb.seeItem(driver)
        elif num == 43: #找文字列表
            com.findItems(driver,rz.text)
        elif num == 44: #检查风险点
            rb.checkpo(driver,rz.text,rz.message)
        elif num == 45: #检查绑定
            rb.checkbind(driver,3)



    #进入页面
    def intopage(self,driver,num):
        url=ex.dataCon('murl')
        if num==1: #进入风险区域划分页面
            driver.get('https://www.51safety.com.cn/space-' + url + '/app/!/information/QuYuChangSuoDanYuanX')
        elif num==2:  #进入区域固有风险评估
            driver.get('https://www.51safety.com.cn/space-' + url + '/app/!/information/QuYuGuYouFengXianPin')
        elif num==3:  #进入区域控制风险评估
            driver.get('https://www.51safety.com.cn/space-' + url + '/app/!/information/GuYouFengXianPingGu')
        elif num==4:  #进入企业风险四色图
            driver.get('https://www.51safety.com.cn/safetyapp/entRisk/view')
        # if not com.waitInvisib(driver,'xpath',ex.xpathCon('setInf')):
        #     com.messageShow('首页未切换')
        com.waitSuMom(driver)
        com.update(driver)


    #点击添加
    def add(self,driver):
        com.forclickcss(driver,'i[class="iconfont icon-xinjian"]')
        # wd.clickByCss(driver,'i[class="iconfont icon-xinjian"]')
        com.waitAmoment()

    # 区域固有风险评估页点击添加
    def add1(self,driver):
        com.forclick(driver,ex.xpathCon('QuYuFengXianadd'))
        com.waitAmoment()

    # 区域控制风险评估点击添加
    def add2(self,driver):
        com.forclick(driver,ex.xpathCon('GuYouFengXianadd'))
        com.waitAmoment()


    #填写评估单元表格
    def evaluation(self,driver,text):
        com.xpathExist(driver,ex.xpathCon('epname1'))
        #企业名称
        try:
            com.dropDownBox(driver,ex.xpathCon('epname1'),'测试企业')
        except:
            com.tapWeb(driver)
            com.dropDownBox(driver, ex.xpathCon('epname1'), '测试企业')
        #区域/场所/单元名称
        wd.enterByXpath(driver,ex.xpathCon('acdname'),text)
        #是否涉及重点监管化工工艺
        wd.clickByXpath(driver,ex.xpathCon('zhongdiangongyi'))
        sleep(1)
        com.keyBoard()
        #包含重大危险源等级
        com.dropDownBox(driver,ex.xpathCon('zhongdaweixianyuan'),'二级')
        #是否涉及重点监管危化品
        wd.clickByXpath(driver,ex.xpathCon('zhongdianjianguang'))
        sleep(1)
        com.keyBoard()
        #是否涉及剧毒易制爆化学品
        wd.clickByXpath(driver,ex.xpathCon('juduyizhi'))
        sleep(1)
        com.keyBoard()
        #区域/场所/单元描述
        wd.enterByXpath(driver,ex.xpathCon('acdname1'),'交通局')
        #单元编码
        wd.enterByXpath(driver,ex.xpathCon('danyuanbianma'),'交通局')
        #记录人
        wd.enterByXpath(driver,ex.xpathCon('recorder'),'交通局')

    #新建风险点清单
    def riskPoints(self,driver):
        #滑动到记录人
        com.dragXpath(driver,ex.xpathCon('recorder'))
        #点击添加
        wd.clickByXpath(driver,ex.xpathCon('jixinjianfenxian'))#基线容器
        # wd.clickByXpath(driver,ex.xpathCon('fengxiandianadd')) #泰兴容器
        com.waitAmoment()
        com.tapWeb(driver)
        #风险点基本信息
        try:
            wd.clickByXpath(driver,ex.xpathCon('fenxiandianjiben'))
        except:
            com.tapWeb(driver)
            wd.clickByXpath(driver,ex.xpathCon('fenxiandianjiben'))
        sleep(1)
        com.keyBoard()
        # com.waitAndClickByCss(driver, 'li[class="el-select-dropdown__item selected"][title="测试企业"]')
        # wd.clickByXpath(driver,'//li[contains(@title,"测试企业")]')
        # xpath='/html/body/div[8]/div[1]/div[3]/div'  #/html/body/div[8]/div[1]/div[1]/ul/li[2]
        #风险点名称
        wd.enterByXpath(driver,ex.xpathCon('riskName'),'交通局')
        #风险点编号
        wd.enterByXpath(driver,ex.xpathCon('riskNum'),com.getFourRandomNum())
        #风险点类型
        wd.clickByXpath(driver,ex.xpathCon('riskType'))
        sleep(1)
        com.keyBoard2()
        sleep(1)
        # 风险点类别
        wd.clickByXpath(driver,
                        ex.xpathCon('fenxiandianleibie'))
        sleep(1)
        com.keyBoard2()
        #点击保存
        wd.clickByXpath(driver,ex.xpathCon('save1'))
        com.waitAmoment()

    #填写区域固有风险评估
    def enterInherent(self,driver,text):
        com.waitElemVisibByXpath(driver,ex.xpathCon('epname2'))
        #企业名称
        com.dropDownBox(driver,ex.xpathCon('epname2'),'测试企业')
        #区域名称
        com.dropDownBox(driver,ex.xpathCon('quyumingcheng'),text)
        #区域内火灾危险性类别
        com.dropDownBox(driver,ex.xpathCon('quyuhuozai'),'丙类（不含丙类）以下')
        #化学品急性毒性危害类别
        com.dropDownBox(driver,ex.xpathCon('jixingduxing'),'类别4、类别5')
        #危险工艺和重点监管危险化学品
        com.dropDownBox(driver,ex.xpathCon('gongyihezhongdian'),
                        '（1）不涉及重点监管危险化学品且不涉及危险工艺和金属有机物合成反应（包括格氏反应）。')
        #工艺压力(p)
        com.dropDownBox(driver,ex.xpathCon('gongyiyali'),'p≤0.1MPa')
        #工艺温度(t)
        com.dropDownBox(driver,ex.xpathCon('gongyiwendu'),'t≤20℃')
        #评估区域与周边相邻的不符合防火间距要求的其他区域（包括周边企业）现场人数之和
        com.dropDownBox(driver,ex.xpathCon('bufuhefanghuo'),'0-2人')
        #评估区域与周边相邻其他区域（包括周边企业）现场人数的最大值
        com.dragXpath(driver,ex.xpathCon('renshuzuidazhi'))
        # com.dropDownBox(driver,'/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]/div/div/div/div[1]/input','0-2人')
        wd.clickByXpath(driver,ex.xpathCon('renshuzuidazhi'))
        sleep(1)
        com.keyBoard()
        #所在企业任一装置设施类区域最大现场人数
        # com.dropDownBox(driver,'/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div[3]/div[2]/div/div/div/div/input','0-2人')
        wd.clickByXpath(driver,
                        ex.xpathCon('zuidaxianchang'))
        sleep(1)
        com.keyBoard()
        #评估区域重大危险源等级
        com.dropDownBox(driver,ex.xpathCon('pinggudengji'),'非重大危险源')
        #企业边界外500米范围内
        com.dropDownBox(driver,ex.xpathCon('qiyebianjie'),'无或有1个低密度人员场所')
        #点击确定
        com.clickOnText(driver,'确定')
        com.waitAmoment()


    #检查LSR值
    def checkLSR(self,driver,message):
        com.waitSuMom(driver)
        com.tapWeb(driver)
        L=wd.findXpath(driver,ex.xpathCon('valueL')).text
        S=wd.findXpath(driver,ex.xpathCon('valueS')).text
        R=wd.findXpath(driver, ex.xpathCon('valueR')).text
        print(L,S,R)
        if L!='1' or S!='1' or R!='Ⅳ':
            com.messageAndScreen(driver,message)

    #删除记录
    def delete(self,driver):
        try:
            wd.clickByXpath(driver,
                            ex.xpathCon('allSelection'))
            sleep(2)
            com.clickOnText(driver,'删除')
            wd.clickByXpath(driver,ex.xpathCon('sureButton1'))
            com.waitAmoment()
        except:
            pass


    #填写区域控制风险评估
    def enterConRi(self,driver):
        com.waitAmoment()
        com.tapWeb(driver)
        #企业名称
        # js = "document.getElementsByClassName('el-input__inner')[0].removeAttribute('readonly');"
        # driver.execute_script(js)
        # wd.enterByXpath(driver, ex.xpathCon('epname3'), '测试企业')
        try:
            wd.clickByXpath(driver,ex.xpathCon('epname3'))
            com.waitAmoment()
            com.forclick(driver, '//span[contains(text(),"测试企业")]')
        except:
            com.tapWeb(driver)
            wd.clickByXpath(driver, ex.xpathCon('epname3'))
            com.waitAmoment()
            com.forclick(driver, '//span[contains(text(),"测试企业")]')
        #风险点名称
        js = "document.getElementsByClassName('el-input__inner')[1].removeAttribute('readonly');"
        driver.execute_script(js)
        wd.enterByXpath(driver,ex.xpathCon('rickName1'),'交通局')
        #评估类型
        com.dropDownBox(driver,ex.xpathCon('pingguleixing'),'定期风险评估')
        com.waitAmoment()
        #拉动页面到是否采用事故后果模拟法
        com.dragXpath(driver,ex.xpathCon('houguomoni'))
        com.waitAmoment()



    #填写LES
    def enterLES(self,driver):
        #点击添加按钮
        if com.isElement(driver,'xpath',ex.xpathCon('LECadd')):
            wd.clickByXpath(driver,ex.xpathCon('LECadd'))
        else:
            com.dragXpath(driver, ex.xpathCon('houguomoni'))
            com.waitAmoment()
            wd.clickByXpath(driver, ex.xpathCon('LECadd'))
        com.waitAmoment()
        com.tapWeb(driver)
        #事故发生的可能性
        try:
            com.dropDownBox(driver,ex.xpathCon('jishigukeneng'),'完全可能预料')
        except:
            com.tapWeb(driver)
            com.dropDownBox(driver, ex.xpathCon('jishigukeneng'), '完全可能预料')
        #暴露于危险环境的频率
        com.dropDownBox(driver,ex.xpathCon('jibaolupinglv'),'每月一次暴露')
        #事故后果严重程度
        com.dropDownBox(driver,ex.xpathCon('jishiguyanzhong'),'潜在违反法规和标准，造成3人以下死亡，或10人以下重伤，直接经济损失100万元以上，部分装置停工，造成地区影响')
        #点击保存
        wd.clickByXpath(driver,ex.xpathCon('save1'))
        com.waitAmoment()

    #填写LS
    def enterLS(self,driver):
        # 点击添加按钮
        if com.isElement(driver, 'xpath', ex.xpathCon('LSadd')):
            wd.clickByXpath(driver,ex.xpathCon('LSadd'))
        else:
            com.dragXpath(driver, ex.xpathCon('houguomoni'))
            com.waitAmoment()
            wd.clickByXpath(driver, ex.xpathCon('LSadd'))
        com.waitAmoment()
        com.tapWeb(driver)
        #可能发生的事故类型
        try:
            com.dropDownBox(driver,ex.xpathCon('shiguyanzhong'),'火灾')
        except:
            com.tapWeb(driver)
            com.dropDownBox(driver, ex.xpathCon('shiguyanzhong'), '火灾')
        #可能性级别
        com.clickOnText(driver, '可能发生的事故类型')
        com.dropDownBox(driver,ex.xpathCon('jikennegxingjibei'),'有充分、有效的防范、')
        #后果严重性
        com.dropDownBox(driver,ex.xpathCon('jibaolupinglv'),'完全符合，人员无伤亡，无直接经济损失，没有停工，形象没有受损')
        # 点击保存
        wd.clickByXpath(driver,ex.xpathCon('save1'))
        com.waitAmoment()

    #填写MES
    def enterMES(self,driver):
        #滑动到MES法评估等级
        com.dragXpath(driver,ex.xpathCon('MESdengji'))
        # 点击添加按钮
        wd.clickByXpath(driver,ex.xpathCon('MESadd'))
        com.waitAmoment()
        com.tapWeb(driver)
        #可能发生的事故类型
        try:
            com.dropDownBox(driver,ex.xpathCon('shiguyanzhong'),'火灾')
        except:
            com.tapWeb(driver)
            com.dropDownBox(driver, ex.xpathCon('shiguyanzhong'), '火灾')
        #控制措施的状态
        com.clickOnText(driver, '可能发生的事故类型')
        com.dropDownBox(driver,ex.xpathCon('jishigukeneng'),'无控制措施')
        #人体暴露的时间
        com.dropDownBox(driver,ex.xpathCon('jirentibaolu'),'更少的暴露')
        #伤害
        com.dropDownBox(driver,ex.xpathCon('jishanghai'),'轻微，仅需急救')
        # 点击保存
        wd.clickByXpath(driver, ex.xpathCon('save1'))
        com.waitAmoment()

    #校验计算风险等级
    def checkLECLCMES(self,driver):
        com.waitAmoment()
        #点击第一项
        wd.clickByXpath(driver,ex.xpathCon('diyixiang'))
        com.waitSuMom(driver)
        try:
            #LS法评估等级
            valueLS=wd.findXpath(driver,ex.xpathCon('LSfapinggu')).text
            #LEC法评估等级
            valueLEC=wd.findXpath(driver,ex.xpathCon('LECfapinggu')).text
            #MES法评估等级
            valueMES=wd.findXpath(driver,ex.xpathCon('MESfapinggu')).text
            #风险点固有等级
            valueRick=wd.findCss(driver,'.vertical > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)').text
            #管控等级
            valueCon=wd.findXpath(driver,ex.xpathCon('guangkongdengji')).text
            print(valueLS,valueLEC,valueMES,valueRick,valueCon)
            if valueLS!='低风险' or valueLEC!='较大风险' or valueMES!='低风险' or valueRick!='低风险' or valueCon!='车间级':
                com.messageAndScreen(driver,'计算风险等级失败')
        except:
            com.messageAndScreen(driver,'未自动生成评估方法')


    #例子
    # def clickable(self,driver):
    #     js="document.getElementsByClassName('el-select-dropdown el-popper is-multiple')[0].style.display='block';"
    #     driver.execute_script(js)
    #     bec=wd.findClassName(driver,'el-select-dropdown__empty')
    #     WebDriverWait(driver, 60).until(EC.invisibility_of_element_located(bec))
    #     kec=wd.findXpath(driver,'/html/body/div[1]/div/div[2]/div[4]/div/div/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/input')
    #     WebDriverWait(driver, 60).until(EC.element_to_be_clickable(kec))
    #     kec.click()

    #时间比较
    def complieTime(self,driver,time,messsage):
        #评估时间
        txt=com.getTextByXpath(driver,ex.xpathCon('pinggushijian'))
        print('服务器时间为'+txt)
        if txt<time:
            com.messageShow(messsage)

    #之后的操作
    def thenMende(self, driver,txt,message):
        self.intopage(driver,3)
        com.forclick(driver,ex.xpathCon('theFirst'))
        com.waitAmoment()
        if com.getTextByXpath(driver,ex.xpathCon('fengxianzhi'))!=txt:
            com.messageShow(message)

    #事故模拟之后的操作
    def thenMende1(self, driver,txt,message):
        self.intopage(driver,3)
        com.forclick(driver,ex.xpathCon('shoukuang'))
        com.waitAmoment()
        com.clickOnText(driver,'历史记录')
        com.waitAmoment()
        if not com.findItem(driver,txt):
            com.messageAndScreen(driver,message)

    #新建四色图上传图片检查图片是否存在
    def newBuild(self,driver,message):
        css = '.content-container > svg:nth-child(1) > image:nth-child(1)'
        com.cssExist(driver, css)
        if not com.isElement(driver, 'css', css):
            com.messageAndScreen(driver,message)


    #1、填写评估单元划分
    def assessmentUnits(self,driver):
        rz.text='交通局'+com.getFourRandomNum()
        rz.message='新建评估单元失败！'
        self.basePr(driver,[0,1,2,3,4,5])

    #2、区域固有风险评估（校验值），L值，S值，区域固有风险的验证。
    def inherent(self,driver):
        rz.text = '交通局' + com.getFourRandomNum()
        rz.message='未计算风险值'
        self.basePr(driver,[0,1,2,4,6,7,8,9])

    #3、控制风险评估
    def controlRisk(self,driver):
        rz.text = '交通局' + com.getFourRandomNum()
        self.basePr(driver,[10,15,11,12,13,4,14])

    #4、蒙德法-生成安全预评价结
    def mende(self,driver):
        rz.text='单元初次安全预评价结果'
        rz.message='未生成安全预评价结果'
        self.basePr(driver, [10, 15, 11, 12,16,17,5])

    #5、蒙德法-安全补偿评价结果
    def mende1(self,driver):
        rz.text='安全补偿评价结果'
        rz.message='未生成安全补偿评价结果'
        self.basePr(driver, [10, 15, 11, 12,16,17,18,5])

    #6、蒙德法-提交
    def mende2(self,driver):
        rz.text=com.localTime()
        print('本地时间为' + rz.text)
        rz.message='未保存成功'
        self.basePr(driver, [10, 15, 11, 12,16,17,18,19,23])

    #7、道化学-生成安全预评价结
    def dowHua(self,driver):
        rz.text = '单元初期安全评价结果'
        rz.message = '未生成安全预评价结果'
        self.basePr(driver, [10, 15, 11, 12,20,21,5])

    #8、道化学-安全补偿评价结果
    def dowHua1(self,driver):
        rz.text = '单元安全补偿评价结果'
        rz.message = '未生成安全补偿评价结果'
        self.basePr(driver, [10, 15, 11, 12,20,21,22,5])

    #9、道化学-提交
    def dowHua2(self,driver):
        rz.text = com.localTime()
        print('本地时间为'+rz.text)
        rz.message = '未保存成功'
        self.basePr(driver, [10, 15, 11, 12,20,21,22,19,23])

    #10、蒙德法校验
    def mendeCheck(self,driver):
        rz.text='低风险'
        rz.message='蒙德法未显示'
        self.basePr(driver, [10, 15, 11, 12,16,17,18,19,24])

    #11、道化学校验
    def dowCheck(self,driver):
        rz.text='低风险'
        rz.message='道化学未显示'
        self.basePr(driver, [10, 15, 11, 12,20,21,22,19,24])

    #12.事故后果模拟计算值
    def shiguCalValue(self,driver):
        rz.message = '计算值未显示'
        self.basePr(driver, [10, 15, 11, 12,25,26,27])

    #13.事故后果模拟
    def shiguSimulation(self,driver):
        rz.message = '模拟值未显示'
        self.basePr(driver, [10, 15, 11, 12,25,26,28])

    #14.事故后果模拟提交
    def shiguRefer(self,driver):
        rz.text = com.localTime()
        print('本地时间为' + rz.text)
        rz.message = '未保存成功'
        self.basePr(driver, [10, 15, 11, 12,25,26,27,29,23])

    #15.事故后果模拟校验
    def shiguCheck(self,driver):
        rz.text = '事故后果模拟'
        rz.message = '未找到事故后果模拟'
        self.basePr(driver, [10, 15, 11, 12,25,26,27,29,30])

    #16.查看导入图片
    def picture(self,driver):
        rz.message = '未新建成功'
        self.basePr(driver, [31,32,33,34])

    #17.画多边形图形
    def drawIrreg(self, driver):
        rz.text = '绑定'
        rz.message = '未创建多边形图形'
        self.basePr(driver, [31, 32, 33,35,5])

    #18.画方形
    def drawSqu(self,driver):
        rz.text = '绑定'
        rz.message = '未创建方形图形'
        self.basePr(driver, [31, 32, 33,36,5])

    #19.画椭圆
    def drawCir(self, driver):
        rz.text = '绑定'
        rz.message = '未创建椭圆图形'
        self.basePr(driver, [31, 32, 33,37,5])

    #20.打点
    def drawPt(self,driver):
        rz.text = '绑定'
        rz.message = '未创建风险点'
        self.basePr(driver, [31, 32, 33, 38, 5])

    #21.多边形图形绑定区域
    def bindIrreg(self,driver):
        rz.text = '绑定成功!'
        rz.message = '未绑定成功!'
        self.basePr(driver, [31, 32, 33, 35, 39,34])

    #22.多边形图形绑定区域校验
    def bindIrregcheck(self,driver):
        rz.text = '区域名称：'
        rz.message = '未检查到浮出的信息!'
        self.basePr(driver, [31, 32, 33, 35, 39,40,5])

    #23.方形图形绑定区域
    def bindSqu(self,driver):
        rz.text = '绑定成功!'
        rz.message = '未绑定成功!'
        self.basePr(driver, [31, 32, 33,36,39,34])

    #24.方形图形绑定区域校验
    def bindSqucheck(self,driver):
        rz.text = '区域名称：'
        rz.message = '未检查到浮出的信息!'
        self.basePr(driver, [31, 32, 33, 36, 39,40,5])

    #25.椭圆形绑定区域
    def bindCir(self,driver):
        rz.text = '绑定成功!'
        rz.message = '未绑定成功!'
        self.basePr(driver, [31, 32, 33,37,39,34])

    #26.椭圆形绑定区域校验
    def bindCircheck(self,driver):
        rz.text = '区域名称：'
        rz.message = '未检查到浮出的信息!'
        self.basePr(driver, [31, 32, 33,37, 39,41,5])

    #27.风险点绑定
    def bindPt(self,driver):
        rz.text = '绑定成功!'
        rz.message = '未绑定成功!'
        self.basePr(driver, [31, 32, 33,38,39,34])

    #28.风险点绑定区域校验
    def bindPtcheck(self,driver):
        rz.text = '交通局'
        rz.message = '未检查到浮出的信息!'
        self.basePr(driver, [31, 32, 33,38,39,45,5])

    #29.区域校验风险等级
    def areaCheck(self,driver):
        rz.text = ['低风险']
        rz.message = '未检查到区域校验风险等级!'
        self.basePr(driver, [31, 32, 33,37, 39,41,42,43])

    #30.点校验风险等级
    def pointCheck(self,driver):
        rz.text = '低风险'
        rz.message = '未检查到低风险!'
        self.basePr(driver, [31, 32, 33,38,39,40,42,44])

















