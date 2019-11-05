from django.conf.urls import include
from django.urls import path

from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import EntryViewSet, EntryDocumentViewSet


router = ExtendedDefaultRouter(trailing_slash=False)
router.register('entries', EntryViewSet)
router.register('es/entries/', EntryDocumentViewSet, base_name='entrydocument')


urlpatterns = [
    path('', include(router.urls)),
]