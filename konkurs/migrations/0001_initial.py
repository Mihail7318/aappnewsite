# Generated by Django 3.2.5 on 2021-07-07 12:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя рубрики(ru)')),
                ('nameen', models.CharField(max_length=255, verbose_name='Имя рубрики(en)')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Изображение')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='konkurs.category')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skinnews', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Обложка блога')),
                ('skincat', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Обложка категории')),
                ('skintag', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Обложка тега')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], max_length=30, verbose_name='Статус')),
                ('name', models.CharField(max_length=30, verbose_name='Название(ru)')),
                ('nameen', models.CharField(max_length=30, verbose_name='Название(en)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Метка',
                'verbose_name_plural': 'Метки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='P', max_length=30, verbose_name='Статус')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Наименование(ru)')),
                ('titleen', models.CharField(db_index=True, max_length=255, verbose_name='Наименование(en)')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание(ru)')),
                ('contenten', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Описание(en)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='konkurs.category', verbose_name='Рубрики')),
                ('tags', models.ManyToManyField(to='konkurs.Tag', verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Статья(ю)',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-created_at'],
            },
        ),
    ]
