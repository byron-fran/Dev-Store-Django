from django.db import models
from django.db.models import Q
from django.db.models import  Manager, Avg, Count, Sum


class ProductsManager(models.Manager):
    def get_all_products(self):
        all_products =  self.all()
        return all_products
    
    def products_search(self, q : str):
        if len(q) > 0:
            products = self.filter(Q (name__icontains=q) | Q ( description__icontains=q) )
            return products
    def avg_stars(self, product):
        result = product.reviews_set.all().aggregate(
            stars_avg=Avg('stars')
        )
        return result['stars_avg']