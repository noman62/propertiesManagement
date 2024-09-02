import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connections, connection
from properties.models import Property, Location, Image, Amenity


class Command(BaseCommand):
    help = 'Migrate data from Scrapy database to Django'

    def handle(self, *args, **kwargs):
        # Connect to the Scrapy database
        scrapy_conn = connections['scrapy']

        # Fetch data from the Scrapy database's hotels table
        with scrapy_conn.cursor() as cursor:
            cursor.execute('''
                SELECT id, title, location, image_paths, latitude, longitude, price, rating, room
                FROM hotels;
            ''')
            rows = cursor.fetchall()

        # Migrate data to Django models
        for row in rows:
            hotel_id, title, location, image_paths, latitude, longitude, price, rating, room = row

            location_obj, _ = Location.objects.get_or_create(
                name=location,
                defaults={
                    'type': 'CITY',
                    'latitude': latitude,
                    'longitude': longitude
                }
            )

            property_obj, created = Property.objects.update_or_create(
                property_id=hotel_id,
                defaults={
                    'title': title,
                    'description': f"Price: {price}, Rating: {rating}",
                }
            )

            property_obj.locations.add(location_obj)

            if room:
                room_amenities = room.strip('{}').split(',')
                for amenity_name in room_amenities:
                    amenity_name = amenity_name.strip().strip('"')
                    amenity_obj, _ = Amenity.objects.get_or_create(
                        name=amenity_name)
                    property_obj.amenities.add(amenity_obj)

            if image_paths:
                image_files = image_paths.split(',')
                for image_file in image_files:
                    possible_paths = [
                        os.path.join(settings.BASE_DIR, '..', 'scrapyAssignment',
                                     'hotels_crawler', 'images', image_file),
                    ]

                    scrapy_image_path = next(
                        (path for path in possible_paths if os.path.exists(path)), None)

                    if scrapy_image_path:
                        destination_path = os.path.join(
                            settings.MEDIA_ROOT, image_file)
                        os.makedirs(os.path.dirname(
                            destination_path), exist_ok=True)

                        if not os.path.exists(destination_path):
                            try:
                                shutil.copy(scrapy_image_path,
                                            destination_path)
                            except Exception as e:
                                self.stdout.write(self.style.WARNING(
                                    f'Error copying image {image_file}: {str(e)}'))
                                continue

                        relative_path = image_file

                        Image.objects.get_or_create(
                            property=property_obj,
                            image=relative_path
                        )

            property_obj.save()

        # Update the sequence for property_id
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT setval(pg_get_serial_sequence('properties_property', 'property_id'), (SELECT MAX(property_id) FROM properties_property)+1);"
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully migrated data from Scrapy to Django and updated sequence for property_id'))
