from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import ProductViewSet

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
