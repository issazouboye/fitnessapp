from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "authentication/index.html")

def signin(request):
    return render(request, "authentication/signin.html")

def kcalcounter(request):
    return render(request, "authentication/kcalcounter.html")

def signup(request):
    return render(request, "authentication/signup.html")

    
