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
        return self._pname

    @pname.setter
    def pname(self, pname):
        self._pname = pname

    @property
    def sname(self):
        return self._sname

    @sname.setter
    def sname(self, sname):
        self._sname = sname

    @property
    def itext(self):
        return self._itext

    @itext.setter
    def itext(self, itext):
        self._itext = itext

