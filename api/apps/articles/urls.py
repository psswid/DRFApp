from django.conf.urls import include
from django.urls import path

from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import ArticleViewSet, ArticleDocumentViewSet
from api.apps.comments.views import CommentViewSet


router = ExtendedDefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)
# źle, nie działa, zly regexp
router.register('articles/(?P<pk>[^/.]+)/comments', CommentViewSet, base_name='article-comments')
router.register('es/articles/', ArticleDocumentViewSet, base_name='articledocument')


urlpatterns = [
    path('', include(router.urls)),
]