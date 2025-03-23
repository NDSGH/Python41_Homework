from django.db import models
from django.utils import timezone


# Модель для кафедры:
class Faculty(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Модель для группы:
class Group(models.Model):
    title = models.CharField(max_length=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Модель для студента:
class Student(models.Model):
    name = models.CharField(max_length=255, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
