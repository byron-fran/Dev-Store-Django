from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from Products.models import Product
from .models import Order
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def add_to_cart(request, pk):
    
    product_found = Product.objects.get(id=pk)
    print(product_found)
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
    return redirect('cart')

def remove_from_cart(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('cart')

class ListOrdersView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    template_name = 'cart.html'
    context_object_name = 'orders'
    model = Order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(user=self.request.user)
        return context

    

    

  
    
    