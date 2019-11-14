from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    fields = ['product', 'quantities', 'price_total', 'owner']


admin.site.register(Cart, CartAdmin)