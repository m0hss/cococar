from django.contrib import admin
from cars.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'owner', 'departure_city', 'arrival_city', 'departure_date', 'seats')
    list_filter = ('departure_city', 'arrival_city', 'departure_date')
    search_fields = ('brand', 'owner__username')
