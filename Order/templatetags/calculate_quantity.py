from django import template

register = template.Library()

@register.filter
def calculate_quantity(value):
    if len(value)  > 0:
        return True
    return False

