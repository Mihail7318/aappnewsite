# Generated by Django 3.0.8 on 2021-07-14 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vidjet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidjetone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjetone', to='news.Category', verbose_name='Виджет-1')),
                ('vidjetthree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjetthree', to='news.Category', verbose_name='Виджет-3')),
                ('vidjettwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjettwo', to='news.Category', verbose_name='Виджет-2')),
            ],
            options={
                'verbose_name': 'Троица категории',
                'verbose_name_plural': 'Троица категорий',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publish', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='Publish', max_length=30, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/image/', verbose_name='Изображение')),
                ('views', models.IntegerField(default=0, null=True, verbose_name='Количество просмотров')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Slidertitle', to='news.Post', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Saidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saidebar', models.ManyToManyField(related_name='saidebar', to='news.Category', verbose_name='Список')),
            ],
            options={
                'verbose_name': 'Сайдбар',
                'verbose_name_plural': 'Сайдбар',
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourites', models.ManyToManyField(related_name='favourites', to='news.Category', verbose_name='Список')),
            ],
            options={
                'verbose_name': 'Избранная категория',
                'verbose_name_plural': 'Избранные категорий',
            },
        ),
        migrations.CreateModel(
            name='Favorit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorit', to='news.Category', verbose_name='Ибранная категория')),
            ],
            options={
                'verbose_name': 'Ибранная категория',
                'verbose_name_plural': 'Ибранная категория',
            },
        ),
    ]
