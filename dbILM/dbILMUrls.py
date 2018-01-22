from django.conf.urls import url

from . import dbILMViews

urlpatterns = [
    url(r'^$', dbILMViews.index, name='index'),
]
