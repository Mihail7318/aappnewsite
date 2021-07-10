from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models



class Slider(models.Model):

    title = models.CharField(max_length=30, verbose_name='Название')
    keyword = models.CharField(max_length=255, verbose_name='Ключевые слова')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"



