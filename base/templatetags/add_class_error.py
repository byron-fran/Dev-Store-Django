from django import template
from django.forms.utils import ErrorDict,ErrorList
register =  template.Library()

@register.filter
def add_class_error(field : ErrorDict):
    
    errors : ErrorList = []
    errors = field.get('new_password2')
    errors.data[0] = 'The two password fields did not match.'
  
    return errors.data[0]