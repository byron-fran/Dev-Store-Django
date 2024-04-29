from django.contrib import admin
from .models import Product, Mark, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','descount')
    list_filter = ['category', 'mark', 'price']
    prepopulated_fields = {'slug': ('name', )}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class MarkAdmin(admin.ModelAdmin):
    list_display = ['name']

    
admin.site.register(Product, ProductAdmin)   
admin.site.register(Mark, MarkAdmin)
admin.site.register(Category, CategoryAdmin)    
