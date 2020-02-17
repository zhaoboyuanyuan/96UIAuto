# coding=utf-8
import unittest

from process.commonProc import commonProc
from process.courseCommProc import courseCommProc
from public.openWeb import openWeb

o = openWeb()
com = commonProc()
cou = courseCommProc()


class courseCommTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()

    def tearDown(self):
        o.writeTearDown()

    # 1、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“确定”按钮，成功删除
    def testDeleteSuccess(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“确定”按钮，成功删除"""
        cou.deleteSuccess(self.driver)

    # 2、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“取消”按钮，取消删除
    def testDeleteCancel(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“取消”按钮，取消删除"""
        cou.deleteCancel(self.driver)


    # 3、AEL“课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“关闭”按钮，取消删除
    def testDeleteCancel1(self):
        u"""课程评论管理”页面>选择一条评价，点击“删除”按钮，点击“关闭”按钮，取消删除"""
        cou.deleteCancel1(self.driver)

    # 4、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“取消”取消删除
    def testAllDeleteCancel(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“取消”取消删除"""
        cou.allDeleteCancel(self.driver)

    # 5、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“关闭”取消删除
    def testAllDeleteCancel1(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“关闭”取消删除"""
        cou.allDeleteCancel1(self.driver)

    # 6、AEL“课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“确定”按钮，成功删除
    def testAllDeleteSucc(self):
        u"""课程评论管理”页面>选中多个评价信息>点击批量“删除”按钮>点击“确定”按钮，成功删除"""
        cou.allDeleteSucc(self.driver)

    # 7、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息
    def testScoreSucc(self):
        u"""课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息"""
        cou.scoreSucc(self.driver)

    # 8、AEL“课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息,点击“重置”按钮，取消筛选，显示全部信息
    def testScoreCanc(self):
        u"""课程评论管理”页面>设置“评分”、“开始时间”和“结束时间”组合筛选，点击“确定”按钮，输出正确的筛选信息,点击“重置”按钮，取消筛选，显示全部信息"""
        cou.scoreCanc(self.driver)

    # 9、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间
    def testCircleClose(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间"""
        cou.circleClose(self.driver)

    # 10、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间，点击“确定”按钮，取消筛选，显示所有信息
    def testCircleClose1(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的结束时间"""
        cou.circleClose1(self.driver)

    # 11、AEL“课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出小于等于结束时间的评论信息
    def testEndtime(self):
        u"""课程评论管理”页面>设置“结束时间”，点击“确定”按钮，输出小于等于结束时间的评论信息"""
        cou.endtime(self.driver)

    # 12、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间
    def testBegintime(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间"""
        cou.begintime(self.driver)

    # 13、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间，点击“确定”按钮，取消筛选，显示所有信息
    def testBegintime1(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出筛选结果>点击“X”按钮清空设置的开始时间，点击“确定”按钮，取消筛选，显示所有信息"""
        cou.begintime1(self.driver)

    # 14、AEL“课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出大于等于开始时间的评论信息
    def testbegintime2(self):
        u"""课程评论管理”页面>设置“开始时间”，点击“确定”按钮，输出大于等于开始时间的评论信息"""
        cou.begintime2(self.driver)




if __name__ == '__main__':
    unittest.main()
