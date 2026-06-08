from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Sold', 'Sold'),
    ]

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=100)

    brand = models.CharField(max_length=50)

    model = models.CharField(max_length=50)

    year = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    kilometers = models.IntegerField()

    fuel_type = models.CharField(max_length=20)

    location = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(
        upload_to='vehicles/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return self.title


class Inquiry(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer_inquiries'
    )

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='seller_inquiries'
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.buyer.username} -> {self.vehicle.title}"


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.title}"
class VehicleImage(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='vehicle_gallery/'
    )

    def __str__(self):
        return self.vehicle.title
class Review(models.Model):

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_received'
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews_given'
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.seller.username} - {self.rating}"

