from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class ImagesModel(models.Model):
    user = models.ForeignKey(
        User,
        related_name='image_created',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        'Название',
        max_length=200
    )
    slug = models.SlugField(
        'Слаг',
        max_length=200,
        blank=True,
    )
    url = models.URLField(
        'URL',
        max_length=2000
    )
    image = models.ImageField(
        'Изображение',
        upload_to='images/%Y/%m/%d'
    )
    description = models.TextField(
        'Описание',
        blank=True,
    )
    created = models.DateField(
        'Дата создания',
        auto_now_add=True
    )
    users_like = models.ManyToManyField(
        User,
        verbose_name='Понравилось',
        blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ('-created',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
