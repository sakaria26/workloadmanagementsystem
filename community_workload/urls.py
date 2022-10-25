from django.contrib import admin
from django.urls import path, include
from community_workload.views import *

urlpatterns = [
    path('', all_community_workloads, name="community_load"),
]