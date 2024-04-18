from django import template

register = template.Library()

@register.filter
def currency(value):
    currency = "${:,.2f}".format(value)
    return currency