from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True
    )
    short_description = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    long_description = HTMLField(
        verbose_name='Полное описание',
        blank=True
    )
    longitude = models.FloatField(verbose_name='Долгота местоположения')
    latitude = models.FloatField(verbose_name='Широта местоположения')

    class Meta:
        ordering = ['title']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    number = models.PositiveIntegerField(
        verbose_name='Номер изображения',
        blank=True,
        default=0,
        db_index=True
    )
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )

    class Meta:
        ordering = ['number']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f"{self.place.title} - Image {self.number}"
