from django.conf.urls import url

from . import dbSQLAuditViews

urlpatterns = [
    url(r'^$', dbSQLAuditViews.index, name='index'),
]
