from django import template

register = template.Library()

@register.filter
def product_stock(stock : int):
    if stock == 0:
        return True
    return False