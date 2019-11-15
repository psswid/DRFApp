from django.contrib import admin

from .models import Cart, CartItem, Order, OrderItem


class CartAdmin(admin.ModelAdmin):
    fields = ['owner']


class CartItemAdmin(admin.ModelAdmin):
    fields = ['cart', 'product', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    fields = ['owner', 'total']


class OrderItemAdmin(admin.ModelAdmin):
    fields = ['order', 'product', 'quantity']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)