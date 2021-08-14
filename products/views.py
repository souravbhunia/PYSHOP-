from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Product
def index(request):
    products=Product.objects.all()
    return  render(request,'index.html',
                   {'products':products})