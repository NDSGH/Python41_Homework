from django.contrib import admin
from .models import Order, Price


admin.site.site_title = "ESK-Admin"


class OrderAdmin(admin.ModelAdmin):
    """Display model Order in admin"""
    list_display = ('name', 'phone', 'order', 'created')
    readonly_fields = ('name', 'phone', 'order', 'created')


class PriceAdmin(admin.ModelAdmin):
    """Display model Price in admin"""
    list_display = ('service', 'cost', 'created')
    readonly_fields = ('created', )


admin.site.register(Order, OrderAdmin)
admin.site.register(Price, PriceAdmin)
