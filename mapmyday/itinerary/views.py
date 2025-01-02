from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Itinerary
import json

@login_required
def itinerary_view(request):
    itinerary_items = Itinerary.objects.filter(user=request.user)
    data = [{
        "name": item.name,
        "latitude": item.latitude,
        "longitude": item.longitude,
        "date": item.date.strftime('%Y-%m-%d'),
        "time": item.time.strftime('%H:%M'),
    } for item in itinerary_items]
    
    return render(request, 'itinerary.html', {'itinerary': json.dumps(data)})


@csrf_exempt
@login_required
def add_to_itinerary(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        itinerary = Itinerary.objects.create(
            user=request.user,
            name=data.get('name'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            type=data.get('type'),
            address=data.get('address'),
            website=data.get('website'),
            phone=data.get('phone'),
            email=data.get('email'),
            opening_hours=data.get('openingHours'),
            date=data.get('date'),
            time=data.get('time'),
        )
        return JsonResponse({'success': True, 'id': itinerary.id})

    return JsonResponse({'error': 'Invalid request'}, status=400)
