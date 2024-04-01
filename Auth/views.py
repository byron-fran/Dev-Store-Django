from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomAuthLogin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from .forms import UserForm
from django.contrib.auth.views import (
                                        PasswordResetView, 
                                        PasswordResetDoneView, 
                                        PasswordResetCompleteView,
                                        PasswordResetConfirmView
                                    )

#register view
class RegisterView(UserPassesTestMixin, FormView):
    template_name = 'registration/register.html'
    form_class = UserForm
    redirect_authenticated_user = True
    login_url = reverse_lazy('product:list_products')  # Redirige a 'products' si el usuario está autenticado

    def test_func(self):
  
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('product:list_products')



#Logout    
def logout_view(request):
    logout(request)
    return redirect('account_login')
    

class ResetPassword(PasswordResetView):
    template_name = 'reset_password.html'

class PasswordResetDone(PasswordResetDoneView):    
   template_name = 'reset_password_done.html' 

class PasswordRestConfirm(PasswordResetConfirmView):
    template_name = 'password_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'password_complete.html'    

    
