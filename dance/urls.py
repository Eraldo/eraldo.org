from django.conf.urls import patterns, url
from dance.views import DanceView

__author__ = 'eraldo'


urlpatterns = patterns('',
    # ex: ../dance/
    url(r'^$',
        DanceView.as_view(),
        name='home'),
    )