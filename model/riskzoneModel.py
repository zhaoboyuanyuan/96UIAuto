# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/2/28 10:36

class riskzoneModel(object):

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text