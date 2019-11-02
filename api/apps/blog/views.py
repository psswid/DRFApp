from rest_framework import generics, viewsets, status
from rest_framework.permissions import (AllowAny, IsAdminUser)
from rest_framework.decorators import action
from rest_framework.response import Response

from .tasks import count_comments
from .models import Entry
from .renderers import EntryJSONRenderer
from .serializers import EntrySerializer

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


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    renderer_classes = (EntryJSONRenderer,)
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Entry.objects.all()

    def create(self, request, *args, **kwargs):
        count_comments(self)

