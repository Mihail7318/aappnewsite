from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from news.models import *

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    onli = models.BooleanField(default=False, verbose_name='Ученик онлайн')
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение', null=True, blank=True, )
    dt = models.DateField(max_length=255, verbose_name='Дата рождения')
    status = models.BooleanField(default=False, verbose_name='Статус')
    STATUS_PUNKT = [
        ('Ульяновск', (
            ('sc-1', 'Школа №1'),
            ('sc-2', 'Школа №1'),
        )
         ),
        ('Барыш', (
            ('sc-1', 'Школа №1'),
            ('sc-2', 'Школа №1'),
        )
         ),
        ('Димитровград', (
            ('sc-1', 'Школа №1'),
            ('sc-2', 'Школа №1'),
        )
         ),
    ]

    punkt = models.CharField(max_length=30, choices=STATUS_PUNKT, verbose_name='Населеный пункт')

    STATUS_KLASS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )
    klass = models.CharField(default=1, max_length=30, choices=STATUS_KLASS, verbose_name='Класс')

    def __str__(self):
        return "Пользователь: {} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'



class CustomUseris(User):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
