from django.conf.urls import include
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter

from .views import CommentDocumentViewSet, CommentViewSet

router = ExtendedDefaultRouter(trailing_slash=False)
router.register("comments", CommentViewSet)
router.register("es/comments/", CommentDocumentViewSet, base_name="commentdocument")

urlpatterns = [
    path("", include(router.urls)),
]
