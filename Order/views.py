from django.shortcuts import render
from Products.models import Product
from .models import Order

# Create your views here.
def add_to_cart(request, pk):
    
    product_found = Product.objects.get(id=pk)
  
    order, created = Order.objects.get_or_create(
        user=request.user,
        name=product_found.name,
        description=product_found.description,
        price=product_found.price,
        image_url=product_found.image_url,
        descount=product_found.descount
    )

    # Agregar el producto a la relación ManyToManyField
    order.product.add(product_found)
    
    return render(request, 'cart.html')