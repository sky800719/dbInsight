# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from .utils import DALUtil, SYSConfig, authCheck

from django.http import HttpResponse

import logging
log = logging.getLogger(__name__)


def index(request):
    return render_to_response('login.html')


"""
首页初始化流程：
1. def login 进行登录认证，认证成功后进入sysInit
2. def sysInit 进行系统初始化，初始化菜单、数据库列表、应用模块，初始化完成后，进入index.html
3. index.html 页面使用jQuery进行页面初始化，调用请求为mainPageInit
4. def mainPageInit 完成首页初始化，进入mainPage.html页面
"""


def login(request):
    """ 系统登录校验
    """

    returnMessage = ''
    returnDict = {}

    logUser = request.GET.get('userName', None).strip()
    logPass = request.GET.get('passWord', None).strip()

    log.debug('logUser  => %s', logUser)
    log.debug('logPass  => %s', logPass)

    if len(logUser) == 0 or len(logPass) == 0:
        returnMessage = '用户/口令不能为空，请重新输入!'
        returnDict['returnMessage'] = returnMessage
        return render_to_response('login.html', returnDict)

    encrptyPass = authCheck.passEncrypt(logPass)
    checkPassList = DALUtil.checkUserPass(logUser, encrptyPass)

    if len(checkPassList) < 1:
        returnMessage = '用户/口令不一致，请输入正确的用户及口令!'
        returnDict['returnMessage'] = returnMessage
        return render_to_response('login.html', returnDict)
    else:
        # 登录成功，跳转到系统初始化页面，直接访问sysInit方法
        request.session["LOGON"] = 'Y'
        return HttpResponseRedirect('sysInit')


def sysInit(request):
    """初始化系统菜单
    """

    # http://blog.chinaunix.net/uid-10915175-id-5572399.html
    # http://www.yiibai.com/django/django_sessions.html 会话管理
    # http://www.cnblogs.com/fnng/p/3841246.html
    # http://code.ziqiangxuetang.com/django/django-session.html
    request.session["fav_color"] = "blue"
    print('index fav_color -> ', request.session["fav_color"])

    returnMessage = ''

    # 定义查询返回字典
    returnDict = {}

    # 获取菜单配置，菜单配置表为:DBMP_SYS_MENU_URL
    menuList = DALUtil.getCfgSqlResult('menuQry')
    returnDict['menuList'] = menuList

    # 获取APP配置，APP配置表为:DBMP_APP_CONFIG
    appList = DALUtil.getAPPCfgResult()
    returnDict['appList'] = appList

    # 获取DB配置，DB配置表为:DBMP_DB_INFO
    dbList = DALUtil.getDBCfgResult()
    returnDict['dbList'] = dbList

    # 数据初始化成功后，进入首页，首页通过jQuery进行初始化，进入mainPageInit方法
    return render(request, 'index.html', returnDict)


def mainPageInit(request):
    """ 首页初始化代码,用于展现查询首页展现内容信息
    """

    print('mainPageInit fav_color -> ', request.session["fav_color"])

    MENU_URL = request.GET['MENU_URL']

    # 定义查询返回字典
    returnMessage = ''
    returnDict = {}

    tabList = DALUtil.getCfgSqlResultWithColName(MENU_URL, '')

    if len(tabList) <= 1:
        returnMessage = '没有找到查询的实例信息！'

    # 获取数据库运行负载信息，模拟数据
    dbLoadDict = '''
    [
    {value: 8, name: 'PUBDB'},
    {value: 18, name: 'YYDBA'},
    {value: 28, name: 'YYDBB'},
    {value: 18, name: 'CBDB'},
    {value: 18, name: 'ZGDBA'},
    {value: 10, name: 'ZGDBB'},
    ]
    '''

    # 获取数据库TOP负载信息

    # 获取数据库告警信息

    returnDict['returnMessage'] = returnMessage
    returnDict['queryResult'] = tabList
    returnDict['dbLoadChart'] = dbLoadDict

    return render_to_response('mainPage.html', returnDict)


"""
通用菜单查询处理流程：
1. def sysInit 中完成 menuList 的初始化，在页面中展现菜单的URL配置信息，菜单配置语句从DBMP_SYS_MENU_URL表中获取
2. 点击index.html的连接，调用commMenuInitQry函数调用def commMenuInitQry方法，进行菜单配置信息查询
3. 多个表格的配置信息，从DBMP_MENU_URL_EXTEND表中获取，查询结果返回commMenuInit.html页面
4. commMenuInit.html中循环生产展现表格，并且对表格配置的URL请求进行循环调用
5. def commURLSQLQuery方法完成最终表格SQL查询内容的展现以及非表格图表的展现，配置信息存放在DBMP_MENU_URL_EXTEND表中

index.html -> function commMenuInitQry(MENU_URL)
           -> def commMenuInitQry -> commMenuInit.html
           -> commURLSQLQuery -> def commURLSQLQuery
"""


def commMenuInitQry(request):
    """ 通用菜单初始化，用于简单表格配置的展现，返回展现表格所需的DIV，触发URL，结果返回commMenuInit.html
    """

    MENU_URL = request.GET['MENU_URL']

    # 定义查询返回字典
    returnDict = {}

    # 菜单对应配置表格信息，菜单与展现表格存在一对多关系
    menuList = DALUtil.getMenuCfg(MENU_URL, '')
    returnDict['MENU_ACTION'] = menuList

    menuDict = menuList[0]
    returnURL = menuDict['RESPONSE_URL']

    return render_to_response(returnURL, returnDict)


def commURLSQLQuery(request):
    """ 菜单配置URL对应查询解析方法，用于将页面请求的调用转换到对应的SQL查询，结果返回commTabDisplay.html页面
    """

    MENU_URL = request.GET['MENU_URL']
    URL_ACTION = request.GET['URL_ACTION']

    # 定义查询返回字典
    returnDict = {}

    # 展现表格配置信息，存放在DBMP_MENU_URL_EXTEND中
    menuDict = DALUtil.getURLExtendInfo(MENU_URL, URL_ACTION)

    for mk in menuDict:
        returnDict[mk] = menuDict[mk]

    # 菜单返回URL地址
    returnURL = menuDict['RESPONSE_URL']

    # 配置语句查询结果，存放在DBMP_MENU_URL_SQL_MAP中
    tabList = DALUtil.getCfgSqlResultWithColName(MENU_URL, URL_ACTION)

    returnMessage = ''
    if len(tabList) <= 1:
        returnMessage = '没有找到查询的实例信息！'

    returnDict['queryResult'] = tabList
    returnDict['returnMessage'] = returnMessage

    return render_to_response(returnURL, returnDict)
