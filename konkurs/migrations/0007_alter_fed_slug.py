# Generated by Django 3.2.5 on 2021-07-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0006_auto_20210708_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fed',
            name='slug',
            field=models.CharField(max_length=255, unique=True, verbose_name='Ссылка'),
        ),
    ]
