# Generated by Django 3.2.5 on 2021-07-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akaynt', '0002_remove_customer_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='klass',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default=1, max_length=30, verbose_name='Класс'),
        ),
        migrations.AddField(
            model_name='customer',
            name='punkt',
            field=models.CharField(choices=[('Ульяновск', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1'))), ('Барыш', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1'))), ('Димитровград', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1')))], default=1, max_length=30, verbose_name='Населеный пункт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
    ]
