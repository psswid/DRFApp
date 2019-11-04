from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Comment
from .documents import CommentDocument


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'body',
            'object_id',
            'created_at',
            'updated_at',
        )


class CommentDocumentSerializer(DocumentSerializer):

    class Meta:
        document = CommentDocument
        fields = (
            'id',
            'body',
            'object_id'
            'created_at',
            'updated_at',
        )
