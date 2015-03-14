__author__ = 'zys'
from django import template


register = template.Library()


@register.simple_tag(name="show_percentage")
def tag_percentage(val):
    return str(val * 100) + '% OFF'


@register.simple_tag(name="cut_email")
def tag_email_cut(val):
    return str.split(val, '@')[0]


@register.simple_tag(name="calc_total")
def tag_calc_total(num, price):
    return num*price


# implement tax by calculation of location
@register.simple_tag(name="calc_total_tax")
def tag_calc_total_tax(num, price, location=None):
    return num*price