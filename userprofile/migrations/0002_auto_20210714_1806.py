# Generated by Django 3.0.8 on 2021-07-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuseris',
            name='region',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='rubric',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('Maim', 'Опубликовать'), ('Not_to_publish', 'Не публиковать')], default='Maim', max_length=30, verbose_name='Статус'),
        ),
    ]
