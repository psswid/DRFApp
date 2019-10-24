from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import fields, Index
from django_elasticsearch_dsl.documents import DocType

from .models import Comment
from api.apps.blog.models import Entry
from api.apps.articles.models import Article


html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

comment = Index('comment')

comment.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@comment.doc_type
class CommentDocument(DocType):

    entry = fields.ObjectField(properties={
        'title': fields.TextField(),
        'body': fields.TextField()
    })

    article = fields.ObjectField(properties={
        'title': fields.TextField(),
        'body': fields.TextField()
    })

    class Index:
        name = 'comments'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Comment

        fields = [
            'body'
        ]

        related_models = [Entry, Article]

    def get_queryset(self):
        return super(CommentDocument, self).get_queryset().select_related(
            'comment'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Entry):
            return related_instance.entry
        if isinstance(related_instance, Article):
            return related_instance.article
