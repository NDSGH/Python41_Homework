from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator, \
    RegexValidator
from django.db import models
from django.utils import timezone


class FromForm(models.Model):
    """Data from form"""
    name = models.CharField(validators=[
        MinLengthValidator(2, message="Минимальное количество символов 2"),
        MaxLengthValidator(30, message="Максимальное количество символов 30"),
        RegexValidator(regex=r'[абвгдеёжзийклмнопрстуфхцчшщъыьэюя .]',
                       message='Только русские буквы, пробелы и точки')
    ])

    phone = models.CharField(validators=[
        MinLengthValidator(10, message="Минимальное количество символов 10"),
        MaxLengthValidator(12, message="Максимальное количество символов 12"),
        RegexValidator(regex=r'^(\+)?[0-9]{10,11}', message='Только цифры и знак +')
    ])

    order = models.CharField(validators=[
        MinLengthValidator(5, message="Минимальное количество символов 5"),
        MaxLengthValidator(1000, message="Максимальное количество символов 1000")
    ])

    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявки из формы обратной связи'
        verbose_name_plural = 'Заявки из формы обратной связи'


class Price(models.Model):
    """Data from admin"""
    service = models.CharField(validators=[
        MinLengthValidator(1, message="Минимальное количество символов 1"),
        MaxLengthValidator(100, message="Максимальное количество символов 100")
    ], unique=True)

    cost = models.IntegerField(validators=[
        MinValueValidator(1, message="Минимальное значение 1"),
        MaxValueValidator(99999, message="Максимальное значение 99999")
    ])
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс лист'
        ordering = ['-cost']
