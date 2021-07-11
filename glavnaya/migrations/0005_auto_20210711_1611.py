# Generated by Django 3.0.8 on 2021-07-11 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('glavnaya', '0004_favourites'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourites',
            new_name='Favorites',
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
            name='Favorit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorit', to='news.Category', verbose_name='Ибранная категория')),
            ],
            options={
                'verbose_name': 'Троица категории',
                'verbose_name_plural': 'Троица категорий',
            },
        ),
    ]