# Generated by Django 3.2.5 on 2021-07-17 12:31

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0002_auto_20210717_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vopros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('varian_1', models.CharField(db_index=True, max_length=255, verbose_name='Ответ №1')),
                ('otvet_1', models.BooleanField(default=False, verbose_name='Верный')),
                ('varian_2', models.CharField(db_index=True, max_length=255, verbose_name='Ответ №2')),
                ('otvet_2', models.BooleanField(default=False, verbose_name='Верный')),
                ('varian_3', models.CharField(db_index=True, max_length=255, verbose_name='Ответ №3')),
                ('otvet_3', models.BooleanField(default=False, verbose_name='Верный')),
                ('varian_4', models.CharField(db_index=True, max_length=255, verbose_name='Ответ №4')),
                ('otvet_4', models.BooleanField(default=False, verbose_name='Верный')),
                ('views', models.IntegerField(default=0, verbose_name='Количество пройденых')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Zadacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='Publish', max_length=30, verbose_name='Статус')),
                ('yved', models.BooleanField(default=False, verbose_name='Уведомить')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('title_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('title_ru', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('content_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Задание(ю)',
                'verbose_name_plural': 'Задания',
                'ordering': ['-created_at'],
            },
        ),
    ]
