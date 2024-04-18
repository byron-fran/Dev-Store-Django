from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from Products.models import Product
from .models import Order
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def add_to_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    quantity = int(request.POST.get('quantity'))
    total_price = product.price * quantity

    try:
        order = Order.objects.get(product_id=product.id)
        order.quantity = quantity
        order.total_price = total_price
        order.save()
    except Order.DoesNotExist:
        order = Order.objects.create(
            user=request.user,
            name=product.name,
            description=product.description,
            price=product.price,
            image_url=product.image_url,
            descount=product.descount,
            quantity=quantity,
            total_price=total_price,
            product_id=product.id
        )
        order.product.add(product)

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

    

    

  
    
    