# Carpool Mini-Platform

A simple Django app to manage one-day carpool trips and bookings.

## Setup

```bash
# Activate the virtual environment
source bin/activate

# Make migrations and migrate
python manage.py makemigrations cities cars bookings
python manage.py migrate

# Create a superuser (for adding cities)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

## Features
- User signup/login/logout
- Admin-only City management
- Add a car with departure/arrival cities and date
- Search available cars by city and date
- Booking system with per-car-per-day uniqueness
- User calendars: bookings made by the user and bookings on the user's cars

## Tests (minimal)
Run:
```bash
python manage.py test
```
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
