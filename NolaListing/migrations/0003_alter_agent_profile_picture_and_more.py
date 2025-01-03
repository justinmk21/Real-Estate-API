# Generated by Django 5.1.3 on 2024-12-27 20:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NolaListing', '0002_property_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile images'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='images'),
        ),
    ]
