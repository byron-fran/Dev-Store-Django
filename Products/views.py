#import a list view
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView,FormView, TemplateView
from .models import Product
from .forms import ProductFilterForm
from .models import Mark

class ProductsListView(TemplateView):
    
    model = Product
    template_name = 'products.html'
 
    
    def get_queryset(self) -> QuerySet[Any]:
        return Product.objects.get_all_products()
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['all_products'] = Product.objects.get_all_products()
            context['form'] = ProductFilterForm()
            context['marks'] = Mark.objects.all()
            return context
    
    
    def get(self, request: HttpRequest) -> HttpResponse:
        q =  request.GET.get('q')
        mark = request.GET.get('mark')
        category = request.GET.get('category')

        if q:
            products = Product.objects.products_search(q)
            return render(request, self.template_name,{'all_products':  products})
        return render(request, self.template_name,{'all_products': Product.objects.get_all_products()})
        

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    


