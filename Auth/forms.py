from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',       
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'pedro@pedro.com'} ))

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
       
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Write your name'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email  

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido. 254 caracteres como maximo y debe ser valido')
    class Meta:
        model = User
        fields = ['email'] 
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya se encuentra registrado')
        return email           
        

class CustomAuthLogin(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
