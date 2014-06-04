from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.shortcuts import redirect

admin.autodiscover()
from django.contrib.auth.models import Group
admin.site.unregister(Group)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eroapp.views.home', name='home'),
    # url(r'^eroapp/', include('eroapp.foo.urls')),

    # main urls
    url(r'^', include('pages.urls', namespace="pages")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
