# coding=utf-8
import os
import time

# import BeautifulReport
from BeautifulReport import BeautifulReport
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util.webdr import webdr

wd=webdr()
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
            elif identifyBy == "css selector":
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
        screenpath = r'D:\code\SafetyappEducate\save_img'
        driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(screenpath), current_time + img_name))
        png = "../save_img" + "/" + current_time + img_name + ".png"
        print("<img src='" + png + "' width=1200 height=600 />")


    def waitAmoment(self):
        time.sleep(3)


    #当点击打开新的页面时，需要切换页柄到当前页面，比如只有两页的情况下
    def tapWeb(self,driver):
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])

    # 等待元素可见
    def waitElemByXpath(self,driver,xpath):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    #等待元素并点击
    def waitAndClickByXpath(self,driver,xpath):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()




