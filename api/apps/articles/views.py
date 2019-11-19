from django.shortcuts import render
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

from .documents import ArticleDocument
from .models import Article
from .renderers import ArticleJSONRenderer
from .serializers import ArticleDocumentSerializer, ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
     API endpoint to Article CRUD
     """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = (ArticleJSONRenderer,)
    permission_classes = [
        AllowAny,
    ]

    def get_queryset(self):
        return Article.objects


class ArticleDocumentViewSet(DocumentViewSet):
    """
     API endpoint to Article ElasticSearch query
     """
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer

    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        "title",
        "body",
    )

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
        "title": "title.raw",
        "body": "body.raw",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "pub_date": "pub_date",
    }

    # Define ordering fields
    ordering_fields = {
        "id": "id",
        "title": "title.raw",
        "created_at": "created_at",
        "updated_at": "updated_at",
        "pub_date": "pub_date",
    }

    # Specify default ordering
    ordering = (
        "id",
        "created_at",
    )


def search(request):
    """
     Html ElasticSearch
     """
    q = request.GET.get("q")

    if q:
        articles = ArticleDocument.search().query("match", body=q)
    else:
        articles = ""

    return render(request, "search/search.html", {"articles": articles})
