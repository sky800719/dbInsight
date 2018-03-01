# -*- coding:utf-8 -*-

import sys
import time
import multiprocessing
from urllib import request

from .SYSConfig import SYS_URL


class dbGatherPorc(multiprocessing.Process):

    """ 数据库信息采集进程定义类
    """

    def __init__(self, sourceDBUID, extractType):
        multiprocessing.Process.__init__(self)
        self.sourceDBUID = sourceDBUID
        self.extractType = extractType

    def run(self):

        # 连接源库与目标库数据库
        try:
            print('self.sourceDBUID => ', self.sourceDBUID)
            print('self.extractType => ', self.extractType)
            url = SYS_URL + '/gatherDBInfo?sourceDBUID=' + self.sourceDBUID + '&extractType=' + self.extractType
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
            url = SYS_URL + '/cleanGatherData'
            req = request.urlopen(url)
        except BaseException:
            print("定时任务执行失败: %s", sys.exc_info()[1])
