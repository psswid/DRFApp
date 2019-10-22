from django.conf.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet


router = DefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]