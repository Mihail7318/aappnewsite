# Generated by Django 3.0.8 on 2021-07-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sovet', '0002_auto_20210708_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exsov',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='popsov',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
