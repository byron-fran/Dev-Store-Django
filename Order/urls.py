from django.urls import path
from .views import add_to_cart, ListOrdersView, remove_from_cart

urlpatterns = [
    path('cart/', ListOrdersView.as_view(), name='cart'),
    path('cart/add/<str:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<str:pk>', remove_from_cart, name='remove_from_cart')
   
]
