__author__ = 'zys'
from django import template


register = template.Library()


@register.simple_tag(name="show_percentage")
def tag_percentage(val):
    return str(val * 100) + '% OFF'


@register.simple_tag(name="cut_email")
def tag_email_cut(val):
    return str.split(val, '@')[0]