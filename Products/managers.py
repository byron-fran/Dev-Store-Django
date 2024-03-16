from django.db import models

class ProductsManager(models.Manager):
    def get_all_products(self):
        all_products =  self.all()
        return all_products