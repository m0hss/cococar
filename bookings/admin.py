from django.contrib import admin
from bookings.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('user__username', 'car_brand')
