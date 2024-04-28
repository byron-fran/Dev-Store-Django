from django import template

register = template.Library()

@register.filter
def get_remainder(value):
    total_stars = 5
    missing_stars =  total_stars - int(value)
    
    return range(missing_stars)