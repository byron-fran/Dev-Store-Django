#import a list view
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
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
    
    def post(self, request, *args, **kwargs):
        form = ProductFilterForm(request.POST)
        if form.is_valid():
            print(request.POST)
            # Tu lógica de filtrado aquí
            # Actualiza context['product_list'] con los resultados filtrados
            # Puedes utilizar form.cleaned_data para obtener los datos del formulario
            pass
        else:
            # El formulario no es válido, puedes manejar los errores aquí
            pass

        return render(request, self.template_name, {'form': form, 'all_products': Product.objects.get_all_products()})


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    


