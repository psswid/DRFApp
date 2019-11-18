from django.db import models

from api.apps.core.models import BaseModel
from api.apps.users.models import User
from api.apps.products.models import Product

from decimal import Decimal



class Cart(BaseModel):
    owner = models.OneToOneField(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )


class CartItem(BaseModel):
    """A model that contains data for an item in the shopping cart."""
    cart = models.ForeignKey(
        Cart,
        related_name='items',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        related_name='items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.name, self.quantity)

class Order(BaseModel):
    """
    An Order is the more permanent counterpart of the shopping cart. It represents
    the frozen the state of the cart on the moment of a purchase. In other words,
    an order is a customer purchase.
    """
    owner = models.ForeignKey(User, related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class OrderItem(BaseModel):
    """A model that contains data for an item in an order."""
    order = models.ForeignKey(
        Order,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.name, self.quantity)

