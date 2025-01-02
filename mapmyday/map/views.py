from django.shortcuts import render, redirect
from django.contrib.gis.geos import Point
from authentication.models import Profile

def map_view(request):
    # checking if user is authenticated
    if not request.user.is_authenticated:
        return redirect('authentication:login')
    return render(request, 'map.html', {
    })
