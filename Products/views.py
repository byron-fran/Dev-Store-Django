from typing import Any
from django.db.models.base import Model as Model
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Product
from .filters import ProductFilter

class ProductsListView(ListView):

    model = Product
    template_name = "products.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        
        super().get_context_data(**kwargs)
        
        q = self.request.GET.get("q")
        f = ProductFilter(self.request.GET, queryset=Product.objects.all())
        
        if q:
            products = Product.objects.products_search(q)
            return {'all_products':  products, 'form' : f.form}
        else:
            return { 'all_products' : f.qs,'form' : f.form}

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product.html"

