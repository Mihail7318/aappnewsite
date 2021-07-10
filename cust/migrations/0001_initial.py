# Generated by Django 3.2.5 on 2021-07-10 03:08

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.TextField(max_length=255, verbose_name='Вопрос(RU)')),
                ('reply', models.TextField(verbose_name='Ответ(RU)')),
                ('problemen', models.TextField(max_length=255, verbose_name='Вопрос(EN)')),
                ('replyen', models.TextField(verbose_name='Ответ(EN)')),
            ],
            options={
                'verbose_name': 'ЧаВо',
                'verbose_name_plural': 'ЧаВо',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('keyword', models.CharField(max_length=255, verbose_name='Ключевые слова')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('copyright', models.CharField(max_length=255, verbose_name='copyright')),
                ('favicon', models.ImageField(blank=True, upload_to='images/', verbose_name='Иконка сайта')),
                ('logotip', models.ImageField(blank=True, upload_to='images/', verbose_name='Логотип')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Телефон')),
                ('workschedule', models.CharField(blank=True, max_length=15, verbose_name='График работы')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Электроная почта')),
                ('smtpserver', models.CharField(blank=True, max_length=50, verbose_name='SMTPserver')),
                ('smtpemail', models.CharField(blank=True, max_length=50, verbose_name='SMTPemail')),
                ('smtppassword', models.CharField(blank=True, max_length=50, verbose_name='SMTPpassword')),
                ('smtpport', models.CharField(blank=True, max_length=8, verbose_name='SMTPport')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Общие настроики',
                'verbose_name_plural': 'Общие настроики',
            },
        ),
        migrations.CreateModel(
            name='Standartpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacypolicy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Политика конфиденциальности(ru)')),
                ('privacypolicyen', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Политика конфиденциальности(en)')),
                ('useragreement', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Пользовательское соглашение(ru)')),
                ('useragreementen', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Пользовательское соглашение(en)')),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Контакты(ru)')),
                ('contacten', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Контакты(en)')),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='О нас(ru)')),
                ('aboutusen', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='О нас(en)')),
            ],
            options={
                'verbose_name': 'стандартные страницы',
                'verbose_name_plural': 'стандартные страницы',
            },
        ),
    ]
