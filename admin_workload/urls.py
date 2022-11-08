from django.contrib import admin
from django.urls import path, include
from admin_workload.views import *

urlpatterns = [
    path('', all_admin_workloads, name="admin_load"),
    path('add/', add_admin_workload, name="add_admin_load"),
    path('edit/<str:pk>', edit_admin_workload, name="edit_admin_load"),
]