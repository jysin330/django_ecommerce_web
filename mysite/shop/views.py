from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    # products = Product.objects.all()

    # params = {'product': products, 'nslide': nslide, 'range': range(nslide)}
    # allprod = [[products, nslide, range(1, nslide)], [
    #     products, nslide, range(1, nslide)]]
    # params = {'allproduct': allprod}

    allprod = []
    allcats = Product.objects.values('category', 'id')
    cats = {item['category'] for item in allcats}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslide = n//4 + ceil((n/4)-(n//4))
        allprod.append([prod, range(1, nslide), nslide])

    params = {'allproduct': allprod}

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
    return render(request, 'shop/productview1.html')


def checkout(request):
    return render(request, 'shop/checkout1.html')
