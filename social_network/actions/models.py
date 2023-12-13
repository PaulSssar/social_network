from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

class Actions(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
    )
    verb = models.CharField(
        'Действие',
        max_length=255
    )
    created = models.DateTimeField(
        'Дата',
        auto_now_add=True
    )
    target_ct = models.ForeignKey(
        ContentType,
        verbose_name='Модель',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='action'
    )
    target_id = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    target = GenericForeignKey('target_ct', 'target_id')

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct', 'target_id'])
        ]
        ordering = ('-created', )
