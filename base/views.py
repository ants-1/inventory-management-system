from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def navbar(request):
    return render(request, 'navbar.html')