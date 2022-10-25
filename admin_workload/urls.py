from django.contrib import admin
from django.urls import path, include
from admin_workload.views import *

urlpatterns = [
    path('', all_admin_workloads, name="admin_load"),
]