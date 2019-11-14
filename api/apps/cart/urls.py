from django.conf.urls import include
from django.urls import path

from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet


router = ExtendedDefaultRouter(trailing_slash=False)
router.register(r'carts', CartViewSet)
router.register(r'cart_items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]