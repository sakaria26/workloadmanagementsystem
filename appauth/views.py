from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .models import *
from teaching_workload.models import *
from community_workload.models import *
from admin_workload.models import *
from research_workload.models import *


# Create your views here.
def home_view(request):

    return render(request, 'appauth/home.html')

def login_user(request):
    user = None
    staff_member = None
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Incorrect Username or Password")

        user = authenticate(request, username=username, password=password)
        staff_member = Staff_Member.objects.get(staff=user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                print('The user ', user)
                messages.error(request, "Account is disabled")
        else:
            messages.error(request, "Username or Password Does Not Exist")

    context = {'user': user, 'staff_member': staff_member}
    return render(request, "appauth/login.html", context)

@login_required(login_url='login')
def profile(request):
    user = request.user
    staff_member = Staff_Member.objects.get(staff=user)
    context = {'user': user, 'staff_member': staff_member}
    return render(request, 'appauth/profile.html', context)

def logout_user(request):
    logout(request)
    return redirect("login")