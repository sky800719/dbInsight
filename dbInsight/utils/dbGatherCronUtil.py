# -*- coding:utf-8 -*-

import sys
import time
from urllib import request
from .cronGatherProcProxy import dbGatherProxy, osGatherProxy 


def gatherDBData():

    # 连接源库与目标库数据库
    try:
        print('--------------------------------------------gatherDBData begin--------------------------------------------')
        dbGatherProxy()
        print('--------------------------------------------gatherDBData end--------------------------------------------')
    except BaseException:
        print("定时任务执行失败: %s", sys.exc_info()[1])


def cleanHisDBData():

    # 连接源库与目标库数据库
    try:
        print('--------------------------------------------cleanHisDBData begin--------------------------------------------')
        dbGatherProxy()
        print('--------------------------------------------cleanHisDBData end--------------------------------------------')
    except BaseException:
        print("定时清理任务执行失败: %s", sys.exc_info()[1])
