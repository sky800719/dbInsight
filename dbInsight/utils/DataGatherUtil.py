# -*- coding:utf-8 -*-

import sys
import cx_Oracle
import logging

from django.db import connection
from django.db import connections
from dbInsight.utils import SYSConfigSQL, DBDirectUtil

log = logging.getLogger(__name__)

def dataExtract(sourceDBID, sourceDBNAME, catalogDB, gatherType, jobType):

    """ 采集源端数据库数据到资料库
    """

    # 创建源端数据库连接信息
    srcConnectInfo = ''
    srcConnect = ''
    snapDBName = ''

    try:
        log.debug('开始创建源端数据库连接！')
        srcConnectInfo = DBDirectUtil.getDBConnection(sourceDBID, sourceDBNAME)

        if srcConnectInfo['MSGCODE'] == 0:
            srcConnect = srcConnectInfo['CONNECT']
            snapDBName = srcConnectInfo['DBNAME']
        else:
            log.error('创建源端数据库连接失败！')
            log.error('写错误日志表')
            return ''
        log.debug('创建源端数据库连接完成！')
    except BaseException:
        log.error("创建源端数据库连接失败: %s", sys.exc_info()[0])
        log.error("创建源端数据库连接失败: %s", sys.exc_info()[1])
        log.error("创建源端数据库连接失败: %s", sys.exc_info()[2])
        return ''

    # 创建目标端数据库连接信息
    catalogConnectInfo = ''
    catalogConnect = ''

    try:
        log.debug('开始创建资料数据库连接！')
        catalogConnectInfo = DBDirectUtil.getCatalogDBConn()

        if catalogConnectInfo['MSGCODE'] == 0:
            catalogConnect = catalogConnectInfo['CONNECT'].cursor()
        else:
            log.error('创建源端数据库连接失败！')
            log.error('写错误日志表')
    except BaseException:
        log.error("创建资料数据库连接失败: %s", sys.exc_info()[0])
        log.error("创建资料数据库连接失败: %s", sys.exc_info()[1])
        log.error("创建资料数据库连接失败: %s", sys.exc_info()[2])
        return ''

    # 获取数据库采集配置信息
    extractList = []
    try:
        log.debug('开始获取数据库采集配置信息！')

        # 根据采集类型，获取采集语句
        print('gatherType => ', gatherType)
        print('jobType => ', jobType)

        # 根据crontab参数，获取对应的查询采集语句
        extractList = DBDirectUtil.getSQLResult(SYSConfigSQL.ExtractCfgSQL, {'EXTRACT_RULE_TYPE': 'DAILY'})
    except BaseException:
        log.error("获取数据库采集配置信息失败: %s", sys.exc_info()[0])
        log.error("获取数据库采集配置信息失败: %s", sys.exc_info()[1])
        log.error("获取数据库采集配置信息失败: %s", sys.exc_info()[2])
        return ''

    for extractRule in extractList:

        """ 对采集配置进行循环处理
        """

        log.debug("获取源端数据库查询语句！")
        # 源端数据库查询语句
        sql_src = extractRule['SRCDB_EXTRACT_SQL']
        # 资料数据库数据写入语句
        sql_dest = extractRule['CATALOG_RECORD_SQL']
        
        # 源端数据库查询数据结果集
        rowList = []
        extract_sql = ''

        try:
            log.debug("开始创建源端数据库连接！")
            cursor_src = srcConnect.cursor()

            log.debug("开始执行源端数据库采集语句！")
            extract_sql = sql_src.replace('${DB_UID}', str(sourceDBID)).replace('${SNAP_ID}', str(sourceDBID))
            print('extract_sql -> ', extract_sql)

            cursor_src.execute(extract_sql)

            # 获取源库语句执行结果
            log.debug("开始获取源端数据库采集结果！")
            result_src = cursor_src.fetchall()
            columnList = DBDirectUtil.qrySQLColParse(cursor_src)

            # 处理查询结果集
            log.debug("开始获取源端数据库采集结果！")
            for row in result_src:
                rowInfo = {}
                for col in range(len(columnList)):
                    rowInfo[columnList[col]] = row[col]
                rowList.append(rowInfo)

            log.debug('源端数据库查询结果解析完成！')
        except BaseException:
            log.error("源端数据库查询失败: %s", sys.exc_info()[0])
            log.error("源端数据库查询失败: %s", sys.exc_info()[1])
            log.error("源端数据库查询失败: %s", sys.exc_info()[2])
            log.error("源端数据库查询失败，查询语句为: %s", extract_sql)

        log.debug('源端数据库查询结果 rowList => %s', rowList)
        log.debug('源端数据库查询结果数据量 len(rowList) => %s', len(rowList))

        # 创建资料数据库连接
        try:
            log.debug('创建资料数据库连接！')
            catalogCursor = catalogConnect.cursor()
            log.debug('开始写入源端数据库结果到资料库！')
            catalogCursor.executemany(sql_dest, rowList)
            catalogConnect.commit()
            log.debug('源端数据库结果写入资料库完成！')
        except BaseException:
            log.error("资料数据库写入失败: %s", sys.exc_info()[0])
            log.error("资料数据库写入失败: %s", sys.exc_info()[1])
            log.error("资料数据库写入失败: %s", sys.exc_info()[2])

