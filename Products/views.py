#import a list view
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Product
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ProductFilter
from django.shortcuts import render



class ProducstListView(ListView):
   
    queryset = Product.objects.all()    
    context = {
        'products' : queryset,
        'saludo' : 'Hola mundo'
    }
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        self.model = Product
        self.redirect_field_name = 'login'
        self.context_object_name = 'products'
        self.paginate_by= 3
        self.template_name = 'products.html'
        
        return super().get_context_data(**kwargs) 
  

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    

def products_filters(request):
    all_products = Product.objects.order_by('name')
    my_filter = ProductFilter(request.GET, queryset=all_products)
    all_products = my_filter.qs
    context = {
        'all_products': all_products,
        'my_filter' : my_filter
    }
    return render(request,'filter.html', context)


class ProductsViews(TemplateView):
    def get_template_names(self) -> list[str]:
        return super().get_template_names() 