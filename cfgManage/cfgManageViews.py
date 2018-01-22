# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response

import logging

log = logging.getLogger(__name__)

def index(request):
    return render_to_response('cfgManage/index.html')

def menuConfig(request):
    return render_to_response('cfgManage/menuConfig.html')

def addConfig(request):

    print('---------------------------------------------')

    menuName = request.GET['menuName']
    menuUrl = request.GET['menuUrl']
    menuSQL = request.GET['menuSQL']

    log.error('menuName => %s', menuName)
    log.debug('menuUrl  => %s', menuUrl)
    log.debug('menuSQL  => %s', menuSQL)

    return render_to_response('cfgManage/index.html')
