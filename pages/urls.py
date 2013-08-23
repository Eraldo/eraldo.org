#!/usr/bin/env python
"""
Contains the web pages related url mappings.
"""

__author__ = "Eraldo Helal"

from django.conf.urls import patterns, url
from django.shortcuts import redirect
from pages.views import HomeView, TestView, ChatView, ContactView, DanceView, PersonalDevelopmentView, WebDesignView, T42View, TechnologyView

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
    # ex: ../T42/
    url(r'^T42/$',
        T42View.as_view(),
        name='T42'),

    # TOPICS
    # ex: ../dance/
    url(r'^dance/$',
        DanceView.as_view(),
        name='dance'),
    # ex: ../personal-development/
    url(r'^personal-development/$',
        PersonalDevelopmentView.as_view(),
        name='personal-development'),
    # ex: ../web-design/
    url(r'^web-design/$',
        WebDesignView.as_view(),
        name='web-design'),
    # ex: ../T42/
    url(r'^technology/$',
        TechnologyView.as_view(),
        name='technology'),

    # ex: ../chat/
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    # ex: ../test/
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
