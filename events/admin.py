from django.contrib import admin
from events.models import Event

__author__ = 'eraldo'


class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end', 'type', 'country', 'city', 'has_url')

admin.site.register(Event, EventsAdmin)