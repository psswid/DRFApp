from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import (AllowAny, IsAdminUser)
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Entry
from .documents import EntryDocument
from .renderers import EntryJSONRenderer
from .serializers import EntrySerializer, EntryDocumentSerializer

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


class EntryDocumentViewSet(DocumentViewSet):
    document = EntryDocument
    serializer_class = EntryDocumentSerializer

    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'title',
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
        'title': 'title.raw',
        'body': 'body.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'pub_date': 'pub_date',
    }

    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'pub_date': 'pub_date',
    }

    # Specify default ordering
    ordering = ('id', 'created_at',)


def search(request):

    q = request.GET.get('q')

    if q:
        entries = EntryDocument.search().query("match", body=q)
    else:
        entries = ''

    return render(request, 'search/search.html', {'entries': entries})
