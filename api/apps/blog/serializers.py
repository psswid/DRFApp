from rest_framework import serializers

from .models import Entry
from api.apps.comments.serializers import CommentSerializer


class EntrySerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    class Meta:
        model = Entry
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

