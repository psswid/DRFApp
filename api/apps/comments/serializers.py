from rest_framework import serializers

from .models import Comment


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
