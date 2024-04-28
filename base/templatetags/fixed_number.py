from django import template

register = template.Library()

@register.filter
def fixed_number(number):
    return round(int(number))