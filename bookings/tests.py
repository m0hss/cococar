from django.test import TestCase
from django.contrib.auth.models import User
from models.car_model import City
from models.car_model import Car
from ..models.booking_model import Booking
from datetime import date
from django.db import IntegrityError

class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass12345')
        self.owner = User.objects.create_user(username='bob', password='pass12345')
        self.dep = City.objects.create(name='A City')
        self.arr = City.objects.create(name='B City')
        self.car = Car.objects.create(owner=self.owner, make='Sedan', seats=4,
                                      departure_city=self.dep, arrival_city=self.arr,
                                      departure_date=date(2025, 12, 25))

    def test_unique_booking_per_day(self):
        Booking.objects.create(user=self.user, car=self.car, date=self.car.departure_date)
        with self.assertRaises(IntegrityError):
            Booking.objects.create(user=self.user, car=self.car, date=self.car.departure_date)
