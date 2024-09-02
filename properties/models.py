from django.contrib import admin
from django.db import models
from django.utils.html import mark_safe


# Models
class Property(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    locations = models.ManyToManyField('Location', blank=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title or f"Property {self.property_id}"


class Image(models.Model):
    property = models.ForeignKey(
        Property, related_name='images', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return f"{self.property.title if self.property else 'Unknown Property'}"

    def thumbnail(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe(f'<img src="{self.image.url}" width="100" />')
        return "No Image"

    thumbnail.short_description = 'Thumbnail'


class Location(models.Model):
    LOCATION_TYPES = [
        ('COUNTRY', 'Country'),
        ('STATE', 'State'),
        ('CITY', 'City'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(
        max_length=10, choices=LOCATION_TYPES, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        if self.name and self.type:
            return f"{self.name} ({self.get_type_display()})"
        return "Unnamed Location"


class Amenity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name or "Unnamed Amenity"