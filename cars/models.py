from django.db import models
from django.contrib.auth.models import User
from cities.models import City

class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    seats = models.PositiveIntegerField(default=4)
    # trip info for a one-day trip
    departure_city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='departures')
    arrival_city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='arrivals')
    departure_date = models.DateField()

    class Meta:
        ordering = ['departure_date']
        constraints = [
            models.UniqueConstraint(fields=['id', 'departure_date'], name='car_unique_trip_per_day')
        ]

    def __str__(self):
        return f"{self.brand} by {self.owner.username} ({self.departure_city} -> {self.arrival_city} on {self.departure_date})"
