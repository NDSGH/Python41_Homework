from django.shortcuts import render
from .models import Faculty, Group, Student


def index(request):
    db_data = {
        'db_faculty': Faculty.objects.all(),
        'db_group': Group.objects.all(),
        'db_student': Student.objects.all()
    }
    return render(request, 'my_app/index.html', context=db_data)
