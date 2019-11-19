from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import ArticleDocumentViewSet, ArticleViewSet, search

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("articles", ArticleViewSet)
router.register("es/articles/", ArticleDocumentViewSet, base_name="articledocument")

urlpatterns = [
    path("", include(router.urls)),
    path("articles/search/", search, name="articles-search"),
]
