# -*- coding:utf-8 -*-

import sys
import time
import multiprocessing
from urllib import request


class dbGatherPorc(multiprocessing.Process):

    """ 数据库信息采集进程定义类
    """

    def __init__(self, sourceDBID, extractType):
        multiprocessing.Process.__init__(self)
        self.sourceDBID = sourceDBID
        self.extractType = extractType

    def run(self):

        # 连接源库与目标库数据库
        try:
            print('self.sourceDBID => ', self.sourceDBID)
            print('self.extractType => ', self.extractType)
            url = 'http://192.168.56.200:8000/gatherDBInfo?sourceDBID=' + self.sourceDBID + '&extractType=' + self.extractType
            req = request.urlopen(url)
        except BaseException:
            print("定时任务执行失败: ", sys.exc_info()[1])


class osGatherPorc(multiprocessing.Process):

    """ 操作系统信息采集进程定义类
    """

    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):

        # 连接源库与目标库数据库
        try:
            url = 'http://192.168.56.200:8000/cleanGatherData'
            req = request.urlopen(url)
        except BaseException:
            print("定时任务执行失败: %s", sys.exc_info()[1])
