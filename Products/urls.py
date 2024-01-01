from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProducstListView.as_view(), name='products'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
]
