from django import template

register = template.Library()

@register.filter(name='rest_one')
def rest_one(value : int):
    
    return value -1