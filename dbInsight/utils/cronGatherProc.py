# -*- coding:utf-8 -*-

import sys
import time
import multiprocessing
from urllib import request

from .SYSConfig import SYS_URL, DB_CATALOG_CONN
from . import DataGatherUtil

#import DALUtil,DataGatherUtil,SYSConfig

class dbGatherTimePorc(multiprocessing.Process):

    """ 数据库信息采集进程定义类
    """

    def __init__(self, sourceDBID, sourceDBNAME, gatherType, jobType):
        multiprocessing.Process.__init__(self)
        self.sourceDBID = sourceDBID
        self.sourceDBNAME = sourceDBNAME
        self.gatherType = gatherType
        self.jobType = jobType 


    def run(self):

        # 调用数据库信息采集URL
        dbGatherTimeURL = ''

        try:
            dbGatherTimeURL = self.gatherType + '->' + self.jobType + ' 调用数据库信息采集'

            #print(dbGatherTimeURL, ', self.sourceDBID => ', self.sourceDBID)
            #print(dbGatherTimeURL, ', self.sourceDBNAME => ', self.sourceDBNAME)
            #print(dbGatherTimeURL, ', self.gatherType => ', self.gatherType)
            #print(dbGatherTimeURL, ', self.jobType => ', self.jobType)
            #gatherURL = SYS_URL + '/gatherDBInfo?sourceDBID=' + self.sourceDBID + \
            #                             '&sourceDBNAME=' + self.sourceDBNAME + \
            #                             '&gatherType=' + self.gatherType + \
            #                             '&jobType=' + self.jobType

            DataGatherUtil.dataExtract(self.sourceDBID, self.sourceDBNAME, DB_CATALOG_CONN, self.gatherType, self.jobType)

            #print(dbGatherTimeURL, ', URL -> ', gatherURL)
            #req = request.urlopen(gatherURL)
        except BaseException:
            print(dbGatherTimeURL, ' 执行失败: ', sys.exc_info()[0])
            print(dbGatherTimeURL, ' 执行失败: ', sys.exc_info()[1])
            print(dbGatherTimeURL, ' 执行失败: ', sys.exc_info()[2])


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
