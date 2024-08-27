from django.db import models
import uuid
from .managers import ProductsManager
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=200, )
    image = models.FileField(upload_to='categories/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering =  ['-name']
        
class Mark (models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering =  ['-name']
        db_table='marks'
  
 
class Product (models.Model):

    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    descount = models.FloatField()
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    image_url = models.FileField(upload_to='products/', blank=True)
    slug = models.SlugField(null=True, blank=True)
    # field for manager
    objects = ProductsManager()
    
    def __str__(self):
        return f"{self.name} - {self.price}" 
    
    class Meta:
        ordering = ['-stock', '-price']
        db_table= 'products'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='products_images/', blank=True)
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}"
