from django.conf.urls import url

from . import dbRobotViews

urlpatterns = [
    url(r'^$', dbRobotViews.index, name='index'),
]
