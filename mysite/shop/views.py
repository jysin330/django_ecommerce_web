from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shop/index1.html')


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
