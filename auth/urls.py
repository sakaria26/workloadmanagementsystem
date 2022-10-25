from django.contrib import admin
from django.urls import path, include
from auth.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('login', login, name="login")
]