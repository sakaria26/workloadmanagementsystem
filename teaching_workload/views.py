from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_teaching_workloads(request):
    return HttpResponse("<h1> Teaching Load </h1>")