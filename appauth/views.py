from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from decouple import config
import json
# Create your views here.
def home_view(request):
    return render(request, 'appauth/home.html', {})

def login(request):
    return HttpResponse("<h1> Login </h1>")

def profile(request):
    user = request.user
    auth0_user = user.social_auth.get(provider='auth0')
    user_data = {
        'user_id': auth0_user.uid,
        'name': user.first_name,
        'picture': auth0_user.extra_data['picture'],
    }
    context = {'user_data': json.dumps(user_data, indent=4), 'auth0_user': auth0_user}
    return render(request, 'appauth/profile.html', context)

def logout_user(request):
    logout(request)
    domain = config('APP_DOMAIN')
    client_id = config('APP_CLIENT_ID')
    return_to = 'http://127.0.0.1:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')