from django import template
from Products.models import Product
from Auth.models import User
from reviews.models import Reviews
register = template.Library()

@register.filter_function
def verify_user_review(user : User, product : Product):
    reviews = Reviews.objects.filter(product=product)
  
    if len(reviews):
        try:
            user_found = reviews.get(user=user)
            if user_found:
                
                return False
            else:
                return True
        except:
            return True    
    else:
        
        return True      
    