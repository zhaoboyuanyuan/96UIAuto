# -*- coding: utf-8 -*-
# @Author  : 赵永健
# @Time    : 2019/12/31 14:07
import os
import time
import logging

import sys


class logt():
    def logOutput(self,log_dir):
        '''
        :param log_dir: 日志路径
        :param name_project: 项目名称=>用于日志命名
        :return:
        '''

        # now = time.strftime("%Y_%m_%d %H_%M_%S")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            # filename= log_dir + now + '-' + '_test_log.log',
                            filename= log_dir+'test_log.log',
                            filemode='w')
        logger = logging.getLogger()
        logger.info(self)


