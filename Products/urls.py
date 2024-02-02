from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('product/<str:pk>/', views.ProductDetailView.as_view(), name='product'),

]
