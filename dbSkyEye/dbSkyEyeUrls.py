from django.conf.urls import url

from . import dbSkyEyeViews

urlpatterns = [
    url(r'^$', dbSkyEyeViews.index, name='index'),
]
