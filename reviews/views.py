from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .models import Reviews
from .forms import ReviewForm
from Products.models import Product
from .models import Reviews

# Create your views here.


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