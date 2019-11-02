from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import fields, Index
from django_elasticsearch_dsl.documents import DocType
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField


from .models import Article
from api.apps.comments.models import Comment


html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

article_index = Index('articles')

article_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@article_index.doc_type
class ArticleDocument(DocType):
    title = fields.TextField(
        attr='title',
        fields={
            'suggest': fields.Completion(),
        }
    )
    body = fields.TextField(
        attr='body',
        fields={
            'suggest': fields.Completion(),
        }
    )

    comments_count = fields.IntegerField()

    class Django:
        model = Article
        fields = [
            'id',
            'pub_date',
            'created_at',
            'updated_at',
        ]

