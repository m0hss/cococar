from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'seats', 'departure_city', 'arrival_city', 'departure_date']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'})
        }
