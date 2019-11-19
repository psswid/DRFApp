from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import CartItemViewSet, CartViewSet, OrderItemViewSet, OrderViewSet

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("carts", CartViewSet)
router.register("cart_items", CartItemViewSet)
router.register("orders", OrderViewSet)
router.register("order_items", OrderItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
