from django.shortcuts import render, redirect
from teplo.forms import OrderForm
from .models import Price
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    """Main page"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    "Заявка",
                    f"Имя: {str(form.cleaned_data['name'])}\n\n\r"
                    f"Телефон: {str(form.cleaned_data['phone'])}\n\n\r"
                    f"Заявка: {str(form.cleaned_data['order'])}",
                    "shadow-of-toilet@yandex.ru",
                    ["shadow-of-toilet@yandex.ru"],
                    fail_silently=False,
                )
                messages.success(request, 'Заявка успешно отправлена! Мы свяжемся в Вами в ближайшее время.')
                return redirect('/')
            except:
                messages.error(request, 'Данные не отправлены, повторите попытку.')
    else:
        form = OrderForm()

    home_data = {
        'title': "главная",
        'form': form
    }

    return render(request, 'teplo/index.html', context=home_data)


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
