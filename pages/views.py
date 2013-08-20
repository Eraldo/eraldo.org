#!/usr/bin/env python
"""
This module contains the web pages based views.
"""
from django.contrib import messages

__author__ = "Eraldo Helal"

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


class ChatView(TemplateView):
    template_name = "pages/chat.html"


class TestView(TemplateView):
    template_name = "pages/test.html"
    def get(self, request, *args, **kwargs):
        messages.info(request, 'Welcome to the Legend of..')
        messages.success(request, 'AWESOME')
        messages.debug(request, 'debugging')
        messages.warning(request, 'Take care..')
        messages.error(request, 'This will change your life!')
        return super(TestView, self).get(request, *args, **kwargs)

