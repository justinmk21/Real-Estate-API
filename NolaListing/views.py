from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Property, Agent, Testimonial, Contact, Location
from .serializers import PropertySerializer, AgentSerializer, TestimonialsSerializer , ContactSerializer
from .serializers import LocationSerializer, PropertySerializer

# List locations
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# List all properties or create a new property
class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Get details of a particular property
class PropertyDetail(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# Submit a contact from for a property
class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# List all agents
class AgentList(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer