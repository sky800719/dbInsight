# -*- coding:utf-8 -*-

import logging
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from .utils import DALUtil, DataGatherUtil, SYSConfig, authCheck

from django.http import HttpResponse
from .tasks import task_a

log = logging.getLogger(__name__)

def index(request):
    return render_to_response('login.html')

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

    # 获取菜单配置
    menuList = DALUtil.getCfgSqlResult('menuQry')
    returnDict['menuList'] = menuList 

    # 获取APP配置
    appList = DALUtil.getAPPCfgResult()
    returnDict['appList'] = appList 

    # 获取DB配置
    dbList = DALUtil.getDBCfgResult()
    returnDict['dbList'] = dbList

    return render_to_response('index.html', returnDict)


def mainPageInit(request):

    """首页初始化代码,用于展现查询首页展现内容信息
    """

    print('mainPageInit fav_color -> ', request.session["fav_color"])

    urlQryType = request.GET['urlQryType']

    # 定义查询返回字典
    returnMessage = ''
    returnDict = {}

    tabList = DALUtil.getCfgSqlResultWithColName(urlQryType, '')

    if len(tabList) <= 1:
        returnMessage = '没有找到查询的实例信息！'

    # 获取数据库运行负载信息
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

def commMenuInitQry(request):

    """ 通用菜单初始化，用于简单表格配置的展现，返回展现表格所需的DIV，触发URL，调整页面
    """

    urlQryType = request.GET['urlQryType']

    # 定义查询返回字典
    returnDict = {}

    # 菜单对应配置表格信息
    menuList = DALUtil.getMenuCfg(urlQryType, '')

    menuDict = menuList[0]
    returnDict['MENU_ACTION'] = menuList

    returnURL = menuDict['RESPONSE_URL']

    return render_to_response(returnURL, returnDict)

def commURLSQLQuery(request):

    """ 通用菜单表格配置语句结果展现
    """

    urlQryType = request.GET['urlQryType']
    urlQryAction = request.GET['urlQryAction']

    # 定义查询返回字典
    returnDict = {}

    # 菜单配置信息
    menuDict = DALUtil.getURLExtendInfo(urlQryType, urlQryAction)

    for mk in menuDict:
        returnDict[mk] = menuDict[mk]

    returnURL = menuDict['RESPONSE_URL']

    # 配置语句查询结果
    tabList = DALUtil.getCfgSqlResultWithColName(urlQryType, urlQryAction)

    returnMessage = ''
    if len(tabList) <= 1:
        returnMessage = '没有找到查询的实例信息！'

    returnDict['queryResult'] = tabList
    returnDict['returnMessage'] = returnMessage

    return render_to_response(returnURL, returnDict)

def get(request):
    task_a.delay()  # 发送消息，触发后台任务
    return HttpResponse("django and celery!")
