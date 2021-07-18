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

    def __str__(self):
        return "Пользователь: {} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'



class CustomUseris(User):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Punkt(models.Model):
    punct = models.CharField(max_length=255, verbose_name='Населеный пункт')

    def __str__(self):
        return self.punct

    class Meta:
        verbose_name = 'Населеный пункт'
        verbose_name_plural = 'Населеные пункты'

class School(models.Model):
    punct = models.ForeignKey(Punkt, verbose_name='Населеный пункт', on_delete=models.CASCADE)
    school = models.CharField(max_length=255, verbose_name='Школа')

    def __str__(self):
        return self.school

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

class Klas(models.Model):
    school = models.ForeignKey(School, verbose_name='Школа', on_delete=models.CASCADE)

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
    klas = models.CharField(max_length=30, choices=STATUS_KLASS, verbose_name='Статус')
    STATUS_ALF = (
        ('1', 'А'),
        ('2', 'Б'),
        ('3', 'В'),
        ('4', 'Г'),
        ('5', 'Д'),
        ('6', 'Е'),
        ('7', 'Ё'),
        ('8', 'Ж'),
        ('9', 'З'),
        ('10', 'И'),
        ('11', 'Й'),
        ('12', 'К'),
        ('13', 'Л'),
        ('14', 'М'),
        ('15', 'Н'),
    )
    alf = models.CharField(max_length=30, choices=STATUS_ALF, verbose_name='Статус')

    def __str__(self):
        return self.klas

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Класс'