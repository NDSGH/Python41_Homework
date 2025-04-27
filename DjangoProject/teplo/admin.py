from django.contrib import admin
from .models import FromForm, Price


admin.site.site_title = "ESK-Admin"


class FromFormAdmin(admin.ModelAdmin):
    """Display model FromForm in admin"""
    list_display = ('name', 'phone', 'order', 'created')
    readonly_fields = ('name', 'phone', 'order', 'created')


class PriceAdmin(admin.ModelAdmin):
    """Display model Price in admin"""
    list_display = ('service', 'cost', 'created')
    readonly_fields = ('created', )


admin.site.register(FromForm, FromFormAdmin)
admin.site.register(Price, PriceAdmin)
