from django.contrib import admin
from django.urls import path, include
from appauth.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('login', login_user, name="login"),
    path('profile', profile, name="profile"),
    path('logout', logout_user, name="logout"),

]