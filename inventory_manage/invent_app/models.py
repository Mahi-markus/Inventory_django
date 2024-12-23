from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Function that returns the default Location
def get_default_location():
    # Replace this with logic to return a valid Location instance
    return Location.objects.first() 

class Location(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    center = models.PointField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    location_type = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    state_abbr = models.CharField(max_length=3, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Accommodation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    feed = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    bedroom_count = models.PositiveIntegerField()
    review_score = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    usd_rate = models.DecimalField(max_digits=10, decimal_places=2)
    center = models.PointField(null=True, blank=True)
    images = models.JSONField(default=list)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=get_default_location)
    amenities = models.JSONField(default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class LocalizeAccommodation(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    language = models.CharField(max_length=2)
    description = models.TextField()
    policy = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.property.title} - {self.language}"
