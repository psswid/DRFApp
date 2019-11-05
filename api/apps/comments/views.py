from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAdminUser)

from .models import Comment
from .documents import CommentDocument
from .renderers import CommentJSONRenderer
from .serializers import CommentObjectSerializer, CommentDocumentSerializer
from .tasks import count_comments

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentObjectSerializer
    renderer_classes = (CommentJSONRenderer,)
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Comment.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_url = serializer.data
        count_comments(obj_url)
        return response


class CommentDocumentViewSet(DocumentViewSet):
    document = CommentDocument
    serializer_class = CommentDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'body',
    )

    # Filter fields
    filter_fields = {
        'id': {
            'field': 'id',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
        'body': 'body.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
    }

    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'body.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
    }

    # Specify default ordering
    ordering = ('id', 'created_at',)

