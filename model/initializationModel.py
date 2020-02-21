# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/21 15:12

class initializationModel(object):

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def pname(self):
        return self.pname

    @pname.setter
    def pname(self, pname):
        self.pname = pname

    @property
    def sname(self):
        return self.sname

    @sname.setter
    def sname(self, sname):
        self.sname = sname

