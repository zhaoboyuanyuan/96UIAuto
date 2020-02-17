# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2019/12/24 16:27
import unittest

import time

from selenium.webdriver import ActionChains

from process.commonProc import commonProc
from public.openWeb import openWeb
from util.webdr import webdr

o = openWeb()
com = commonProc()
wd=webdr()


class courseCommentTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()


    def tearDown(self):
        o.writeTearDown()

    #1、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“确定”按钮，成功删除
    def testDeleteSuccess(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“确定”按钮，成功删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div/section/section/section/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[9]/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
        # if com.findItem(self.driver,'消息推送测试课程1')==True:
        if com.findItem(self.driver,'消息推送测试课程1')==True:
            com.messageAndScreen(self.driver,'评价刪除失敗')


    #2、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“取消”按钮，取消删除
    def testDeleteCancel(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“取消”按钮，取消删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.clickByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
        com.clickOnText(self.driver, '删除')
        wd.clickByXpath(self.driver, '/html/body/div[2]/div/div[3]/button[1]')
        if com.findItem(self.driver,'课程1206（admin_51）')==False:
            com.messageAndScreen(self.driver,'评价取消刪除失敗')


    #3、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“关闭”按钮，取消删除
    def testDeleteCancel1(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“关闭”按钮，取消删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.clickByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
        com.clickOnText(self.driver, '删除')
        wd.clickByXpath(self.driver, '/html/body/div[2]/div/div[1]/button/i')
        if com.findItem(self.driver,'课程1206（admin_51）')==False:
            com.messageAndScreen(self.driver,'评价取消刪除失敗')



    #4、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“取消”取消删除
    def testAllDeleteCancel(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“取消”取消删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.clickByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
        wd.clickByXpath(self.driver,'/html/body/div/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[4]/td[1]/div/label/span/span')
        com.clickOnText(self.driver,'删除')
        wd.clickByXpath(self.driver,'/html/body/div[2]/div/div[3]/button[1]')
        if com.findItem(self.driver, '课程1206（admin_51）') == False:
            com.messageAndScreen(self.driver,'取消删除失败')


    #5、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“关闭”取消删除
    def testAllDeleteCancel1(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“关闭”取消删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.clickByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
        wd.clickByXpath(self.driver,'/html/body/div/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[4]/td[1]/div/label/span/span')
        com.clickOnText(self.driver,'删除')
        wd.clickByXpath(self.driver,'/html/body/div[2]/div/div[1]/button/i')
        if com.findItem(self.driver,'课程1206（admin_51）')==False:
            com.messageAndScreen(self.driver,'关闭取消删除失败')


    #6、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“确定”按钮，成功删除
    def testAllDeleteSucc(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“确定”按钮，成功删除"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.clickByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span')
        wd.clickByXpath(self.driver,
                        '/html/body/div/div[2]/div/section/section/section/div[2]/div[1]/div/div[4]/div[2]/table/tbody/tr[4]/td[1]/div/label/span/span')
        com.clickOnText(self.driver, '删除')
        wd.clickByXpath(self.driver, '/html/body/div[2]/div/div[3]/button[1]')
        if com.findItem(self.driver,'消息推送测试课程1')==True:
            com.messageAndScreen(self.driver,'评价刪除失敗')


    #7、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息
    def testScoreSucc(self):
        u"""课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input','2019-12-06 14:10:01')
        wd.enterByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input','2019-12-27 00:00:00')
        com.clickOnText(self.driver,'确认')
        time.sleep(3)
        if com.findItem(self.driver,'课程1206（admin_51）')==False:
            com.messageAndScreen(self.driver,'搜索课程失敗')


    #8、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息,点击“重置”按钮，取消筛选，显示全部信息
    def testScoreCanc(self):
        u"""课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息,点击“重置”按钮，取消筛选，显示全部信息"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input','2019-12-06 14:10:01')
        wd.enterByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input','2019-12-27 00:00:00')
        com.clickOnText(self.driver,'确认')
        com.clickOnText(self.driver,'重置')
        text=['课程1206（admin_51）','课程1206（administrator02）','测试课程1112-视频（很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长']
        if com.findItems(self.driver,text)==False:
            com.messageAndScreen(self.driver,'搜索课程失敗')


    #9、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间
    def testCircleClose(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input',
                        '2019-12-27 00:00:00')
        com.clickOnText(self.driver, '确认')
        wd.aboveByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input')
        time.sleep(3)
        js = 'document.getElementsByClassName("el-input__icon el-icon-circle-close")[0].click();'
        wd.execute_script(self.driver,js)

        if com.findItem(self.driver,'2019-12-27 00:00:00')==True:
            com.messageAndScreen(self.driver,'清空设置的结束时间失败')


    #10、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间，点击“确定”按钮，取消筛选，显示所有信息
    def testCircleClose1(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input',
                        '2019-12-27 00:00:00')
        com.clickOnText(self.driver, '确认')
        wd.aboveByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input')
        time.sleep(3)
        js = 'document.getElementsByClassName("el-input__icon el-icon-circle-close")[0].click();'
        wd.execute_script(self.driver,js)

        com.clickOnText(self.driver, '确认')
        text = ['课程1206（admin_51）', '课程1206（administrator02）', '测试课程1112-视频（很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长']
        if com.findItems(self.driver, text) == False:
            com.messageAndScreen(self.driver,'显示所有信息失敗')


    #11、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出小于等于结束时间的评论信息
    def testEndtime(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出小于等于结束时间的评论信息"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[4]/div/input',
                        '2019-08-29 09:51:20')
        com.clickOnText(self.driver, '确认')
        time.sleep(3)
        text=com.getTextByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[3]/table/tbody/tr/td[6]/div')
        if text>'2019-08-29 09:51:20':
            com.messageAndScreen(self.driver,'评论信息的時間大於結束時間')


    #12、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间
    def testBegintime(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input',
                        '2019-12-01 10:01:59')
        com.clickOnText(self.driver, '确认')
        wd.aboveByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input')
        time.sleep(3)
        js = 'document.getElementsByClassName("el-input__icon el-icon-circle-close")[0].click();'
        wd.execute_script(self.driver,js)

        if com.findItem(self.driver,'2019-12-01 10:01:59')==True:
            com.messageAndScreen(self.driver,'清空设置的開始时间失败')

    #13、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间，点击“确定”按钮，取消筛选，显示所有信息
    def testBegintime1(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间，点击“确定”按钮，取消筛选，显示所有信息"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input',
                        '2019-12-01 10:01:59')
        com.clickOnText(self.driver, '确认')
        wd.aboveByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input')
        time.sleep(3)
        js = 'document.getElementsByClassName("el-input__icon el-icon-circle-close")[0].click();'
        wd.execute_script(self.driver, js)
        com.clickOnText(self.driver, '确认')
        time.sleep(3)
        text = ['课程1206（admin_51）', '课程1206（administrator02）', '测试课程1112-视频（很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长']
        if com.findItems(self.driver, text) == False:
            com.messageAndScreen(self.driver,'显示所有信息失敗')

    #14、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出大于等于开始时间的评论信息
    def testbegintime2(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出大于等于开始时间的评论信息"""
        self.driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        time.sleep(3)
        wd.enterByXpath(self.driver,
                        '/html/body/div[1]/div[2]/div/section/section/section/div[1]/div[1]/div[2]/div/input',
                        '2019-12-06 00:00:00')
        com.clickOnText(self.driver, '确认')
        time.sleep(3)
        text=com.getTextByXpath(self.driver,'/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div')
        if text<'2019-12-06 00:00:00':
            com.messageAndScreen(self.driver,'评论信息的時間小于开始時間')








if __name__ == '__main__':
    unittest.main()