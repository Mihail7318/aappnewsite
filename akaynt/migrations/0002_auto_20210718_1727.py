# Generated by Django 2.2.2 on 2021-07-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akaynt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klas',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Класс'},
        ),
        migrations.AlterField(
            model_name='klas',
            name='alf',
            field=models.CharField(choices=[('1', 'А'), ('2', 'Б'), ('3', 'В'), ('4', 'Г'), ('5', 'Д'), ('6', 'Е'), ('7', 'Ё'), ('8', 'Ж'), ('9', 'З'), ('10', 'И'), ('11', 'Й'), ('12', 'К'), ('13', 'Л'), ('14', 'М'), ('15', 'Н')], max_length=30, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='klas',
            name='klas',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=30, verbose_name='Статус'),
        ),
    ]