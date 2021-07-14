from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from news.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение', null=True, blank=True,)
    rubric = models.ManyToManyField('news.Category', verbose_name='Интересы')

    STATUS_PUNKT = (
        ('Ul', 'Ульяновск'),
        ('Bar', 'Барыш'),
    )

    punkt = models.CharField(max_length=30, choices=STATUS_PUNKT, verbose_name='Населеный пункт')

    STATUS_ZAVED = (
        ('Sc-1', 'Школа №1'),
        ('Sc-2', 'Школа №1'),
    )

    zaved = models.CharField(max_length=30, choices=STATUS_ZAVED, verbose_name='Учебное заведение')
    klas = models.IntegerField(verbose_name='Класс')
    dt = models.DateField(max_length=255, verbose_name='Дата рождения')

    STATUS_POL = (
        ('Maim', 'Мужчина'),
        ('Woman', 'Женщина'),
    )

    status = models.CharField(max_length=30, choices=STATUS_POL, verbose_name='Пол')

    def __unicode__(self):
        return self.avatar


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class CustomUser(User):


    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class CustomUseris(User):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'