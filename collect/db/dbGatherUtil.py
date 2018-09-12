# -*- coding:utf-8 -*-

import sys
import cx_Oracle

sys.path.append("..")

from util import dbAccessUtil
from util import qryConfigSQL

def dataExtract(srcDBDictInfo, gatherFlag):

    """ 采集源端数据库数据到资料库
    """

    # 创建资料数据库连接信息
    catalogConnDict = ''
    catalogConn = ''
    catalogCursor = ''

    try:
        print('1. 开始创建资料数据库连接！')
        catalogConnDict = dbAccessUtil.getCataLogDBConn()

        if catalogConnDict['MSGCODE'] == 0:
            catalogConn = catalogConnDict['CONNECT']
            catalogCursor = catalogConn.cursor()
        else:
            print('1. 创建资料数据库连接失败！')
            return '-1'
    except Exception:
        print("1. 创建资料数据库连接失败: ", sys.exc_info()[1])
        return '-1'

    # 创建源端采集数据库连接信息
    srcDBConnDict = ''
    srcDBIP = ''
    srcDBUName = ''
    srcDBVersion = ''
    srcDBRole = ''
    srcDBConn = ''
    srcDBCursor = ''
    msgContent = ''
    extractLogDict = {
        'DB_IP': '',
        'DB_UNAME': '',
        'EXTRACT_RULE_CODE': 'CONNECT_SOURCE_DB',
        'EXTRACT_FLAG': 'SUCESS',
        'SRCDB_EXTRACT_SQL': '',
        'CATALOG_RECORD_SQL': '',
        'ERROR_MESSAGE': '数据采集开始！'
    }

    try:
        print('2. 开始创建源端数据库连接！')
        srcDBConnDict = dbAccessUtil.getSrcDBConn(srcDBDictInfo)
    
        srcDBIP = srcDBConnDict['SRC_DB_IP']
        srcDBUName = srcDBConnDict['SRC_DB_UNAME']
        msgContent = srcDBConnDict['MSGCONTENT']

        extractLogDict['DB_IP'] = srcDBIP
        extractLogDict['DB_UNAME'] = srcDBUName 

        if srcDBConnDict['MSGCODE'] == 0:
            srcDBConn = srcDBConnDict['CONNECT']
            srcDBVersion = srcDBConnDict['SRC_DB_VERSION']
            srcDBRole = srcDBConnDict['SRC_DB_ROLE']
            srcDBCursor = srcDBConn.cursor()

            dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)
        else:
            msgContent = '2. 建源端数据库连接失败！'
            print(msgContent)

            extractLogDict['ERROR_MESSAGE'] = srcDBUName 
            dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)
            return '-1'
    except Exception:
        msgContent = "2. 创建源端数据库连接失败: " + str(sys.exc_info()[1])
        print(msgContent)

        extractLogDict['EXTRACT_FLAG'] = 'FAILED'
        extractLogDict['ERROR_MESSAGE'] = msgContent
        dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)
        return '-1'

    # 获取数据库采集配置信息
    extractRuleCode = ''
    extractSrcSQL = ''
    extractList = []

    try:
        print('3. 开始获取数据库采集配置信息！')
        dbMainVersion = srcDBVersion.split('.')[0]

        # 根据crontab参数，获取对应的查询采集语句
        print('3. 数据库采集配置信息条件：') 
        print('3. EXTRACT_RULE_TYPE -> ', gatherFlag) 
        print('3. DB_VERSION -> ', dbMainVersion) 

        extractList = dbAccessUtil.getSQLResult(catalogCursor, 
                qryConfigSQL.ExtractCfgSQL, 
                {'EXTRACT_RULE_TYPE': gatherFlag, 'DB_VERSION': dbMainVersion, 'EXTRACT_DB_ROLE': srcDBRole})

        print('3. 获取数据库采集配置信息成功！')
    except BaseException:
        msgContent = "3. 获取数据库采集配置信息失败: " + str(sys.exc_info()[1])
        print(msgContent)

        extractLogDict['EXTRACT_RULE_CODE'] = 'GET_EXTRACT_SQL'
        extractLogDict['EXTRACT_FLAG'] = 'FAILED'
        extractLogDict['ERROR_MESSAGE'] = msgContent
        dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)

        return '-1'

    for extractRule in extractList:

        """ 对采集配置进行循环处理
        """

        print("4. 获取源端数据库查询语句！")
        extractRuleCode = extractRule['EXTRACT_RULE_CODE']
        extractLogDict['EXTRACT_RULE_CODE'] = extractRuleCode

        # 源端数据库查询语句
        tmpExtractSrcSQL = extractRule['SRCDB_EXTRACT_SQL']
        extractSrcSQL = tmpExtractSrcSQL.replace('{DB_IP}', str(srcDBIP)).replace('{DB_UNAME}', str(srcDBUName))
        # print('4. 数据库查询语句 -> ', extractSrcSQL)

        # 资料数据库数据写入语句
        extractDestSQL = extractRule['CATALOG_RECORD_SQL']
        
        # 源端数据库查询数据结果集
        rowList = []

        try:
            print("4. 开始执行源端数据库采集语句！")

            srcDBCursor.execute(extractSrcSQL)

            # 获取源库语句执行结果
            print("4. 开始获取源端数据库采集结果！")
            srcDBQryResult = srcDBCursor.fetchall()
            columnList = dbAccessUtil.qrySQLColParse(srcDBCursor)

            # 处理查询结果集
            print("4. 开始处理源端数据库采集结果！")
            for row in srcDBQryResult:
                rowInfo = {}
                for col in range(len(columnList)):
                    rowInfo[columnList[col]] = row[col]
                rowList.append(rowInfo)

            print('4. 源端数据库查询结果解析完成！')
        except BaseException:
            msgContent = "4. 源端数据库查询失败: " + str(sys.exc_info()[1])
            print(msgContent)
            print("4. 源端数据库查询失败，查询语句为: ", extractSrcSQL)

            extractLogDict['EXTRACT_FLAG'] = 'FAILED'
            extractLogDict['SRCDB_EXTRACT_SQL'] = extractSrcSQL
            extractLogDict['CATALOG_RECORD_SQL'] = extractDestSQL
            extractLogDict['ERROR_MESSAGE'] = msgContent
            dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)

        #print('4. 源端数据库查询结果 rowList => ', rowList)
        #print('4. 源端数据库查询结果数据量 len(rowList) => ', len(rowList))

        # 创建资料数据库连接
        try:
            print('5. 开始写入源端数据库结果到资料库！')


            #for row in rowList:
            #    print('row -> ', row)
            #    catalogCursor.execute(extractDestSQL, row)
            #    catalogConn.commit()

            catalogCursor.executemany(extractDestSQL, rowList)
            catalogConn.commit()
            print('5. 源端数据库结果写入资料库完成！')

            extractLogDict['EXTRACT_FLAG'] = 'SUCESS'
            extractLogDict['SRCDB_EXTRACT_SQL'] = extractSrcSQL
            extractLogDict['CATALOG_RECORD_SQL'] = extractDestSQL
            extractLogDict['ERROR_MESSAGE'] = '数据采集成功！'
            dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)
        except BaseException:
            msgContent = "5. 资料数据库写入失败: " + str(sys.exc_info()[1])
            print(msgContent)

            extractLogDict['EXTRACT_FLAG'] = 'FAILED'
            extractLogDict['SRCDB_EXTRACT_SQL'] = extractSrcSQL
            extractLogDict['CATALOG_RECORD_SQL'] = extractDestSQL
            extractLogDict['ERROR_MESSAGE'] = msgContent

            dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)


    # 关闭资料库与源端采集库连接和游标
    extractLogDict['EXTRACT_RULE_CODE'] = 'CLOSE_DB_CONNECT'

    try:
        extractLogDict['EXTRACT_FLAG'] = 'SUCESS'
        extractLogDict['SRCDB_EXTRACT_SQL'] = '' 
        extractLogDict['CATALOG_RECORD_SQL'] = ''
        extractLogDict['ERROR_MESSAGE'] = '数据采集完成！'
        dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)

        catalogCursor.close()
        catalogConn.close()

        srcDBCursor.close()
        srcDBConn.close()
    except Exception:
        msgContent = "6. 关闭数据库连接失败: " + str(sys.exc_info()[1])
        print(msgContent)

        extractLogDict['EXTRACT_FLAG'] = 'FAILED'
        extractLogDict['SRCDB_EXTRACT_SQL'] = '' 
        extractLogDict['CATALOG_RECORD_SQL'] = ''
        extractLogDict['ERROR_MESSAGE'] = msgContent
        dbAccessUtil.extractLogRecord(catalogConn, catalogCursor, extractLogDict)

        return '-1'
