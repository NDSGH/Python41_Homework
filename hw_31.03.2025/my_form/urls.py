from django.urls import path
from . import views

app_name = 'my_form'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]
