# Generated by Django 5.2 on 2025-04-27 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teplo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['-cost'], 'verbose_name': 'Прайс лист', 'verbose_name_plural': 'Прайс лист'},
        ),
        migrations.RenameField(
            model_name='fromform',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='fromform',
            name='name',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(2, message='Минимальное количество символов 2'), django.core.validators.MaxLengthValidator(30, message='Максимальное количество символов 30'), django.core.validators.RegexValidator(message='Только русские буквы, пробелы и точки', regex='[абвгдеёжзийклмнопрстуфхцчшщъыьэюя .]')]),
        ),
        migrations.AlterField(
            model_name='fromform',
            name='order',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(5, message='Минимальное количество символов 5'), django.core.validators.MaxLengthValidator(1000, message='Максимальное количество символов 1000')]),
        ),
        migrations.AlterField(
            model_name='fromform',
            name='phone',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(10, message='Минимальное количество символов 10'), django.core.validators.MaxLengthValidator(12, message='Максимальное количество символов 12'), django.core.validators.RegexValidator(message='Только цифры и знак +', regex='^(\\+)?[0-9]{10,11}')]),
        ),
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное значение 1'), django.core.validators.MaxValueValidator(99999, message='Максимальное значение 99999')]),
        ),
        migrations.AlterField(
            model_name='price',
            name='service',
            field=models.CharField(unique=True, validators=[django.core.validators.MinLengthValidator(1, message='Минимальное количество символов 1'), django.core.validators.MaxLengthValidator(100, message='Максимальное количество символов 100')]),
        ),
    ]
