from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:pk>/', views.add_review, name='add_review'),

]
