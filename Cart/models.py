from django.contrib.auth.models import User
from django.db import models
from Products.models import Product


class Cart (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    