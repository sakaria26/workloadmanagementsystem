from django.contrib import admin
from django.urls import path, include
from community_workload.views import *

urlpatterns = [
    path('', all_community_workloads, name="community_load"),
    path('add_community_load', add_community_workload, name="add_community_load"),
]