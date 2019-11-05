from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Article
from .documents import ArticleDocument
from api.apps.comments.serializers import CommentObjectSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    comments = CommentObjectSerializer(many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'comments',
            'comments_count',
            'pub_date',
            'created_at',
            'updated_at'
        )
        depth = 1


class ArticleDocumentSerializer(DocumentSerializer):

    class Meta:
        document = ArticleDocument
        fields = (
            'id',
            'title',
            'body',
            'comments',
            'created_at',
            'updated_at',
            'pub_date',
        )

