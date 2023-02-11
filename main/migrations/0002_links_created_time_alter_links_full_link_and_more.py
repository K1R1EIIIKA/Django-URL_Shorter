# Generated by Django 4.1.5 on 2023-02-10 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='links',
            name='full_link',
            field=models.URLField(max_length=500, verbose_name='Полная ссылка'),
        ),
        migrations.AlterField(
            model_name='links',
            name='short_link',
            field=models.CharField(max_length=50, verbose_name='Сокращенная ссылка'),
        ),
    ]