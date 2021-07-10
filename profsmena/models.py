from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')
    name = models.CharField(max_length=255, verbose_name='Имя рубрики')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')
    photo = models.ImageField(blank=True, upload_to='image', null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Smena(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    start = models.DateTimeField(null=True, blank=True, verbose_name='Начало')
    end = models.DateTimeField(null=True, blank=True, verbose_name='Окончание')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    category = TreeForeignKey('Category', verbose_name='Рубрики', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Профильная смена'
        verbose_name_plural = 'Профильная смена'
        ordering = ['-created_at']