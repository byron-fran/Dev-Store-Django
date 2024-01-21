from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.FileField(upload_to='products/')
    descount = models.FloatField()
    

