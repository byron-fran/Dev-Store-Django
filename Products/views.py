#import a list view
from django.views.generic import ListView, DetailView
from .models import Product
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ProductFilter
from django.shortcuts import render

class ProducstListView(ListView):
    model = Product
    redirect_field_name = 'login'
    context_object_name = 'products'
    paginate_by= 3
    filter = ['name']
    template_name = 'products.html'


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