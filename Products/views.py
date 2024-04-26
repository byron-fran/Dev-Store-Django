from typing import Any
from django.core.paginator import Paginator
from django.db.models.base import Model as Model
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Product
from .filters import ProductFilter

class ProductsListView(ListView):
    model = Product
    template_name = "products.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
      
        q = self.request.GET.get("q")
        mark = self.request.GET.get("mark")
        category = self.request.GET.get("category")
        page_number : str = '1'
        if self.request.GET.get("page") is not None:
            page_number = self.request.GET.get("page")

        f = ProductFilter(self.request.GET, queryset=Product.objects.all())
        
        context['form'] = f.form
        context['page_number'] = page_number
    
        
        if q:
            products = Product.objects.products_search(q)
            paginator = Paginator(products, 9)
            page_obj = paginator.get_page(page_number)
            products_per_page = page_obj.object_list
            context['p'] = paginator
            context['page_obj'] =  page_obj
            context['products'] = products_per_page
            
        elif mark is not None or category is not None:
            paginator = Paginator(f.qs, 9)
            page_obj = paginator.get_page(page_number)
            products_per_page = page_obj.object_list
            context['p'] = paginator
            context['page_obj'] =  page_obj
            context['products'] = products_per_page
       
        else:
            paginator = Paginator(Product.objects.all(), 9)
            page_obj = paginator.get_page(page_number)
            products_per_page = page_obj.object_list
            context['p'] = paginator
            context['page_obj'] =  page_obj
            context['products'] = products_per_page
            
        return context    

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product.html"
