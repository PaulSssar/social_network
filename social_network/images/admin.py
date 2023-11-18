from django.contrib import admin
from .models import ImagesModel


@admin.register(ImagesModel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']