from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    products = Product.objects.all()
    n = len(products)
    nslide = n//4 + ceil((n/4)-(n//4))

    params = {'product': products, 'nslide': nslide, 'range': range(nslide)}

    print(products)
    return render(request, 'shop/index1.html', params)


def about(request):
    return render(request, 'shop/about1.html')


def contact(request):
    return render(request, 'shop/contact1.html')


def tracker(request):
    return render(request, 'shop/tracker1.html')


def search(request):
    return render(request, 'shop/search1.html')


def productview(request):
    return render(request, 'shop/productview.html')


def checkout(request):
    return render(request, 'shop/checkout1.html')
