from django.contrib import admin
from django.urls import path, include
from appauth.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('login', login, name="login"),
    path('profile', profile, name="profile"),
    path('', include('social_django.urls')),
    path('logout', logout_user, name="logout"),

]