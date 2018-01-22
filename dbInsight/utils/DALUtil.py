# -*- coding:utf-8 -*-

from django.db import connection
from django.db import connections

import sys
import cx_Oracle
import logging

from dbInsight.utils import SYSConfigSQL

# 定义数据库连接信息
DB_QUERY_CONN = 'QUERY'
DB_CATALOG_CONN = 'CATALOG'

log = logging.getLogger(__name__)


def getDBConnection(DBID):

    # 获取数据库连接
    dbName = ''
    msgCode = 0
    msgContent = ''

    log.debug('开始获取数据库连接信息配置！')
    resultList = getSQLResult(SYSConfigSQL.DBConnectInfoSQL, {'DBID': DBID})

    if len(resultList) > 0:
        dbInfo = resultList[0]
        dbName = dbInfo['DB_NAME']

        try:
            log.debug('获取数据库连接信息成功，开始创建数据库连接！')

            # 创建数据库连接信息
            oradns = cx_Oracle.makedsn(
                dbInfo['HOST_IP'],
                dbInfo['TNS_PORT'],
                dbInfo['DB_NAME'])

            # 连接源库与目标库数据库
            dbConn = cx_Oracle.connect(
                dbInfo['CONN_USER'], dbInfo['CONN_PASS'], oradns)

            log.debug('数据库连接创建成功！')
        except BaseException:
            msgCode = -1
            msgContent = '连接数据库异常' + sys.exc_info()[0]
            log.error(msgContent)

    else:
        msgCode = -1
        msgContent = '未找到指定的数据库配置信息'
        log.error(msgContent)

    returnDict = {
        'CONNECT': dbConn,
        'DBNAME': dbName,
        'MSGCODE': msgCode,
        'MSGCONTENT': msgContent}

    log.debug('数据库连接信息 => %s', returnDict)

    return returnDict


def getSQLSingleCell(SQLStr, bindList):

    # 返回查询结果单行第一列信息，用于获取数据库中的配置语句
    log.debug("查询语句 SQLStr => %s", SQLStr)
    log.debug("查询绑定变量 bindList => %s", bindList)

    resultStr = ""

    try:
        cursor = connections[DB_QUERY_CONN].cursor()
        cursor.execute(SQLStr, bindList)
        result = cursor.fetchmany(1)

        for row in result:
            resultStr = row[0]

    except BaseException:
        log.error("查询数据库异常: %s", sys.exc_info()[0])
    finally:
        cursor.close()

    log.debug("查询返回结果 resultStr => %s", resultStr)

    return resultStr


def getSQLResult(SQLStr, bindList):

    # 获取SQL查询结果
    log.debug("查询语句 SQLStr => %s", SQLStr)
    log.debug("查询绑定变量 bindList => %s", bindList)

    resultList = []

    try:
        cursor = connections[DB_QUERY_CONN].cursor()
        cursor.execute(SQLStr, bindList)

        # 获取配置语句查询列名称
        columnList = qrySQLColParse(cursor)
        qryResult = cursor.fetchall()

        # 处理查询结果集
        for row in qryResult:
            rowDict = {}
            for col in range(len(columnList)):
                rowDict[columnList[col]] = row[col]
            resultList.append(rowDict)

    except BaseException:
        log.error("查询数据库异常: %s", sys.exc_info())
        log.error("查询数据库异常: %s", sys.exc_info()[0])
        log.error("查询数据库异常: %s", sys.exc_info()[1])
        log.error("查询数据库异常: %s", sys.exc_info()[2])
    finally:
        cursor.close()

    #log.debug("查询返回结果 resultList => %s", resultList)

    return resultList


def getSQLResultWithColName(SQLStr, bindList):

    # 获取SQL查询列明及查询结果
    log.debug("查询语句 SQLStr => %s", SQLStr)
    log.debug("查询绑定变量 bindList => %s", bindList)

    resultList = []

    try:
        cursor = connections[DB_QUERY_CONN].cursor()
        cursor.execute(SQLStr, bindList)

        # 获取配置语句查询列名称
        columnList = qrySQLColParse(cursor)
        qryResult = cursor.fetchall()

        # 处理查询语句展现列名称信息
        colName = {}
        for col in range(len(columnList)):
            colName[columnList[col]] = columnList[col]
        resultList.append(colName)

        # 处理查询语句结果集信息
        for row in qryResult:
            rowDict = {}
            for col in range(len(columnList)):
                rowDict[columnList[col]] = row[col]
            resultList.append(rowDict)

    except BaseException:
        log.error("查询数据库异常: %s", sys.exc_info())
        log.error("查询数据库异常: %s", sys.exc_info()[0])
        log.error("查询数据库异常: %s", sys.exc_info()[1])
        log.error("查询数据库异常: %s", sys.exc_info()[2])
    finally:
        cursor.close()

    #log.debug("查询返回结果 resultList => %s", resultList)

    return resultList


def qrySQLColParse(sqlCursor):

    # 获取查询语句查询列名称
    columnList = []
    columnDesc = sqlCursor.description
    #log.debug("查询语句列信息 columnDesc => %s", columnDesc)

    for index, value in enumerate(columnDesc):
        columnList.append(value[0])

    #log.debug("查询语句列名信息 columnList => %s", columnList)

    return columnList


def getCfgSQLAndBind(SQLStr, bindList):

    # 获取配置语句及绑定变量信息
    log.debug('查询语句 SQLStr => %s', SQLStr)
    log.debug('查询绑定变量 bindList => %s', bindList)

    resultSQL = ""
    resultBindList = {}

    try:
        cursor = connections[DB_QUERY_CONN].cursor()
        cursor.execute(SQLStr, bindList)
        result = cursor.fetchmany(1)

        #　当前系统最大支持每条查询语句有３个变量
        for row in result:
            resultSQL = row[0]
            if row[1] is not None:
                resultBindList[row[1]] = row[2]
            if row[3] is not None:
                resultBindList[row[3]] = row[4]
            if row[5] is not None:
                resultBindList[row[5]] = row[6]

    except BaseException:
        log.error("查询数据库异常: %s", sys.exc_info()[0])
    finally:
        cursor.close()

    returnDict = {'resultSQL': resultSQL, 'resultBindList': resultBindList}
    log.debug('查询返回结果 returnDict => %s', returnDict)

    return returnDict


def getCfgSqlResult(MENU_URL):

    # 用于获取DBMP_URL_SQL_MAP表URL_SQL列配置查询语句数据
    sqlInfo = getCfgSQLAndBind(SYSConfigSQL.URLQrySQLWithBind, {'MENU_URL': MENU_URL})

    SQLStr = sqlInfo['resultSQL']
    bindList = sqlInfo['resultBindList']
    resultList = getSQLResult(SQLStr, bindList)

    return resultList


def getCfgSqlResultWithColName(MENU_URL, URL_ACTION):

    # 用于获取DBMP_URL_SQL_MAP表URL_SQL列配置查询语句数据
    sqlInfo = ''

    if URL_ACTION == '':
        sqlInfo = getCfgSQLAndBind(SYSConfigSQL.URLQrySQLWithBind, {'MENU_URL': MENU_URL})
    else :
        sqlInfo = getCfgSQLAndBind(SYSConfigSQL.URLMapQrySQLWithBind, {'MENU_URL': MENU_URL, 'URL_ACTION': URL_ACTION})

    SQLStr = sqlInfo['resultSQL']
    bindList = sqlInfo['resultBindList']
    resultList = getSQLResultWithColName(SQLStr, bindList)

    return resultList

def getMenuCfg(MENU_URL, URL_ACTION):

    # 用于获取DBMP_URL_SQL_MAP表URL_SQL列配置扩展信息
    if URL_ACTION == '':
        resultList = getSQLResult(SYSConfigSQL.MenuURLMapSQL, {'MENU_URL': MENU_URL})
    else:
        resultList = getSQLResult(SYSConfigSQL.URLMapQrySQLWithBind, {'MENU_URL': MENU_URL, 'URL_ACTION': URL_ACTION})

    return resultList

def getURLExtendInfo(MENU_URL, URL_ACTION):

    # 用于获取DBMP_MENU_URL_EXTEND表中扩展信息
    resultList = getSQLResult(SYSConfigSQL.URLDisplaySQL, {'MENU_URL': MENU_URL, 'URL_ACTION': URL_ACTION})

    return resultList[0]

def getAPPCfgResult():

    # 用于获取DBMP_URL_SQL_MAP表URL_SQL列配置查询语句数据
    resultList = getSQLResult(SYSConfigSQL.APPQrySQL, {})

    return resultList

def getDBCfgResult():

    # 用于获取DBMP_URL_SQL_MAP表URL_SQL列配置查询语句数据
    resultList = getSQLResult(SYSConfigSQL.DBInfoSQL, {})

    return resultList
