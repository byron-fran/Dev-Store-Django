from django.contrib import admin
from .models import Product, Mark, Category, ProductImages

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','descount')
    list_filter = ['category', 'mark', 'price']
    prepopulated_fields = {'slug': ('name', )}

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text')

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class MarkAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Product, ProductAdmin)   
admin.site.register(Mark, MarkAdmin)
admin.site.register(Category, CategoryAdmin)    
admin.site.register(ProductImages, ProductImagesAdmin)