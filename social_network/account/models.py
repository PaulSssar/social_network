from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    birthday = models.DateField(
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True
    )

    def __str__(self):
        return f'Профиль пользователя {self.user}'


class Contact(models.Model):
    user_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_from'
    )
    user_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_to'
    )
    created = models.DateTimeField(
        'Дата',
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['-created', ])
        ]
        ordering = ('-created', )

    def __str__(self):
        return f'{self.user_from} подписался на {self.user_to}'


User.add_to_class('following',
                  models.ManyToManyField(
                      'self',
                      through=Contact,
                      related_name='followers',
                      symmetrical=False
                  ))
