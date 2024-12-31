from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point

# Create your models here.

#Store a point location on a user's profile.
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)

    def __str__(self):

        return self.user.username
    
    # update a user's profile to include a location point.
    def set_user_location(user_id, latitude, longitude):
        user = User.objects.get(id=user_id)
        location = Point(longitude, latitude)  # Point takes (longitude, latitude)

        # Create or update the user's profile
        profile, created = Profile.objects.get_or_create(user=user)
        profile.location = location
        profile.save()

        return profile