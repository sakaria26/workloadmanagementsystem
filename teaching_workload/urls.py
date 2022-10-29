from django.contrib import admin
from django.urls import path, include
from teaching_workload.views import *

urlpatterns = [
    path('', all_teaching_workloads, name="teaching_load"),
    path('add_teaching_load', add_teaching_workloads, name="add_teaching_load"),
]
