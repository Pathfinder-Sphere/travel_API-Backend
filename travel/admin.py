from django.contrib import admin
from .models import Flights, Airline, Booking
from unfold.admin import ModelAdmin

@admin.register(Flights)
class FlightsAdmin(ModelAdmin):
    list_display = ['flight_number', 'airline', 'location', 'destination', 'departure_time', 'arrival_time', 'total_seats', 'available_seats', 'price']
    search_fields = ['location', 'destination', 'flight_number']
    list_filter = ['location', 'destination', 'airline']

@admin.register(Airline)
class AirlineAdmin(ModelAdmin):
    list_display = ['name', 'picture']
    list_filter = ['name']


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ['passenger', 'flight', 'booked_at', 'seats_booked']
    search_fields = ['passenger__user__username', 'flight__location', 'flight__destination']

# admin.site.register(Flights, FlightsAdmin)
# admin.site.register(Booking, BookingAdmin)
# admin.site.register(Airline, AirlineAdmin)
