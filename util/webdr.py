# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2019/12/26 15:11
#对webdriver进行二次封装


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By



class webdr(object):

    #点击事件封装
    def clickById(self,driver,id):
        self.findId(driver,id).click()

    def clickByXpath(self,driver,xpath):
        self.findXpath(driver,xpath).click()

    def clickByName(self,driver,name):
        self.findName(driver,name).click()

    def clickByClassName(self,driver,classname):
        self.findClassName(driver,classname).click()

    def clickBylinkText(self,driver,link_text):
        self.findliText(driver,link_text).click()

    def clickByCss(self,driver,css_selector):
        self.findCss(driver,css_selector).click()


    #输入事件封装
    def enterById(self,driver,id,content):
        self.findId(driver, id).send_keys(content)

    def enterByXpath(self,driver,xpath,content):
        self.findXpath(driver,xpath).send_keys(content)

    def enterByName(self,driver,name,content):
        self.findName(driver,name).send_keys(content)

    def enterByClassName(self,driver,classname,content):
        self.findClassName(driver,classname).send_keys(content)

    def enterBylinkText(self,driver,link_text,content):
        self.findliText(driver,link_text).send_keys(content)

    def enterByCss(self,driver,css_selector,content):
        self.findCss(driver,css_selector).send_keys(content)

    #鼠标事件

    #鼠标右击
    def rightClickByXpath(self,driver,xpath):
        right=self.findXpath(driver,xpath)
        ActionChains(driver).context_click(right).perform()


    def rightClickById(self, driver, id):
        right = self.findId(driver, id)
        ActionChains(driver).context_click(right).perform()

    #鼠标双击
    def doubleClickByXpath(self,driver,xpath):
        double = self.findXpath(driver, xpath)
        ActionChains(driver).double_click(double).perform()

    def doubleClickById(self,driver,id):
        double = self.findXpath(driver, id)
        ActionChains(driver).double_click(double).perform()


    #鼠标拖放
    def dragById(self,driver,id1,id2):
        source=self.findId(driver,id1)
        target=self.findId(driver,id2)
        ActionChains(driver).drag_and_drop(source, target).perform()

    def dragByXpath(self,driver,xpath1,xpath2):
        source=self.findId(driver,xpath1)
        target=self.findId(driver,xpath2)
        ActionChains(driver).drag_and_drop(source, target).perform()


    #鼠标移到元素上
    def aboveById(self,driver,id):
        above=self.findId(driver,id)
        ActionChains(driver).move_to_element(above).perform()

    def aboveByXpath(self,driver,xpath):
        above=self.findXpath(driver,xpath)
        ActionChains(driver).move_to_element(above).perform()

    def aboveByClassname(self,driver,classname):
        above=self.findClassName(driver,classname)
        ActionChains(driver).move_to_element(above).perform()


    #按住鼠标左键在一个元素
    def leftCAHById(self,driver,id):
        left=self.findId(driver,id)
        ActionChains(driver).click_and_hold(left).perform()

    def leftCAHByXpath(self,driver,xpath):
        left=self.findXpath(driver,xpath)
        ActionChains(driver).click_and_hold(left).perform()



    def title(self, driver):
        return driver.title()

    def findId(self, driver, id):
        return driver.find_element_by_id(id)

    def findElsId(self, driver, id):
        return driver.find_elements_by_id(self, id)

    def findXpath(self, driver, xpath):
        return driver.find_element_by_xpath(xpath)

    def findElsXpath(self, driver, xpath):
        return driver.find_elements_by_xpath(xpath)

    def findliText(self, driver, link_text):
        return driver.find_element_by_link_text(link_text)

    def findElsliText(self, driver, text):
        return driver.find_elements_by_link_text(text)

    def findpaliText(self, driver, link_text):
        return driver.find_element_by_partial_link_text(link_text)

    def findElsPaliText(self, driver, link_text):
        return driver.find_elements_by_partial_link_text(link_text)

    def findName(self, driver, name):
        return driver.find_element_by_name(name)

    def findElsName(self, driver, name):
        return driver.find_elements_by_name(name)

    def findTagName(self, driver, name):
        return driver.find_element_by_tag_name(name)

    def findElsTagName(self, driver, name):
        return driver.find_elements_by_tag_name(name)

    def findClassName(self, driver, name):
        return driver.find_element_by_class_name(name)

    def findElsClassName(self, driver, name):
        return driver.find_elements_by_class_name(name)

    def findCss(self, driver, css_selector):
        return driver.find_element_by_css_selector(css_selector)

    def findElsCss(self, driver, css_selector):
        return driver.find_elements_by_css_selector(css_selector)

    def execute_script(self, driver, script, *args):
        return driver.execute_script(script, *args)

    def execute_async_script(self, driver, script, *args):
        return driver.execute_async_script(script, *args)

    def current_url(self, driver):
        return driver.current_url()

    def page_source(self, driver):
        return driver.page_source()

    def close(self, driver):
        return driver.close()

    def quit(self, driver):
        return driver.quit()

    def current_window_handle(self, driver):
        return driver.current_window_handle()

    def window_handles(self, driver):
        return driver.window_handles()

    def maximize_window(self, driver):
        return driver.maximize_window()

    def fullscreen_window(self, driver):
        return driver.fullscreen_window()

    def minimize_window(self, driver):
        return driver.minimize_window()

    def switch_to(self, driver):
        return driver.switch_to()

    # Target Locators
    def switch_to_active_element(self, driver):
        return driver.switch_to_active_element()

    def switch_to_window(self, driver, window_name):
        return driver.switch_to_window(window_name)

    def switch_to_frame(self, driver, frame_reference):
        return driver.switch_to_frame(frame_reference)

    def switch_to_default_content(self, driver):
        return driver.switch_to_default_content()

    def switch_to_alert(self, driver):
        return driver.switch_to_alert()

    # Navigation
    def back(self, driver):
        return driver.back()

    def forward(self,driver):
       return driver.forward()

    def refresh(self,driver):
        return driver.refresh()

    # Options
    def get_cookies(self,driver):
        return driver.get_cookies()

    def get_cookie(self, driver,name):
        return driver.get_cookie(name)

    def delete_cookie(self, driver,name):
        return driver.delete_cookie(name)

    def delete_all_cookies(self,driver):
        return driver.delete_all_cookies()

    def add_cookie(self, driver,cookie_dict):
        return driver.add_cookie(cookie_dict)

    # Timeouts
    def implicitly_wait(self,driver, time_to_wait):
        return driver.implicitly_wait(time_to_wait)

    def set_script_timeout(self, driver,time_to_wait):
        return driver.set_script_timeout(time_to_wait)

    def set_page_load_timeout(self,driver, time_to_wait):
        return driver.set_page_load_timeout(time_to_wait)

    def find_element(self, driver):
        return driver.find_element()

    def find_elements(self,driver):
        return driver.find_elements()


    def desired_capabilities(self,driver):
       return driver.desired_capabilities()

    def get_screenshot_as_file(self, driver,filename):
        return driver.get_screenshot_as_file(filename)

    def save_screenshot(self, driver,filename):
       return driver.save_screenshot(filename)

    def get_screenshot_as_png(self,driver):
        return driver.get_screenshot_as_png()

    def get_screenshot_as_base64(self,driver):
        return driver.get_screenshot_as_base64()

    def set_window_size(self,driver, width, height):
        return driver.set_window_size(width, height)

    def get_window_size(self,driver):
        return driver.get_window_size()

    def set_window_position(self, driver,x, y):
        return driver.set_window_position(x,y)

    def get_window_position(self,driver):
        return driver.get_window_position()

    def get_window_rect(self,driver):
        return driver.get_window_rect()

    def set_window_rect(self, driver):
        return driver.set_window_rect()