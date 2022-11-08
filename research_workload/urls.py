from django.contrib import admin
from django.urls import path, include
from research_workload.views import *

urlpatterns = [
    path('', all_research_workloads, name="research_load"),
    path('add_research_load', add_research_workloads, name="add_research_load"),
    path('edit_research_load/<int:research_load_id>', edit_research_workloads, name="edit_research_load"),
]