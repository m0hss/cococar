from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from datetime import datetime
from cars.models import Car
from bookings.models import Booking


@login_required
def create_booking(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    date = request.GET.get('date') or request.POST.get('date')

    # Convert date to YYYY-MM-DD format if needed
    if date:
        try:
            # Try parsing common formats
            for fmt in ['%b. %d, %Y', '%B %d, %Y', '%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                    parsed_date = datetime.strptime(date, fmt)
                    date = parsed_date.strftime('%Y-%m-%d')
                    break
                except ValueError:
                    continue
        except Exception:
            pass  # If all formats fail, let Django handle the error

    if request.method == 'POST':
        try:
            booking = Booking.objects.create(
                user=request.user, car=car, date=date)
            return redirect('booking_detail', pk=booking.pk)
        except IntegrityError:
            return render(request, 'bookings/booking_conflict.html', {'car': car, 'date': date})
    return render(request, 'bookings/create_booking.html', {'car': car, 'date': date})


@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})


@login_required
def calendar(request):
    my_bookings = Booking.objects.filter(user=request.user).order_by('date')
    on_my_cars = Booking.objects.filter(
        car__owner=request.user).order_by('date')
    # function group by date

    def group_by_date(qs):
        grouped = {}
        for b in qs:
            grouped.setdefault(b.date, []).append(b)
        return grouped
    return render(request, 'bookings/calendar.html', {
        'my_bookings': group_by_date(my_bookings),
        'on_my_cars': group_by_date(on_my_cars),
    })


@login_required
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    # Only allow if user made the booking or owns the car
    if booking.user == request.user or booking.car.owner == request.user:
        if request.method == 'POST':
            booking.delete()
            return redirect('calendar')
        return render(request, 'bookings/confirm_delete.html', {'booking': booking})
    return HttpResponseForbidden('You do not have permission to delete this booking.')
