# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2019/12/31 10:57

class baseProc(object):

    def basePr(self, driver, list=[]):
        for i in list:
            self.switch(driver, i)

    def switch(self, driver, num):
        pass
