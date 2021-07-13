# Generated by Django 3.0.8 on 2021-07-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exsov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='Publish', max_length=30, verbose_name='Статус')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('doljnost', models.CharField(db_index=True, max_length=255, verbose_name='Должность')),
                ('works', models.CharField(db_index=True, max_length=255, verbose_name='Место работы')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Экспертный совет',
                'verbose_name_plural': 'Экспертный совет',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Popsov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='P', max_length=30, verbose_name='Статус')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('doljnost', models.CharField(db_index=True, max_length=255, verbose_name='Должность')),
                ('works', models.CharField(db_index=True, max_length=255, verbose_name='Место работы')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Попечительский совет',
                'verbose_name_plural': 'Попечительский совет',
                'ordering': ['-created_at'],
            },
        ),
    ]
