from django.contrib import admin
from django.urls import path, include
from research_workload.views import *

urlpatterns = [
    path('', all_research_workloads, name="research_load"),
]