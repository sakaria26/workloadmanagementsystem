from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1> Hello, World </h1>")

def login(request):
    return HttpResponse("<h1> Login </h1>")