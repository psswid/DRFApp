from django_elasticsearch_dsl import Index, fields
from django_elasticsearch_dsl.documents import DocType
from elasticsearch_dsl import analyzer

from .models import Comment

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)

comment_index = Index("comments")

comment_index.settings(number_of_shards=1, number_of_replicas=0)


@comment_index.doc_type
class CommentDocument(DocType):
    body = fields.TextField(attr="body", fields={"suggest": fields.Completion(), })

    class Django:
        model = Comment
        fields = [
            "id",
            "object_id",
            "created_at",
            "updated_at",
        ]
