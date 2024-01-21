from django.urls import path, include

from . import views 

urlpatterns = [
    path('register/',views.RegisterView.as_view() , name='register'),
    path('login/', views.LoginViewUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
  
   
]