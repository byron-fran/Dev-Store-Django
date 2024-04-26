from django.urls import path
from . import views
from .models import Product

app_name ='product'

urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='list_products'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='detail_product'),
]


