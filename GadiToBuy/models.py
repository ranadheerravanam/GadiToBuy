from django.db import models
from django.contrib.auth.models import User
class Vehicle(models.Model):
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kilometers = models.IntegerField()
    fuel_type = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
    upload_to='vehicles/',
    blank=True,
    null=True
    
)

    def __str__(self):
        return self.title