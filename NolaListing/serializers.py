from rest_framework import serializers
from .models import Property, Agent, PropertyImage, Testimonial, Contact, Location

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image']

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'message', 'created_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'created_at']

class AgentSerializer(serializers.ModelSerializer):
    properties = serializers.StringRelatedField(many=True)

    class Meta:
        model = Agent
        fields = [
            'id', 'name', 'email','phone_number', 'profile_picture', 'bio',
            'properties'
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'province', 'country']


class PropertySerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    images = PropertyImageSerializer(many=True)
    testimonials = TestimonialsSerializer(many=True)
    location = LocationSerializer()
    class Meta:
        model = Property
        fields = [
            'id',
            'name',
            'title',
            'description',
            'price',
            'price_per_sqm',
            'address',
            'location',
            'bedrooms',
            'bathrooms',
            'space_in_sqm',
            'property_type',
            'furnished_status',
            'kitchen_type',
            'flooring_type',
            'heating_type',
            'view',
            'security_system',
            'garage',
            'swimming_pool',
            'accessibility_features',
            'agent',
            'testimonials',
            'images'
        ]

        def validate_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Price cannot be negative.")
            return value
