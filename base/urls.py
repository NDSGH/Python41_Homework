from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('teplo.urls')),
    path('captcha/', include('captcha.urls')),
]

handler404 = page_not_found

# Admin panel styles
admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'ESK-Teplo'
