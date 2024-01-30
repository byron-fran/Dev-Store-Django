#import a list view
from typing import Any
from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Product
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ProductFilter
from django.shortcuts import render


class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'all_products'
    

    def get_queryset(self):
        queryset = Product.objects.order_by('name')
        all_filters = ProductFilter(self.request.GET, queryset=queryset)
        self.all_products = all_filters.qs
        return self.all_products

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        queryset = Product.objects.order_by('name')
        all_filters = ProductFilter(self.request.GET, queryset=queryset)
        self.all_products = all_filters.qs
        all_filters = ProductFilter(self.request.GET, queryset=self.all_products)
        self.paginate_by = 3
        context = {
            'all_products' : self.all_products,
            'filters' : all_filters
        }
        return context


  

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

