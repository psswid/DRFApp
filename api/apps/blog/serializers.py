from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from api.apps.comments.serializers import CommentObjectSerializer

from .documents import EntryDocument
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    comments = CommentObjectSerializer(many=True)

    class Meta:
        model = Entry
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


class EntryDocumentSerializer(DocumentSerializer):
    class Meta:
        document = EntryDocument
        fields = (
            "id",
            "title",
            "body",
            "comments",
            "created_at",
            "updated_at",
            "pub_date",
        )
