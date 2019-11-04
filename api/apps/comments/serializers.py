from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from generic_relations.relations import GenericRelatedField

from .models import Comment
from .documents import CommentDocument

from api.apps.articles.models import Article
from api.apps.blog.models import Entry


class CommentObjectSerializer(serializers.ModelSerializer):
    # POST /comments
    # {
    #     "body": "komentarz",
    #     "comment_object": "/articles/7"
    # }
    comment_object = GenericRelatedField({
        Article: serializers.HyperlinkedRelatedField(
            queryset=Article.objects.all(),
            view_name='article-detail',
        ),
        Entry: serializers.HyperlinkedRelatedField(
            queryset=Entry.objects.all(),
            view_name='entry-detail'
        ),
    })

    class Meta:
        model = Comment
        fields = ('id', 'body', 'comment_object')


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
