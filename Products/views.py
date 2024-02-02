#import a list view
from typing import Any
from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Product
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ProductFilter
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ProductsListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'all_products'
    paginate_by = 3

    def get_queryset(self):
          queryset = Product.objects.order_by('name')
          all_filters = ProductFilter(self.request.GET, queryset=queryset)
          filtered_products = all_filters.qs
          return filtered_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_filters = ProductFilter(self.request.GET, queryset=self.get_queryset())

        try:
            paginated_data = self.paginate_queryset(all_filters.qs, self.paginate_by)
            context['page_obj'] = paginated_data[0]
            context['has_previous'] = paginated_data[1].has_previous()
            context['next_page_number'] = paginated_data[1].next_page_number() if paginated_data[1].has_next() else None
            context['num_pages'] = paginated_data[1].paginator.num_pages
            context['total_pages'] = paginated_data[1].paginator.page_range
            context['filters'] = all_filters
            print(context['has_previous'])
     
        except PageNotAnInteger:
            paginated_data = self.paginate_queryset(all_filters.qs, 1)
            context['page_obj'] = paginated_data[0]
            context['has_previous'] = paginated_data[1].has_previous()
            context['next_page_number'] = paginated_data[1].next_page_number() if paginated_data[1].has_next() else None
            context['num_pages'] = paginated_data[1].paginator.num_pages
            context['filters'] = all_filters
        except EmptyPage:
            paginated_data = self.paginate_queryset(all_filters.qs, self.paginate_by)
            context['page_obj'] = paginated_data[0]
            context['has_previous'] = paginated_data[1].has_previous()
            context['next_page_number'] = paginated_data[1].next_page_number() if paginated_data[1].has_next() else None
            context['num_pages'] = paginated_data[1].paginator.num_pages
            context['filters'] = all_filters
        context['paginator'] = paginated_data[1]  # Añade el paginator al contexto

        return context

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    


