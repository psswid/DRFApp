from django.conf.urls import include
from django.urls import path

from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import ArticleViewSet, ArticleDocumentViewSet


router = ExtendedDefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)
router.register('es/articles/', ArticleDocumentViewSet, base_name='articledocument')

urlpatterns = [
    path('', include(router.urls)),
]