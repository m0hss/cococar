from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from cars.models import Car
from cities.models import City
from .forms import CarForm

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            # return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    
    # Get user's existing cars
    user_cars = Car.objects.filter(owner=request.user).order_by('-departure_date')
    
    return render(request, 'cars/add_car.html', {'form': form, 'user_cars': user_cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})


def search(request):
    qs = Car.objects.all()
    departure_city_id = request.GET.get('departure_city')
    arrival_city_id = request.GET.get('arrival_city')
    date = request.GET.get('date')
    if departure_city_id:
        qs = qs.filter(departure_city_id=departure_city_id)
    if arrival_city_id:
        qs = qs.filter(arrival_city_id=arrival_city_id)
    if date:
        qs = qs.filter(departure_date=date)
    cities = City.objects.all()
    return render(request, 'cars/search.html', {'cars': qs, 'cities': cities})


@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    # Only allow the owner to delete the car
    if car.owner != request.user:
        return HttpResponseForbidden('You do not have permission to delete this car.')
    
    if request.method == 'POST':
        car.delete()
        return redirect('add_car')
    
    return redirect('add_car')
