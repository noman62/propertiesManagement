from django.contrib import admin
from .models import Property, Image, Location, Amenity


# Admin Configurations
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['thumbnail']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_date', 'update_date')
    inlines = [ImageInline]
    filter_horizontal = ('locations', 'amenities')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'thumbnail']
    readonly_fields = ['thumbnail']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude')


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Optional, for better display in the admin

