# Generated by Django 3.2.5 on 2021-07-07 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konkurs', '0003_auto_20210707_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
