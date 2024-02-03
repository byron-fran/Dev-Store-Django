from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 
from .forms import CustomAuthLogin
urlpatterns = [
    path('signup/',views.RegisterView.as_view() , name='account_signup'),
    path('logout/', views.logout_view, name='account_logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthLogin), name='account_login'),
   
]