from .models import Flights, Booking, Airline, FlightImageFile
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['passenger', 'flight', 'seats_booked', 'booked_at']
        
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class FlightImageFileSerializer(serializers.ModelSerializer):
    class meta:
        model: FlightImageFile
        fields = ('image')

class CreateBookSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='id', queryset=Booking.objects.all())
    flight = serializers.SlugRelatedField(slug_field='destination', queryset=Flights.objects.all())

    class Meta:
        model = Booking
        fields = ['cart', 'product', 'quantity']

    def create(self, validated_data):
        return Booking.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance