# Generated by Django 3.0.8 on 2021-07-11 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('glavnaya', '0002_auto_20210711_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vidjet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidjetone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjetone', to='news.Category', verbose_name='Виджет-1')),
                ('vidjetthree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjetthree', to='news.Category', verbose_name='Виджет-3')),
                ('vidjettwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vidjettwo', to='news.Category', verbose_name='Виджет-2')),
            ],
            options={
                'verbose_name': 'Троица категории',
                'verbose_name_plural': 'Троица категорий',
            },
        ),
    ]
