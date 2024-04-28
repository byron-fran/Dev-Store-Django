from django.urls import path
from . import views

app_name='favorites'

urlpatterns = [
    path('add/<str:id>/', views.add_favorite, name='add'),
    path('remove/<str:pk>/', views.remove_Favorite, name='remove'),
    path('list/', views.ListFavorite.as_view(), name='list')
]
