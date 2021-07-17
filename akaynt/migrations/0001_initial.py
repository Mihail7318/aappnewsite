# Generated by Django 3.2.5 on 2021-07-17 17:35

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUseris',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('onli', models.BooleanField(default=False, verbose_name='Ученик онлайн')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/users', verbose_name='Изображение')),
                ('dt', models.DateField(max_length=255, verbose_name='Дата рождения')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('punkt', models.CharField(choices=[('Ульяновск', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1'))), ('Барыш', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1'))), ('Димитровград', (('sc-1', 'Школа №1'), ('sc-2', 'Школа №1')))], max_length=30, verbose_name='Населеный пункт')),
                ('klass', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default=1, max_length=30, verbose_name='Класс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
    ]
