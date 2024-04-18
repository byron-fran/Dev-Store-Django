from django.db import models
from django.db.models import Q
class ProductsManager(models.Manager):
    def get_all_products(self):
        all_products =  self.all()
        return all_products
    
    def products_search(self, q : str):
        if len(q) > 0:
            products = self.filter(Q (name__icontains=q) | Q ( description__icontains=q) )
            return products