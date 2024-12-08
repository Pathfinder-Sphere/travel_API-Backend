# Generated by Django 5.1.3 on 2024-12-07 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customuser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Airline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("picture", models.ImageField(upload_to="airline_images/")),
            ],
        ),
        migrations.CreateModel(
            name="FlightImageFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="flight_images/")),
            ],
        ),
        migrations.CreateModel(
            name="Flights",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flight_number", models.CharField(max_length=10, unique=True)),
                ("location", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                ("total_seats", models.PositiveIntegerField()),
                ("available_seats", models.PositiveIntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image", models.ImageField(upload_to="flight_images/")),
                (
                    "airline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="travel.airline"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("booked_at", models.DateTimeField(auto_now_add=True)),
                ("seats_booked", models.PositiveIntegerField()),
                (
                    "passenger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customuser.customuser",
                    ),
                ),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="travel.flights"
                    ),
                ),
            ],
        ),
    ]