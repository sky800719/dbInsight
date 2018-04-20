# -*- coding:utf-8 -*-

""" 监控数据库查询信息
"""
# 监控数据库信息
DBInfoSQL = "SELECT DB_UID, DB_ID, DB_NAME FROM DBMP_DB_INFO"

# 获取数据库连接配置信息
DBConnectInfoSQL = '''
SELECT DB_UID, HOST_IP, TNS_PORT, DB_NAME, CONN_USER, CONN_PASS 
  FROM DBMP_DB_INFO 
 WHERE DB_ID = :DB_ID AND DB_NAME = :DB_NAME'''

""" 应用信息查询信息 
"""
# 获取应用APP信息
APPQrySQL = "SELECT APP_ID, APP_CODE, APP_URL, APP_NAME FROM DBMP_APP_CONFIG ORDER BY APP_DISP_ORDER"

""" 菜单查询配置信息
"""
# 简单菜单查询配置语句
SimpleURLQrySQL = "SELECT URL_SQL FROM DBMP_MENU_URL_SQL_MAP WHERE MENU_URL = :MENU_URL"

# 复杂菜单查询配置语句包含绑定变量信息语句
URLQrySQLWithBind = '''
SELECT URL_SQL, SQL_PARAM1, SQL_VALUE1, SQL_PARAM2, SQL_VALUE2, SQL_PARAM3, SQL_VALUE3
  FROM DBMP_MENU_URL_SQL_MAP
 WHERE MENU_URL = :MENU_URL'''

# 复杂菜单查询配置语句包含绑定变量信息语句
URLMapQrySQLWithBind = '''
SELECT URL_SQL, SQL_PARAM1, SQL_VALUE1, SQL_PARAM2, SQL_VALUE2, SQL_PARAM3, SQL_VALUE3
  FROM DBMP_MENU_URL_SQL_MAP
 WHERE MENU_URL = :MENU_URL
   AND URL_ACTION = :URL_ACTION '''

""" 菜单扩展配置信息
"""
# 获取菜单关联URL配置信息
MenuURLMapSQL = '''
SELECT URL.MENU_NAME,
       URL.MENU_URL,
       NVL(URL.RESPONSE_URL, 'index.html') RESPONSE_URL,
       EXT.URL_FUNC,
       EXT.URL_ACTION,
       EXT.URL_ACTION||'DIV' URL_DIV,
       EXT.URL_ACTION||'TAB' URL_TAB,
       EXT.ACTION_DESC
  FROM DBMP_SYS_MENU_URL URL, DBMP_MENU_URL_EXTEND EXT
 WHERE URL.MENU_URL = EXT.MENU_URL
   AND URL.MENU_URL = :MENU_URL
 ORDER BY ORDER_FLAG'''

# 获取展现表格配置信息
URLDisplaySQL = '''
SELECT URL_ACTION || 'TAB' URL_TAB, ACTION_DESC, RESPONSE_URL
  FROM DBMP_MENU_URL_EXTEND
 WHERE MENU_URL = :MENU_URL
   AND URL_ACTION = :URL_ACTION'''

# 获取采集规划语句
ExtractCfgSQL = '''
SELECT CATALOG_RECORD_SQL, SRCDB_EXTRACT_SQL, RULE_SEQ
  FROM DBMP_DATA_EXTRACT_CFG WHERE EXTRACT_RULE_TYPE = :EXTRACT_RULE_TYPE'''

""" 登录认证
"""

# 检查用户口令及帐号有效期
CheckUserAuth = '''
SELECT * FROM DBMP_APP_USER 
 WHERE USER_NAME = :USER_NAME AND USER_PASS = :USER_PASS AND STATUS = 'ACTIVE' AND SYSDATE < EXP_DATE '''
