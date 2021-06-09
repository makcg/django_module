from django.shortcuts import render
# from models import *


def home(request):
    # product1()
    return render(request, 'product/home.html')


def contacts(request):
    return render(request, 'product/contacts.html')


def basket(request):
    return render(request, 'product/basket.html')


def login(request):
    return render(request, 'product/login.html')


def product1(request):
    return render(request, 'product/product1.html')


def card(request):
    return render(request, 'product/card.html')


def checkout(request):
    return render(request, 'product/checkout.html')
