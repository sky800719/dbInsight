from django.conf.urls import url

from . import authManageViews

app_name = 'authManage'

urlpatterns = [
    url(r'^$', authManageViews.index, name='index'),
    url(r'^login/$', authManageViews.login, name='login'),
]
