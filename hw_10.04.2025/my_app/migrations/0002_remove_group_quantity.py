# Generated by Django 5.1.7 on 2025-03-23 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='quantity',
        ),
    ]
