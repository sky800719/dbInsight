# -*- coding:utf-8 -*-

import sys
import time

from util import dbAccessUtil
from db import dbGatherThread

def gatherMain(gatherType, gatherFlag):

    try:
        print('gatherType：', gatherType)
        print('gatherFlag：', gatherFlag)

        # 获取采集数据库配置信息
        srcDBList = dbAccessUtil.getDBCfgResult()

        # 启动数据采集任务，为避免一次启动过多进程，进程启动之间应该有一定间隔
        for srcDBRow in srcDBList:
            print('------------------------------------启动源端数据库采集程序开始：------------------------------------')

            p = dbGatherThread.doDBGather(srcDBRow, gatherFlag)
            p.start()
        
            print('------------------------------------启动源端数据库采集程序结束：------------------------------------')
    except Exception:
        print('源端数据库采集程序执行失败: ', sys.exc_info()[1])

