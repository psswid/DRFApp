from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import EntryViewSet


router = DefaultRouter(trailing_slash=False)
router.register('entries', EntryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]