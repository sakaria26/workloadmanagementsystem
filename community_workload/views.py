from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_community_workloads(request):
    return HttpResponse("<h1> Community Workloads </h1>")
