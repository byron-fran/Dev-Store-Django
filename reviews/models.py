from django.db import models
from Auth.models import User
from Products.models import Product

# Create your models here.
class Reviews(models.Model):
    STAR_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    stars = models.IntegerField(choices=STAR_CHOICES, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name  = 'review'
        verbose_name_plural = 'reviews'
        db_table ='reviews'