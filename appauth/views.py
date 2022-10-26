from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, 'appauth/home.html', {})

def login(request):
    return HttpResponse("<h1> Login </h1>")
