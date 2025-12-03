from django.urls import path
from .views import create_booking, booking_detail, calendar, delete_booking

urlpatterns = [
    path('create/<int:car_id>/', create_booking, name='create_booking'),
    path('detail/<int:pk>/', booking_detail, name='booking_detail'),
    path('calendar/', calendar, name='calendar'),
    path('delete/<int:pk>/', delete_booking, name='delete_booking'),
]
