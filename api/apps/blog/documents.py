from django_elasticsearch_dsl import Index, fields
from django_elasticsearch_dsl.documents import DocType
from elasticsearch_dsl import analyzer

from .models import Entry

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)

entry_index = Index("entries")

entry_index.settings(number_of_shards=1, number_of_replicas=0)


@entry_index.doc_type
class EntryDocument(DocType):
    title = fields.TextField(attr="title", fields={"suggest": fields.Completion(), })
    body = fields.TextField(attr="body", fields={"suggest": fields.Completion(), })

    comments_count = fields.IntegerField()

    class Django:
        model = Entry
        fields = [
            "id",
            "pub_date",
            "created_at",
            "updated_at",
        ]
