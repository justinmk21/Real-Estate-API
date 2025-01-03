from django.contrib import admin
from .models import Property, Agent, Testimonial, PropertyImage, Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'province', 'country')
    search_fields = ('city', 'province', 'country')
    list_filter = ('country', 'province')

# Register Property model.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'address','agent', 'created_at')
    search_fields = ('title', 'address')
    list_filter = ('price', 'agent')
    ordering = ('created_at',) # Order by newest properties first

# Register agent model
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'field')
    ordering = ('name',)

# Register Testimonial model
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)

# Register Image model
@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')
    search_fields = ('property_title',)
    ordering = ('property',)