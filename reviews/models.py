from django.db import models
from Auth.models import User
from Products.models import Product

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    
    class Meta:
        verbose_name  = 'review'
        verbose_name_plural = 'reviews'