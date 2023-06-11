from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def registre(request):
    return render(request,"registre.html")

def about(request):
    return render(request,"about.html")

def cart(request):
    return render(request,"cart.html")

def contact(request):
    return render(request,"contact.html")

def shop(request):
    return render(request,"shop.html")
