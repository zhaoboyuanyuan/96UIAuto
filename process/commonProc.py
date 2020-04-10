# coding=utf-8
import datetime
import os
import random
import time

# import BeautifulReport
import pykeyboard
import re
from BeautifulReport import BeautifulReport
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from public import data
from public import excel
from util.webdr import webdr

wd=webdr()
ex=excel
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
class commonProc(object):
    img_path = 'img'

# 登录按钮判断能否点击
    def loginButtonDecide(self,driver):
        try:
            a=driver.find_element_by_xpath("//button[@style='background-image: none;']")
            print (a)
            return True
        except:
            return False

# 登录页toast捕捉
    def findToast(self,driver,message):
        time.sleep(2)
        ele = driver.find_element_by_class_name("el-message__content").text
        # me=message.decode("utf-8")
        if ele == message:
            return True
        else:
            return False

# 登录成功首页判断
    def loginedORNot(self,driver):
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "area-class-cell-span")))
            return True
        except:
            return False

# 抛出错误信息
    def messageShow(self,message):
        raise NameError(message)

# 抛出错误信息并截图
    def messageAndScreen(self,driver,message):
        self.save_some_img(driver)
        raise NameError(message)


    def login(self,driver):
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/input").send_keys("15951644332")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/input").send_keys("123456abcd")
        driver.find_element_by_xpath("/html/body/div[1]/div/button").click()
        if self.loginedORNot(driver) == False:
            self.messageShow("登录失败！")

    #首页检查
    def homeCheck(self,driver):
        a = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div[2]/span[1]").text
        b = driver.find_element_by_xpath("//*[@id='app']/div/section[2]/div/div/div[3]/span[1]").text
        if a == u"全部分区" and b == u"全部类别":
            return True
        else:
            return False

            #     获取控件的text

    #根据ID获取text
    def getTextById(self, driver, id):
        return driver.find_element_by_id(id).text

    #根据xpath获取text
    def getTextByXpath(self, driver, xpath):
        return wd.findXpath(driver,xpath).text


    # 判断页面元素是否存在
    def isElement(self, driver, identifyBy, c):
        '''
        Determine whether elements exist
        Usage:
        isElement(By.XPATH,"//a")
        '''
        flag = None
        try:
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                driver.find_element_by_tag_name(c)
            elif identifyBy == "css":
                driver.find_element_by_css_selector(c)
            flag = True
        except:
            flag = False
        finally:
            return flag



     # 判断页面上text是否存在
    def findItem(self, driver, text):
        # text = text.decode("utf-8")
        source = driver.page_source
        if text in source:
            return True
        else:
            return False

     # 判断页面上text列表是否存在
    def findItems(self, driver, text):
        # text = text.decode("utf-8")
        source = driver.page_source
        # print(source)
        if type(text)!= list:
            print('输入的text应该为列表')
        else:
            lis = []
            for i in text:
                if i in source:
                    lis.append(i)
            if lis == text:
                return True
            else:
                return False

    #截图
    # def screenShot(self,driver):
    #     pic_path = ("D:\\code\\SafetyappEducate\\img\\" + current_time + ".png")
    #     print(pic_path)
    #     time.sleep(3)
    #     print(driver.title)
    #     driver.save_screenshot(pic_path)


    #点击页面text
    def clickOnText(self,driver,text):
        wd.findXpath(driver,'//*[contains(text(),\''+text+'\')]').click()


    # 截图
    def save_some_img(self, driver):
        img_name='错误截图'
        screenpath = r'D:\code\96UIAutoC\save_img'
        driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(screenpath), current_time + img_name))
        png = "../save_img" + "/" + current_time + img_name + ".png"
        print("<img src='" + png + "' width=1200 height=600 />")


    def waitAmoment(self):
        time.sleep(3)

    def waitSuMom(self,driver):
        WebDriverWait(driver, 1).until(EC.invisibility_of_element_located((By.ID, 'id')))


    #当点击打开新的页面时，需要切换页柄到当前页面，比如只有两页的情况下
    def tapWeb(self,driver):
        windows = driver.window_handles
        # print(windows)
        driver.switch_to.window(windows[-1])

    #关闭原来的窗口
    def closeWeb(self,driver):
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        driver.close()

    #等待判断元素不可见,有返回值
    def eleInvisibility(self, driver,identifyBy, c):
        flag = None
        try:
            if identifyBy == "id":
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, c)))
            elif identifyBy == "xpath":
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, c)))
            elif identifyBy == "class":
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, c)))
            elif identifyBy == "css":
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, c)))
            flag = True
        except:
            flag = False
        finally:
            return flag

    # 等待判断元素不可见,有返回值
    def waitInvisib(self,driver,identifyBy, c):
        try:
            if identifyBy == "id":
                WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.ID, c)))
            elif identifyBy == "xpath":
                WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.XPATH, c)))
            elif identifyBy == "class":
                WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.CLASS_NAME, c)))
            elif identifyBy == "css":
                WebDriverWait(driver, 2).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, c)))
            return True
        except:
            return False



    # 等待判断元素可见,有返回值
    def elevisibility(self, driver,identifyBy, c):
        flag = None
        try:
            if identifyBy == "id":
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, c)))
            elif identifyBy == "xpath":
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, c)))
            elif identifyBy == "class":
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, c)))
            elif identifyBy == "css selector":
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, c)))
            flag = True
        except:
            flag = False
        finally:
            return flag

    # 等待元素加载
    def waitElemByXpath(self,driver,xpath):
        try:
            WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            self.messageShow('元素没加载出来')

    # 等待元素加载
    def waitForPage(self,driver,xpath):
        try:
            WebDriverWait(driver, 20,5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            self.messageShow('元素没加载出来')

    # 等待元素可见
    def waitElemVisibByXpath(self,driver,xpath):
        try:
            WebDriverWait(driver, 20,2).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except:
            self.messageShow('元素不可见')

    # 等待元素可点击
    def waitclickableByXpath(self, driver, xpath):
        WebDriverWait(driver, 20, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    #等待元素并点击
    def waitAndClickByXpath(self,driver,xpath):
        WebDriverWait(driver, 20,0.5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


    #等待元素并点击
    def waitAndClickByCss(self,driver,css):
        WebDriverWait(driver,20,0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css))).click()


    # 下拉菜单并选中
    def dropDownBox(self, driver, xpath, text):
        wd.clickByXpath(driver, xpath)
        time.sleep(1)
        wd.clickByXpath(driver, '//span[contains(text(),"' + text + '")]')

    # 键盘模拟输入,下键+确定
    def keyBoard(self):
        k1 = pykeyboard.PyKeyboard()
        k1.tap_key(k1.down_key)
        time.sleep(1)
        k1.tap_key(k1.enter_key)
        time.sleep(1)

    # 键盘模拟输入,下键两次+确定
    def keyBoard2(self):
        k1 = pykeyboard.PyKeyboard()
        k1.tap_key(k1.down_key)
        time.sleep(1)
        k1.tap_key(k1.down_key)
        time.sleep(1)
        k1.tap_key(k1.enter_key)
        time.sleep(1)

    #登录账户
    def logined(self,driver):
        a=0
        while 1:
            driver.find_element_by_id('login').click()
            driver.find_element_by_id('userName').clear()
            driver.find_element_by_id('userName').send_keys(data.userName)
            driver.find_element_by_id('password').clear()
            driver.find_element_by_id('password').send_keys(data.password)
            driver.find_element_by_id('loginBtn').click()
            if self.findToast(driver, '登录成功') == True:
                break
            elif a==5:
                self.messageShow("登录5次失败，退出")
            else:
                self.waitAmoment()
                driver.find_element_by_xpath('//*[@id="paas-app"]/div/header/nav/ul[2]/li[1]/a/span').click()
                driver.find_element_by_xpath('//*[@id="paas-app"]/div/header/nav/ul[2]/li[1]/div/a[1]').click()
                driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
                a=a+1

        self.waitAmoment()

    # 进入应用中心
    def intoCenter(self, driver):
        wd.clickByXpath(driver, ex.xpathCon('workbench'))
        self.waitAmoment()
        windows = driver.window_handles
        driver.switch_to.window(windows[0])
        driver.close()

    # 测试帐号托管
    def account(self, driver):
        self.tabNewpage(driver, 'https://www.51safety.com.cn/enterprise/orgManage')
        self.waitAmoment()
        if self.findItem(driver, '控制台') == False:
            self.messageShow('未进入控制台!')
        if self.findItem(driver, '删除托管') == False:
            wd.clickByXpath(driver, ex.xpathCon('btn-user1'))
            wd.clickByXpath(driver, ex.xpathCon('topButton'))
            wd.clickByXpath(driver, ex.xpathCon('testId'))
            wd.clickByXpath(driver, ex.xpathCon('defineButton'))
            self.waitAmoment()
            if self.getTextByXpath(driver, ex.xpathCon('btn-user1')) != '删除托管':
                self.messageShow('更改测试账号托管失败！')
        self.back(driver)

    # 退回到工作台
    def back(self, driver):
        wd.clickByXpath(driver, excel.xpathCon('back'))


    # 在打开到新的页面
    def tabNewpage(self, driver, url):
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        driver.get(url)
        self.waitAmoment()

    # 切换为测试账号
    def changeTest(self, driver):
        self.tapWeb(driver)
        wd.clickByXpath(driver, ex.xpathCon('setInf'))
        self.waitAmoment()
        wd.aboveByXpath(driver, ex.xpathCon('accountChange'))
        time.sleep(1)
        wd.clickByXpath(driver, ex.xpathCon('testAc'))
        time.sleep(1)

    #初始化数据
    def initData(self,driver):
        # 进入应用中心
        self.intoCenter(driver)
        # 测试帐号托管
        self.account(driver)
        # 切换为测试账号
        self.changeTest(driver)

    # 滑动到指定xpath元素那
    def dragXpath(self, driver, xpath):
        target = driver.find_element_by_xpath(xpath)
        driver.execute_script("arguments[0].scrollIntoView();", target)

    # 获取四位随机数
    def getFourRandomNum(self):
        seeds = "1234567890"
        # 定义一个空列表，每次循环，将拿到的值，加入列表
        random_num = []
        # choice函数：每次从seeds拿一个值，加入列表
        for i in range(4):
            random_num.append(random.choice(seeds))
        return "".join(random_num)

    #获取当前时间 格式如：2020-03-23 16:19
    def localTime(self):
        time1=time.strftime("%Y-%m-%d %H:%M", time.localtime())
        return str(time1)

    #获取元素列表的个数
    def elecount(self,driver):
        ele=wd.findElsXpath(driver,'/html/body/div[1]/div/section/main/div/section/main/div/div/div[2]/div/div/div[1]/div[4]/div[2]/table/tbody/tr')
        a=str(ele).split('>,')
        print(len(a))

