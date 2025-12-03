from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django import forms
from cities.models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

@staff_member_required
def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cities/city_added.html', {'city': form.instance})
    else:
        form = CityForm()
    return render(request, 'cities/add_city.html', {'form': form})

urlpatterns = [
    path('add/', add_city, name='add_city'),
]
