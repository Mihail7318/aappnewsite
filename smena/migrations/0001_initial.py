# Generated by Django 3.0.8 on 2021-07-11 04:33

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='P', max_length=30, verbose_name='Статус')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
            options={
                'verbose_name': 'Статья(ю)',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at'],
            },
        ),
    ]