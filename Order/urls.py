from django.urls import path
from .views import add_to_cart
urlpatterns = [
    path('add/<int:pk>/', add_to_cart, name='add')
]
