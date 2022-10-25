from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_admin_workloads(request):
    return HttpResponse("<h1> Admin Workload </h1>")