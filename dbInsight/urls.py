"""dbInsight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from . import dashboardViews, dbCronViews

app_name = 'dbInsight'

urlpatterns = [
    url(r'^authManage/', include('authManage.authManageUrls')),
    url(r'^cfgManage/', include('cfgManage.cfgManageUrls')),
    url(r'^dbGuardian/', include('dbGuardian.dbGuardianUrls')),
    url(r'^dbILM/', include('dbILM.dbILMUrls')),
    url(r'^dbReport/', include('dbReport.dbReportUrls')),
    url(r'^dbRobot/', include('dbRobot.dbRobotUrls')),
    url(r'^dbSkyEye/', include('dbSkyEye.dbSkyEyeUrls')),
    url(r'^dbSQLAudit/', include('dbSQLAudit.dbSQLAuditUrls')),
    url(r'^$', dashboardViews.index, name='index'),
    url(r'^get/', dashboardViews.get, name='get'), # celery test URL
    url(r'^login$', dashboardViews.login, name='login'),
    url(r'^sysInit$', dashboardViews.sysInit, name='sysInit'),
    url(r'^mainPageInit$', dashboardViews.mainPageInit, name='mainPageInit'),
    url(r'^commMenuInitQry$', dashboardViews.commMenuInitQry, name='commMenuInitQry'),
    url(r'^commURLSQLQuery$', dashboardViews.commURLSQLQuery, name='commURLSQLQuery'),
    url(r'^gatherDBInfo$', dbCronViews.gatherDBInfo, name='gatherDBInfo'),
    url(r'^cleanGatherData$', dbCronViews.cleanGatherData, name='cleanGatherData'),
    url(r'^getDBList$', dbCronViews.getDBList, name='getDBList'),
]
