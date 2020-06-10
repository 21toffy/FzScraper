from django import template

register = template.Library()


@register.filter
def strip(value):
    return value[0]


