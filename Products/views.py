#import a list view
from django.views.generic import ListView, DetailView
from .models import Product
from django.shortcuts import get_list_or_404, redirect

class ProducstListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by= 3
    template_name = 'products.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    
