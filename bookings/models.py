from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        constraints = [
            models.UniqueConstraint(fields=['car', 'date'], name='unique_car_booking_per_day')
        ]

    def __str__(self):
        return f"{self.user.username} booked {self.car} on {self.date}"
