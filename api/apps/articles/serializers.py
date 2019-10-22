from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'body',
            'comments_count',
            'pub_date',
            'created_at',
            'updated_at'
        )
