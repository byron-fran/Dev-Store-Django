from django.db import models
import uuid
import django_filters

class Category(models.Model):
    name = models.CharField(max_length=200, )
    
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
        
class Product (models.Model):
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


    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.FileField(upload_to='products/', blank=True)
    descount = models.FloatField()
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default='M')
    def __str__(self):
        return f"{self.name} - {self.price}" 
    
    class Meta:
        ordering = ['-stock', '-price']


 