from django.http import HttpResponse
from django.shortcuts import render
from Products.models import Product



def home(request):
    products_offer = Product.objects.filter(descount = 5)
    context = {
        'products_offer' : products_offer
    }
    return render(request, 'home.html', context)