from django_elasticsearch_dsl_drf.constants import (LOOKUP_FILTER_RANGE,
                                                    LOOKUP_QUERY_GT,
                                                    LOOKUP_QUERY_GTE,
                                                    LOOKUP_QUERY_IN,
                                                    LOOKUP_QUERY_LT,
                                                    LOOKUP_QUERY_LTE)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend, FilteringFilterBackend,
    OrderingFilterBackend, SearchFilterBackend)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .documents import CommentDocument
from .models import Comment
from .renderers import CommentJSONRenderer
from .serializers import CommentDocumentSerializer, CommentObjectSerializer
from .tasks import count_comments


class CommentViewSet(viewsets.ModelViewSet):
    """
     API endpoint Comment CRUD
     """
    queryset = Comment.objects.all()
    serializer_class = CommentObjectSerializer
    renderer_classes = (CommentJSONRenderer,)
    permission_classes = [
        AllowAny,
    ]

    """AutoCount comments task added"""
    def create(self, request, *args, **kwargs):
        response = super().create(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_url = serializer.data
        count_comments(obj_url)
        return response


class CommentDocumentViewSet(DocumentViewSet):
    """
    API endpoint to Comment ElasticSearch query
    """
    document = CommentDocument
    serializer_class = CommentDocumentSerializer

    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = ("body",)

    # Filter fields
    filter_fields = {
        "id": {
            "field": "id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        "body": "body.raw",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    # Define ordering fields
    ordering_fields = {
        "id": "id",
        "title": "body.raw",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    # Specify default ordering
    ordering = (
        "id",
        "created_at",
    )
