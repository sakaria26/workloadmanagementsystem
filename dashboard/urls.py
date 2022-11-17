from django.urls import path
from .views import *
urlpatterns = [
    path('', workload_summary, name="dashboard"),
]