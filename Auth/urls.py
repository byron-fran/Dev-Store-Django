from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 
from .forms import CustomAuthLogin

urlpatterns = [
    path('signup/',views.RegisterView.as_view() , name='account_signup'),
    path('logout/', views.logout_view, name='account_logout'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthLogin), name='account_login'),
    path('password_reset/',views.ResetPassword.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordRestConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
   
]