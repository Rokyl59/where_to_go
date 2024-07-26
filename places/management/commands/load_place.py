from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from places.models import Place, PlaceImage

class Command(BaseCommand):
    help = ("Скачивает JSON файл с данными о конкретной локации на карте "
            "и сохраняет информацию в базу данных.")

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help="URL адрес JSON файла для скачивания."
        )

    def handle(self, *args, **kwargs):
        url = kwargs['url']

        response = requests.get(url)
        response.raise_for_status()
        payload = response.json()

        title = payload.get('title')
        if title is None:
            raise ValueError("Поле 'title' обязательно и должно быть заполнено.")

        coordinates = payload.get('coordinates')
        if not coordinates or 'lng' not in coordinates or 'lat' not in coordinates:
            raise ValueError("Поле 'coordinates' обязательно и должно содержать 'lng' и 'lat'.")

        short_description = payload.get('description_short', '')
        long_description = payload.get('description_long', '')
        longitude = coordinates['lng']
        latitude = coordinates['lat']

        place, _ = Place.objects.get_or_create(
            title=title,
            defaults={
                'short_description': short_description,
                'long_description': long_description,
                'longitude': longitude,
                'latitude': latitude
            }
        )

        images_url = payload.get('imgs', [])
        for image_number, image_url in enumerate(images_url):
            response = requests.get(image_url)
            response.raise_for_status()
            image = response.content
            image_name = f'{title}_{image_number}.jpg'

            place_image, _ = PlaceImage.objects.get_or_create(
                image=ContentFile(image, name=image_name),
                number=image_number,
                place=place
            )
