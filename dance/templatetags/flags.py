from django import template
from django.template.loader import render_to_string
from django_countries import countries

register = template.Library()

__author__ = 'eraldo'


@register.simple_tag
def flag(country):
    country_code = countries.by_name(country)
    return render_to_string('dance/_flag.html', {'country': country, 'code': country_code})
