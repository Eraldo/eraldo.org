#!/usr/bin/env python
"""
Contains the web pages related url mappings.
"""

__author__ = "Eraldo Helal"

from django.conf.urls import patterns, url
from django.shortcuts import redirect
from pages.views import HomeView, TestView, ChatView, ContactView

urlpatterns = patterns('',
    # ex: ../
    url(r'^$',
        lambda x: redirect('home/'),
        name='redirect'),
    # ex: ../home/
    url(r'^home/$',
        HomeView.as_view(),
        name='home'),
    # ex: ../contact/
    url(r'^contact/$',
        ContactView.as_view(),
        name='contact'),
    # ex: ../chat/
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    # ex: ../test/
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
