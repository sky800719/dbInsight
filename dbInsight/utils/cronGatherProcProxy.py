# -*- coding:utf-8 -*-

import sys
import time
from urllib import request
from .SYSConfig import SYS_URL
from .cronGatherProc import dbGatherTimePorc, osGatherPorc
from .StringParse import strToList

def dbGatherTimeProxy(gatherType, jobType):

    dbGatherTime = gatherType + '->' + jobType + ' 获取采集数据库配置信息'

    try:
        print(dbGatherTime, ', 开始: ', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        # 获取采集数据库配置信息
        dbListURL = SYS_URL + '/getDBList'
        dbListResp = request.urlopen(dbListURL)

        dbList = strToList(dbListResp.read().decode('utf-8'))

        # 启动数据采集任务，为避免一次启动过多进程，进程启动之间应该有一定间隔
        for dbRow in dbList:
            p = dbGatherTimePorc(str(dbRow['DB_ID']), dbRow['DB_NAME'], gatherType, jobType)
            p.start()
            time.sleep(1)
        
        print(dbGatherTime, ', 结束: ', time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    except BaseException:
        print(dbGatherTime, ', 执行失败: %s', sys.exc_info()[0])
        print(dbGatherTime, ', 执行失败: %s', sys.exc_info()[1])
        print(dbGatherTime, ', 执行失败: %s', sys.exc_info()[2])

def osGatherProxy():

    # 连接源库与目标库数据库
    try:
        print('------------------------------------------osGatherProxy------------------------------------------')
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),' 执行数据库定时清理任务开始！')

        # 启动数据采集任务，为避免一次启动过多进程，进程启动之间应该有一定间隔
        for i in range(2):
            p = dbGatherPorc(str(111 + i), 'DAILY')
            p.start()
            time.sleep(1)

        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),' 执行数据库定时清理任务结束！')
        print('--------------------------------------------------------------------------------------------')
    except BaseException:
        print("数据库定时清理任务执行失败: %s", sys.exc_info()[1])
