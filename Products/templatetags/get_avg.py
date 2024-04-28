from django import template
from django.db.models import  Avg
register = template.Library()

@register.filter(name='get_avg_stars')
def get_avg(product):
    result = product.reviews_set.all().aggregate(
            stars_avg=Avg('stars')
        )
    return round(result['stars_avg'], 2)