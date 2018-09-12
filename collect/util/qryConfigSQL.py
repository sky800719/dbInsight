# -*- coding:utf-8 -*-

# 监控数据库信息
DBListSQL = '''
SELECT DB_ID, INST_ID, DB_NAME, DB_UNIQUE_NAME, DB_VERSION, HOST_IP, TNS_PORT, SERVICE_NAME, CONN_USER, CONN_PASS, DB_ROLE
  FROM DBMP_DB_INFO WHERE DB_STATUS = 'ACTIVE' AND IS_PRIMARY_INST = 'Y' 
'''

# 获取采集规则语句,匹配不同数据库版本对应语句
ExtractCfgSQL = '''
SELECT EXTRACT_RULE_CODE, CATALOG_RECORD_SQL, SRCDB_EXTRACT_SQL
  FROM (SELECT CFG.EXTRACT_RULE_ID,
               CFG.EXTRACT_RULE_CODE,
               EXT.CATALOG_RECORD_SQL,
               EXT.SRCDB_EXTRACT_SQL,
               EXT.DB_VERSION,
               RANK() OVER(PARTITION BY CFG.EXTRACT_RULE_ID ORDER BY(EXT.DB_VERSION) ASC) RANKID
          FROM DBMP_DATA_EXTRACT_CFG CFG, DBMP_DATA_EXTRACT_CFG_EXTEND EXT
         WHERE EXTRACT_RULE_TYPE = :EXTRACT_RULE_TYPE
           AND CFG.EXTRACT_RULE_ID = EXT.EXTRACT_RULE_ID
           AND CFG.EXTRACT_DB_ROLE = :EXTRACT_DB_ROLE
           AND CFG.EXTRACT_RULE_STATUS = 'VALID'
           AND (EXT.DB_VERSION = :DB_VERSION OR EXT.DB_VERSION = 'ALL'))
 WHERE RANKID = 1
 ORDER BY EXTRACT_RULE_ID
'''

# 采集语句执行结果记录
ExtractLogSQL = '''
INSERT INTO DBMP_DATA_EXTRACT_LOG VALUES
(:DB_IP, :DB_UNAME, :EXTRACT_RULE_CODE, SYSDATE, :EXTRACT_FLAG, :SRCDB_EXTRACT_SQL, :CATALOG_RECORD_SQL, :ERROR_MESSAGE)
'''
