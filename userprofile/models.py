from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class UserProfile(MPTTModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение', null=True, blank=True,)
    region = models.CharField(max_length=30, verbose_name='Регион', null=True, blank=True,)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Регион')

    def __unicode__(self):
        return self.region

    class MPTTMeta:
        order_insertion_by = ['region']

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class CustomUser(User):

    class MPTTMeta:
        order_insertion_by = ['region']

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class CustomUseris(User):
    region = models.CharField(max_length=30, verbose_name='Регион')

    class MPTTMeta:
        order_insertion_by = ['region']

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'