from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect, render
from Products.models import Product
from .models import Favorite
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def add_favorite(request : HttpRequest, pk):
    product = Product.objects.get(id=pk)
    
    try:
        favorite = Favorite(user=request.user, product=product)
        favorite.save()
    except product.DoesNotExist:
        print("error")
    return redirect(request.GET['path'])

def remove_Favorite(request : HttpRequest, pk):
    product = Product.objects.get(id=pk)
    try:
        fav = Favorite.objects.filter(product=product, user=request.user)
        fav.delete()
        
    except product.DoesNotExist:
        pass   
   
    return redirect(request.GET['path'])


class ListFavorite(LoginRequiredMixin, ListView):
    model = Favorite
    template_name='favorites.html'
    context_object_name = 'favorites'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
  
        context = super().get_context_data(**kwargs) 
        context['favorites'] = context['favorites'].filter(user=self.request.user)
        return context