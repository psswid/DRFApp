from rest_framework import serializers

from .models import Article
from api.apps.comments.serializers import CommentSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    comments = CommentSerializer(many=True)

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
