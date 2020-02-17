# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/1/6 10:16
import time

from model.courseCommModel import courseCommModel
from process.baseProc import baseProc
from process.commonProc import commonProc
from public import excel
from util.webdr import webdr

com = commonProc()
cm=courseCommModel()
wd=webdr()

class courseCommProc(baseProc):


    def switch(self, driver, num):
        if num == 0: #跳转到课程后台
            driver.get('https://mtools.51safety.com.cn/safetyapp/educate/manage/comment')
        elif num==1:
            time.sleep(3)

        elif num==2:  #选择第一条记录
            wd.clickByXpath(driver,excel.xpathCon('sectionOne'))

        elif num==3:  #点击对应的删除按钮
            wd.clickByXpath(driver,excel.xpathCon('deleteButton'))

        elif num==4:  #点击取消按钮
            wd.clickByXpath(driver,excel.xpathCon('cancelButton'))

        elif num==5:
            if com.findItem(driver,cm.text) == True:
                com.messageAndScreen(driver,cm.message)

        elif num==6:#点击删除按钮
            com.clickOnText(driver, "删除")

        elif num==7:
            if com.findItem(driver,cm.text) == False:
                com.messageAndScreen(driver,cm.message)

        elif num==8:  #点击x按钮
            wd.clickByXpath(driver,excel.xpathCon('closeButton'))

        elif num==9:  #第二条记录
            wd.clickByXpath(driver,excel.xpathCon('sectionTwo'))

        elif num==10: #开始时间输入框
            wd.enterByXpath(driver,excel.xpathCon('beginInput'),cm.timeBegin)

        elif num==11: #结束时间输入框
            wd.enterByXpath(driver,excel.xpathCon('endInput'),cm.timeEnd)

        elif num==12:#点击确认按钮
            com.clickOnText(driver, "确认")

        elif num==13:#点击重置按钮
            com.clickOnText(driver, "重置")

        elif num==14: #搜索所有的课程信息，先罗列三条
            self.search(driver,cm.message)

        elif num==15: #鼠标悬浮结束时间输入框上
            self.above(driver)

        elif num==16: #js点击x按钮
            self.excjs(driver)

        elif num==17: #评论信息的时间大于结束时间就报错
            self.compl(driver,cm.timeEnd)

        elif num==18: ##鼠标悬浮开始时间输入框上
            self.above1(driver)

        elif num==19: #评论信息的時間小于开始時間就报错
            self.comp2(driver,cm.timeBegin)



    #搜索所有的课程信息，先罗列三条
    def search(self,driver,message):
        text = ['课程1206（admin_51）', '课程1206（administrator02）', '测试课程1112-视频（很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长']
        if com.findItems(driver, text) == False:
            com.messageAndScreen(driver, message)

    #鼠标悬浮结束时间输入框上
    def above(self,driver):
        wd.aboveByXpath(driver,excel.xpathCon('endInput'))

    #鼠标悬浮开始时间输入框上
    def above1(self,driver):
        wd.aboveByXpath(driver,excel.xpathCon('beginInput'))
        time.sleep(3)

    #js点击x按钮
    def excjs(self,driver):
        js = 'document.getElementsByClassName("el-input__icon el-icon-circle-close")[0].click();'
        wd.execute_script(driver, js)

    #评论信息的時間大於結束時間就报错
    def compl(self,driver,endtime):
        text = com.getTextByXpath(driver,
                                  '/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[3]/table/tbody/tr/td[6]/div')
        if text > endtime:
            com.messageAndScreen(driver, '评论信息的時間大於結束時間')

    #评论信息的時間小于开始時間就报错
    def comp2(self,driver,begintime):
        text = com.getTextByXpath(driver,
                                  '/html/body/div[1]/div[2]/div/section/section/section/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/td[6]/div')
        if text < begintime:
            com.messageAndScreen(driver, '评论信息的時間小于开始時間')




    #1、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“确定”按钮，成功删除
    def deleteCancel(self,driver):
        # cm.text='课程1206（admin_51）'
        cm.text='啦啦啦啦'
        cm.message='评价取消刪除失敗'
        self.basePr(driver, [0, 1, 2, 6, 4, 7])


    #2、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“取消”按钮，取消删除
    def deleteSuccess(self,driver):
        cm.text='消息推送测试课程1'
        cm.message='评价刪除失敗'
        self.basePr(driver, [0,1,2,3,4,5])


    #3、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“关闭”按钮，取消删除
    def deleteCancel1(self,driver):
        cm.text = '课程1206（admin_51）'
        cm.message = '评价取消刪除失敗'
        self.basePr(driver, [0, 1, 2, 6, 8, 7])


    #4、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“取消”取消删除
    def allDeleteCancel(self,driver):
        cm.text = '课程1206（admin_51）'
        cm.message = '取消删除失败'
        self.basePr(driver, [0, 1, 2, 9, 6, 4, 7])


    #5、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“关闭”取消删除
    def allDeleteCancel1(self,driver):
        cm.text = '课程1206（admin_51）'
        cm.message = '关闭取消删除失败'
        self.basePr(driver, [0, 1, 2, 9, 6, 8, 7])


    #6、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“确定”按钮，成功删除
    def allDeleteSucc(self,driver):
        cm.text = '消息推送测试课程1'
        cm.message = '评价刪除失敗'
        self.basePr(driver, [0, 1, 2, 9, 6, 4, 5])


    #7、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息
    def scoreSucc(self,driver):
        cm.timeBegin='2019-12-06 14:10:01'
        cm.timeEnd='2019-12-27 00:00:00'
        cm.text = '课程1206（admin_51）'
        cm.message = '搜索课程失敗'
        self.basePr(driver, [0,1,10,11,12,1,7])


    #8、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息,点击“重置”按钮，取消筛选，显示全部信息
    def scoreCanc(self,driver):
        cm.timeBegin = '2019-12-06 14:10:01'
        cm.timeEnd = '2019-12-27 00:00:00'
        cm.message = '搜索课程失敗'
        self.basePr(driver, [0, 1, 10, 11, 12, 13,14])



    #9、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间
    def circleClose(self,driver):
        cm.timeEnd = '2019-12-27 00:00:00'
        cm.text='2019-12-27 00:00:00'
        cm.message = '清空设置的结束时间失败'
        self.basePr(driver, [0, 1, 11, 12, 15,1,16,5])


    #10、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间，点击“确定”按钮，取消筛选，显示所有信息
    def circleClose1(self,driver):
        cm.timeEnd = '2019-12-27 00:00:00'
        cm.message = '显示所有信息失敗'
        self.basePr(driver, [0, 1, 11, 12, 15, 1, 16, 12,14])



    #11、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出小于等于结束时间的评论信息
    def endtime(self,driver):
        cm.timeEnd = '2019-08-29 09:51:20'
        self.basePr(driver, [0, 1, 11, 12,1,17])


    #12、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间
    def begintime(self,driver):
        cm.timeBegin = '2019-12-01 10:01:59'
        cm.text='2019-12-01 10:01:59'
        cm.message = '清空设置的開始时间失败'
        self.basePr(driver, [0, 1, 10, 12,18,16,5])



    #13、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间，点击“确定”按钮，取消筛选，显示所有信息
    def begintime1(self,driver):
        cm.timeBegin = '2019-12-01 10:01:59'
        cm.message = '显示所有信息失敗'
        self.basePr(driver, [0, 1, 10, 12, 18, 16,12,1,14])


    #14、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出大于等于开始时间的评论信息
    def begintime2(self,driver):
        cm.timeBegin = '2019-12-06 00:00:00'
        self.basePr(driver, [0, 1, 10, 12,1,19])