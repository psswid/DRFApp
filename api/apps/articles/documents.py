from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import fields, Index
from django_elasticsearch_dsl.documents import DocType

from .models import Article
from api.apps.comments.models import Comment


html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

article = Index('article')

article.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@article.doc_type
class ArticleDocument(DocType):

    comment = fields.NestedField(properties={
        'body': fields.TextField(analyzer=html_strip)
    })

    class Index:
        name = 'articles'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Article

        fields = [
            'title',
            'body',
        ]

        related_models = [Comment]

    def get_queryset(self):
        return super(ArticleDocument, self).get_queryset().select_related(
            'comments'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Comment):
            return related_instance.article
