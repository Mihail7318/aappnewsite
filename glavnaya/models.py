from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from news.models import Post, Category

class Slider(models.Model):

    STATUS_SLIDER = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='Publish', max_length=30, choices=STATUS_SLIDER, verbose_name='Статус')
    title = models.ForeignKey(Post,  related_name='Slidertitle', on_delete=models.CASCADE, verbose_name='Новость')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"
        ordering = ['-created_at']



class Vidjet(models.Model):

    vidjetone = models.ForeignKey(Category, related_name='Vidjetone', on_delete=models.CASCADE, verbose_name='Виджет-1')
    vidjettwo = models.ForeignKey(Category, related_name='Vidjettwo', on_delete=models.CASCADE, verbose_name='Виджет-2')
    vidjetthree = models.ForeignKey(Category, related_name='Vidjetthree', on_delete=models.CASCADE, verbose_name='Виджет-3')


    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Троица категории'
        verbose_name_plural = 'Троица категорий'


class Favourites(models.Model):

    favourites = models.ManyToManyField(Category, related_name='favourites', verbose_name='Список')

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Избранная категория'
        verbose_name_plural = 'Избранные категорий'
