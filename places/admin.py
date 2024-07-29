from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline

from .models import Place, PlaceImage


class PlaceImageInline(SortableTabularInline):
    model = PlaceImage
    readonly_fields = ['preview_image']

    def preview_image(self, place_image):
        if place_image.image:
            return format_html(
                '<img src="{}" style="max-width: 200px; max-height: 200px;">',
                place_image.image.url
            )
        return 'No image'


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'number']
    raw_id_fields = ['place']
