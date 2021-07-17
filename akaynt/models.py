from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from news.models import *

User = get_user_model()


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='Статус')
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



class CustomUseris(models.Model):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
