from django import template
from Auth.models import User
register = template.Library()

@register.filter
def first_letter(user : User):
    return user.username[0]