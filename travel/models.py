from django.db import models
from customuser.models import CustomUser

class FlightImageFile(models.Model):
    image = models.ImageField(upload_to='flight_images/')

    def __str__(self):
        return f"Flight Image: {self.image.name}"

class Airline(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='airline_images/')

    def __str__(self):
        return self.name

class Flights(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flight_images/')

    def __str__(self):
        return f"{self.flight_number} - {self.location} to {self.destination}"
    
class FlightImageFile(models.Model):
    image = models.ImageField(upload_to='flight_images/')

class Booking(models.Model):
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    seats_booked = models.PositiveIntegerField()

    def __str__(self):
        return f"Booking by {self.passenger} for flight {self.flight.location} to {self.flight.destination}"
