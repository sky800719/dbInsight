# -*- coding:utf-8 -*-

import sys
import time
from urllib import request
from .cronGatherProcProxy import dbGatherTimeProxy, osGatherProxy 


def gatherDBDataJob(gatherType, jobType):

    """ 定时任务
        gatherType  任务类型     SQLAUDIT/DBMONITOR/
        jobType     任务作业类型 MINUTE/HOUR/DAY
    """
    gatherDBJobName = gatherType + '->' + jobType + ' 调用任务'

    try:
        print('------------------------------------------------------------------------------------------')
        print(gatherDBJobName, ', 开始: ', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        dbGatherTimeProxy(gatherType, jobType)
        print(gatherDBJobName, ', 结束: ', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        print('------------------------------------------------------------------------------------------')
    except BaseException:
        print(gatherDBJobName, ', 执行失败: %s', sys.exc_info()[0])
        print(gatherDBJobName, ', 执行失败: %s', sys.exc_info()[1])
        print(gatherDBJobName, ', 执行失败: %s', sys.exc_info()[2])

def cleanHisDBData():

    # 连接源库与目标库数据库
    try:
        print('--------------------------------------------cleanHisDBData begin--------------------------------------------')
        dbGatherProxy()
        print('--------------------------------------------cleanHisDBData end--------------------------------------------')
    except BaseException:
        print("定时清理任务执行失败: %s", sys.exc_info()[1])
