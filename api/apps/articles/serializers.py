from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from api.apps.comments.serializers import CommentObjectSerializer

from .documents import ArticleDocument
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentObjectSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "body",
            "comments",
            "comments_count",
            "pub_date",
            "created_at",
            "updated_at",
        )
        depth = 1


class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = (
            "id",
            "title",
            "body",
            "comments",
            "created_at",
            "updated_at",
            "pub_date",
        )
