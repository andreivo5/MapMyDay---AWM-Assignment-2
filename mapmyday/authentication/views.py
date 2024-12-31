from django.shortcuts import render, redirect
import json
from .models import Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.contrib.gis.db.models.functions import Distance
from django.urls import reverse
from django.shortcuts import redirect


#login & logout views
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('map:index'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('authentication:login')

from django.contrib.gis.geos import Point

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            if latitude and longitude:
                location = Point(float(longitude), float(latitude))
                Profile.objects.create(user=user, location=location)
            else:
                Profile.objects.create(user=user)
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('map:index'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})