from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

import re

regex_name = re.compile(r'[а-яА-Яa-zA-Z]{1,20}')


def index(request):
    return render(request, 'my_form/index.html')


# def hello(request):
#     if request.POST.get('name') and request.method == 'POST':
#         data = {'name': request.POST.get('name')}
#         return render(request, 'my_form/hello.html', context=data)
#     return render(request, 'my_form/index.html')


def hello(request):
    regex_filter = regex_name.findall(request.POST.get('name'))
    if request.POST.get('name') and request.method == 'POST' and request.POST.get('name') in regex_filter:
        data = {'name': request.POST.get('name')}
        return render(request, 'my_form/hello.html', context=data)
    return render(request, 'my_form/index.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
