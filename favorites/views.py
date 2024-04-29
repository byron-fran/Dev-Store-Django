from typing import Any
from django.shortcuts import redirect, render
from Products.models import Product
from .models import Favorite
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def add_favorite(request, id, page):
    product = Product.objects.get(id=id)
    try:
        favorite = Favorite(user=request.user, product=product)
        favorite.save()
    except:
        print("error")
    return redirect(f'/products/?page={page}')

def remove_Favorite(request, pk, page):
    
    product = Product.objects.get(id=pk)
    fav = Favorite.objects.filter(product=product, user=request.user)
    fav.delete()

    return redirect(f'/products/?page={page}')

def remove_Favorite_from_list(request, pk):
    
    try:
        fav = Favorite.objects.get(id=pk)
        fav.delete()
        pass
    except:
        print("Error")
    return redirect('/favorites/list/')


class ListFavorite(LoginRequiredMixin, ListView):
    model = Favorite
    template_name='favorites.html'
    context_object_name = 'favorites'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
  
        context = super().get_context_data(**kwargs) 
        context['favorites'] = context['favorites'].filter(user=self.request.user)
        return context