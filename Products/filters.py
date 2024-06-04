from .models import Product
import django_filters

class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    class Meta:
        model = Product
        fields = [ 'category', 'mark', 'price']
    