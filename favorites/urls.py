from django.urls import path
from . import views

app_name='favorites'

urlpatterns = [
    path('add/<str:id>/<str:page>/', views.add_favorite, name='add'),
    path('remove/<str:pk>/<str:page>/', views.remove_Favorite, name='remove'),
    path('list/', views.ListFavorite.as_view(), name='list'),
    path('remove_from_list/<str:pk>/', views.remove_Favorite_from_list, name='remove_from_list')
]
