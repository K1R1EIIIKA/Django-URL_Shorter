# Generated by Django 4.1.5 on 2023-02-10 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_links_author_alter_links_created_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='created_time',
        ),
    ]