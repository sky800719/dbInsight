# -*- coding:utf-8 -*-

import sys
import cx_Oracle
import logging

from django.db import connection
from django.db import connections
from dbInsight.utils import SYSConfigSQL, DALUtil

log = logging.getLogger(__name__)

def dataExtract(sourceDBID, catalogDB, extractType):

    """ 采集源端数据库数据到资料库
    """

    # 创建源端数据库连接信息
    srcConnectInfo = ''
    srcConnect = ''
    snapDBName = ''

    try:
        log.debug('创建源端数据库连接！')
        srcConnectInfo = DALUtil.getDBConnection(sourceDBID)

        if srcConnectInfo['MSGCODE'] == 0:
            srcConnect = srcConnectInfo['CONNECT']
            snapDBName = srcConnectInfo['DBNAME']
        else:
            log.error('创建源端数据库连接失败！')
            log.error('写错误日志表')
            return ''
    except BaseException:
        log.error("源端数据库查询失败: %s", sys.exc_info()[0])

    # 创建目标端数据库连接信息
    catalogConnect = ''

    try:
        log.debug('创建资料数据库连接！')
        catalogConnect = connections[catalogDB]
    except BaseException:
        log.error("资料数据库写入失败: %s", sys.exc_info()[0])
        print("资料数据库写入失败: ", sys.exc_info()[0])

    # 获取数据库采集配置信息
    extractList = DALUtil.getSQLResult(SYSConfigSQL.ExtractCfgSQL, {'EXTRACT_RULE_TYPE': 'DAILY'})

    for extractRule in extractList:

        """ 对采集配置进行循环处理
        """

        # 源端数据库查询语句
        sql_src = extractRule['SRCDB_EXTRACT_SQL']
        # 资料数据库数据写入语句
        sql_dest = extractRule['CATALOG_RECORD_SQL']
        # 采集SEQENCE
        snap_seq = extractRule['RULE_SEQ']
        
        # 采集数据标识
        snapID = 0

        try:
            snapID = DALUtil.getSQLSingleCell('SELECT ' + snap_seq + '.NEXTVAL FROM DUAL', {})
        except BaseException:
            log.error("查询数据库异常: %s", sys.exc_info())
            snapID = -1

        # 源端数据库查询数据结果集
        rowList = []

        try:
            cursor_src = srcConnect.cursor()

            extract_sql = sql_src.replace('${DB_NAME}', snapDBName).replace('${SNAP_ID}', str(snapID))

            log.debug('执行源端数据库查询语句：%s', extract_sql)
            cursor_src.execute(extract_sql)

            # 获取源库语句执行结果
            result_src = cursor_src.fetchall()
            columnList = DALUtil.qrySQLColParse(cursor_src)

            # 处理查询结果集
            for row in result_src:
                rowInfo = {}
                for col in range(len(columnList)):
                    rowInfo[columnList[col]] = row[col]
                rowList.append(rowInfo)

            log.debug('源端数据库查询结果解析完成！')
        except BaseException:
            log.error("源端数据库查询失败: %s", sys.exc_info()[0])
        finally:
            cursor_src.close()

        log.debug('源端数据库查询结果数据量 len(rowList) => %s', len(rowList))

        # 创建资料数据库连接
        try:
            log.debug('创建资料数据库连接！')
            catalogCursor = catalogConnect.cursor()
            catalogCursor.executemany(sql_dest, rowList)
            catalogConnect.commit()
        except BaseException:
            log.error("资料数据库写入失败: %s", sys.exc_info()[0])
            print("资料数据库写入失败: ", sys.exc_info()[0])
        finally:
            catalogCursor.close()

