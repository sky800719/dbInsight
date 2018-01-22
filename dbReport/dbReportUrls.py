from django.conf.urls import url

from . import dbReportViews

urlpatterns = [
    url(r'^$', dbReportViews.index, name='index'),
]
