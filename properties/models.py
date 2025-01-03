from django.db import models

# Create your models here.
class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"

class Property(models.Model):
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='properties')

    def __str__(self):
        return f"{self.address} - {self.location.city}, {self.location.country}"
