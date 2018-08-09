//<h3 id="overview-database">数据库信息</h3>
var DATABASE_TABID = 'DATABASE_TABID';

var DATABASE_COLUMNVALUE =
[
    {field : 'INST_ID', title : '实例ID' }, 
    {field : 'DBID', title : '数据库ID' }, 
    {field : 'NAME', title : '数据库名称' }, 
    {field : 'LOG_MODE', title : '归档模式' }, 
    {field : 'OPEN_MODE', title : '打开模式' }, 
    {field : 'CURRENT_SCN', title : '当前SCN' }, 
    {field : 'FLASHBACK_ON', title : '闪回状态' }, 
    {field : 'DB_UNIQUE_NAME', title : '数据库唯一名称' },
];

var DATABASE_DATAVALUE =
[
  {'INST_ID' : '1', 'DBID' : '4245605106', 'NAME' : 'SQLAUDIT', 'LOG_MODE' : 'NOARCHIVELOG', 'OPEN_MODE' : 'READ WRITE', 'CURRENT_SCN' : '8745001', 'FLASHBACK_ON' : 'NO', 'DB_UNIQUE_NAME' : 'sqlaudit'}
];

//<h3 id="overview-instance">实例运行信息</h3>
var INSTANCE_TABID = 'INSTANCE_TABID';

var INSTANCE_COLUMNVALUE =
[
    {field : 'INST_ID', title : '实例ID' }, 
    {field : 'INSTANCE_NAME', title : '实例名称' }, 
    {field : 'HOST_NAME', title : '主机名' }, 
    {field : 'STARTUP_TIME', title : '启动时间' }, 
    {field : 'STATUS', title : '启动状态' }, 
    {field : 'THREAD#', title : '归档线程编号' }, 
    {field : 'ARCHIVER', title : '归档状态' },
    {field : 'INSTANCE_ROLE', title : '实例角色' },
];

var INSTANCE_DATAVALUE =
[
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
{'INST_ID' : '2', 'INSTANCE_NAME' : 'sqlaudit', 'HOST_NAME' : 'sqlaudit', 'STARTUP_TIME' : '2018-02-08 02:09:10', 'STATUS' : 'OPEN', 'THREAD#' : '1', 'ARCHIVER' : 'STOPPED', 'INSTANCE_ROLE' : 'PRIMARY_INSTANCE'},
]
