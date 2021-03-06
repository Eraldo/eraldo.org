from django.conf.urls import patterns, url
from contact.views import ContactView, T42View

__author__ = 'eraldo'


urlpatterns = patterns('',
    # ex: ../contact/
    url(r'^$',
        ContactView.as_view(),
        name='home'),
    # ex: ../T42/
    url(r'^T42/$',
        T42View.as_view(),
        name='T42'),
    )