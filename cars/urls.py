from django.urls import path
from .views import add_car, car_detail, search, delete_car

urlpatterns = [
    path('add/', add_car, name='add_car'),
    path('<int:pk>/', car_detail, name='car_detail'),
    path('<int:pk>/delete/', delete_car, name='delete_car'),
    path('search/', search, name='search_cars'),
]
