# -*- coding:utf-8 -*-

import sys
import cx_Oracle

from . import catalogDB
from . import qryConfigSQL

def getCataLogDBConn():

    # 获取资料数据库连接
    msgCode = 0
    msgContent = ''
    catalogConn = ''
    catalogConnDict = ''

    print('------------------------------------获取资料数据库连接开始------------------------------------')

    try:
        print('开始创建资料数据库连接！')

        CATALOG_DB_IP = catalogDB.CATALOG_DB_IP
        CATALOG_DB_PORT = catalogDB.CATALOG_DB_PORT
        CATALOG_DB_SERVICE = catalogDB.CATALOG_DB_SERVICE
        CATALOG_DB_USER = catalogDB.CATALOG_DB_USER
        CATALOG_DB_PASS = catalogDB.CATALOG_DB_PASS

        print('资料数据库IP：', CATALOG_DB_IP)
        print('资料数据库端口：', CATALOG_DB_PORT)
        print('资料数据库服务名：', CATALOG_DB_SERVICE)
        print('资料数据库用户名：', CATALOG_DB_USER)
        print('资料数据库用户口令：', CATALOG_DB_PASS)

        # 创建数据库连接信息
        oradns = cx_Oracle.makedsn(CATALOG_DB_IP, CATALOG_DB_PORT, service_name=CATALOG_DB_SERVICE)

        # 连接源库与目标库数据库
        catalogConn = cx_Oracle.connect(CATALOG_DB_USER, CATALOG_DB_PASS, oradns)

        print('连接资料数据库成功！')

        catalogConnDict = {
            'CONNECT': catalogConn,
            'DBNAME': catalogDB.CATALOG_DB_SERVICE,
            'MSGCODE': msgCode,
            'MSGCONTENT': msgContent}

    except Exception:
        msgCode = -1
        msgContent = '连接资料数据库异常：' + str(sys.exc_info()[1])
        print(msgContent)

        catalogConnDict = {
            'CONNECT': '',
            'DBNAME': catalogDB.CATALOG_DB_SERVICE,
            'MSGCODE': msgCode,
            'MSGCONTENT': msgContent}

    #print('资料数据库连接信息 => ', catalogConnDict)
    print('------------------------------------获取资料数据库连接结束------------------------------------')

    return catalogConnDict


def getSrcDBConn(srcDBDict):

    # 获取源端采集数据库连接
    msgCode = 0
    msgContent = ''
    SRC_DB_UNAME = ''
    SRC_DB_VERSION = ''
    SRC_DB_IP = ''
    SRC_DB_PORT = ''
    SRC_DB_SERVICE = ''
    SRC_DB_USER = ''
    SRC_DB_PASS = ''
    SRC_DB_ROLE = ''
    srcDBConn = ''
    srcDBConnDict = ''

    print('------------------------------------获取源端采集数据库连接开始------------------------------------')

    try:
        print('开始获取源端采集数据库连接！')

        SRC_DB_UNAME = srcDBDict['SRC_DB_UNAME']
        SRC_DB_VERSION = srcDBDict['SRC_DB_VERSION']
        SRC_DB_IP = srcDBDict['SRC_DB_IP']
        SRC_DB_PORT = srcDBDict['SRC_DB_PORT']
        SRC_DB_SERVICE = srcDBDict['SRC_DB_SERVICE']
        SRC_DB_USER = srcDBDict['SRC_DB_USER']
        SRC_DB_PASS = srcDBDict['SRC_DB_PASS']
        SRC_DB_ROLE = srcDBDict['SRC_DB_ROLE']

        print('源端采集数据库唯一名称：', SRC_DB_UNAME)
        print('源端采集数据库版本：', SRC_DB_VERSION)
        print('源端采集数据库IP：', SRC_DB_IP)
        print('源端采集数据库端口：', SRC_DB_PORT)
        print('源端采集数据库服务名：', SRC_DB_SERVICE)
        print('源端采集数据库用户名：', SRC_DB_USER)
        print('源端采集数据库用户口令：', SRC_DB_PASS)
        print('源端采集数据库角色：', SRC_DB_ROLE)

        # 创建数据库连接信息
        oradns = cx_Oracle.makedsn(SRC_DB_IP, SRC_DB_PORT, service_name=SRC_DB_SERVICE)

        # 连接源库与目标库数据库
        srcDBConn = cx_Oracle.connect(SRC_DB_USER, SRC_DB_PASS, oradns)

        print('连接源端采集数据库成功！')

        srcDBConnDict = {
            'CONNECT': srcDBConn,
            'SRC_DB_VERSION': SRC_DB_VERSION,
            'SRC_DB_IP': SRC_DB_IP,
            'SRC_DB_UNAME': SRC_DB_UNAME,
            'SRC_DB_ROLE': SRC_DB_ROLE,
            'MSGCODE': msgCode,
            'MSGCONTENT': msgContent}

    except Exception:
        msgCode = -1
        msgContent = '连接源端采集数据库异常：' + str(sys.exc_info()[1])
        print(msgContent)

        srcDBConnDict = {
            'CONNECT': '',
            'SRC_DB_VERSION': SRC_DB_VERSION,
            'SRC_DB_IP': SRC_DB_IP,
            'SRC_DB_UNAME': SRC_DB_UNAME,
            'SRC_DB_ROLE': SRC_DB_ROLE,
            'MSGCODE': msgCode,
            'MSGCONTENT': msgContent}

    print('源端采集数据库连接信息 => ', srcDBConnDict)
    print('------------------------------------获取源端采集数据库连接结束------------------------------------')

    return srcDBConnDict

def qrySQLColParse(sqlCursor):

    # 获取查询语句查询列名称
    columnList = []
    columnDesc = sqlCursor.description

    try:
        for index, value in enumerate(columnDesc):
            columnList.append(value[0])
    except Exception:
        print("查询语句游标信息 sqlCursor => ", sqlCursor)
        print("查询语句列信息 columnDesc => ", columnDesc)
        print("查询语句列名信息 columnList => ", columnList)

    return columnList

def getSQLResult(connCursor, SQLStr, bindList):

    # 获取指定数据库SQL查询结果

    print('------------------------------------获取SQL查询结果开始------------------------------------')

    resultList = []

    try:
        # 加入connDict结果判断
        connCursor.execute(SQLStr, bindList)

        # 获取配置语句查询列名称
        columnList = qrySQLColParse(connCursor)
        qryResult = connCursor.fetchall()

        # 处理查询结果集
        for row in qryResult:
            rowDict = {}
            for col in range(len(columnList)):
                rowDict[columnList[col]] = row[col]
            resultList.append(rowDict)
    except Exception:
        print("查询语句 SQLStr => ", SQLStr)
        print("查询绑定变量 bindList => ", bindList)
        print("查询执行异常: ", sys.exc_info()[0])
        print("查询执行异常: ", sys.exc_info()[1])
        print("查询执行异常: ", sys.exc_info()[2])

    #print("查询执行结果 resultList => ", resultList)
    print('------------------------------------获取SQL查询结果结束------------------------------------')

    return resultList


def getDBCfgResult():

    # 获取资料数据库中数据库列表信息
    resultList = ''
    catalogDBConn = ''
    connCursor = ''

    try:
        catalogDBDict = getCataLogDBConn()
        catalogDBConn = catalogDBDict['CONNECT']
        connCursor = catalogDBConn.cursor()
        resultList = getSQLResult(connCursor, qryConfigSQL.DBListSQL, {})
    except Exception:
        print("查询采集数据库清单失败: ", sys.exc_info()[0])
        print("查询采集数据库清单失败: ", sys.exc_info()[1])
        print("查询采集数据库清单失败: ", sys.exc_info()[2])
    finally:
        connCursor.close()
        catalogDBConn.close()

    srcDBList = []
    srcDBDict = {}

    for rowList in resultList:
        srcDBDict = {
            'SRC_DB_ID': rowList['DB_ID'],
            'SRC_INST_ID': rowList['INST_ID'],
            'SRC_DB_NAME': rowList['DB_NAME'],
            'SRC_DB_UNAME': rowList['DB_UNIQUE_NAME'],
            'SRC_DB_VERSION': rowList['DB_VERSION'],
            'SRC_DB_IP': rowList['HOST_IP'],
            'SRC_DB_PORT': rowList['TNS_PORT'],
            'SRC_DB_SERVICE': rowList['SERVICE_NAME'],
            'SRC_DB_USER': rowList['CONN_USER'],
            'SRC_DB_PASS': rowList['CONN_PASS'],
            'SRC_DB_ROLE': rowList['DB_ROLE'],
        }

        srcDBList.append(srcDBDict)

    return srcDBList 

def extractLogRecord(catalogConn, catalogCursor, extractLogDict):

    # 数据采集日志记录
    # print('extractLogDict -> ', extractLogDict)

    catalogCursor.execute(qryConfigSQL.ExtractLogSQL, extractLogDict)
    catalogConn.commit()
