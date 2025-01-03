from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import MediaCloudinaryStorage


# Model for an agent handling property listings.
class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(storage=MediaCloudinaryStorage())
    bio = models.TextField()

    def __str__(self):
        return self.name

# Model for location
class Location(models.Model):
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.province}, {self.country}" if self.province else f"{self.city}, {self.country}"

# Model for a property
class Property(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False,default="Unnamed Property")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_sqm = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='properties', null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    space_in_sqm = models.IntegerField(null=True)
    property_type = models.CharField(
        max_length=100,
        choices=[
            ('Apartment', 'Apartment'),
            ('House','House'),
            ('Villa','Villa'),
        ]
    )
    furnished_status = models.CharField(
        max_length=50,
        choices=[
            ('Unfurnished','Unfurnished'),
            ('Partially Furnished','Partially Furnished'),
            ('Fully Furnished','Fully Furnished')
        ]
    )
    kitchen_type = models.CharField(
        max_length=100,
        choices=[
            ('Standard', 'Standard'),
            ('Gourmet', 'Gourmet'),
            ('Open', 'Open')
        ]
    )
    flooring_type = models.CharField(
        max_length=50,
        choices=[
            ('Hardwood', 'Hardwood'),
            ('Carpet', 'Carpet'),
            ('Tile', 'Tile')
        ]
    )
    heating_type = models.CharField(
        max_length=50,
        choices=[('Central', 'Central'), ('Radiant', 'Radiant')]
    )
    view = models.CharField(
        max_length=100,
        choices=[('Ocean', 'Ocean'), ('Mountain', 'Mountain'), ('City', 'City')]
    )
    security_system = models.BooleanField(default=False)
    garage = models.IntegerField(null=True)
    swimming_pool = models.BooleanField(default=False)
    accessibility_features = models.BooleanField(default=False)
    agent = models.ForeignKey(
        'Agent',
        related_name='properties',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Model for property images
class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        related_name='images',
        on_delete=models.CASCADE
    )

    image = models.ImageField(storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"Image for {self.property.title}"

# Model for testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    property = models.ForeignKey(
        Property,
        related_name='testimonials',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial by {self.name} for {self.property.title}"

# Model for customer forms to agents
class Contact(models.Model):
    property = models.ForeignKey(
        Property,
        related_name='contacts',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} about {self.property.title}"