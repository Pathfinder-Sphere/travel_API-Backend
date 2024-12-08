from django.db import models

class CarImageFile(models.Model):
    image = models.ImageField(upload_to='car_images/')

class CarType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='car_images/')
    images = models.ForeignKey(CarImageFile, on_delete=models.CASCADE)
    type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=50)
    has_gps = models.BooleanField(default=False)
    has_ac = models.BooleanField(default=False)
    has_radio = models.BooleanField(default=False)
    has_bluetooth = models.BooleanField(default=False)
    has_usb = models.BooleanField(default=False)
    condition = models.CharField(max_length=50)

class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


