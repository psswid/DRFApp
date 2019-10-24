from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import fields, Index
from django_elasticsearch_dsl.documents import DocType

from .models import Entry
from api.apps.comments.models import Comment


html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

entry = Index('entry')

entry.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@entry.doc_type
class EntryDocument(DocType):

    comment = fields.NestedField(properties={
        'body': fields.TextField(analyzer=html_strip)
    })

    class Index:
        name = 'entries'

        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Entry

        fields = [
            'title',
            'body',
        ]

        related_models = [Comment]

    def get_queryset(self):
        return super(EntryDocument, self).get_queryset().select_related(
            'comment'
        )

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Comment):
            return related_instance.entry
