from django.contrib.auth.models import User
from django.db import models

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField() 
    type = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.date} {self.time})"
