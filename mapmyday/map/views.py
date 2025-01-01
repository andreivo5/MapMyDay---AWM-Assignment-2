from django.shortcuts import render, redirect
from django.contrib.gis.geos import Point
from authentication.models import Profile

def map_view(request):
    # checking if user is authenticated
    if not request.user.is_authenticated:
        return redirect('authentication:login')

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('profile_setup')

    # default location if the user's location is not set
    if profile.location is None:
        user_location = (53.3498, -6.2603)  # Dublin coordinates
    else:
        user_location = (profile.location.y, profile.location.x)

    # passing user's location to the map template
    return render(request, 'map.html', {
        'user_latitude': user_location[0],
        'user_longitude': user_location[1],
    })
