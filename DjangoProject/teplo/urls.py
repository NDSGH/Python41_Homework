from django.urls import path
from . import views


# Routing:
app_name = 'teplo'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),
]
