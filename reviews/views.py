from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .models import Reviews
from .forms import ReviewForm
from Products.models import Product

# Create your views here.

class ListReviews(ListView):
    
    model = Reviews
    context_object_name = 'reviews'
    template_name = 'reviews.html'

def add_review(request : HttpRequest, pk):
    product = Product.objects.get(id=pk)
    comment = request.POST.get('comment')
    stars = request.POST.get('stars')
    user = request.user
    new_review = Reviews(
        product=product,
        comment=comment,
        stars=stars,
        user=user
    )
    new_review.save()
    return redirect('product:detail_product', product.slug)

