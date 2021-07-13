# Generated by Django 3.0.8 on 2021-07-13 03:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_obj', models.FileField(upload_to='media/')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(max_length=255, verbose_name='Вопрос')),
                ('problem_en', models.TextField(max_length=255, null=True, verbose_name='Вопрос')),
                ('problem_ru', models.TextField(max_length=255, null=True, verbose_name='Вопрос')),
                ('reply', models.TextField(verbose_name='Ответ')),
                ('reply_en', models.TextField(null=True, verbose_name='Ответ')),
                ('reply_ru', models.TextField(null=True, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'ЧаВо',
                'verbose_name_plural': 'ЧаВо',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], max_length=30, verbose_name='Статус')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('ssilka', models.CharField(max_length=30, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('title_en', models.CharField(max_length=30, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=30, null=True, verbose_name='Название')),
                ('keyword', models.CharField(max_length=255, verbose_name='Ключевые слова')),
                ('keyword_en', models.CharField(max_length=255, null=True, verbose_name='Ключевые слова')),
                ('keyword_ru', models.CharField(max_length=255, null=True, verbose_name='Ключевые слова')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('description_en', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('description_ru', models.CharField(max_length=255, null=True, verbose_name='Описание')),
                ('copyright', models.CharField(max_length=255, verbose_name='copyright')),
                ('copyright_en', models.CharField(max_length=255, null=True, verbose_name='copyright')),
                ('copyright_ru', models.CharField(max_length=255, null=True, verbose_name='copyright')),
                ('favicon', models.ImageField(blank=True, upload_to='images/', verbose_name='Иконка сайта')),
                ('logotip', models.ImageField(blank=True, upload_to='images/', verbose_name='Логотип')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес')),
                ('address_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('address_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Электроная почта')),
            ],
            options={
                'verbose_name': 'Общие настроики',
                'verbose_name_plural': 'Общие настроики',
            },
        ),
        migrations.CreateModel(
            name='Standartpages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacypolicy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Политика конфиденциальности')),
                ('privacypolicy_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Политика конфиденциальности')),
                ('privacypolicy_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Политика конфиденциальности')),
                ('useragreement', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Пользовательское соглашение')),
                ('useragreement_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Пользовательское соглашение')),
                ('useragreement_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Пользовательское соглашение')),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Контакты')),
                ('contact_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контакты')),
                ('contact_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Контакты')),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='О нас')),
                ('aboutus_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
                ('aboutus_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='О нас')),
            ],
            options={
                'verbose_name': 'стандартные страницы',
                'verbose_name_plural': 'стандартные страницы',
            },
        ),
    ]
