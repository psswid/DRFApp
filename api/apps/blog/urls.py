from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import EntryDocumentViewSet, EntryViewSet, search

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("entries", EntryViewSet)
router.register("es/entries/", EntryDocumentViewSet, base_name="entrydocument")

urlpatterns = [
    path("", include(router.urls)),
    path("entries/search/", search, name="entries-search"),
]
