# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/3/23 10:15

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
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import pykeyboard
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from process.commonProc import commonProc
from public import excel
from util.webdr import webdr

com=commonProc()
wd=webdr()
ex=excel
x = 100
y = 100
class riskzoneBaseProc(object):

    #填写蒙德法表格
    def enterMen(self,driver):
        #点击添加
        try:
            wd.clickByXpath(driver,ex.xpathCon('mondadd'))
        except:
            com.dragXpath(driver, ex.xpathCon('houguomoni'))
            com.waitAmoment()
            wd.clickByXpath(driver, ex.xpathCon('mondadd'))
        com.waitAmoment()
        #点击保存
        com.forclick(driver,ex.xpathCon('save1'))
        com.waitAmoment()
        #点击顶栏蒙德法
        wd.clickByXpath(driver,ex.xpathCon('monddinglan'))
        com.waitAmoment()
        #关闭原窗口
        com.closeWeb(driver)
        com.tapWeb(driver)
        #点击添加按钮
        wd.clickByXpath(driver,ex.xpathCon('add1'))
        com.waitAmoment()
        com.tapWeb(driver)
        #评价单元名称
        wd.enterById(driver,ex.idCon('unitName'),'测试')
        #评价物质名称
        wd.enterById(driver,ex.idCon('substancesName'),'甲醇')
        #工程温度(K)
        wd.enterById(driver,ex.idCon('engineeringTemperature'),'222')
        #单元物质质量(Kg)
        wd.enterById(driver,ex.idCon('substanceMass'),'2222')
        #单元作业面积(㎡)
        wd.enterById(driver,ex.idCon('operatingArea'),'222')
        #单元操作压力(Pa)
        wd.enterById(driver,ex.idCon('operatingPressure'),'222222')
        #单元配置高度(m)
        wd.enterById(driver,ex.idCon('configurationHeight'),'22')

        #点击下一步
        com.forclickid(driver,ex.idCon('nextStep'))
        com.waitAmoment()
        com.tapWeb(driver)
        value='4'
        #单元物质系数
        try:
            wd.enterById(driver,'MF',value)
        except:
            com.tapWeb(driver)
            wd.enterById(driver, 'MF', value)
        #特殊物质危险系数
        wd.enterById(driver,ex.idCon('specialSubStanceHazardousCoefficient'),value)
        #一般工艺危险系数
        wd.enterById(driver,ex.idCon('generalCraftsHazardousCoefficient'),value)
        #特殊工艺危险系数
        wd.enterById(driver,ex.idCon('specialCraftsHazardousCoefficient'),value)
        #毒性危险系数
        wd.enterById(driver,ex.idCon('poisonousHazardousCoefficient'),value)
        #数量危险系数
        wd.enterById(driver,ex.idCon('numberHazardousCraftsCoefficient'),value)
        #混合扩散系数
        wd.enterById(driver,ex.idCon('mixedDiffusionCoefficient'),value)
        #配置危险系数
        wd.enterById(driver,ex.idCon('arrangeHazardousCoefficient'),value)
        #高压危险系数
        wd.enterById(driver,ex.idCon('highPressureHazardousCoefficient'),value)

    # 点击安全初期评价按钮
    def clickInitialEvaluation(self,driver):
        wd.clickById(driver,ex.idCon('initialEvaluation'))
        sleep(1)

    # 道化学点击安全初期评价按钮
    def clickinitialEva(self,driver):
        wd.clickById(driver,ex.idCon('initialEva'))
        sleep(1)


    # 点击安全补偿评价
    def clickCompensationEvaluation(self,driver):
        wd.clickById(driver,ex.idCon('compensationEvaluation'))
        sleep(1)

    # 道化学点击安全补偿评价
    def clickcompenEva(self,driver):
        wd.clickById(driver,ex.idCon('compenEva'))
        sleep(1)

    # 点击提交按钮
    def submit(self,driver):
        wd.clickById(driver,ex.idCon('jumpApp'))
        com.waitAmoment()
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        com.waitAmoment()


    #填写道化学
    def enterdow(self,driver):
        #拖拉页面到Ls
        com.dragXpath(driver,ex.xpathCon('LSkuang'))
        #点击添加按钮
        try:
            wd.clickByXpath(driver,ex.xpathCon('daohuaxueadd'))
        except:
            com.dragXpath(driver, ex.xpathCon('LSkuang'))
            wd.clickByXpath(driver, ex.xpathCon('daohuaxueadd'))
        com.waitAmoment()
        # 点击保存
        com.forclick(driver, ex.xpathCon('save1'))
        com.waitAmoment()
        #点击道化学按钮
        wd.clickByXpath(driver,ex.xpathCon('daohuaxueanniu'))
        com.waitAmoment()
        # 关闭原窗口
        com.closeWeb(driver)
        com.tapWeb(driver)
        #点击添加
        wd.clickByXpath(driver,ex.xpathCon('add1'))
        com.waitAmoment()
        com.tapWeb(driver)

        value='333'
        #评价物质名称
        try:
            com.forclickid(driver,ex.idCon('pjwzmc'))
            sleep(1)
            com.clickOnText(driver,'甲醇')
        except:
            com.tapWeb(driver)
            com.forclickid(driver, ex.idCon('pjwzmc'))
            sleep(1)
            com.clickOnText(driver, '甲醇')
        #物质质量(kg)
        wd.enterById(driver,ex.idCon('wzzl'),value)
        #原始成本(万元)
        wd.enterById(driver,ex.idCon('yscb'),value)
        #增长系数
        wd.enterById(driver,ex.idCon('zzxs'),value)
        #每月产值(万元)
        wd.enterById(driver,ex.idCon('mycz'),value)
        #供应难度
        wd.clickByXpath(driver,ex.xpathCon('gongyingnandu'))
        wd.clickByXpath(driver,ex.xpathCon('gongyingyiban'))

        # 点击下一步
        wd.clickByXpath(driver,ex.xpathCon('xiayibu'))
        com.waitAmoment()
        com.tapWeb(driver)
        #单元物质系数
        wd.clickById(driver,ex.idCon('popWzxsDialog'))
        sleep(1)
        wd.clickByCss(driver,'input[checkid="17"]')
        wd.clickByXpath(driver,ex.xpathCon('queding'))


    # 添加事故模拟,进入重大事故后果模拟评价页面
    def intoShiGu(self,driver):
        # 拖拉页面到Ls
        com.dragXpath(driver, ex.xpathCon('LSkuang'))
        # 点击添加按钮
        try:
            wd.clickByXpath(driver, ex.xpathCon('shiguadd'))
        except:
            com.dragXpath(driver, ex.xpathCon('LSkuang'))
            wd.clickByXpath(driver, ex.xpathCon('shiguadd'))
        com.waitAmoment()
        com.tapWeb(driver)
        #点击保存
        com.forclick(driver,ex.xpathCon('save1'))
        com.waitAmoment()
        #点击事故模拟按钮
        com.forclick(driver,ex.xpathCon('shiguanniu'))
        com.waitAmoment()
        com.tapWeb(driver)
        wd.clickByXpath(driver,ex.xpathCon('add2'))
        com.waitAmoment()
        com.tapWeb(driver)


    # 点击上传
    def upload(self, driver):
        #上传按钮
        wd.clickByXpath(driver,'/html/body/div/div/div/div[1]/div[5]/div/div[2]/div/div/div[2]/div/div[1]/button')
        k1 = pykeyboard.PyKeyboard()
        k1.tap_key(k1.shift_key)
        sleep(1)
        k1.type_string(r'D:\code\2.png')
        sleep(1)
        k1.press_key(k1.control_key)
        k1.tap_key('A')
        k1.release_key(k1.control_key)
        sleep(2)
        k1.tap_key(k1.enter_key)
        com.waitAmoment()


    def picpl(self,driver):
        try:
            # self.findToast(driver, 'el-message el-message--error', '请选择要上传的图片')
            ele = driver.find_element_by_class_name('el-message el-message--error').text
            if ele=='请选择要上传的图片':
                return True
            else:
                return False
        except:
            return False



    # 检查计算值
    def checkPoint(self,driver,message):
        if com.eleInvisibility(driver, 'class', 'tishi'):
            #点击点
            wd.clickByCss(driver,'#mapArea > svg:nth-child(1) > circle:nth-child(4)')
            if not com.findItem(driver,'装置编号'):
                com.messageAndScreen(driver,message)


    #计算值
    def calculate(self,driver):
        #上传图片
        wd.uploadById(driver,'uploadMap',r'D:\code\2.png')
        com.waitAmoment()

        #点击环境参数
        wd.clickById(driver,ex.idCon('basicParameterBtn'))
        com.waitAmoment()
        com.tapWeb(driver)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,ex.idCon('regionInput') )))
        except:
            com.messageShow('未进入页面')
        #所在区域
        wd.clickById(driver,ex.idCon('regionInput'))
        com.clickOnText(driver,'南京')
        com.clickOnText(driver,'所在区域：')
        #点击风向频率
        wd.clickById(driver,ex.idCon('ui-id-2'))
        #点击确定
        # css='div[class="ui-dialog-buttonset"][1]'
        css='.ui-dialog-buttonset button:nth-child(1)'
        wd.clickByCss(driver,css)
        com.waitAmoment()

        #装置信息
        wd.clickById(driver,ex.idCon('deviceInfoBtn'))
        com.waitAmoment()
        #装置名称
        wd.enterById(driver,ex.idCon('deviceName'),'测试')
        com.waitAmoment()
        #装置编号
        value='2222'
        wd.enterById(driver,ex.idCon('deviceNo'),value)
        #点击坐标定位
        # wd.clickById(driver,'getCoordinateBtn')
        # ActionChains(driver).move_by_offset(500, 500).click().perform()
        wd.enterById(driver,ex.idCon('x'),'250')
        wd.enterById(driver,ex.idCon('y'),'250')
        #装置体积
        wd.enterById(driver,ex.idCon('deviceVolume'),value)
        #物料名称
        wd.clickById(driver,ex.idCon('materialName'))
        com.clickOnText(driver,'甲醇')
        #装置类型
        wd.clickById(driver,ex.idCon('select2-chosen-2'))
        wd.clickByXpath(driver,ex.xpathCon('zhuangzhileixing'))
        com.waitAmoment()
        #物料类型
        wd.clickById(driver,ex.idCon('select2-chosen-3'))
        wd.clickByXpath(driver,ex.xpathCon('wuliaoleixing'))
        #删除
        wd.clickByXpath(driver,ex.xpathCon('shanchu'))
        #运行温度
        wd.enterById(driver,ex.idCon('uv_operatingTemperature'),value)
        #运行压力
        wd.enterById(driver,ex.idCon('uv_operatingPressure'),value)
        #气体密度
        wd.enterById(driver,ex.idCon('uv_gasDensity'),value)
        #充装系数
        wd.enterById(driver,ex.idCon('uv_fittingFactor'),'1')
        #泄放总量占设备体积的百分数
        wd.enterById(driver,ex.idCon('uv_dischargeTotalPer'),'1')
        #点击保存
        wd.clickById(driver,ex.idCon('cardInfoSave'))
        com.waitAmoment()

        #点击计算
        wd.clickById(driver,ex.idCon('calcBtn'))

    #点击事故类型模拟
    def shiguleixingmoni(self,driver):
        if com.eleInvisibility(driver, 'class', 'tishi'):
            #选择事故类型
            wd.clickById(driver,ex.idCon('select2-chosen-1'))
            wd.clickByXpath(driver,'//*[contains(@id,"select2-result-label")]')
            #点击模拟
            wd.clickById(driver,ex.idCon('acSimulation'))
        else:
            com.messageShow('计算时，提示没出来')

    #模拟校验
    def moni(self,driver,message):
        self.shiguleixingmoni(driver)
        com.waitAmoment()
        if not com.isElement(driver,'css','#mapArea > svg:nth-child(1) > circle:nth-child(8)'):
            com.messageAndScreen(driver,message)


    # 点击提交
    def clickSub(self,driver):
        self.shiguleixingmoni(driver)
        com.waitAmoment()
        wd.clickByXpath(driver,'//*[@id="jumpApp"]')
        com.waitAmoment()
        com.tapWeb(driver)

    #预处理
    def earliest(self,driver):
        if com.findItem(driver,'暂无数据，快去添加图层吧~'):
            #点击添加图层
            wd.clickByXpath(driver,ex.xpathCon('addtucen'))
        else:
            wd.aboveByXpath(driver,ex.xpathCon('xiaobishang'))
            com.waitAmoment()
            #点小笔
            wd.clickByXpath(driver,ex.xpathCon('axiaob'))
            #添加图层
            wd.aboveByXpath(driver,ex.xpathCon('tucen'))
            #添加上方图层
            wd.clickByXpath(driver,ex.xpathCon('shangfangtc'))
        com.tapWeb(driver)

    #添加
    def build(self,driver):
        #名称
        wd.enterByXpath(driver,ex.xpathCon('mingcheng'),com.getFourRandomNum())
        #上传
        self.upload(driver)
        #点击确定
        wd.clickByXpath(driver,ex.xpathCon('queding1'))

    # 新建成功toast捕捉
    def findToast(self, driver,classname, text):
        sleep(3)
        ele = driver.find_element_by_class_name(classname).text
        if ele == text:
            return True
        else:
            return False

    #鼠标左击
    def leftclick(self,driver,x,y):
        ActionChains(driver).move_by_offset(x, y).click().perform()

    #鼠标双击
    def doubleclick(self,driver,x,y):
        ActionChains(driver).move_by_offset(x, y).double_click().perform()

    #鼠标右击
    def rightclick(self,driver,x,y):
        ActionChains(driver).move_by_offset(x, y).context_click().perform()

    #按住左键拉动
    def leftHold(self,driver,x,y,value):
        ActionChains(driver).move_by_offset(x, y).click_and_hold().perform()
        ActionChains(driver).move_by_offset(x+value, y+value).release().perform()



    #画不规则
    def drawIr(self,driver):
        #点击不规则按钮
        com.forclick(driver,ex.xpathCon('buguize'))
        self.leftclick(driver,x,y)
        sleep(1)
        self.leftclick(driver,x,y-100)
        sleep(1)
        self.leftclick(driver,x,y+100)
        sleep(1)
        self.doubleclick(driver,x-400,y)
        sleep(1)
        #右击原点
        self.rightclick(driver,0,0)


    #画方形
    def drawSquare(self,driver):
        #方形
        com.forclick(driver, ex.xpathCon('fangxing'))
        self.leftHold(driver,x,y,100)
        sleep(1)
        # 右击原点
        self.rightclick(driver, 0, 0)

    #画椭圆形
    def drawCircle(self,driver):
        # 点击椭圆形按钮
        com.forclick(driver, ex.xpathCon('tuoyuan'))
        sleep(1)
        position = driver.get_window_position()
        # 打印窗口坐标
        a=position["x"]+x
        b=position["y"]+y
        self.leftHold(driver,a,b,40)
        sleep(1)
        # 右击原点
        self.rightclick(driver, -50, -50)


    #打点
    def drawPoint(self,driver):
        #风险点
        com.forclick(driver, ex.xpathCon('fengxiandi'))
        self.leftclick(driver,x,y)
        com.waitAmoment()
        # 右击原点
        self.rightclick(driver, 0, 0)
        sleep(1)

    #绑定区域
    def bindTu(self,driver):
        #点击绑定
        wd.clickByXpath(driver,ex.xpathCon('bind'))
        com.waitAmoment()
        # wd.clickByXpath(driver,'/html/body/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div')
        com.clickOnText(driver,'交通局')
        #点击保存
        wd.clickByXpath(driver,ex.xpathCon('save2'))

    #检查绑定
    def checkbind(self,driver,index):
        if index==1:
            self.rightclick(driver,0,0)
        elif index==2:
            self.rightclick(driver,-50, -50)
        elif index==3:
            self.leftclick(driver,0,0)
        else:
            com.messageShow('index输入有误')
        sleep(2)

    #查看
    def seeItem(self,driver):
        #点击查看
        com.forclick(driver,ex.xpathCon('bind'))
        com.waitAmoment()

    #检查风险点
    def checkpo(self,driver,text,message):
        te=com.getTextByXpath(driver,ex.xpathCon('kzfxdj'))
        if te!=text:
            com.messageAndScreen(driver,message)









































































