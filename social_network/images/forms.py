from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .models import ImagesModel

import requests


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImagesModel
        fields = ['description', 'title', 'url']
        widgets = {
            'url': forms.HiddenInput
        }

    def save(self,
             force_update=False,
             force_insert=False,
             commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        response = requests.get(image_url)
        image.image.save(image_name,
                         ContentFile(response.content),
                         save=False)
        if commit:
            image.save()
        return image

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Не является изображением')
        return url
