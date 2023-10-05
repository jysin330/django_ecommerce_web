from django.shortcuts import render
from .models import Product, Contact
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
    if (request.method == "POST"):
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('contact', '')
        desc = request.POST.get('desc', '')
        print(name, phone, email, desc)
        contact = Contact(name=name, email=email, contact=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact1.html')


def tracker(request):
    return render(request, 'shop/tracker1.html')


def search(request):
    return render(request, 'shop/search1.html')


def productview(request, myid):

    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productview1.html', {'product': product[0]})


def checkout(request):
    return render(request, 'shop/checkout1.html')
