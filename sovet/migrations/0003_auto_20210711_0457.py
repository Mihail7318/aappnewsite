# Generated by Django 3.0.8 on 2021-07-11 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0002_auto_20210711_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exsov',
            name='content',
        ),
        migrations.RemoveField(
            model_name='exsov',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='popsov',
            name='content',
        ),
        migrations.RemoveField(
            model_name='popsov',
            name='slug',
        ),
        migrations.AddField(
            model_name='exsov',
            name='works',
            field=models.CharField(db_index=True, default=1, max_length=255, verbose_name='Место работы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='popsov',
            name='works',
            field=models.CharField(db_index=True, default=1, max_length=255, verbose_name='Место работы'),
            preserve_default=False,
        ),
    ]