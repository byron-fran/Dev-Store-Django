from django.db import models
from Auth.models import User
from Products.models import Product

# Create your models here.
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='favorite'
        verbose_name_plural='favorites'
        db_table = 'favorites'
    
    def __str__(self):
        return self.user.username