from django.conf.urls import url

from . import cfgManageViews


app_name = 'cfgManage'

urlpatterns = [
    url(r'^$', cfgManageViews.index, name='index'),
    url(r'^menuConfig$', cfgManageViews.menuConfig, name='menuConfig'),
    url(r'^addConfig$', cfgManageViews.addConfig, name='addConfig'),
]
