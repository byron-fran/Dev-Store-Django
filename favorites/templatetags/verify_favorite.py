from django import template
from ..models import Favorite
register = template.Library()

@register.filter
def verify_favorite(product, user):
    # Filtrar los favoritos relacionados con el producto dado y el usuario dado
    is_favorite = Favorite.objects.filter(product=product, user=user).exists()
    return is_favorite
