# -*- coding:utf-8 -*-

import time

from django.http import HttpResponse

from .utils import DALUtil,DataGatherUtil,SYSConfig

def gatherDBInfo(request):

    """ 数据库信息采集任务页面，定时任务数据采集入口页面，不对外提供访问
    """

    sourceDBUID = request.GET['sourceDBUID']
    extractType = request.GET['extractType']

    DataGatherUtil.dataExtract(sourceDBUID, SYSConfig.DB_CATALOG_CONN, extractType)
    return HttpResponse("gatherDBInfo success!")

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

