from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import UserViewSet

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
