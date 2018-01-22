from django.conf.urls import url

from . import dbGuardianViews

urlpatterns = [
    url(r'^$', dbGuardianViews.index, name='index'),
]
