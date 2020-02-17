# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2020/1/6 10:10

class courseCommModel(object):

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def timeBegin(self):
        return self._timeBegin

    @timeBegin.setter
    def timeBegin(self, timeBegin):
        self._timeBegin = timeBegin

    @property
    def timeEnd(self):
        return self._timeEnd

    @timeEnd.setter
    def timeEnd(self, timeEnd):
        self._timeEnd = timeEnd

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def button(self):
        return self._button

    @button.setter
    def button(self, button):
        self._button = button
