from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from teplo.models import Order


class OrderForm(forms.ModelForm):
    captcha = CaptchaField(label=False,
                           widget=CaptchaTextInput(attrs={
                               'class': 'form-input-captcha',
                               'maxlength': '10',
                               'placeholder': "Ответ"}))

    class Meta:
        model = Order
        fields = ['name', 'phone', 'order']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваше имя',
                'minlength': 2,
                'maxlength': 30
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ваш телефон',
                'minlength': 10,
                'maxlength': 12
            }),
            'order': forms.Textarea(attrs={
                'class': 'form-area',
                'rows': 5,
                'placeholder': 'Напишите заявку сюда..',
                'minlength': 5,
                'maxlength': 1000
            })
        }
        labels = {
            'name': False,
            'phone': False,
            'order': False
        }
