from django.db import models
from Auth.models import User
from Products.models import Product

# Create your models here.
class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.FileField(upload_to='products/')
    descount = models.FloatField()
    paid= models.BooleanField(default=False)
    quantity = models.IntegerField(name='quantity', null=True )
    total_price = models.IntegerField(name='total_price', null=True)
    product_id = models.CharField(max_length=200, null=True)
    
    class Meta:
        ordering = ['-name']
        verbose_name='order'
        verbose_name_plural='orders'
        db_table='Orders'

    def __str__(self):
        return self.name
    