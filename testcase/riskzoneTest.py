# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/18 10:35
import unittest

from process.commonProc import commonProc
from process.initializationProc import initializationProc
from process.riskzoneProc import riskzoneProc
from public.openWeb import openWeb


o = openWeb()
com = commonProc()
rz=riskzoneProc()


class riskzoneTest(unittest.TestCase):
    def setUp(self):
        o.writeSetUp()
        self.driver = o.getDr()
        self.driver.implicitly_wait(10)
        com.initData(self.driver)


    def tearDown(self):
        o.writeTearDown()


    # 1、填写评估单元划分
    def testassessmen(self):
        u"""填写评估单元划分"""
        rz.assessmentUnits(self.driver)

    #2、区域固有风险评估（校验值），L值，S值，区域固有风险的验证。
    def testinherent(self):
        u"""区域固有风险评估（校验值），L值，S值，区域固有风险的验证。"""
        rz.inherent(self.driver)

    # 3、控制风险评估
    def testcontrol(self):
        u"""控制风险评估"""
        rz.controlRisk(self.driver)

    # 4、蒙德法-生成安全预评价结果
    def testmende(self):
        u"""蒙德法-生成安全预评价结果"""
        rz.mende(self.driver)

    # 5、蒙德法-安全补偿评价结果
    def testmende1(self):
        u"""蒙德法-安全补偿评价结果"""
        rz.mende1(self.driver)

    # 6、蒙德法-提交
    def testmende2(self):
        u"""蒙德法-提交"""
        rz.mende2(self.driver)

    # 7、道化学-生成安全预评价结果
    def testdowHua(self):
        u"""道化学-生成安全预评价结果"""
        rz.dowHua(self.driver)

    # 8、道化学-安全补偿评价结果
    def testdowHua1(self):
        u"""道化学-安全补偿评价结果"""
        rz.dowHua1(self.driver)

    # 9、道化学-提交
    def testdowHua2(self):
        u"""道化学-提交"""
        rz.dowHua2(self.driver)

    # 10、蒙德法校验
    def testmendeCheck(self):
        u"""蒙德法校验"""
        rz.mendeCheck(self.driver)

    # 11、道化学校验
    def testdowCheck(self):
        u"""道化学校验"""
        rz.dowCheck(self.driver)

    # 12.事故后果模拟计算值
    def testhiguCalValue(self):
        u"""事故后果模拟计算值"""
        rz.shiguCalValue(self.driver)

    # 13.事故后果模拟
    def testhiguSimulation(self):
        u"""事故后果模拟"""
        rz.shiguSimulation(self.driver)

    # 14.事故后果模拟提交
    def testhiguRefer(self):
        u"""事故后果模拟提交"""
        rz.shiguRefer(self.driver)

    # 15.事故后果模拟校验
    def testhiguCheck(self):
        u"""事故后果模拟校验"""
        rz.shiguCheck(self.driver)

    # 16.查看导入图片
    def testpict(self):
        u"""查看导入图片"""
        rz.picture(self.driver)

    #17.画多边形图形
    def testdrawIrreg(self):
        u"""画多边形图形"""
        rz.drawIrreg(self.driver)

    #18.画方形
    def testdrawSqu(self):
        u"""画方形"""
        rz.drawSqu(self.driver)

    #19.画椭圆
    def testdrawCir(self):
        u"""画椭圆"""
        rz.drawCir(self.driver)

    #20.打点
    def testdrawPt(self):
        u"""打点"""
        rz.drawPt(self.driver)

    #21.多边形图形绑定区域
    def testqbindIrreg(self):
        u"""多边形图形绑定区域"""
        rz.bindIrreg(self.driver)

    #22.多边形图形绑定区域校验
    def testqbindIrregcheck(self):
        u"""多边形图形绑定区域校验"""
        rz.bindIrregcheck(self.driver)

    #23.方形图形绑定区域
    def testqbindSqu(self):
        u"""方形图形绑定区域"""
        rz.bindSqu(self.driver)

    #24.方形图形绑定区域校验
    def testqbindSqucheck(self):
        u"""方形图形绑定区域校验"""
        rz.bindSqucheck(self.driver)

    #25.椭圆形绑定区域
    def testqbindCir(self):
        u"""椭圆形绑定区域"""
        rz.bindCir(self.driver)

    #26.椭圆形绑定区域校验
    def testqbindCircheck(self):
        u"""椭圆形绑定区域校验"""
        rz.bindCircheck(self.driver)

    #27.风险点绑定
    def testqbindPt(self):
        u"""风险点绑定"""
        rz.bindPt(self.driver)

    #28.风险点绑定区域校验
    def testqbindPtcheck(self):
        u"""风险点绑定区域校验"""
        rz.bindPtcheck(self.driver)

    #29.区域校验风险等级
    def testqareaCheck(self):
        u"""区域校验风险等级"""
        rz.areaCheck(self.driver)

    #30.点校验风险等级
    def testqpointCheck(self):
        u"""点校验风险等级"""
        rz.pointCheck(self.driver)


if __name__ == '__main__':
    unittest.main()

