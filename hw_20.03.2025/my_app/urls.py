from django.urls import path
from . import views


app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),
    path('valid/', views.valid, name='valid'),
]
