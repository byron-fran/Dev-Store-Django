from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from .forms import UserForm, UserFormLogin
# Create your views here.

#register view
class RegisterView(UserPassesTestMixin, FormView):
    template_name = 'register.html'
    form_class = UserForm
    redirect_authenticated_user = True
    login_url = reverse_lazy('products')  # Redirige a 'products' si el usuario está autenticado

    def test_func(self):
        # Esta función determina si el usuario debe tener acceso a la vista.
        # Devuelve True si el usuario no está autenticado.
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('products')
#Login 
class LoginViewUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('products')
    


#Logout    
def logout_view(request):
    logout(request)
    return redirect('login')
    
  
    
    
      
    
