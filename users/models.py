from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
