from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UserForm
# Create your views here.


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserForm
    fields = ['__all__']
    redirect_authenticated_user = True
    success_url = reverse_lazy('products')
   
    def form_valid(self, form):
        user  = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
  
  
#Login 
class LoginViewUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('products')
    
    # def form_valid(self, form):
    #     response = super().form_invalid(form)
    #     if self.request.user.is_authenticated:
    #         return  self.get_success_url()
    #     return response


#Logout    
def logout_view(request):
    logout(request)
    return redirect('login')
    
  
    
    
      
    
