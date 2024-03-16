from django.db import models
from Auth.models import User
from Products.models import Product

# Create your models here.
class Order(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
       
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.FileField(upload_to='products/')
    descount = models.FloatField()
    paid= models.BooleanField(default=False)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')


    class Meta:
        ordering = ['-name']
        verbose_name='order'
        verbose_name_plural='orders'
        db_table='Orders'

    def __str__(self):
        return self.name
    