from django.db import models
from django.contrib.auth.models import User
from Products.models import Product

# Create your models here.
class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.FileField(upload_to='products/')
    descount = models.FloatField()
    
    def __str__(self):
        return self.name
    