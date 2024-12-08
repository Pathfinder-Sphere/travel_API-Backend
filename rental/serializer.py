from rest_framework import serializers
from .models import Rental, Car, CarType, CarImageFile

class CarImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImageFile
        fields = '__all__'

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    images = CarImageFileSerializer()
    type = CarTypeSerializer()

    class Meta:
        model = Car
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = Rental
        fields = '__all__'