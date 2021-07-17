# Generated by Django 3.2.5 on 2021-07-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akaynt', '0002_remove_customer_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dt',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='klass',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pol',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='punkt',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='rubric',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='status',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='ychenik',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
    ]
