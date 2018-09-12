# -*- coding:utf-8 -*-

import os
import sys
import time
import multiprocessing
from . import dbGatherUtil

class doDBGather(multiprocessing.Process):

    """ 数据库信息采集进程定义类
    """

    def __init__(self, srcDBDict, gatherFlag):
        multiprocessing.Process.__init__(self)
        self.srcDBDict = srcDBDict
        self.gatherFlag = gatherFlag

    def run(self):
        try:
            print('------------------------------------源端数据库采集程序启动------------------------------------')
            print('进程编号：', os.getpid())
            print('启动时间：', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print('源端采集数据库: ', self.srcDBDict)
            print('源端采集标记: ', self.gatherFlag)

            # 调用源端数据库采集主程序
            dbGatherUtil.dataExtract(self.srcDBDict, self.gatherFlag)

            print('结束时间：', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print('------------------------------------源端数据库采集程序结束------------------------------------')
        except Exception:
            print(' 执行失败: ', sys.exc_info()[1])

