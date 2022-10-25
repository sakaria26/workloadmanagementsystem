from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def all_research_workloads(request):
    return HttpResponse("<h1> Research Workloads </h1>")
