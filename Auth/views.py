from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import UserForm, LoginForm
from .models import User
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
    
# login view
class LoginView(UserPassesTestMixin,FormView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm
    login_url = reverse_lazy('product:list_products')
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Si el inicio de sesión no es válido, redirige a la página de inicio de sesión
            messages.error(self.request, 'Email o contraseña incorrectos.')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('home')


#Logout    
def logout_view(request):
    logout(request)
    return redirect('account_login')
    

class ResetPassword(PasswordResetView):
    template_name = 'passwords/reset_password.html'

class PasswordResetDone(PasswordResetDoneView):    
   template_name = 'passwords/reset_password_done.html' 

class PasswordRestConfirm(PasswordResetConfirmView):
    template_name = 'passwords/password_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'passwords/password_complete.html'    


# Users
class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/accounts/profile/'
    
    def get_context_data(self, **kwargs: reverse_lazy): # type: ignore
        
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.request.user.id)
        context['user'] = user  
        return context
    
    def dispatch(self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy): # type: ignore
        user_id =self.kwargs['pk']
        if int(user_id) != self.request.user.id:
            return redirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return f'{self.success_url}{self.request.user.id}?ok=1'
        