from django import forms
from .models import Mark
class ProductFilterForm(forms.Form):

    mark = forms.CharField(
        label='marks',
        widget=forms.Select(attrs={'class' : 'w-full'},choices=[('python', 'Python'), ('java', 'Java')])
    )
