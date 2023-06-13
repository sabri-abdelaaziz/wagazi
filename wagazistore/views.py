from django.shortcuts import render
import pyodbc
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Product
# Create your views here.





def create(request):
    
    return redirect("index")

def index(request):
    return render(request,"index.html")

def registre(request):
    return render(request,"registre.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render(request,"cart.html")

def shop(request):
    products = Product.objects.all()
    return render(request,"shop.html",{'products': products})


