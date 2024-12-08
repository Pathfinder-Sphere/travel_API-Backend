from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    class ROLE(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'
        CUSTOMER_SUPPORT = 'CUSTOMER_SUPPORT', 'Customer Support'
    role = models.CharField(max_length=20, choices=ROLE.choices, default=ROLE.USER)
    phone_number = models.CharField(max_length=15, unique=True)
    # person_id = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_user_set", blank=True)


    class Meta:
        permissions = [
            ("view_flights_and_airlines", "Can view flights and airlines"),
            ("book_flights_and_buy_tickets", "Can book flights and buy tickets"),
            ("view_hotel_and_lodging_prices", "can see hotels and lodging prices"),
            ("manage_staff", "can manage staff"),
            ("view_transport_and_transport_fair", "can see available transport and price"),
            ("view_payments", "can see payments made"),
            ("manage_payments", "can manage payments"),
            ("view_holiday_plans", "can view holiday plans"),
            ("manage_holiday_plans", "can manage holiday plans"),
            ("manage_user", "can manage user")
        ]

    def __str__(self):
        return self.username
    




