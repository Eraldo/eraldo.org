from django.contrib import admin
from dance.models import Instructor, Group


__author__ = 'eraldo'


admin.site.register(Group)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'partner', 'group', 'country', 'has_url')

admin.site.register(Instructor, InstructorAdmin)
