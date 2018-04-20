# -*- coding:utf-8 -*-

import sys
import time

from django.http import HttpResponse

from .utils import DALUtil,DataGatherUtil,SYSConfig

def gatherDBInfo(request):

    """ 数据库信息采集任务页面，定时任务数据采集入口页面，不对外提供访问
    """

    sourceDBID = ''
    sourceDBNAME = ''
    gatherType = ''
    jobType = ''

    gatherDBInfoName = ''

    try:
        sourceDBID = request.GET['sourceDBID']
        sourceDBNAME = request.GET['sourceDBNAME']
        gatherType = request.GET['gatherType']
        jobType = request.GET['jobType']

        #print('gatherDBInfo(request) -> sourceDBID => ', sourceDBID)
        #print('gatherDBInfo(request) -> sourceDBNAME => ', sourceDBNAME)
        #print('gatherDBInfo(request) -> gatherType => ', gatherType)
        #print('gatherDBInfo(request) -> jobType => ', jobType)
    
        gatherDBInfoName = gatherType + '->' + jobType + ' 数据库信息采集'
        
        DataGatherUtil.dataExtract(sourceDBID, sourceDBNAME, SYSConfig.DB_CATALOG_CONN, gatherType, jobType)
        return HttpResponse(gatherDBInfoName + "成功！执行时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    except BaseException:
        print(gatherDBInfoName, '失败: ', sys.exc_info()[0])
        print(gatherDBInfoName, '失败: ', sys.exc_info()[1])
        print(gatherDBInfoName, '失败: ', sys.exc_info()[2])
        
        return HttpResponse(gatherDBInfoName + "失败！执行时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


def cleanGatherData(request):

    """ 数据库信息采集任务页面，定时任务数据清理入口页面，不对外提供访问
    """

    DataGatherUtil.dataExtract(1, SYSConfig.DB_CATALOG_CONN, 100)
    return HttpResponse("cleanGatherData success!")

def getDBList(request):

    """ 获取被监控数据库列表
    """

    dbList = DALUtil.getDBCfgResult()
    return HttpResponse(dbList)
