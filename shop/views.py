from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request,'shop/index.html')

def search(request):
    return HttpResponse("It is Search Section")

def tracker(request):
    return HttpResponse("It is Tracker Section")
    
def productview(request):
    return HttpResponse("It is Product View Section")

def about(request):
    return HttpResponse("It is About Section")

def checkout(request):
    return HttpResponse("It is Checkout Section")

def contacts(request):
    return HttpResponse("It is Contacts Section")
