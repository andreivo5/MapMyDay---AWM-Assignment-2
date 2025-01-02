from django.urls import path
from . import views

app_name = 'itinerary'

urlpatterns = [
    path('', views.itinerary_view, name='itinerary'),
    path('add/', views.add_to_itinerary, name='add_to_itinerary'),
]