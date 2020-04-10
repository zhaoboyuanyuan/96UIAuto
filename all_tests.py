#coding=utf-8
import os
import sys

import time
from BeautifulReport import BeautifulReport

from public.htmlImg import readhtml
from public.logt import logt
from public.send_email import send_email

# sys.path.append("D:/code/SafetyappEducate/testcase")


spath=os.path.join(os.getcwd(),'testcase')
sys.path.append(spath)

import unittest
import HTMLTestRunner

# 将用例组建成数组
alltestnames = [
    # 'sutie.sogou.test_sogou.Sogou',  # 注意这个用例是二级目录下的
    #'courseCommTest.courseCommTest'
    'initializationTest.initializationTest',
    'riskzoneTest.riskzoneTest'

]
suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite())


if __name__ == '__main__':
    # 这里我们可以使用 defaultTestLoader.loadTestsFromNames(),
    # 但如果不提供一个良好的错误消息时，它无法加载测试
    # 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
    # 最关键的就是这一句，循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print ('ERROR: Skipping tests from "%s".' % test)
            try:
                __import__(test)
            except ImportError:
                print ('Could not import the test module.')
            else:
                print ('Could not load the test suite.')
            from traceback import print_exc
            print_exc()

    print ('Running the tests...')


    #输出日志
    log_dir=os.getcwd()+'\log\\'
    log=logt()
    log.logOutput(log_dir)

    #输出美化后的html报告
    log_path = os.path.join(os.getcwd(),'result')
    BeautifulReport(suite).report(filename='result', description='96号容器测试', log_path=log_path)



    # 输出html报告
    # filename = 'D:\\code\\SafetyappEducate\\result\\result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    # # runner=HTMLTestReportCN.HTMLTestRunner(
    #     stream=fp,
    #     # tester='赵永健',
    #     title=u'安全教育系统测试报告',
    #     description=u'用例执行情况')
    # runner.run(suite)
    # fp.close()


    #处理报告中的图片
    readhtml()
    #发送邮件
    send_email().send()
