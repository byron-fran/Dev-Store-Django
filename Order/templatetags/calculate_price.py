from django import template
from ..models import Order
register = template.Library()

@register.filter
def calulate_total_price(orders : Order ):
    
    total_price : int = 0
    for index in range(len(orders)):
        total_price += orders[index].price * orders[index].quantity
    
    return total_price