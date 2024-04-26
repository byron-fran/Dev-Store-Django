from django  import template

register = template.Library()

@register.filter
def to_number(vlaue):
    return int(vlaue)