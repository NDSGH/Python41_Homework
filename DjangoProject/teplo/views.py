from django.shortcuts import render, redirect
from teplo.forms import ToMailForm
from .models import Price
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    """Main page"""
    if request.method == 'POST':
        form = ToMailForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                "Заявка",
                str(form.cleaned_data),
                "shadow-of-toilet@yandex.ru",
                ["shadow-of-toilet@yandex.ru"],
                fail_silently=False,
            )
            messages.success(request, 'Заявка успешно отправлена! Мы свяжемся в Вами в ближайшее время.')
            return redirect('/')
    else:
        form = ToMailForm()

    form_data = {
        'title': "главная",
        'form': form
    }

    return render(request, 'teplo/index.html', context=form_data)


def about(request):
    """About page"""
    return render(request, 'teplo/about.html', {'title': 'о нас'})


def service(request):
    """Services page"""
    return render(request, 'teplo/service.html', {'title': 'услуги'})


def price(request):
    """Price page"""
    price_data = {
        'title': 'цены',
        'db_price': Price.objects.all(),
    }
    return render(request, 'teplo/price.html', context=price_data)
